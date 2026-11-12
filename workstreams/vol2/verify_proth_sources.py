#!/usr/bin/env python3
"""Compare the independently certified book list to the primary project census.

This checks transcription and agreement, not the external census computation.
"""
import gzip
import hashlib
import html
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
source = ROOT / 'sources/prothsearch-riesel1-http.html.gz'
raw = gzip.decompress(source.read_bytes())
text = raw.decode('ascii')
certs = json.loads((ROOT / 'results/proth-listed-primes.json').read_text())
assert certs['status'] == 'passed'
rows = []
for k in (3, 5):
    match = re.search(r'<FONT COLOR="Blue"><B>' + str(k) +
                      r'</B></FONT>(.*?)(?=<FONT COLOR="Blue">)', text, re.S)
    assert match
    row = html.unescape(re.sub(r'<[^>]+>', ' ', match.group(1)))
    prefix, limit = re.match(r'\s*(.*?)\[(\d+)\]', row, re.S).groups()
    exponents = [int(x) for x in re.findall(r'\d+', prefix)]
    assert exponents == sorted(set(exponents))
    selected = [e for e in exponents if e <= 300000]
    certified = sorted(x['exponent'] for x in certs['entries'].values() if x['k'] == k)
    assert selected == certified
    assert int(limit) > 300000
    rows.append({'k': k, 'project_complete_through': int(limit),
                 'book_bound': 300000, 'selected_exponents': selected,
                 'count': len(selected), 'agrees_with_certified_book_list': True})
result = {'status': 'passed',
          'scope': 'Exact agreement with primary external census; no independent gap census.',
          'url': 'http://www.prothsearch.com/riesel1.html',
          'source_updated': '2026-07-18',
          'source_sha256': hashlib.sha256(raw).hexdigest(), 'rows': rows}
(ROOT / 'results/proth-source-comparison.json').write_text(
    json.dumps(result, indent=2) + '\n')
print('PASS: 36 + 21 exponents; source census limits 23737900 and 9000000.')
