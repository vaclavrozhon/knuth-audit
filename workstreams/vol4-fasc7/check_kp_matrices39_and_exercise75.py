#!/usr/bin/env python3
"""Exact printed matrix certificates and tiny fixed-cardinality checks of E75.

No general graceful-labeling search: two given matrices, and subsets only
for n<=5. The proof of the recurrence and arbitrary n is in the note.
"""
from collections import Counter
from itertools import combinations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MATRICES = [
    [[0,96,4,93,5,90,11,88,22,84],
     [1,3,13,65,89,14,62,25,81,58],
     [91,9,87,7,77,50,18,72,51,69],
     [95,28,73,12,55,17,82,33,68,27]],
    [[10,56,99,0,100,13,93],
     [33,66,7,77,12,87,59],
     [81,95,1,41,3,94,8],
     [86,2,97,15,70,26,71],
     [89,6,79,52,69,45,24]],
]


def matrix_certificate(a):
    n, r = len(a), len(a[0])
    m = r*n*(n-1)//2 + (r-1)*n
    values = [v for row in a for v in row]
    assert len(set(values)) == n*r and min(values) >= 0 and max(values) <= m
    columns = []
    rows = []
    for j in range(r):
        columns.append([
            {'ends': [[i+1,j+1],[k+1,j+1]],
             'labels': [a[i][j],a[k][j]], 'difference': abs(a[i][j]-a[k][j])}
            for i,k in combinations(range(n),2)])
    for i in range(n):
        rows.append([
            {'ends': [[i+1,j+1],[i+1,j+2]],
             'labels': [a[i][j],a[i][j+1]], 'difference': abs(a[i][j]-a[i][j+1])}
            for j in range(r-1)])
    edges = [e for collection in columns+rows for e in collection]
    assert len(edges) == m
    assert Counter(e['difference'] for e in edges) == Counter(range(1,m+1))
    pos = {a[i][j]:(i,j) for i in range(n) for j in range(r)}
    def adjacent(x,y):
        i,j=pos[x]; k,l=pos[y]
        return j==l or (i==k and abs(j-l)==1)
    assert adjacent(0,m-1) and not (1 in pos and adjacent(1,m))
    reflected = sorted([list(reversed(row)) for row in a])
    literal = lambda b: all(b[i][0]<b[i+1][0] for i in range(n-1)) and b[0][0]<b[0][-1]
    corrected = lambda b: all(b[i][0]<b[i+1][0] for i in range(n-1)) and all(b[0][0]<row[-1] for row in b)
    canonical = sorted(a if min(row[0] for row in a)<min(row[-1] for row in a) else reflected)
    assert corrected(canonical)
    return {'matrix':a,'n':n,'r':r,'m':m,'columns':columns,'rows':rows,
            'positions':{str(v):[i+1,j+1] for v,(i,j) in pos.items()},
            'literal40':literal(a),'corrected40':corrected(a),
            'reflected_sorted':reflected,'reflected_literal40':literal(reflected),
            'reflected_corrected40':corrected(reflected),
            'corrected_canonical':canonical}


def recurrence_sets(d,m):
    """Sets have cardinality (m-1)//2; not the unconstrained literal union."""
    assert m>=1 and m%2==1 and d>=1
    if d>m:return set()
    if d==m:
        sets={()}
        for k in range(1,(m+1)//2):
            sets={tuple(sorted(s+(v,))) for s in sets for v in (k,m-k)}
        return sets
    if d==(m+1)//2:return {tuple(range(d+1,m+1))}
    if d>(m+1)//2:return set()
    top=tuple(range(m-d+1,m+1))
    return {tuple(sorted(s+top)) for s in recurrence_sets(d,m-2*d)}


def direct_sets(d,m):
    n=(m-1)//2
    answer=set()
    for s in combinations([k for k in range(1,m+1) if k!=d],n):
        differences=list(s)+[abs(k-d) for k in s]+[d]
        if Counter(differences)==Counter(range(1,m+1)):answer.add(s)
    return answer


def main():
    matrix_results=[matrix_certificate(a) for a in MATRICES]
    assert [e['difference'] for e in matrix_results[0]['columns'][0]]==[1,91,95,90,94,4]
    assert [e['difference'] for e in matrix_results[0]['rows'][0]]==[96,92,89,88,85,79,77,66,62]
    small=[]
    for n in range(1,6):
        m=2*n+1; cases=[]
        for d in range(1,m+2):
            expected=recurrence_sets(d,m)
            actual=direct_sets(d,m) if d<=m else set()
            assert expected==actual
            cases.append({'d':d,'count':len(actual),'sets':sorted(actual)})
        raw=sum(c['count'] for c in cases)
        formula=sum(2**((d-1)//2) for d in range(1,m+1) if m%d==0)
        formula+=sum(1 for d in range(1,n+2) if (n+1)%d==0)-1
        assert raw==formula
        canonical=raw-2**(n-1)-2*(n==1)
        small.append({'n':n,'m':m,'cases':cases,'raw_count':raw,'canonical_count':canonical})
    assert [row['canonical_count'] for row in small]==[1,4,7,12,20]
    result={'scope':'Every given matrix entry/edge; E75 fixed-cardinality subsets only for n<=5.',
            'matrices39':matrix_results,'exercise75':small,
            'ordinary_union_definition_counterexample':{'d':3,'m':3,'S':[1,2],
                 'union':[1,2,3],'size':2,'required_size':1}}
    path=ROOT/'results/kp-matrices39-and-exercise75.json'
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'matrices':[[r['n'],r['r'],r['m']] for r in matrix_results],
                      'canonical_counts_n1_to5':[r['canonical_count'] for r in small]}))


if __name__=='__main__':main()
