"""Small exact/interval optimizer comparison for answer 3.3.4-30.

This does not refute the printed final bounds. It shows that identifying
the minimum coordinate product with the maximum sine weight needs care.
"""
from datetime import datetime, timezone
from fractions import Fraction as Q
import argparse
import json
from pathlib import Path
import time
import mpmath as mp


def ends(x):
    def rational(v):
        sign, mantissa, exponent, _ = v
        return (-1)**sign * Q(mantissa) * Q(2)**exponent
    return tuple(map(rational, x._mpi_))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--case', type=int, choices=[29, 49], default=49)
    case = parser.parse_args().case
    start = time.monotonic()
    mp.iv.dps = 70
    m, a = (29, 12) if case == 29 else (49, 15)
    winner_pairs = [[1, 12], [12, 1]] if case == 29 else [[13, 1]]
    rows = []
    for u in range(1, m//2+1):
        v = min(a*u % m, -a*u % m)
        product = mp.iv.sin(mp.iv.pi*u/m)*mp.iv.sin(mp.iv.pi*v/m)
        rows.append({'u': u, 'v': v, 'coordinate_product': u*v,
                     'sine_product_interval': list(map(str, ends(product)))})
    winners = [r for r in rows if [r['u'], r['v']] in winner_pairs]
    others = [r for r in rows if r not in winners]
    assert len(winners) == len(winner_pairs)
    assert max(Q(r['sine_product_interval'][1]) for r in winners) < min(
        Q(r['sine_product_interval'][0]) for r in others)
    minimum_product = min(r['coordinate_product'] for r in rows)
    expected_minimum, expected_winner = (10, 12) if case == 29 else (12, 13)
    assert minimum_product == expected_minimum
    assert all(r['coordinate_product'] == expected_winner for r in winners)
    digits = []
    x, y = m, a
    while y:
        digits.append(x//y)
        x, y = y, x % y
    # The weak product interval asserted in the book still holds here.
    A = max(digits)
    assert A*expected_winner <= m < (A+2)*expected_winner
    period = None
    if case == 49:
        x = 0
        states = []
        while x not in states:
            states.append(x)
            x = (a*x+1) % m
        assert x == 0 and sorted(states) == list(range(m))
        assert a % 7 == 1 and m == 7**2
        period = len(states)
    result = {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
              'm': m, 'a': a, 'continued_fraction': digits,
              'increment_one_period': period,
              'rows': rows, 'minimum_coordinate_product': minimum_product,
              'maximum_weight_pairs': [[r['u'], r['v']] for r in winners],
              'scope': 'Different optimizers certified. The printed final bounds and the weaker product interval are not refuted; the possible proof-transfer issue remains interpretive.',
              'seconds': time.monotonic()-start}
    name = 'sequential-spectral-product-example.json' if case == 29 else 'sequential-spectral-product-full-period.json'
    output = Path(__file__).resolve().parent/'results'/name
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['m','a','minimum_coordinate_product',
                     'maximum_weight_pairs','scope','seconds']}))


if __name__ == '__main__':
    main()
