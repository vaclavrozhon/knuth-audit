"""Exact ambiguity witnesses for TAOCP2 exercise 3.6-7.

No recovery attack or complexity claim: compare iterative states with an
independent closed expression, and exhibit indistinguishable observations.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
M = 1 << 32
B = 1 << 16


def recurrence(a, c, x, count):
    out = []
    for _ in range(count):
        out.append(x)
        x = (a * x + c) % M
    return out


def closed(a, c, x, n):
    if a == 1:
        return (x + n * c) % M
    power = pow(a, n)
    return (power * x + c * ((power - 1) // (a - 1))) % M


def main():
    data = {}
    examples = [recurrence(1, c, 0, 150) for c in (1, 3)]
    for c, states in zip((1, 3), examples):
        assert states == [closed(1, c, 0, n) for n in range(150)]
        assert all(x // B == 0 for x in states)
    assert examples[0][1] - examples[0][0] == 1
    assert examples[1][1] - examples[1][0] == 3
    data['full_observation_ambiguity'] = {
        'modulus': M, 'multipliers': [1, 1], 'increments': [1, 3],
        'initial_states': [0, 0], 'observations': 150,
        'common_top16': 0, 'last_states': [149, 447],
        'first_differences': [1, 3],
        'period_proof': 'For a=1, odd c is invertible modulo 2^32; n*c returns to zero first at n=2^32.'
    }
    low_modulus = 1 << 18
    baseline = recurrence(5, 1, 0, 150)
    comparisons = 0
    for u, v in [(0, 0), (1, 0), (0, 1), (16383, 16383)] + [
        ((7919 * j) % 16384, (3571 * j) % 16384) for j in range(1, 65)
    ]:
        a, c = 5 + u * low_modulus, 1 + v * low_modulus
        assert 0 < a < M and 0 < c < M and a % 4 == 1 and c % 2 == 1
        states = recurrence(a, c, 0, 150)
        assert states == [closed(a, c, 0, n) for n in range(150)]
        assert [x % low_modulus for x in states] == [x % low_modulus for x in baseline]
        comparisons += 150
    changed_a = recurrence(5 + low_modulus, 1, 0, 3)
    changed_c = recurrence(5, 1 + low_modulus, 0, 3)
    assert changed_a[2] // B == 4 and baseline[2] // B == 0
    assert changed_c[1] // B == 4 and baseline[1] // B == 0
    middle = [(x // B) % 4 for x in baseline]
    assert set(middle) == {0, 1, 2, 3}
    data['two_bit_ambiguity'] = {
        'parameter_family': 'a=5+u*2^18, c=1+v*2^18, X0=0; 0<=u,v<2^14',
        'distinct_parameter_pairs': 1 << 28,
        'common_middle_bits_first_20': middle[:20],
        'independent_closed_form_comparisons': comparisons,
        'first_top16_difference_changed_a': 2,
        'first_top16_difference_changed_c': 1,
        'proof_scope': 'Induction proves equality modulo2^18 for every n, not only tested prefixes. Hull-Dobell gives period2^32 for each pair.'
    }
    (ROOT / 'results/truncated-lcg.json').write_text(json.dumps(data, indent=2) + '\n')
    print('PASS finite-observation and permanent two-bit ambiguities; 10500 independent closed-form state checks')


if __name__ == '__main__':
    main()
