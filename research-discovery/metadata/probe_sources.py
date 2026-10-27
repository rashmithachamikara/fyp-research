"""Read bounded public dataset metadata; never download the large audio/mission archives."""
import csv
import hashlib
import io
import json
from pathlib import Path
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'source-checks'
OUT.mkdir(exist_ok=True)
MAX_BYTES = 5_000_000

def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'FYP-research-evidence-check/1.0'})
    with urllib.request.urlopen(req, timeout=45) as response:
        payload = response.read(MAX_BYTES + 1)
        if len(payload) > MAX_BYTES:
            raise ValueError('Response exceeds bounded metadata limit')
        return payload

summary = {'checked_date': '2026-10-27', 'checks': []}
for record in ['6337421', '12528696']:
    url = f'https://zenodo.org/api/records/{record}'
    try:
        raw = fetch(url)
        data = json.loads(raw)
        (OUT / f'zenodo-{record}.json').write_bytes(raw)
        check = {'url': url, 'record': record, 'access_right': data['metadata'].get('access_right'),
                 'license': data['metadata'].get('license'), 'files': [
                     {'name': f['key'], 'bytes': f.get('size'), 'url': f['links']['self']}
                     for f in data.get('files', [])]}
        if record == '6337421':
            for entry in data.get('files', []):
                if entry['key'].endswith(('.doc.zip', '.meta.zip')):
                    payload = fetch(entry['links']['self'])
                    (OUT / entry['key']).write_bytes(payload)
                    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
                        members = [m for m in archive.namelist() if not m.endswith('/')]
                        check.setdefault('inspected_archives', []).append({'file': entry['key'], 'bytes_downloaded': len(payload), 'members': members})
                        for member in members:
                            if member.lower().endswith(('.md', '.txt', '.csv', '.html')):
                                text = archive.read(member).decode('utf-8-sig', errors='replace')
                                safe_name = member.replace('/', '__').replace('\\', '__')
                                (OUT / safe_name).write_text(text, encoding='utf-8')
                                check.setdefault('text_previews', []).append({'member': member, 'first_lines': text.splitlines()[:6]})
        summary['checks'].append(check)
    except Exception as exc:
        summary['checks'].append({'url': url, 'error': str(exc)})

(OUT / 'dataset-probes.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
for check in summary['checks']:
    print(json.dumps({k: v for k, v in check.items() if k != 'files'}, ensure_ascii=False))
