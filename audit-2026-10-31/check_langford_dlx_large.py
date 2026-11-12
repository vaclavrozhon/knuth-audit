#!/usr/bin/env python3
"""Read, authenticate and compare completed DLX15 n16 jobs; never reenumerate."""
from datetime import datetime, timezone
from fractions import Fraction as F
import json

from check_langford_dlx import OUT, encoding
from dlx1_audit_tools import ROOT, sha, input_text, statistics


def rational(value):
    return dict(numerator=value.numerator, denominator=value.denominator, decimal=float(value))


def main():
    wrapper = json.loads((OUT / 'large-wrapper.json').read_text())
    validation = json.loads((OUT / 'validation.json').read_text())
    assert wrapper['status'] == 'finished'
    assert wrapper['source_sha256'] == sha(ROOT / 'run_langford_dlx.py')
    assert wrapper['validation_sha256'] == sha(OUT / 'validation.json')
    assert validation['source_sha256'] == sha(ROOT / 'check_langford_dlx.py')
    assert validation['helper_sha256'] == sha(ROOT / 'dlx1_audit_tools.py')
    cases = {}
    for cut in ['special', 'one']:
        label = f'n16-{cut}'
        metadata = json.loads((OUT / f'{label}-run.json').read_text())
        case = next(c for c in wrapper['cases'] if c['label'] == label)
        assert metadata == case
        assert case['status'] == 'finished' and case['returncode'] == 0
        names, rows = encoding(16, cut)
        assert (OUT / f'{label}.dlx').read_text() == input_text(names, rows)
        assert case['input_sha256'] == sha(OUT / f'{label}.dlx')
        assert case['log_sha256'] == sha(OUT / f'{label}.log')
        stats = statistics((OUT / f'{label}.log').read_text())
        assert stats == case['result'] and stats['solutions'] == 326721800
        cases[cut] = stats
    special = cases['special']['search_mems']
    one = cases['one']['search_mems']
    result = dict(status='verified', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  source_sha256=sha(__file__), wrapper_sha256=sha(OUT / 'large-wrapper.json'),
                  cases=cases, saving_fraction=rational(F(one-special, one)),
                  mems_per_solution=rational(F(special, 326721800)),
                  relative_difference_from_printed_1_13T=rational(F(1130000000000-special, 1130000000000)),
                  scope='Complete originalDLX1 runs, both cuts, authenticated logs and full node profiles. '
                        'The 7.895% saving supports the informal about10% statement alongside n11/12. '
                        'This does not claim exact reproduction of the separate book memory accounting on p70.')
    (OUT / 'large-comparison.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'cases'}, indent=2))


if __name__ == '__main__':
    main()
