#!/usr/bin/env python3
"""DLX15 and equation16: symmetry cuts against independent label placement."""
from datetime import datetime, timezone
import hashlib
import json

from check_langford_algorithm import oracle, valid, dual
from dlx1_audit_tools import ROOT, sha, input_text, run, decode_rows

OUT = ROOT/'results/langford_dlx'


def encoding(n, cut):
    assert cut in ('none', 'special', 'one')
    names = [f'L{i}' for i in range(1, n+1)]+[f'S{j}' for j in range(1, 2*n+1)]
    special = n-(n % 2 == 0)
    rows = []
    for i in range(1, n+1):
        for j in range(1, 2*n-i):
            if cut == 'special' and i == special and 2*j > n:
                continue
            if cut == 'one' and i == 1 and j >= n:
                continue
            rows.append((i, n+j, n+i+j+1))
    return names, rows


def decode(models, rows, n):
    out = set()
    for model in models:
        assert len(model) == n
        placement = [0]*(2*n)
        for r in model:
            i, a, b = rows[r]
            assert placement[a-n-1] == placement[b-n-1] == 0
            placement[a-n-1] = i
            placement[b-n-1] = -i
        placement = tuple(placement)
        assert valid(placement) and placement not in out
        out.add(placement)
    return out


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    cases = []
    for n in range(1, 11):
        expected = set(oracle(n))
        special = n-(n % 2 == 0)
        assert all(dual(model) in expected and dual(model) != model for model in expected)
        _, all_rows = encoding(n, 'none')
        assert len(all_rows) == 3*n*(n-1)//2
        for cut in ('none', 'special', 'one'):
            names, rows = encoding(n, cut)
            removed = len(all_rows)-len(rows)
            assert removed == (0 if cut == 'none' else n//2 if cut == 'special' else n-1)
            filtered = expected if cut == 'none' else {
                model for model in expected if (2*(model.index(special)+1) <= n
                    if cut == 'special' else model.index(1)+1 < n)}
            stats, text = run(OUT, f'n{n}-{cut}', input_text(names, rows), models=True)
            actual = decode(decode_rows(text, names, rows), rows, n)
            assert actual == filtered and len(actual) == stats['solutions']
            if cut != 'none':
                mirrored = {dual(model) for model in actual}
                assert not actual & mirrored and actual | mirrored == expected
            canonical = json.dumps(sorted(actual), separators=(',', ':')).encode()
            cases.append(dict(n=n, cut=cut, removed_options=removed, **stats,
                full_model_sets_equal=True, model_set_sha256=hashlib.sha256(canonical).hexdigest()))
    medium = []
    for n, expected in [(11, 17792), (12, 108144)]:
        for cut in ('special', 'one'):
            names, rows = encoding(n, cut)
            stats, _ = run(OUT, f'n{n}-{cut}', input_text(names, rows))
            assert stats['solutions'] == expected
            medium.append(dict(n=n, cut=cut, **stats))
    report = dict(status='verified', checked_at_utc=datetime.now(timezone.utc).isoformat(),
        source_sha256=sha(__file__), helper_sha256=sha(ROOT/'dlx1_audit_tools.py'),
        oracle_sha256=sha(ROOT/'check_langford_algorithm.py'),
        small_cases=cases, medium_cases=medium,
        scope='General mirror-involution proof in DLX_ENCODINGS_NOTES.md; '
              '30 complete model sets for n1..10 and four independent-count comparisons '
              'for n11/12. The n16 memory claim and relative timing need their own full runs.')
    (OUT/'validation.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(status=report['status'], full_small_model_sets=len(cases),
                          medium_cases=medium), indent=2), flush=True)


if __name__ == '__main__':
    main()
