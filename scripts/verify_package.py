#!/usr/bin/env python3
"""Check the portable snapshot without opening any personal annotation database."""
import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = 'data/files.sha256.json'
SKIP_DIRS = {'.git', 'node_modules', '__pycache__', 'test-results', 'playwright-report'}
FORBIDDEN_SUFFIXES = {'.pdf', '.djvu', '.djv', '.ps', '.gz', '.zip', '.textxt',
                      '.sqlite', '.sqlite3', '.db'}
SECRET_PATTERNS = [
    re.compile(rb'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----'),
    re.compile(rb'gh[pousr]_[A-Za-z0-9]{30,}'),
    re.compile(rb'github_pat_[A-Za-z0-9_]{30,}'),
    re.compile(rb'sk-(?:proj-)?[A-Za-z0-9_-]{35,}'),
]


def read(name):
    return json.loads((ROOT / name).read_text())


def release_files():
    result = []
    for directory, dirs, files in os.walk(ROOT):
        rel = Path(directory).relative_to(ROOT)
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS
                         and (rel / d).as_posix() not in {'books', 'review-ui/data'})
        for name in sorted(files):
            path = rel / name
            if path.suffix not in {'.pyc', '.pyo'} and path.as_posix() != MANIFEST:
                result.append(path.as_posix())
    return sorted(result)


def check(condition, message):
    if not condition:
        raise ValueError(message)


def validate():
    catalog = read('review-ui/catalog.json')
    review = read('data/review-decisions.json')
    focused = read('data/focused-4b-review-decisions.json')
    findings = {f['id']: f for f in catalog['findings']}
    decisions = {r['id']: r for r in review['records']}
    expected = {'retained': 797, 'prior_public_found': 4, 'candidate': 1, 'dismissed': 4}
    check(len(findings) == len(catalog['findings']) == 946, 'Wrong or duplicate card inventory')
    check(Counter(f['status'] for f in findings.values()) ==
          {'confirmed': 817, 'candidate': 112, 'dismissed': 17}, 'Wrong visible status counts')
    check(len(decisions) == len(review['records']) == review['total'] == 806,
          'Wrong or duplicate review inventory')
    check(Counter(r['decision'] for r in decisions.values()) == expected == review['decisions'],
          'Wrong review decision counts')
    focused_ids = {f'F{n}' for n in range(257, 272)} | {'C025', 'C048', 'C034', 'C008', 'C006'}
    additional = {r['id']: r for r in focused['records']}
    check(set(additional) == focused_ids and len(focused['records']) == focused['total'] == 20,
          'Wrong focused-review inventory')
    check(not (set(decisions) & set(additional)), 'Duplicate review across audit passes')
    check(Counter(r['decision'] for r in additional.values()) == focused['decisions'] == {'retained': 20},
          'Wrong focused-review decisions')
    decisions.update(additional)
    index = read('data/volume-4b-findings-index.json')
    check([r['number'] for r in index] == list(range(1, 275)), 'Wrong text item numbering')
    expected_text = {f['id'] for f in findings.values()
                     if f['volume'] == 'vol4b' and f['status'] == 'confirmed'} - {'F024', 'F117'}
    check({r['id'] for r in index} == expected_text and len(index) == 274,
          'Wrong text selection or duplicate item')
    text = (ROOT / 'volume-4b-findings.txt').read_text()
    for row in index:
        heading = f"{row['number']}. {row['location']}"
        check(heading in text.splitlines(), f'Missing text item: {row["id"]}')
        check(row['evidence'] == f'findings/{row["id"]}.md', 'Wrong text evidence mapping')
    allowed = set(read('review-ui/evidence-files.json'))
    images = set(read('data/export-selection.json')['images'])
    check(len(images) == 3, 'The release must contain exactly the three original witness images')
    for path in allowed:
        p = ROOT / path
        check(not p.is_symlink() and p.is_file() and p.resolve().is_relative_to(ROOT),
              f'Missing or unsafe evidence: {path}')
    for ident, record in decisions.items():
        check(record['review_status'] == 'reviewed', f'Unfinished review: {ident}')
        check(not record.get('priority_established'), f'Absolute priority claimed: {ident}')
        check(record['evidence'] in allowed, f'Missing review record: {ident}')
        if record['decision'] == 'prior_public_found':
            check(ident not in findings, f'Prior public report remains an active card: {ident}')
        else:
            expected_status = 'confirmed' if record['decision'] == 'retained' else record['decision']
            check(findings[ident]['status'] == expected_status, f'Stale card status: {ident}')
            check(findings[ident]['publication_review']['decision'] == record['decision'],
                  f'Stale review on card: {ident}')
    for ident, finding in findings.items():
        if finding['status'] == 'confirmed':
            check(decisions[ident]['decision'] == 'retained', f'Unreviewed confirmed card: {ident}')
        check(all(finding.get(k) for k in ('title', 'target', 'summary')), f'Empty card: {ident}')
        check('awaiting an update' not in finding['summary'], f'Stale English: {ident}')
        check(not finding.get('annotation'), f'Personal data in snapshot: {ident}')
        check(finding['evidence'], f'No supporting argument: {ident}')
        for evidence in finding['evidence']:
            check(evidence['path'] in allowed, f'Unserved evidence on {ident}: {evidence["path"]}')
    check(sum(v['page_map']['total'] for v in catalog['volumes']) == 4308,
          'Wrong page inventory')
    for volume in catalog['volumes']:
        check(volume['review_evidence'] in allowed, f'Missing review scope: {volume["id"]}')
        for page in volume['page_map']['pages']:
            check(page['coverage'] in {'reviewed', 'not_reviewed'}, 'Invalid coverage state')
            for path in page['evidence']:
                check(path in allowed, f'Missing page review evidence: {path}')
            for ident in page['errors'] + page['candidates'] + page['related']:
                check(ident in findings, f'Hidden or unknown finding on page map: {ident}')
    files = release_files()
    check({p for p in files if Path(p).suffix.lower() == '.png'} == images, 'Unexpected image')
    for path in files:
        p = ROOT / path
        check(not p.is_symlink(), f'Symlink in release: {path}')
        check(p.suffix.lower() not in FORBIDDEN_SUFFIXES, f'Forbidden file: {path}')
        check(not p.name.startswith('.env'), f'Environment file: {path}')
        data = p.read_bytes()
        check(not data.startswith((b'%PDF-', b'AT&TFORM', b'SQLite format 3')), f'Private format: {path}')
        check(not any(pattern.search(data) for pattern in SECRET_PATTERNS), f'Credential pattern: {path}')
        check(b'/home/' + b'vasek/' not in data, f'Private workstation path: {path}')
    if (ROOT / '.git').exists():
        tracked = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0')
        check(not (set(tracked) - {''} - set(files) - {MANIFEST}), 'Git tracks excluded local files')
    check((ROOT / 'review-ui/dist/index.html').is_file(), 'Missing compiled frontend')
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-manifest', action='store_true', help='Refresh hashes after a reviewed release change')
    args = parser.parse_args()
    files = validate()
    hashes = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in files}
    if args.write_manifest:
        (ROOT / MANIFEST).write_text(json.dumps(hashes, indent=2) + '\n')
    else:
        check(read(MANIFEST) == hashes, 'Release files differ from the SHA-256 manifest')
    print(f'Package verified: {len(files)} files; 826 reviews; 817 retained; 274 text items; 3 original images; no bundled books or personal notes.')


if __name__ == '__main__':
    main()
