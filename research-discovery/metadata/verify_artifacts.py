"""Offline integrity checks for the research-discovery handoff, not model validation."""
import csv
import json
from pathlib import Path
import re

root = Path(__file__).resolve().parent
discovery_root = root.parent
reports_root = discovery_root / 'reports'
searches = json.loads((root / 'search-records.json').read_text(encoding='utf-8'))
dups = json.loads((root / 'duplication-records.json').read_text(encoding='utf-8'))
refined = json.loads((root / 'refined-duplication-records.json').read_text(encoding='utf-8'))
with (root / 'evidence-ledger.csv').open(encoding='utf-8', newline='') as handle:
    rows = list(csv.DictReader(handle))

assert len(searches) == 8
assert all(len(s['data']['results']) == 20 for s in searches)
assert {s['id'].split('-')[0] for s in searches} == {'CV', 'NLP', 'AU', 'TS'}
assert len(dups) == 12 and len(refined) == 3
assert all(s['data'].get('nearest_neighbours') for s in dups + refined)
assert len({r['evidence_id'] for r in rows}) == len(rows)
assert all(None not in r for r in rows), 'CSV contains extra columns'
assert all(r['source_url'] and r['supported_claim'] and r['access_status'] for r in rows)

assert root.name == 'metadata'
assert {p.name for p in discovery_root.iterdir()} == {'reports', 'metadata'}
assert not any(p.suffix in {'.json', '.csv', '.py', '.zip'} for p in reports_root.rglob('*'))

broken = []
missing_anchors = []
report_files = sorted(reports_root.rglob('*.md'))
assert {path.relative_to(reports_root).as_posix() for path in report_files} == {
    'areas.md',
    'research-candidates.md',
    'gaps/au2-r-audio-confidence.md',
    'gaps/ts2-r-load-forecasting.md',
    'gaps/cv1-r-defect-adaptation.md',
}
readable_files = report_files
slug = lambda title: re.sub(r'[^\w\- ]', '', title.lower()).replace(' ', '-')
for path in readable_files:
    text = path.read_text(encoding='utf-8')
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if '://' not in target and not target.startswith('#'):
            parts = target.split('#', 1)
            destination = path.parent / parts[0]
            if not destination.exists():
                broken.append((str(path.relative_to(discovery_root)), target))
            elif len(parts) == 2:
                headings = re.findall(r'^#{1,6} (.+)$', destination.read_text(encoding='utf-8'), re.M)
                if parts[1] not in {slug(heading) for heading in headings}:
                    missing_anchors.append((str(path.relative_to(discovery_root)), target))
assert not broken, broken
assert not missing_anchors, missing_anchors

expected_sections = ['1. Problem', '2. Research gap and question', '3. Evidence from closest work',
                     '4. Proposed approach', '5. Data and resources', '6. Three-member contributions',
                     '7. Evaluation', '8. Score and next decision']
gap_files = sorted((reports_root / 'gaps').glob('*.md'))
assert len(gap_files) == 3
for path in gap_files:
    assert re.findall(r'^## (.+)$', path.read_text(encoding='utf-8'), re.M) == expected_sections

expected_unknown_gates = {
    'au2-r-audio-confidence.md': 0,
    'ts2-r-load-forecasting.md': 2,
    'cv1-r-defect-adaptation.md': 5,
}
for path in gap_files:
    text = path.read_text(encoding='utf-8')
    gate_rows = [line for line in text.split('### Mandatory gates', 1)[1].splitlines()
                 if re.match(r'^\| \d+\.', line)]
    assert len(gate_rows) == 13, path.name
    assert sum('| Unknown |' in row for row in gate_rows) == expected_unknown_gates[path.name]

summary = json.loads((root / 'discovery-summary.json').read_text(encoding='utf-8'))
assessments = summary['candidate_assessments']
assert set(assessments) == {'AU2-R', 'TS2-R', 'CV1-R'}
weights = [16, 15, 14, 12, 12, 12, 9, 5, 3]
overview = (reports_root / 'research-candidates.md').read_text(encoding='utf-8')
for candidate_id, assessment in assessments.items():
    brief = (discovery_root / assessment['report']).read_text(encoding='utf-8')
    rubric = brief.split('### Weighted rubric', 1)[1].split('### Mandatory gates', 1)[0]
    rubric_rows = [line for line in rubric.splitlines()
                   if re.match(r'^\| [^|]+ \| \d+ \|', line)]
    assert len(rubric_rows) == 9, candidate_id
    assert 'Ethics/responsible use' not in rubric
    assert [row['weight'] for row in assessment['ratings']] == weights
    for line, row in zip(rubric_rows, assessment['ratings']):
        cells = [cell.strip() for cell in line.strip('|').split('|')]
        assert 0 <= row['rating'] <= 5
        assert cells == [row['category'], str(row['weight']),
                         f"**{row['rating']}**" if '**' in cells[2] else str(row['rating']),
                         f"{row['weighted_points']:.1f}", row['confidence_and_reason']]
        assert row['weighted_points'] == round(row['weight'] * row['rating'] / 5, 1)
    raw_points = round(sum(row['weighted_points'] for row in assessment['ratings']), 1)
    assert assessment['raw_weighted_score'] == raw_points
    assert assessment['weight_total'] == sum(weights)
    calculated = round(raw_points / sum(weights) * 100, 1)
    assert calculated == assessment['weighted_score']
    assert f'{calculated:.1f}' in overview and f'{calculated:.1f}' in brief
    gate_rows = [line for line in brief.split('### Mandatory gates', 1)[1].splitlines()
                 if re.match(r'^\| \d+\.', line)]
    actual_gates = {'G' + str(i + 1): line.split('|')[2].strip()
                    for i, line in enumerate(gate_rows)}
    assert actual_gates == assessment['gate_decisions']
    assert assessment['unresolved_gates'] == [gate for gate, decision in actual_gates.items()
                                             if decision == 'Unknown']
    unmet = [row['category'] for i, row in enumerate(assessment['ratings'])
             if row['rating'] < (4 if i in (0, 1, 2, 5) else 3)]
    assert unmet == assessment['below_required_category_ratings']
    qualified = calculated >= 75 and not unmet and all(v == 'Pass' for v in actual_gates.values())
    assert qualified == assessment['qualified']
    if assessment['unresolved_gates']:
        assert 'Provisional' in brief and not qualified

score = assessments['AU2-R']['weighted_score']
assert sum(weights) == 98 and score == 77.3
assert assessments['AU2-R']['ratings'][0]['rating'] < 4
assert len(summary['screened_candidates']) == 12
assert all(len(candidate['gate_decisions']) == 13 for candidate in summary['screened_candidates'])
assert '# Research areas' in (reports_root / 'areas.md').read_text(encoding='utf-8')
assert '# Research candidates' in (reports_root / 'research-candidates.md').read_text(encoding='utf-8')

audit = json.loads((root / 'source-checks/tau-dcase25-split-audit.json').read_text(encoding='utf-8'))
assert audit['parts']['split25.csv']['rows'] == 34900
assert audit['parts']['split5.csv']['rows'] == 6980
assert audit['parts']['test.csv']['rows'] == 29680
assert not audit['train25_test_location_overlap']
assert not audit['train25_test_filename_overlap']
assert audit['audio_downloaded'] is False

report = {
    'checked_date': '2026-10-28',
    'checks_passed': True,
    'discovery_queries': len(searches),
    'discovery_result_occurrences': sum(len(s['data']['results']) for s in searches),
    'unique_discovery_records': len({p.get('id') or p.get('doi') or p['url'] for s in searches for p in s['data']['results']}),
    'semifinal_duplication_queries': len(dups),
    'refined_duplication_queries': len(refined),
    'ledger_rows': len(rows),
    'curated_evidence_rows': sum(r['evidence_id'].startswith('E-') for r in rows),
    'au2_r_weighted_score': score,
    'provisional_weighted_scores': {candidate_id: assessment['weighted_score']
                                    for candidate_id, assessment in assessments.items()
                                    if assessment['unresolved_gates']},
    'fully_qualified_candidates': sum(assessment['qualified'] for assessment in assessments.values()),
    'local_markdown_links_broken': broken,
    'local_markdown_anchors_missing': missing_anchors,
    'readable_markdown_files_checked': len(readable_files),
    'standard_gap_briefs_checked': len(gap_files),
    'candidate_gate_assessments_checked': 13 * len(gap_files),
    'full_weighted_rubric_preserved': True,
    'full_weighted_rubrics_checked': len(assessments),
    'rubric_categories': len(weights),
    'relative_weight_total': sum(weights),
    'scores_normalised_to': 100,
    'screened_candidates_preserved_in_metadata': len(summary['screened_candidates']),
    'reports_and_metadata_separated': True,
    'model_training_run': False,
    'qualification_note': 'AU2-R misses the required novelty rating; TS2-R and CV1-R have unresolved hard gates.'
}
(root / 'verification.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps(report, indent=2))
