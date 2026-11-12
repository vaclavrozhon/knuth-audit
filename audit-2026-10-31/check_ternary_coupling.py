"""Exact finite-state audit of MPR exercises 103-104, with published errata."""
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import json


def step(state,bit,backwards):
    f = (1,2,2) if bit else (0,0,1)
    return tuple(state[f[i]] for i in range(3)) if backwards else tuple(f[x] for x in state)


def solve(a,b):
    """Exact Gaussian elimination, independent of any closed-form answer."""
    n = len(b)
    a = [list(row)+[rhs] for row,rhs in zip(a,b)]
    for k in range(n):
        pivot = next(i for i in range(k,n) if a[i][k])
        a[k],a[pivot] = a[pivot],a[k]
        scale = a[k][k]
        a[k] = [x/scale for x in a[k]]
        for i in range(n):
            if i != k:
                scale = a[i][k]
                a[i] = [x-scale*y for x,y in zip(a[i],a[k])]
    return [row[-1] for row in a]


def chain(p,backwards,z=F(1)):
    states = [(0,1,2)]
    for state in states:
        for bit in (0,1):
            nxt = step(state,bit,backwards)
            if nxt[0] != nxt[2] and nxt not in states:
                states.append(nxt)
    n = len(states)
    q = [[F(0)]*n for _ in states]
    r = [[F(0)]*3 for _ in states]
    for i,state in enumerate(states):
        for bit,weight in [(0,1-p),(1,p)]:
            nxt = step(state,bit,backwards)
            if nxt[0] == nxt[2]:
                r[i][nxt[0]] += weight
            else:
                q[i][states.index(nxt)] += weight
    a = [[F(i==j)-z*q[i][j] for j in range(n)] for i in range(n)]
    outputs = [solve(a,[z*row[j] for row in r])[0] for j in range(3)]
    moments = None
    if z == 1:
        means = solve(a,[F(1)]*n)
        second = solve(a,[1+2*sum(q[i][j]*means[j] for j in range(n)) for i in range(n)])
        moments = (means[0],second[0]-means[0]**2)
    return outputs,moments


def full_distribution(length,backwards):
    counts = {(0,1,2):1}
    for _ in range(length):
        nxt = defaultdict(int)
        for state,count in counts.items():
            for bit in (0,1):
                nxt[step(state,bit,backwards)] += count
        counts = nxt
    return counts


def main():
    probabilities = sorted({F(k,d) for d in range(1,13) for k in range(d+1)})
    checks = 0
    for p in probabilities:
        q = 1-p
        expected_back = [q*q/(1-p*q),p*q/(1-p*q),p*p/(1-p*q)]
        expected_forward = [q*q*(1+p)/(1-p*q),F(0),p*p*(1+q)/(1-p*q)]
        for backwards,expected in [(True,expected_back),(False,expected_forward)]:
            outputs,moments = chain(p,backwards)
            assert outputs == expected, (p,backwards,outputs,expected)
            assert moments == (3/(1-p*q)-1,(5-2*p*q)*p*q/(1-p*q)**2)
            for z in (F(1,4),F(1,2),F(3,4)):
                g,_ = chain(p,backwards,z)
                assert sum(g) == (1-p*q*(2-z))*z*z/(1-p*q*z*z)
            checks += 1
    matrix_checks = 0
    for n in range(21):
        back = full_distribution(n,True)
        forward = full_distribution(n,False)
        for i in range(3):
            for j in range(3):
                b = sum(count for state,count in back.items() if state[i]==j)
                f = sum(count for state,count in forward.items() if state[i]==j)
                assert b == f
                floor = (i!=j and n%2==0) or (i+j==2 and n%2==1)
                expected = (2**n)//3 if floor else (2**n+2)//3
                assert b == expected, (n,i,j,b,expected)
                matrix_checks += 1
    for t in range(2,21,2):
        counts = full_distribution(t,False)
        out = [sum(c for state,c in counts.items() if state[0]!=state[2])]
        out += [counts.get((j,j,j),0) for j in range(3)]
        assert out == [2,(2**t-1)//3,(2**t-4)//3,(2**t-1)//3]
    survival = F(1)
    output_zero = F(0)
    for k in range(1,10):
        t = 2**k
        output_zero += survival*F(2**t-1,3*2**t)
        survival *= F(2,2**t)
    assert abs(float(output_zero)-0.427) < .001
    report = {'exercises':'MPR 103-104',
              'status':'All tested formulas pass after the published 2026-03-03 corrections to 104.',
              'distinct_bias_probabilities':len(probabilities),
              'absorbing_chains_checked':checks,
              'moment_and_generating_function_checks':'Exact rational linear systems; both composition directions; three z values per chain.',
              'finite_time_probability_entries_checked':matrix_checks,
              'subroutine_e':'Return probabilities verified at even T=2,4,...,20.',
              'fresh_bits_algorithm_output_zero_approx':float(output_zero),
              'remaining_probability_after_nine_stages_upper_bound':float(survival),
              'known_errata':['2025-01-02: X_n instead of X in 103(e).',
                              '2026-03-03: corrected three output probabilities in both directions in 104.'],
              'limitations':'This tests the finite-state identities and corrected distributions, not a concrete PRNG resetting implementation for 103(f).'}
    (Path(__file__).parent/'results/ternary_coupling.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
