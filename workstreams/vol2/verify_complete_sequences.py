"""Exact checks of TAOCP 3.2.2-17,21,29, including the 2001 erratum."""
from itertools import product
from math import gcd
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent


def greedy(m, k):
    """Literal Martin construction, with its final k-1 zeros retained."""
    seq = [0] * k
    seen = {tuple(seq)}
    while True:
        tail = tuple(seq[-(k-1):]) if k > 1 else ()
        for y in range(m-1, -1, -1):
            if tail + (y,) not in seen:
                seen.add(tail + (y,))
                seq.append(y)
                break
        else:
            break
    assert len(seq) == m**k+k-1
    assert k == 1 or seq[-(k-1):] == [0]*(k-1)
    return seq


def windows(seq, k):
    return [tuple(seq[(n+j) % len(seq)] for j in range(k))
            for n in range(len(seq))]


def check_complete(seq, m, k, missing_zero=False):
    target = set(product(range(m), repeat=k))
    if missing_zero:
        target.remove((0,)*k)
    actual = windows(seq, k)
    assert len(actual) == len(target) and set(actual) == target


def is_head(word):
    """Maximal rotation starts at the first nonzero; last digit is nonzero."""
    if not word[-1]:
        return False
    first = next(j for j, x in enumerate(word) if x)
    root = word[first:]+word[:first]
    return all(root >= word[j:]+word[:j] for j in range(len(word)))


def threshold(tail, m):
    good = [x for x in range(1, m) if is_head(tail+(x,))]
    h = max(good, default=0)
    assert good == list(range(1, h+1))
    return h


def xy(word, m):
    """Literal X/Y, with the trivial unary alphabet handled before X2."""
    if m == 1:
        return 0, 0, 0
    k = len(word)
    a = list(word)+[m-1]
    i = next(j for j in range(1, k+1) if a[j] > 0)
    comparisons = 0

    def digit(j):
        return a[1+(j-1) % k]

    for j in range(i+1, k+1):
        if a[k] == 0:
            break
        ell = 0
        while True:
            comparisons += 1
            left, right = digit(i+ell), digit(j+ell)
            if left > right:
                break
            if j+ell == k:
                a[k] = left
            elif left == right:
                pass
            elif j+ell > k:
                a[k] -= 1
                break
            else:
                a[k] = 0
                break
            ell += 1
            if ell == k:
                break
    h = a[k]
    return (a[0] if a[0] > h else a[0]-1 if a[0] else h), h, comparisons


def fkm(m, k):
    """Independent necklace enumeration, complemented Lyndon concatenation."""
    representatives = []
    for d in range(1, k+1):
        if k % d:
            continue
        for w in product(range(m), repeat=d):
            if all(w < w[j:]+w[:j] for j in range(1, d)):
                representatives.append(w)
    representatives.sort()
    return [m-1-x for w in representatives for x in w]


def group(seq, base, q):
    assert gcd(len(seq), q) == 1
    out = []
    for n in range(len(seq)):
        z = 0
        for j in range(q):
            z = base*z + seq[(q*n+j) % len(seq)]
        out.append(z)
    return out


def insert_zero(seq, k):
    # Insert at any run of k-1 zeros. There are m-1 such runs
    # in a type-A sequence; each gives exactly the one new all-zero window.
    if k == 1:
        return [0]+seq
    starts = [n for n in range(len(seq))
              if all(seq[(n+j) % len(seq)] == 0 for j in range(k-1))]
    assert starts
    n = starts[0]
    return seq[:n]+[0]+seq[n:]


def least_period(seq):
    return next(d for d in range(1, len(seq)+1)
                if len(seq) % d == 0 and all(x == seq[j % d] for j, x in enumerate(seq)))


def main():
    if '--resume' in sys.argv:
        cached = json.loads((ROOT/'results/complete-sequences-martin.json').read_text())
        cases, state_checks = cached['cases'], cached['states_checked']
    else:
        cases = []
        state_checks = 0
        for m in range(1, 9):
            for k in range(1, 13):
                if m**k > 20000:
                    break
                seq = greedy(m, k)
                cycle = seq[:m**k]
                check_complete(cycle, m, k)
                other = fkm(m, k)
                assert len(other) == len(cycle)
                # Compare the entire cyclic order, not merely window coverage.
                pos = next(j for j, w in enumerate(windows(other, k)) if w == (0,)*k)
                assert other[pos:]+other[:pos] == cycle
                checked_tails = {}
                max_ops = total_ops = 0
                for j, word in enumerate(windows(cycle, k)):
                    tail = word[1:]
                    if tail not in checked_tails:
                        checked_tails[tail] = threshold(tail, m)
                    expected_h = checked_tails[tail]
                    got, h, ops = xy(word, m)
                    assert max(0, h) == expected_h and got == cycle[(j+k) % len(cycle)]
                    assert ops <= k*(k-1)
                    max_ops = max(max_ops, ops)
                    total_ops += ops
                    state_checks += 1
                cases.append(dict(m=m,k=k,states=len(cycle),max_y_comparisons=max_ops,
                                  total_y_comparisons=total_ops))
        (ROOT/'results/complete-sequences-martin.json').write_text(json.dumps(dict(cases=cases,states_checked=state_checks),indent=2)+'\n')
    printed = '00022212202112102012001110100'
    assert ''.join(map(str, greedy(3, 3))) == printed
    print('Martin / X-Y / necklace models:',len(cases),'cases,',state_checks,'states',flush=True)

    rees = []
    for p,e,k in [(2,1,1),(2,2,3),(2,3,2),(2,4,2),(2,6,2),
                  (3,2,2),(3,3,2),(3,6,1),(5,2,2)]:
        q,r = 1,e
        while r % p == 0:
            q *= p
            r //= p
        b = greedy(p,e*k)[:p**(e*k)]
        a = b[1:]  # The period begins with the unique run of e*k zeros.
        check_complete(a,p,e*k,True)
        grouped_a = group(a,p,q)
        check_complete(grouped_a,p**q,r*k,True)
        grouped_b = insert_zero(grouped_a,r*k)
        check_complete(grouped_b,p**q,r*k)
        final = group(grouped_b,p**q,r)
        check_complete(final,p**e,k)
        rees.append(dict(p=p,e=e,k=k,q=q,r=r,period=len(final)))
    print('Rees grouping:',len(rees),'prime-power cases',flush=True)

    products = []
    for r,s in [(2,3),(2,5),(3,4),(3,5),(4,5),(5,6)]:
        for k in range(1,4):
            x=greedy(r,k)[:r**k];y=greedy(s,k)[:s**k]
            n=(r*s)**k
            original=[s*x[j % len(x)]+y[j % len(y)] for j in range(n)]
            corrected=[(x[j % len(x)]+y[j % len(y)]) % (r*s) for j in range(n)]
            # A separate CRT coordinate encoding also works.
            crt=[(s*pow(s,-1,r)*x[j % len(x)] + r*pow(r,-1,s)*y[j % len(y)]) % (r*s)
                 for j in range(n)]
            check_complete(original,r*s,k)
            check_complete(crt,r*s,k)
            assert max(corrected) <= r+s-2 < r*s-1
            assert (r*s-1,)*k not in set(windows(corrected,k))
            products.append(dict(r=r,s=s,k=k,period=n,erratum_max_digit=max(corrected)))
    # Smallest nontrivial explicit counterexample, independently by residue formulas.
    wrong=[(j%2+j%3)%6 for j in range(6)]
    right=[3*(j%2)+j%3 for j in range(6)]
    assert wrong == [0,2,2,1,1,3] and right == [0,4,2,3,1,5]
    assert least_period(wrong)==6 and least_period(right)==6
    # The wrong sequence cannot obey any order-one deterministic recurrence.
    assert wrong[1]==wrong[2] and wrong[2]!=wrong[3]
    out=dict(status='all_checks_passed',martin_cases=cases,states_checked=state_checks,
             printed_example=printed,rees_cases=rees,product_cases=products,
             C0012=dict(r=2,s=3,k=1,erratum=wrong,original=right,least_period=6,
                        missing_digits=[4,5],conflicting_input=2,successors=[2,1]),
             scope='Finite exact checks accompany proofs; observed operation averages are not asymptotic claims.')
    (ROOT/'results/complete-sequences.json').write_text(json.dumps(out,indent=2)+'\n')
    print('ALL checks passed; product cases:',len(products),flush=True)


if __name__ == '__main__':
    main()
