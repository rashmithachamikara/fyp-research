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
summary = json.loads((root / 'discovery-summary.json').read_text(encoding='utf-8'))
assessments = summary['candidate_assessments']
expansion = json.loads((root / 'expansion-records.json').read_text(encoding='utf-8'))
cv_expansion = json.loads((root / 'cv-expansion-records.json').read_text(encoding='utf-8'))
elephant_expansion = json.loads((root / 'elephant-expansion-records.json').read_text(encoding='utf-8'))
satellite_ais = json.loads((root / 'satellite-ais-records.json').read_text(encoding='utf-8'))
maritime = json.loads((root / 'maritime-expansion-records.json').read_text(encoding='utf-8'))
report_files = sorted(reports_root.rglob('*.md'))
expected_reports = {'areas.md', 'research-candidates.md'} | {
    assessment['report'].removeprefix('reports/') for assessment in assessments.values()
}
assert {path.relative_to(reports_root).as_posix() for path in report_files} == expected_reports
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
assert len(gap_files) == len(assessments)
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
    if path.name in expected_unknown_gates:
        assert sum('| Unknown |' in row for row in gate_rows) == expected_unknown_gates[path.name]

new_ids = {f'X{i:02}' for i in range(1, 11)}
cv_ids = {f'X{i:02}' for i in range(11, 16)}
elephant_ids = {f'X{i:02}' for i in range(16, 21)}
maritime_ids = {f'X{i:02}' for i in range(22, 32)}
assert set(assessments) == {'AU2-R', 'TS2-R', 'CV1-R'} | new_ids | cv_ids | elephant_ids | {'X21', 'X32', 'X33'} | maritime_ids
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
    overview_link = assessment['report'].removeprefix('reports/')
    overview_rows = [line for line in overview.splitlines() if f']({overview_link})' in line]
    assert len(overview_rows) == 1 and f'{calculated:.1f}' in overview_rows[0]
    assert f'{calculated:.1f}' in brief
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

assert len(expansion['candidates']) == 10
assert {candidate['id'] for candidate in expansion['candidates']} == new_ids
assert len(expansion['searches']) == 22 and len(expansion['duplications']) == 20
assert all(query['requested_limit'] == 20 and 0 < len(query['data']['results']) <= 20
           for query in expansion['searches'])
assert all(query['data'].get('nearest_neighbours') for query in expansion['duplications'])
assert len(expansion['debate_maps']) == 4 and len(expansion['citation_checks']) == 3
assert len(expansion['code_route_checks']) == 9
for candidate in expansion['candidates']:
    candidate_id = candidate['id']
    evidence = [source for source in expansion['curated_sources']
                if source['candidate_ids'] == candidate_id]
    assert sum(source['stage'] == 'closest-work' for source in evidence) >= 3
    assert any(source['stage'] == 'dataset-check' for source in evidence)
    assert candidate['weighted_score'] == assessments[candidate_id]['weighted_score']
    assert candidate['gate_decisions'] == assessments[candidate_id]['gate_decisions']
    brief = (discovery_root / candidate['report']).read_text(encoding='utf-8')
    team_section = brief.split('## 6. Three-member contributions', 1)[1].split('## 7. Evaluation', 1)[0]
    members = re.findall(r'^\| [ABC]:.+$', team_section, re.M)
    assert len(members) == 3 and all(' H: ' in row for row in members)
    assert len(candidate['team_hypotheses']) == 3
    for source in evidence:
        assert any(row['evidence_id'] == source['evidence_id'] and row['source_url'] == source['source_url']
                   for row in rows), source['evidence_id']

assert {candidate['id'] for candidate in cv_expansion['candidates']} == cv_ids
assert len(cv_expansion['searches']) == 15 and len(cv_expansion['duplications']) == 10
assert all(query['requested_limit'] == 20 and 0 < len(query['data']['results']) <= 20
           for query in cv_expansion['searches'])
assert len({query['id'] for query in cv_expansion['searches']}) == 15
assert all(query['data'].get('nearest_neighbours') for query in cv_expansion['duplications'])
assert len(cv_expansion['debate_maps']) == 2 and len(cv_expansion['citation_checks']) == 2
for candidate in cv_expansion['candidates']:
    candidate_id = candidate['id']
    assert candidate['weighted_score'] == assessments[candidate_id]['weighted_score']
    assert candidate['gate_decisions'] == assessments[candidate_id]['gate_decisions']
    assert candidate['rating_details'] == assessments[candidate_id]['ratings']
    assert not candidate['qualified'] and not candidate['model_training_or_runtime_measured']
    assert 3 <= len(candidate['literature']) <= 5
    assert len(candidate['team_hypotheses']) == 3 and all(candidate['team_hypotheses'])
    evidence = [source for source in cv_expansion['curated_sources']
                if source['candidate_ids'] == candidate_id]
    assert sum(source['stage'] == 'closest-work' for source in evidence) >= 3
    assert any(source['stage'] == 'dataset-check' for source in evidence)
    for source in evidence:
        assert any(row['evidence_id'] == source['evidence_id'] and row['source_url'] == source['source_url']
                   for row in rows), source['evidence_id']
    brief = (discovery_root / candidate['report']).read_text(encoding='utf-8')
    team_section = brief.split('## 6. Three-member contributions', 1)[1].split('## 7. Evaluation', 1)[0]
    members = re.findall(r'^\| [ABC]:.+$', team_section, re.M)
    assert len(members) == 3 and all(' H: ' in row for row in members)
cv_data_checks = {check['id']: check for check in cv_expansion['bounded_data_checks']}
assert cv_data_checks['CV26-CCT20-META']['downloaded_bytes'] == 2997071
assert len(cv_data_checks['CV26-CCT20-META']['parsed_files']) == 5
assert not cv_data_checks['CV26-CCT20-META']['images_downloaded']
assert cv_data_checks['CV26-LEVIR-COORDS']['entries'] == 637
assert '| Research topic | Core gap to investigate | Research area |' in overview
assert '| Dataset |' not in overview

assert {candidate['id'] for candidate in elephant_expansion['candidates']} == elephant_ids
assert len(elephant_expansion['searches']) == 8 and len(elephant_expansion['duplications']) == 10
assert sum(len(query['data']['results']) for query in elephant_expansion['searches']) == 116
assert all(query['requested_limit'] == 20 and 0 < len(query['data']['results']) <= 20
           for query in elephant_expansion['searches'])
assert all(query['data'].get('nearest_neighbours') for query in elephant_expansion['duplications'])
for candidate in elephant_expansion['candidates']:
    candidate_id = candidate['id']
    assert candidate['weighted_score'] == assessments[candidate_id]['weighted_score']
    assert candidate['gate_decisions'] == assessments[candidate_id]['gate_decisions']
    assert candidate['rating_details'] == assessments[candidate_id]['ratings']
    assert not candidate['qualified'] and not candidate['model_training_or_runtime_measured']
    assert candidate['gate_decisions']['G4'] == 'Unknown'
    assert set(candidate['unresolved_gates']) == {'G4', 'G6', 'G9', 'G12'}
    assert len(candidate['literature']) >= 3
    assert len(candidate['team_hypotheses']) == 3 and all(candidate['team_hypotheses'])
    sources = [source for source in elephant_expansion['curated_sources']
               if source['candidate_ids'] == candidate_id]
    assert sum(source['stage'] == 'closest-work' for source in sources) >= 3
    assert any(source['stage'] == 'dataset-check' for source in sources)
    for source in sources:
        assert any(row['evidence_id'] == source['evidence_id'] and row['source_url'] == source['source_url']
                   for row in rows), source['evidence_id']
    brief = (discovery_root / candidate['report']).read_text(encoding='utf-8')
    assert 'Conditional opportunity' in brief and 'Four mandatory gates remain Unknown' in brief
    team_section = brief.split('## 6. Three-member contributions', 1)[1].split('## 7. Evaluation', 1)[0]
    assert len(re.findall(r'^\| [ABC]:.+ H: .+$', team_section, re.M)) == 3
elephant_data = json.loads((root / elephant_expansion['data_check_file']).read_text(encoding='utf-8'))
overlay_check = next(check for check in elephant_data['checks'] if check['file'] == 'Overlays.rar')
assert overlay_check['bytes'] == 1142384 and overlay_check['list_exit'] == 0
assert sum(name.endswith('.tif') for name in overlay_check['members']) == 4
assert len(elephant_data['checks']) == 3 and not elephant_data['models_run']
review_extract = json.loads((root / elephant_expansion['source_review']['extraction']).read_text(encoding='utf-8'))
assert len(review_extract['pages']) == 63

assert satellite_ais['candidate_assessment'] == assessments['X21']
assert len(satellite_ais['searches']) == 7 and len(satellite_ais['duplications']) == 3
assert sum(len(query['data']['results']) for query in satellite_ais['searches']) == 140
assert len(satellite_ais['gap_directions']) == 5 and len(satellite_ais['team_hypotheses']) == 3
assert set(assessments['X21']['unresolved_gates']) == {'G4', 'G6', 'G7', 'G9', 'G12'}
assert assessments['X21']['ratings'][0]['rating'] == 2
assert assessments['X21']['weighted_score'] == 64.5
gap_validation = json.loads((root / satellite_ais['gap_validation_file']).read_text(encoding='utf-8'))
assert gap_validation['revised_assessment'] == assessments['X21']
assert gap_validation['previous_assessment']['weighted_score'] == 67.8
assert len(gap_validation['searches']) == 10 and len(gap_validation['duplications']) == 5
assert sum(len(query['data']['results']) for query in gap_validation['searches']) == 186
assert {gap['gap'] for gap in gap_validation['gap_verdicts']} == {'G1', 'G2', 'G3', 'G4', 'G5'}
assert not any(gap['novel_gap_verified'] for gap in gap_validation['gap_verdicts'])
assert len(gap_validation['curated_sources']) == 13
for source in gap_validation['curated_sources']:
    assert any(row['evidence_id'] == source['evidence_id'] and row['source_url'] == source['source_url']
               for row in rows), source['evidence_id']
for gap in gap_validation['gap_verdicts']:
    assert all(any(row['evidence_id'] == evidence_id for row in rows)
               for evidence_id in gap['evidence_ids'])
for source in satellite_ais['curated_sources']:
    assert any(row['evidence_id'] == source['evidence_id'] and row['source_url'] == source['source_url']
               for row in rows), source['evidence_id']
ais_audit = json.loads((root / satellite_ais['data_check_file']).read_text(encoding='utf-8'))
assert not ais_audit['models_run']
roi_audit = next(check for check in ais_audit['checks']
                 if check.get('type') == 'author-repository-metadata-format-check')
assert roi_audit['bytes_read'] == 10596 and len(roi_audit['parsed_rows']) == 9
assert len({row[1] for row in roi_audit['parsed_rows'][1:]}) == 5
vessel_csv = next(check for check in ais_audit['checks']
                  if check.get('url', '').endswith('/44031663'))
assert vessel_csv['samples'][0]['row_count'] == 3172
assert vessel_csv['samples'][0]['columns'] == ['detect_id', 'length_m', 'presence']

assert {candidate['id'] for candidate in maritime['candidates']} == maritime_ids
assert len(maritime['searches']) == 20 and len(maritime['duplications']) == 20
assert sum(len(query['data']['results']) for query in maritime['searches']) == 329
assert len({query['id'] for query in maritime['searches'] + maritime['duplications']}) == 40
assert len(maritime['screened_out_formulations']) == 5
for candidate in maritime['candidates']:
    candidate_id = candidate['id']
    assessment = assessments[candidate_id]
    assert candidate['weighted_score'] == assessment['weighted_score']
    assert candidate['gate_decisions'] == assessment['gate_decisions']
    assert not candidate['qualified'] and assessment['ratings'][0]['rating'] == 3
    assert candidate['unresolved_gates'] == assessment['unresolved_gates']
    assert 'G6' in assessment['unresolved_gates']
    assert len(candidate['sources']) >= 3 and candidate['dataSources']
    assert len(candidate['members']) == 3
    assert all(' H: ' in member[1] for member in candidate['members'])
    brief = (discovery_root / candidate['report']).read_text(encoding='utf-8')
    assert 'Rival explanation' in brief and 'Unmeasured resource estimate' in brief
    assert 'Useful findings without outperforming the strongest baseline' in brief
for source in maritime['curated_sources']:
    assert any(row['evidence_id'] == source['evidence_id'] and row['source_url'] == source['source_url']
               for row in rows), source['evidence_id']
maritime_data = json.loads((root / maritime['data_check_file']).read_text(encoding='utf-8'))
assert not maritime_data['models_run']
assert {check['id'] for check in maritime_data['checks']} == {15860212, 18391027}
assert all(check['metadata']['license']['id'] == 'cc-by-4.0' for check in maritime_data['checks'])

source_audit = json.loads((root / 'source-checks/expansion-data-checks.json').read_text(encoding='utf-8'))
source_checks = {check['id']: check for check in source_audit['checks']}
assert source_checks['car-parts-original']['parsed_sample']['series_count'] == 2674
assert source_checks['car-parts-original']['parsed_sample']['missing_marker_count'] == 6122
assert source_checks['car-parts-original']['parsed_sample']['zero_count'] == 97398
assert source_checks['crema-audio-vote-schema']['query_type_column_present']
assert source_checks['maestro-label-schema']['parsed_sample']['annotation_files'] == 49
assert source_checks['maestro-label-schema']['parsed_sample']['segment_lengths_seconds'] == [1.0]
assert not source_checks['maestro-label-schema']['parsed_sample']['audio_decoded']

audit = json.loads((root / 'source-checks/tau-dcase25-split-audit.json').read_text(encoding='utf-8'))
assert audit['parts']['split25.csv']['rows'] == 34900
assert audit['parts']['split5.csv']['rows'] == 6980
assert audit['parts']['test.csv']['rows'] == 29680
assert not audit['train25_test_location_overlap']
assert not audit['train25_test_filename_overlap']
assert audit['audio_downloaded'] is False

sinhala_partial = json.loads((root / 'source-checks/sinhala-partial-gap-validation.json').read_text(encoding='utf-8'))
assert sinhala_partial['candidate_id'] == 'X32'
assert sinhala_partial['assessment'] == assessments['X32']
assert len(sinhala_partial['searches']) == 8
assert len(sinhala_partial['duplications']) == 4
assert sum(len(query['data']['results']) for query in sinhala_partial['searches']) == 137
assert all(query['requested_limit'] == 20 and query['status'] == 'fulfilled'
           for query in sinhala_partial['searches'])
assert assessments['X32']['weighted_score'] == 62.0
assert set(assessments['X32']['unresolved_gates']) == {'G4', 'G6', 'G8', 'G9', 'G12'}
assert not assessments['X32']['qualified']
assert len(sinhala_partial['parked_formulations']) == 5
x32_brief = (discovery_root / assessments['X32']['report']).read_text(encoding='utf-8')
assert len(re.findall(r'^### Member [ABC]:', x32_brief, re.M)) == 3
assert 'Quick explanation:' in x32_brief
assert 'No model has been trained or timed.' in x32_brief
import_link = re.search(r'Import these (\d+) papers into Zotero or EndNote\]\(https://literature.researchfasttrack.com/zotero\?ids=([^)]+)\)', x32_brief)
assert import_link and int(import_link[1]) == len(set(import_link[2].split(','))) == 9
for source in sinhala_partial['curated_sources']:
    assert any(row['evidence_id'] == source['evidence_id'] and row['source_url'] == source['source_url']
               for row in rows), source['evidence_id']

sinhala_streaming = json.loads((root / 'source-checks/sinhala-streaming-gap-validation.json').read_text(encoding='utf-8'))
assert sinhala_streaming['candidate_id'] == 'X33'
assert sinhala_streaming['assessment'] == assessments['X33']
assert len(sinhala_streaming['searches']) == 2
assert len(sinhala_streaming['duplications']) == 1
assert sum(len(query['data']['results']) for query in sinhala_streaming['searches']) == 40
assert assessments['X33']['weighted_score'] == 62.0
assert set(assessments['X33']['unresolved_gates']) == {'G4', 'G6', 'G8', 'G9', 'G12'}
assert not assessments['X33']['qualified']
x33_brief = (discovery_root / assessments['X33']['report']).read_text(encoding='utf-8')
assert len(re.findall(r'^### Member [ABC]:', x33_brief, re.M)) == 3
assert 'Quick explanation:' in x33_brief and 'No model has been trained or timed.' in x33_brief
import_link = re.search(r'Import these (\d+) papers into Zotero or EndNote\]\(https://literature.researchfasttrack.com/zotero\?ids=([^)]+)\)', x33_brief)
assert import_link and int(import_link[1]) == len(set(import_link[2].split(','))) == 9
for source in sinhala_streaming['curated_sources']:
    assert any(row['evidence_id'] == source['evidence_id'] and row['source_url'] == source['source_url']
               for row in rows), source['evidence_id']

streaming_novelty = sinhala_streaming['novelty_recheck']
assert len(streaming_novelty['searches']) == 7
assert len(streaming_novelty['duplications']) == 3
assert sum(len(q['data']['results']) for q in streaming_novelty['searches']) == 130
assert streaming_novelty['general_problem_real']
assert not streaming_novelty['sinhala_specific_failure_demonstrated']
assert not streaming_novelty['novel_method_established']
assert 'now withdrawn as a novelty claim' in x33_brief
for source in streaming_novelty['curated_sources']:
    assert any(row['evidence_id'] == source['evidence_id'] and row['source_url'] == source['source_url']
               for row in rows), source['evidence_id']

report = {
    'checked_date': '2026-10-29',
    'checks_passed': True,
    'discovery_queries': len(searches),
    'discovery_result_occurrences': sum(len(s['data']['results']) for s in searches),
    'unique_discovery_records': len({p.get('id') or p.get('doi') or p['url'] for s in searches for p in s['data']['results']}),
    'semifinal_duplication_queries': len(dups),
    'refined_duplication_queries': len(refined),
    'ledger_rows': len(rows),
    'curated_evidence_rows': sum(r['evidence_id'].startswith('E-') or r['stage'] in
                                 {'expansion-closest-work', 'expansion-dataset-check',
                                  'closest-work', 'dataset-check', 'baseline-check'} for r in rows),
    'additional_candidates': len(expansion['candidates']),
    'additional_discovery_queries': len(expansion['searches']),
    'additional_search_record_occurrences': sum(len(query['data']['results']) for query in expansion['searches']),
    'additional_duplication_queries': len(expansion['duplications']),
    'additional_curated_source_rows': len(expansion['curated_sources']),
    'additional_debate_maps': len(expansion['debate_maps']),
    'additional_citation_checks': len(expansion['citation_checks']),
    'code_routes_checked': len(expansion['code_route_checks']),
    'further_cv_candidates': len(cv_expansion['candidates']),
    'further_cv_discovery_queries': len(cv_expansion['searches']),
    'further_cv_search_record_occurrences': sum(len(query['data']['results']) for query in cv_expansion['searches']),
    'further_cv_duplication_queries': len(cv_expansion['duplications']),
    'further_cv_curated_sources': len(cv_expansion['curated_sources']),
    'further_cv_code_routes_checked': len(cv_expansion['code_route_checks']) + len(cv_expansion['additional_code_route_checks']),
    'further_cv_bounded_data_checks': len(cv_expansion['bounded_data_checks']),
    'total_evaluated_candidates': len(assessments),
    'sinhala_partial_gap_searches': len(sinhala_partial['searches']),
    'sinhala_partial_gap_search_occurrences': sinhala_partial['search_result_occurrences'],
    'sinhala_partial_gap_duplications': len(sinhala_partial['duplications']),
    'sinhala_partial_gap_curated_sources': len(sinhala_partial['curated_sources']),
    'sinhala_partial_gap_qualified': assessments['X32']['qualified'],
    'sinhala_streaming_gap_searches': len(sinhala_streaming['searches']),
    'sinhala_streaming_gap_search_occurrences': sinhala_streaming['search_result_occurrences'],
    'sinhala_streaming_gap_duplications': len(sinhala_streaming['duplications']),
    'sinhala_streaming_gap_curated_sources': len(sinhala_streaming['curated_sources']),
    'sinhala_streaming_gap_qualified': assessments['X33']['qualified'],
    'sinhala_streaming_novelty_searches': len(streaming_novelty['searches']),
    'sinhala_streaming_novelty_search_occurrences': streaming_novelty['search_result_occurrences'],
    'sinhala_streaming_novelty_duplications': len(streaming_novelty['duplications']),
    'sinhala_streaming_novel_method_established': streaming_novelty['novel_method_established'],
    'further_maritime_candidates': len(maritime['candidates']),
    'further_maritime_discovery_queries': len(maritime['searches']),
    'further_maritime_search_occurrences': 329,
    'further_maritime_duplication_queries': len(maritime['duplications']),
    'further_maritime_curated_evidence_rows': len(maritime['curated_sources']),
    'elephant_conditional_opportunities': len(elephant_expansion['candidates']),
    'elephant_discovery_queries': len(elephant_expansion['searches']),
    'elephant_discovery_occurrences': sum(len(query['data']['results']) for query in elephant_expansion['searches']),
    'elephant_duplication_queries': len(elephant_expansion['duplications']),
    'elephant_curated_sources': len(elephant_expansion['curated_sources']),
    'elephant_local_outcome_data_access_secured': False,
    'satellite_ais_gaps_verified': len(gap_validation['gap_verdicts']),
    'satellite_ais_novel_gaps_established': sum(gap['novel_gap_verified'] for gap in gap_validation['gap_verdicts']),
    'satellite_ais_validation_searches': len(gap_validation['searches']),
    'satellite_ais_validation_occurrences': sum(len(query['data']['results']) for query in gap_validation['searches']),
    'satellite_ais_validation_duplication_queries': len(gap_validation['duplications']),
    'satellite_ais_additional_method_records': len(gap_validation['curated_sources']),
    'au2_r_weighted_score': score,
    'provisional_weighted_scores': {candidate_id: assessment['weighted_score']
                                    for candidate_id, assessment in assessments.items()
                                    if assessment['unresolved_gates'] or assessment['mode'].startswith('Provisional')},
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
    'qualification_note': 'No candidate meets every category threshold. All thirty-three added-candidate scores are provisional. X22-X31 are maritime opportunities with unresolved novelty. X32 and X33 are distinct Sinhala audio opportunities with data, novelty, evaluation, feasibility and reuse gates unresolved. Other critical dependencies remain in their gate assessments.'
}
(root / 'verification.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps(report, indent=2))
