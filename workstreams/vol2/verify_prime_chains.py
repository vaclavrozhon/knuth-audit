"""Exact certificates for TAOCP2 4.5.4-39, with a bounded greedy extension.

SymPy proposes factors and primes only. A separate verifier checks every
complete-factorization Lucas certificate and every composite exclusion using
explicit binary modular exponentiation. No probable-prime verdict is accepted.
"""
from pathlib import Path
from math import gcd, prod, lcm
import json
import time
import sympy

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/prime-chains.json'
SMALL = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
         47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
PRINTED = [2, 3, 7, 29, 59, 1889, 3779, 7559, 4058207223809,
           32465657790473, 4462046030502692971872257,
           9582170887127842377060195852353537,
           2066678528579921308409812579227882652882296135112078218441270655539079806279302783351291332069672615937]


def explicit_power(a, e, n):
    x = 1
    for bit in bin(e)[2:]:
        x = x*x % n
        if bit == '1':
            x = x*a % n
    return x


def strong_composite(n, a):
    d, s = n-1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    x = pow(a, d, n)
    if x in (1, n-1):
        return False
    for _ in range(s-1):
        x = x*x % n
        if x == n-1:
            return False
    return True


def exclusion(n):
    for q in SMALL:
        if q < n and n % q == 0:
            return ['divisor', q]
    for a in SMALL:
        if a < n and strong_composite(n, a):
            return ['strong', a]
    raise AssertionError(('no composite certificate', n))


def validate_exclusion(n, witness):
    kind, a = witness
    assert 1 < a < n
    if kind == 'divisor':
        r = 0
        for digit in str(n):
            r = (10*r + int(digit)) % a
        assert r == 0
    else:
        assert kind == 'strong'
        exponents = []
        d = n-1
        while d % 2 == 0:
            d //= 2
            exponents.append(d)
        assert explicit_power(a, d, n) != 1
        assert all(explicit_power(a, e, n) != n-1 for e in exponents)


class Certificates:
    def __init__(self):
        self.data = {2: {'n': 2, 'factors': [], 'base': None}}

    def add(self, n, factors=None):
        if n in self.data:
            return
        if factors is None:
            factors = {int(p): int(e) for p, e in sympy.factorint(n-1).items()}
        assert prod(p**e for p, e in factors.items()) == n-1
        for p in factors:
            self.add(p)
        a = next(a for a in range(2, 10000)
                 if pow(a, n-1, n) == 1
                 and all(gcd(pow(a, (n-1)//p, n)-1, n) == 1 for p in factors))
        self.data[n] = dict(n=n, factors=sorted(factors.items()), base=a)

    def validate_all(self):
        proven = {2}
        for n in sorted(self.data):
            if n == 2:
                continue
            row = self.data[n]
            factors = row['factors']
            assert all(p in proven and e >= 1 for p, e in factors)
            assert len({p for p, _ in factors}) == len(factors)
            assert prod(p**e for p, e in factors) == n-1
            a = row['base']
            assert 1 < a < n and explicit_power(a, n-1, n) == 1
            for p, _ in factors:
                assert gcd(explicit_power(a, (n-1)//p, n)-1, n) == 1
            proven.add(n)
        return len(proven)


def link(certificates, p, k):
    q = (p << k) + 1
    factors = {2: k, p: 1} if p != 2 else {2: k+1}
    factors = {p: e for p, e in factors.items() if e}
    certificates.add(q, factors)
    excluded = []
    for j in range(k):
        n = (p << j) + 1
        witness = exclusion(n)
        validate_exclusion(n, witness)
        excluded.append([j, *witness])
    return dict(p=p, exponent=k, q=q, excluded=excluded)


def covering(coefficient, primes):
    rows = []
    for p in primes:
        assert p < coefficient
        assert all(p % j for j in range(2, int(p**0.5)+1))
        period = next(d for d in range(1, p) if pow(2, d, p) == 1)
        residues = [r for r in range(period)
                    if (coefficient*pow(2, r, p)+1) % p == 0]
        rows.append(dict(prime=p, period=period, residues=residues))
    period = lcm(*(row['period'] for row in rows))
    # Direct recurrence over a common period is independent of the residue lists.
    assigned = []
    for n in range(period):
        ds = [p for p in primes if (coefficient*2**n+1) % p == 0]
        assert ds
        assert any(n % row['period'] in row['residues'] for row in rows)
        assigned.append(ds[0])
    return dict(coefficient=coefficient, rows=rows, period=period,
                divisor_for_each_residue=assigned,
                infinite_progression_step=2*prod(primes))


def main():
    start = time.perf_counter()
    certs = Certificates()
    result = dict(status='running', printed_links=[], extension_links=[])
    for p, q in zip(PRINTED, PRINTED[1:]):
        ratio, r = divmod(q-1, p)
        assert r == 0 and ratio > 0 and ratio & (ratio-1) == 0
        row = link(certs, p, ratio.bit_length()-1)
        result['printed_links'].append(row)
    assert len(str(PRINTED[-2])) == 34
    assert str(PRINTED[-2]).startswith('95') and str(PRINTED[-2]).endswith('37')
    assert len(str(PRINTED[-1])) == 103
    print('printed chain and least 103-digit successor certified', flush=True)

    # The research exercise has no global optimum claimed. Limit this extension
    # to twenty vertices, 4096 bits, and exponents below 4096.
    p = PRINTED[-1]
    for _ in range(20-len(PRINTED)):
        k = next((k for k in range(4096)
                  if p.bit_length()+k <= 4096 and sympy.isprime((p << k)+1)), None)
        if k is None:
            result['extension_stop'] = 'finite exponent/bit limit; no nonexistence assertion'
            break
        row = link(certs, p, k)
        result['extension_links'].append(row)
        p = row['q']
        print('extension', len(PRINTED)+len(result['extension_links']),
              'exponent', k, 'digits', len(str(p)), flush=True)
    else:
        result['extension_stop'] = 'twenty certified vertices; no maximality assertion'

    simple = [5, 11, 23, 47]
    for p in simple:
        certs.add(p)
    assert all(q == 2*p+1 for p, q in zip(simple, simple[1:]))
    loh = [554688278430*2**k-1 for k in range(12)]
    for p in loh:
        certs.add(p)
    next_loh = 554688278430*2**12-1
    next_witness = exclusion(next_loh)
    validate_exclusion(next_loh, next_witness)
    result['loh'] = dict(primes=loh, next_composite=next_loh, witness=next_witness)
    result['covers'] = [covering(78557, [3, 5, 7, 13, 19, 37, 73]),
                        covering(271129, [3, 5, 7, 13, 17, 241])]
    certs.add(271129)
    assert 78557 == 17*4621
    result['certificates_verified'] = certs.validate_all()
    result['certificates'] = [certs.data[p] for p in sorted(certs.data)]
    result['chain_vertices'] = len(PRINTED)+len(result['extension_links'])
    result['composite_exclusions'] = sum(row['exponent'] for key in
        ['printed_links', 'extension_links'] for row in result[key])
    result.update(status='passed', seconds=time.perf_counter()-start)
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print('passed', result['chain_vertices'], 'vertices;',
          result['composite_exclusions'], 'excluded candidates;',
          result['certificates_verified'], 'Lucas certificates;',
          result['seconds'], 'seconds', flush=True)


if __name__ == '__main__':
    main()
