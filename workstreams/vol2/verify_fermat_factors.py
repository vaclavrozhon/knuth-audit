"""Exact independent verification of TAOCP 2 p.403 factorizations.

PARI only proposes elliptic-curve certificates. verify_ecpp.Verifier uses
Python integer arithmetic and recursively proved Lucas terminal certificates.
The composite residuals of F12 and F13 have explicit Fermat witnesses.
"""
from pathlib import Path
from math import prod, gcd
import datetime
import hashlib
import json
import os
import time

from certify_fermat_factors import KNOWN, targets, save
from verify_ecpp import Verifier

ROOT = Path(__file__).resolve().parent


def binary_power(a, exponent, modulus):
    result = 1
    for digit in bin(exponent)[2:]:
        result = result * result % modulus
        if digit == '1':
            result = result * a % modulus
    return result


def main():
    start = time.monotonic()
    print(f'Independent validator pid={os.getpid()}', flush=True)
    v = Verifier()
    result = dict(started_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  pid=os.getpid(), status='running', targets=[], factorizations=[])
    destination = ROOT / 'results/fermat-factors-validation.json'
    for target in targets():
        path = ROOT / 'results/fermat-factor-certificates' / f'{target["id"]}.json'
        row = json.loads(path.read_text())
        assert row['target'] == target and row['status'] == 'generated'
        # The short Weierstrass model used by the shared validator requires
        # odd characteristic; check this also for every intermediate node.
        if isinstance(row['certificate'], list):
            assert all(node[0] % 2 for node in row['certificate'])
        before = v.links
        v.verify(row['certificate'], target['value'])
        result['targets'].append(dict(id=target['id'], value=target['value'],
                                      digits=len(str(target['value'])),
                                      elliptic_curve_links=v.links-before,
                                      certificate_sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
        save(destination, result)
        print(target['id'], 'proved prime', flush=True)
    for m, factors in KNOWN.items():
        N = (1 << (1 << m)) + 1
        cofactor, remainder = divmod(N, prod(factors))
        assert remainder == 0 and cofactor * prod(factors) == N
        expected = {9:99, 10:252, 11:564, 12:1187, 13:2391}[m]
        assert 10**(expected-1) <= cofactor < 10**expected
        row = dict(fermat_index=m, number=N, number_digits=len(str(N)),
                   known_factors=factors, cofactor=cofactor, cofactor_digits=expected)
        if m <= 11:
            assert any(t['value'] == cofactor for t in result['targets'])
            row['status'] = 'complete prime factorization'
        else:
            # Find a concrete witness, not a probable-prime/composite oracle.
            for a in range(2, 100):
                residue = pow(a, cofactor-1, cofactor)
                if residue != 1:
                    assert gcd(a, cofactor) == 1
                    assert residue == binary_power(a, cofactor-1, cofactor)
                    row['fermat_compositeness_witness'] = dict(base=a, residue=residue)
                    break
            else:
                raise AssertionError(('No Fermat witness in tested bases', m))
            row['status'] = 'partial factorization; residual proved composite'
        if m == 11:
            assert all(p < 10**22 for p in factors)
        elif m == 12:
            assert len(factors) == 5 and all(p < 10**16 for p in factors)
        elif m == 13:
            assert len(factors) == 4 and all(p < 10**27 for p in factors)
        result['factorizations'].append(row)
        save(destination, result)
        print(f'F{m}: {row["status"]}, residual digits={expected}', flush=True)
    v.validate_small_certificates()
    result.update(status='passed', elliptic_curve_links=v.links,
                  small_lucas_certificates=[v.small[p] for p in sorted(v.small)],
                  seconds=time.monotonic()-start,
                  method='Independent affine elliptic arithmetic with unit denominators, Hasse bound, recursive Lucas terminal proofs; exact factor products and dual modular-power Fermat witnesses.')
    save(destination, result)
    print('ALL', len(result['targets']), 'prime factors proved;', v.links,
          'ECPP links;', len(v.small), 'Lucas terminal primes;', result['seconds'], 'seconds', flush=True)


if __name__ == '__main__':
    main()
