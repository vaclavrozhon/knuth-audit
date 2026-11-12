#!/usr/bin/env python3
"""Small new certificates for exercises9/14, reusing saved base primes.

No MMIX execution, historical verifier rerun or resieving of 2..3571.
The new sieve interval is3572..65537. Variant profiles use closed stopping
criteria and the already saved exact prime/composite classification.
"""
import hashlib
import json
import os
from pathlib import Path

BASE = Path(__file__).resolve().parent


def save(name, data):
    (BASE / 'results' / name).write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def main():
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15, 'Use nice -n15.'
    original = BASE / 'results/printed-prime-indices.json'
    prior_profile = BASE / 'results/program-p-profile.json'
    cert = json.loads(original.read_text())
    old = json.loads(prior_profile.read_text())
    primes = cert['all_primes_through_last_entry']
    assert len(primes) == 500 and primes[-1] == 3571
    inherited = dict(path=str(original.relative_to(BASE)),
                     sha256=hashlib.sha256(original.read_bytes()).hexdigest())

    lo, hi = 3572, 65537
    divisor = [0] * (hi - lo + 1)
    progressions = []
    for p in primes:
        if p * p > hi:
            break
        first = max(p * p, ((lo + p - 1) // p) * p)
        progressions.append(dict(prime=p, first=first,
                                 last=hi - hi % p, step=p))
        for n in range(first, hi + 1, p):
            if divisor[n - lo] == 0:
                divisor[n - lo] = p
    extension = [n for n in range(lo, hi + 1) if divisor[n - lo] == 0]
    all_primes = primes + extension
    assert all(p == 0 or 2 <= p < n and n % p == 0
               for n, p in zip(range(lo, hi + 1), divisor))
    assert all_primes[1228:1230] == [9973, 10007]
    assert all_primes[6541:6543] == [65521, 65537]
    assert len(all_primes) == 6543
    save('exercise-0132-prime-bounds.json', dict(
        scope='Exact first five-digit and first non-wyde prime indices; new interval3572..65537 only.',
        proof='notes/exercises-1.3.2-009-014-recovery.md', inherited=inherited,
        new_interval=[lo, hi], marking_progressions=progressions,
        new_composite_count=sum(p != 0 for p in divisor),
        new_prime_count=len(extension), all_new_primes=extension,
        composite_divisor_vector_sha256=hashlib.sha256(
            bytes(divisor)).hexdigest(),
        four_digit_prime_count=1229, first_five_digit_prime=dict(index=1230, value=10007),
        wyde_prime_count=6542, last_wyde_prime=dict(index=6542, value=65521),
        first_non_wyde_prime=dict(index=6543, value=65537)))

    rank = {p: i + 1 for i, p in enumerate(primes)}
    factors = dict(cert['composite_divisor_witnesses'])
    rows = []
    for row in old['candidate_stopping_certificates']:
        n = row['n']
        if n in factors:
            p_sqrt = p_offset = factors[n]
            reason = 'least prime divisor'
        else:
            p_sqrt = next(p for p in primes[1:] if p * p >= n)
            p_offset = next(p for p in primes[1:]
                            if 100000000 * n <= (10000 * p + 19999) ** 2)
            reason = 'prime; first exact stopping threshold'
        rows.append(dict(n=n, reason=reason, inherited_tests=row['tests'],
                         sqrt_stop=p_sqrt, sqrt_tests=rank[p_sqrt] - 1,
                         offset_stop=p_offset, offset_tests=rank[p_offset] - 1))
    t0 = old['division_tests']
    t1 = sum(r['sqrt_tests'] for r in rows)
    t2 = sum(r['offset_tests'] for r in rows)
    c = len(rows)
    assert (t0, t1, t2, c) == (9538, 9597, 9357, 1784)
    first_saving = 53 * t0 - 14 * (t1 - t0) - 44 * c
    short_saving = 4 * t1 + c - 4 * 500 - 3
    offset_delta = 4 * c - 14 * (t1 - t2)
    assert (first_saving, short_saving, offset_delta) == (426192, 38169, 3776)
    # Round19999/10000 to the nearest binary64 in [1,2), using integer arithmetic.
    q, r = divmod(19999 * 2**52, 10000)
    sig = q + (2 * r > 10000 or (2 * r == 10000 and q % 2))
    bits = (1023 << 52) + sig - 2**52
    save('exercise-0132-fp-profiles.json', dict(
        scope='Exact closed path counts for exercise14; no MMIX or old verifier execution.',
        proof='notes/exercises-1.3.2-009-014-recovery.md', inherited=inherited,
        prior_profile=dict(path=str(prior_profile.relative_to(BASE)),
                           sha256=hashlib.sha256(prior_profile.read_bytes()).hexdigest()),
        candidates=c, old_tests=t0, sqrt_tests=t1, offset_sqrt_tests=t2,
        first_variant_saving=dict(oops=first_saving, mems=-(t1 - t0)),
        short_float_additional_saving_oops=short_saving,
        offset_vs_first_variant_extra=dict(oops=offset_delta, mems=-(t1 - t2)),
        decimal_1_9999_nearest_binary64_hex=f'{bits:016x}',
        rounding_numerator_remainder=r, stopping_certificates=rows))
    print(json.dumps(dict(new_sieve_interval=[lo, hi], five_digit_index=1230,
                          wyde_primes=6542, sqrt_tests=t1, offset_tests=t2,
                          first_saving_oops=first_saving,
                          short_additional_saving_oops=short_saving)))


if __name__ == '__main__':
    main()
