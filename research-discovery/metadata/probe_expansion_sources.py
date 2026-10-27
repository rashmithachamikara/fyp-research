"""Bounded source checks for the ten-candidate expansion; no model experiments."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import csv
import hashlib
import io
import json
import urllib.request
import zipfile

CHECKS = [
    ('car-parts-original', 'https://zenodo.org/api/records/4656022', 'zenodo'),
    ('car-parts-zero-filled', 'https://zenodo.org/api/records/4656021', 'zenodo'),
    ('maestro-real', 'https://zenodo.org/api/records/7244360', 'zenodo'),
    ('crema-audio-vote-schema', 'https://raw.githubusercontent.com/CheyneyComputerScience/CREMA-D/master/finishedResponses.csv', 'csv-prefix'),
    ('maestro-license', 'https://zenodo.org/api/records/7244360/files/LICENSE.txt/content', 'text'),
    ('maestro-readme', 'https://zenodo.org/api/records/7244360/files/README.md/content', 'text'),
    ('maestro-label-schema', 'https://zenodo.org/api/records/7244360/files/development_annotation.zip/content', 'zip-labels'),
]

def get(url, cap):
    request = urllib.request.Request(url, headers={'User-Agent': 'FYP-research-source-check/1.0'})
    with urllib.request.urlopen(request, timeout=15) as response:
        return response.read(cap), response.status

def check(item):
    key, url, kind = item
    record = {'id': key, 'source_url': url, 'checked_date': '2026-10-28'}
    try:
        raw, status = get(url, 2_000_000 if kind in ('zenodo', 'zip-labels') else 16_384)
        record.update({'http_status': status, 'bytes_read': len(raw)})
        if kind == 'zenodo':
            obj = json.loads(raw)
            record['title'] = obj.get('metadata', {}).get('title')
            record['license'] = obj.get('metadata', {}).get('license')
            record['files'] = [{k: f.get(k) for k in ['key', 'size', 'checksum', 'links']} for f in obj.get('files', [])]
            if key == 'car-parts-original':
                small = next(f for f in obj['files'] if f['key'].endswith('.zip') and f['size'] < 100_000)
                file_url = small['links'].get('self') or small['links'].get('content')
                archive, _ = get(file_url, 100_001)
                assert len(archive) <= 100_000
                record['archive_sha256'] = hashlib.sha256(archive).hexdigest()
                with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
                    assert sum(f.file_size for f in bundle.infolist()) < 5_000_000
                    member = next(f for f in bundle.infolist() if f.filename.endswith('.tsf'))
                    lines = bundle.read(member).decode('utf-8-sig').splitlines()
                data = [line for line in lines if line and not line.startswith(('#', '@'))]
                values = [line.rsplit(':', 1)[-1].split(',') for line in data]
                record['parsed_sample'] = {
                    'series_count': len(data), 'series_lengths': sorted(set(map(len, values))),
                    'missing_marker_count': sum(v == '?' for row in values for v in row),
                    'zero_count': sum(v in ('0', '0.0') for row in values for v in row),
                    'metadata_lines': [line for line in lines if line.startswith('@') and line != '@data'],
                }
        elif kind == 'zip-labels':
            assert len(raw) < 1_000_000
            with zipfile.ZipFile(io.BytesIO(raw)) as bundle:
                members = [f for f in bundle.infolist() if f.filename.endswith('.txt') and not f.filename.startswith('__MACOSX/')]
                assert sum(f.file_size for f in members) < 80_000_000
                labels, step_lengths, extents = set(), set(), []
                outside_unit_interval = 0
                for member in members:
                    assert member.file_size < 5_000_000
                    rows = list(csv.reader(io.StringIO(bundle.read(member).decode('utf-8-sig')), delimiter='\t'))
                    ends = []
                    for row in rows:
                        if len(row) == 4:
                            try:
                                start, end, value = float(row[0]), float(row[1]), float(row[3])
                            except ValueError:
                                continue
                            outside_unit_interval += not (-1e-8 <= value <= 1 + 1e-8)
                            labels.add(row[2])
                            step_lengths.add(round(end - start, 5))
                            ends.append(end)
                    if ends:
                        extents.append(max(ends))
            record['parsed_sample'] = {
                'annotation_files': len(members), 'files_with_numeric_rows': len(extents),
                'label_names': sorted(labels), 'segment_lengths_seconds': sorted(step_lengths),
                'sum_annotation_endpoints_seconds': sum(extents),
                'values_outside_unit_interval_beyond_roundoff': outside_unit_interval,
                'audio_decoded': False,
            }
        elif kind == 'csv-prefix':
            lines = raw.decode('utf-8-sig', errors='replace').splitlines()
            header = next(csv.reader([lines[0]]))
            record['header'] = header
            record['query_type_column_present'] = 'queryType' in header
            record['complete_rows_in_prefix'] = max(0, len(lines) - 2)
            record['raw_rows_saved'] = False
        else:
            record['text'] = raw.decode('utf-8-sig', errors='replace')
        record['status'] = 'checked'
    except Exception as error:
        record['status'] = 'not_verified'
        record['error'] = f'{type(error).__name__}: {error}'
    return record

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(check, CHECKS))
    output = {
        'checked_date': '2026-10-28',
        'purpose': 'Bounded metadata, tiny archive and annotation-schema checks; no model experiment',
        'checks': results,
    }
    path = Path(__file__).resolve().parent / 'source-checks/expansion-data-checks.json'
    path.write_text(json.dumps(output, indent=2) + '\n', encoding='utf-8')
    for result in results:
        print(json.dumps({k: v for k, v in result.items() if k != 'files'}))
