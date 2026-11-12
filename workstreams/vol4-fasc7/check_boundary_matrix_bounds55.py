#!/usr/bin/env python3
"""Complete finite q=3..6 edge cases of the all-q proof in the note."""
from itertools import product
import json
from check_clasp_projection import ROOT

A=((1,1),(1,0));B=((1,-1),(-1,0));X=((1,0),(0,-1));I=((1,0),(0,1))

def multiply(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def tr(a):return a[0][0]+a[1][1]
def det(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]

def main():
    c=multiply(multiply(A,X),A);d=multiply(multiply(c,X),A)
    assert c==((0,1),(1,1)) and d==((-1,0),(0,1))
    aba=multiply(multiply(A,B),A);bab=multiply(multiply(B,A),B)
    assert aba==bab==d
    fib=[0,1];lucas=[2,1]
    for _ in range(6):fib.append(sum(fib[-2:]));lucas.append(sum(lucas[-2:]))
    cases=[]
    for q in range(3,7):
        words=[]
        for letters in product('AB',repeat=q):
            m=I
            for letter in letters:m=multiply(m,A if letter=='A' else B)
            t=tr(m);total=t+lucas[q]
            assert det(m)==(-1)**q and 2*fib[q]<=total<=2*lucas[q]
            words.append({'word':''.join(letters),'matrix':m,'trace':t,'labelings':total})
        cases.append({'q':q,'all_words':words,'minimum_trace':min(w['trace'] for w in words),
                      'maximum_trace':max(w['trace'] for w in words),
                      'minimum_labelings':min(w['labelings'] for w in words),
                      'maximum_labelings':max(w['labelings'] for w in words)})
    out={'scope':'All120 binary matrix words of lengths3–6, filling exactly the small cases excluded by the printed q>6 estimate. This is not a substitute for the separate all-q proof.',
         'AXA':c,'AXAXA':d,'ABA_equals_BAB':aba,'cases':cases}
    (ROOT/'results/boundary-matrix-bounds55.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps([{k:v for k,v in r.items() if k!='all_words'} for r in cases],indent=2))

if __name__=='__main__':main()
