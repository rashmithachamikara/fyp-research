"""Audit official DCASE 2025 split metadata against the published TAU archive."""
import csv
import io
import json
from pathlib import Path
import urllib.request
import zipfile
from collections import Counter

root = Path(__file__).resolve().parent / 'source-checks'
base = 'https://github.com/CPJKU/dcase2024_task1_baseline/releases/download/files/'
with zipfile.ZipFile(next(root.glob('*.meta.zip'))) as archive:
    member = next(n for n in archive.namelist() if n.endswith('/meta.csv'))
    rows = list(csv.DictReader(io.StringIO(archive.read(member).decode('utf-8-sig')), delimiter='\t'))
meta = {r['filename']: r for r in rows}
parts = {}
for name in ['split5.csv', 'split25.csv', 'test.csv']:
    with urllib.request.urlopen(base + name, timeout=45) as response:
        raw = response.read(5_000_001)
    if len(raw) > 5_000_000:
        raise ValueError('Metadata size limit exceeded')
    (root / name).write_bytes(raw)
    parts[name] = list(csv.DictReader(io.StringIO(raw.decode('utf-8-sig')), delimiter='\t'))

def describe(rows):
    matched = [meta[r['filename']] for r in rows]
    return {'rows': len(rows), 'classes': dict(Counter(r['scene_label'] for r in matched)),
            'devices': dict(Counter(r['source_label'] for r in matched))}

def identifiers(rows):
    return {meta[r['filename']]['identifier'] for r in rows}

report = {'checked_date': '2026-10-27', 'split_source': base,
          'audio_downloaded': False, 'parts': {name: describe(rows) for name, rows in parts.items()},
          'train25_test_location_overlap': sorted(identifiers(parts['split25.csv']) & identifiers(parts['test.csv'])),
          'train25_test_filename_overlap': sorted({r['filename'] for r in parts['split25.csv']} & {r['filename'] for r in parts['test.csv']})}
(root / 'tau-dcase25-split-audit.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps(report, indent=2))
