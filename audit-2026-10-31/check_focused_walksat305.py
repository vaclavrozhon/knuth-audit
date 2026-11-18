#!/usr/bin/env python3
"""Exact, small verification of the n=12 numerical claim in SAT answer 305.

No Monte Carlo trials: transitions are obtained directly from Algorithm W.
States (a,b) count ones among the first two and remaining n-2 variables.
Permuting variables within either group preserves clauses and the algorithm.
Run with nice -n 15. Only n=4 (printed control) and n=12 are evaluated.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from math import comb
from pathlib import Path
import json


def transition(n, a, b, noise=F(0)):
    bits = [1] * a + [0] * (2-a) + [1] * b + [0] * (n-2-b)
    clauses = [(-(j+1), k+1) for j in range(n) for k in range(n) if j != k]
    clauses.append((-1, -2))

    def true(lit):
        return bits[abs(lit)-1] == (lit > 0)

    unsat, costs = [], [0] * n
    for clause in clauses:
        satisfied = [lit for lit in clause if true(lit)]
        if not satisfied:
            unsat.append(clause)
        elif len(satisfied) == 1:
            costs[abs(satisfied[0])-1] += 1
    if not unsat:
        assert (a, b) == (0, 0)
        return {}
    result = defaultdict(F)
    for clause in unsat:
        indices = [abs(lit)-1 for lit in clause]
        minimum = min(costs[j] for j in indices)
        greedy = [j for j in indices if costs[j] == minimum]
        random_weight = noise if minimum else F(0)
        for j in indices:
            prob = random_weight / len(indices)
            if j in greedy:
                prob += (1-random_weight) / len(greedy)
            delta = 1-2*bits[j]
            target = (a+delta, b) if j < 2 else (a, b+delta)
            result[target] += prob / len(unsat)
    result = {s: p for s, p in result.items() if p}
    assert sum(result.values()) == 1
    return result


def model(n, noise=F(0)):
    return {(a,b): transition(n,a,b,noise) for a in range(3) for b in range(n-1)}


def initial(n, state):
    a,b = state
    return F(comb(2,a)*comb(n-2,b), 2**n)


def greedy_polynomial(n):
    edges = model(n)
    good = {(0,0)}
    while True:
        larger = good | {s for s, row in edges.items() if any(t in good for t in row)}
        if larger == good:
            break
        good = larger
    visiting = set()

    @lru_cache(None)
    def polynomial(s):
        if s == (0,0):
            return (F(1),)
        if s not in good:
            return ()
        assert s not in visiting, 'Unexpected cycle among states that can succeed'
        visiting.add(s)
        result = defaultdict(F)
        for t, prob in edges[s].items():
            for k, coefficient in enumerate(polynomial(t)):
                result[k+1] += prob * coefficient
        visiting.remove(s)
        return tuple(result[k] for k in range(max(result, default=-1)+1))

    result = defaultdict(F)
    for s in edges:
        for k, coefficient in enumerate(polynomial(s)):
            result[k] += initial(n,s)*coefficient
    coefficients = [result[k] for k in range(max(result)+1)]
    prob = sum(coefficients)
    derivative = sum(k*x for k,x in enumerate(coefficients))
    return coefficients, prob, derivative, sorted(set(edges)-good)


def expected_flips(n, noise):
    edges = model(n,noise)
    states = [s for s in edges if s != (0,0)]
    indices = {s:i for i,s in enumerate(states)}
    size = len(states)
    matrix = [[F(i==j) for j in range(size)] + [F(1)] for i in range(size)]
    for s in states:
        for t,prob in edges[s].items():
            if t in indices:
                matrix[indices[s]][indices[t]] -= prob
    for k in range(size):
        pivot = next(i for i in range(k,size) if matrix[i][k])
        matrix[k],matrix[pivot] = matrix[pivot],matrix[k]
        value = matrix[k][k]
        matrix[k] = [x/value for x in matrix[k]]
        for i in range(k+1,size):
            factor = matrix[i][k]
            if factor:
                matrix[i] = [x-factor*y for x,y in zip(matrix[i],matrix[k])]
    solution = [F(0)]*size
    for i in reversed(range(size)):
        solution[i] = matrix[i][-1] - sum(matrix[i][j]*solution[j] for j in range(i+1,size))
    for s,i in indices.items():
        assert solution[i] == 1 + sum(p*solution[indices[t]] for t,p in edges[s].items() if t in indices)
    return sum(initial(n,s)*solution[i] for s,i in indices.items())


def number(x):
    return {'exact': str(x), 'decimal': float(x)}


def main():
    rows = []
    for n in (4,12):
        coefficients, prob, derivative, traps = greedy_polynomial(n)
        if n == 4:
            assert coefficients == [F(k,640) for k in (40,160,164,15,3)]
        cutoffs = {}
        for cutoff in (len(coefficients)-1,n):
            cutoffs[str(cutoff)] = number((derivative+cutoff*(1-prob))/prob)
        rows.append(dict(n=n,coefficients=[str(x) for x in coefficients],
                         success=number(prob),derivative=number(derivative),
                         initializations=number(1/prob),restart_expected_flips=cutoffs,
                         states_unable_to_reach_solution=traps))
    table = []
    for noise in map(F,('.001','.01','.1','.5','.9','.99','.999')):
        value = expected_flips(12,noise)
        table.append(dict(greed_avoidance=str(noise),expected_flips=number(value)))
    result = dict(greedy=rows,n12_positive_noise=table)
    path = Path(__file__).parent/'results/focused-walksat305.json'
    path.write_text(json.dumps(result,indent=2)+'\n')
    for row in rows:
        print('n=',row['n'],'success=',row['success'],'derivative=',row['derivative'])
        print('restart flips=',row['restart_expected_flips'])
    print('Positive-noise table:',[(r['greed_avoidance'],r['expected_flips']['decimal']) for r in table])
    print('Saved',path)


if __name__ == '__main__':
    main()
