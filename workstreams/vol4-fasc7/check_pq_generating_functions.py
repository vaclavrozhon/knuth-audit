#!/usr/bin/env python3
"""Exact finite-dimensional certificates for the ten printed rational functions."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
special = {
    (2,4): ([1,1,1,1,-1,-1], [1,-1,-1,0,-1,0,1]),
    (2,5): ([1,1,2,2,2,-1,-1,-2,-1,-1], [1,-1,0,-1,0,-2,0,0,1,0,1]),
    (3,5): ([1,1,1,2,2,-1,-1,0,-1,-1], [1,-1,-1,0,-1,-2,0,1,0,0,1]),
}
certificates = []
for q in range(2,6):
    for p in range(1,q):
        if p == 1:
            numerator = [1]*q
            denominator = [1,-1] + [0]*(q-2) + [-1]
        elif p == q-1:
            numerator = [1]*q
            denominator = [1]+[-1]*q
        else:
            numerator, denominator = special[p,q]
        states = [x for x in range(1 << q) if x.bit_count() <= p]
        index = {s:i for i,s in enumerate(states)}
        edges = [(index[s],index[t]) for s in states for bit in (0,1)
                 if (t := ((s << 1) & ((1 << q)-1)) | bit) in index]
        d = len(states)
        degree = len(denominator)-1
        def step(v):
            out = [0]*d
            for src,dst in edges:out[dst] += v[src]
            return out
        start = [0]*d
        start[index[0]] = 1
        powers = [start]
        for _ in range(max(10,degree+d-1)):
            powers.append(step(powers[-1]))
        counts = list(map(sum,powers))
        initial_residuals = []
        for n in range(degree):
            residual = sum(denominator[j]*counts[n-j] for j in range(min(n,degree)+1))
            residual -= numerator[n] if n < len(numerator) else 0
            initial_residuals.append(residual)
        v = [sum(denominator[j]*powers[degree-j][i] for j in range(degree+1)) for i in range(d)]
        initial_v = list(v)
        tail_observations = []
        for _ in range(d):
            tail_observations.append(sum(v))
            v = step(v)
        assert not any(initial_residuals)
        assert len(numerator) <= degree
        assert not any(tail_observations)
        certificates.append({'p':p,'q':q,'states':[format(x,f'0{q}b') for x in states],
                             'edges_by_state_index':edges,'dimension':d,
                             'numerator_ascending':numerator,'denominator_ascending':denominator,
                             'initial_residuals':initial_residuals,'tail_start_vector':initial_v,
                             'dimension_many_tail_observations':tail_observations,
                             'counts_0_through_10':counts[:11]})
assert [c['counts_0_through_10'][10] for c in certificates[:3]] == [144,60,504]
result = {'scope':'Ten exact rational identities for1≤p<q≤5. This is a full linear-algebra certificate, not an unbounded extrapolation from a coefficient sample.',
          'proof':'notes/pq-strings-and-exercises-024-025.md',
          'lemma':'If l A^k v=0 for k=0,...,d−1 in a d-dimensional space, the Krylov dependence of v,Av,...,A^d v proves l A^k v=0 for every k. Initial coefficients plus this tail certificate prove QG=P.',
          'certificates':certificates}
(ROOT/'results/pq-generating-functions.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'rational_identities_certified':len(certificates),'largest_dimension':max(c['dimension'] for c in certificates),'length10_counts':[c['counts_0_through_10'][10] for c in certificates[:3]]}))
