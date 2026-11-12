"""Certify printed spectral table by two different exact lattice searches.

Inputs are transcribed from original printed pp106--107. Checkpoint every
dimension and every row, so --resume preserves all successful work.
"""
import argparse
from fractions import Fraction as Q
import json
from pathlib import Path
import time
import mpmath as mp
from spectral import spectral_s,dot
from spectral_independent import shortest_basis,lcg_basis,recurrence_basis,reduced_box_minimum

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/spectral-table.json'
mp.mp.dps=100

PAIRS=[(23,10**8+1),(2**7+1,2**35),(2**18+1,2**35),(3141592653,2**35),
       (137,256),(3141592621,10**10),(3141592221,10**10),(4219755981,10**10),
       (4160984121,10**10),(2**24+2**13+5,2**35),(5**13,2**35),(2**16+3,2**29),
       (1812433253,2**32),(1566083941,2**32),(69069,2**32),(1664525,2**32),
       (314159269,2**31-1),(62089911,2**31-1),(16807,2**31-1),(48271,2**31-1),
       (40692,2**31-249),(44485709377909,2**46),(31167285,2**48),
       (1431853894371298687,(2**31-1)*(2**31-249)),
       (None,(2**31-1)**2),(6364136223846793005,2**64),
       (65430*2**31+1,65430*2**62+2**31-1)]
for b,r,s,step in [(2**24,24,10,389),(2**32-5,43,22,400)]:
    m=b**r-b**s+1
    PAIRS.append((pow(b,-step,m),m))

SQUARED=[
[530,530,530,530,447],
[16642,16642,16642,15602,252],
[34359738368,6,4,4,4],
[2997222016,1026050,27822,1118,1118],
[274,30,14,6,4],
[4577114792,1034718,62454,1776,542],
[4293881050,276266,97450,3366,2382],
[10721093248,2595578,49362,5868,820],
[9183801602,4615650,16686,6840,1344],
[8364058,8364058,21476,16712,1496],
[33161885770,2925242,113374,13070,2256],
[536936458,118,116,116,116],
[4326934538,1462856,15082,4866,906],
[4659748970,2079590,44902,4652,662],
[4243209856,2072544,52804,6990,242],
[4938916874,2322494,63712,4092,1038],
[1432232969,899290,36985,3427,1144],
[1977289717,1662317,48191,6101,1462],
[282475250,408197,21682,4439,895],
[1990735345,1433881,47418,4404,1402],
[1655838865,1403422,42475,6507,1438],
['5.6e13',1180915002,1882426,279928,26230],
['3.2e14',4111841446,17341510,306326,59278],
['2.4e18','4.7e11','1.9e9',3194548,1611610],
[(2**31-1)**2,'1.4e12',643578623,12930027,837632],
['8.8e18','6.4e12','4.1e9',45662836,1846368],
[2**62+1,4281084902,'2.2e9','1.8e9',1862407],
['1.8e173','3.5e115','4.4e86','2e69','5e57'],
['1.6e414','8.6e275','1e207','2e165','8e137']]
LOGS='''
4.5 4.5 4.5 4.5 4.4
7.0 7.0 7.0 7.0 4.0
17.5 1.3 1.0 1.0 1.0
15.7 10.0 7.4 5.1 5.1
4.0 2.5 1.9 1.3 1.0
16.0 10.0 8.0 5.4 4.5
16.0 9.0 8.3 5.9 5.6
16.7 10.7 7.8 6.3 4.8
16.5 11.1 7.0 6.4 5.2
11.5 11.5 7.2 7.0 5.3
17.5 10.7 8.4 6.8 5.6
14.5 3.4 3.4 3.4 3.4
16.0 10.2 6.9 6.1 4.9
16.1 10.5 7.7 6.1 4.7
16.0 10.5 7.8 6.4 4.0
16.1 10.6 8.0 6.0 5.0
15.2 9.9 7.6 5.9 5.1
15.4 10.3 7.8 6.3 5.3
14.0 9.3 7.2 6.1 4.9
15.4 10.2 7.8 6.1 5.2
15.3 10.2 7.7 6.3 5.2
22.8 15.1 10.4 9.0 7.3
24.1 16.0 12.0 9.1 7.9
30.5 19.4 15.4 10.8 10.3
31.0 20.2 15.6 11.8 9.8
31.5 21.3 16.0 12.7 10.4
31.0 16.0 15.5 15.4 10.4
288. 192. 144. 115. 95.9
688. 458. 344. 275. 229.
'''
MERITS='''
2e-5 5e-4 0.01 0.34 4.62
2e-6 3e-4 0.04 4.66 2e-3
3.14 2e-9 2e-9 5e-9 1e-8
0.27 0.13 0.11 0.01 0.21
3.36 2.69 3.78 1.81 1.29
1.44 0.44 1.92 0.07 0.08
1.35 0.06 4.69 0.35 6.98
3.37 1.75 1.20 1.39 0.28
2.89 4.15 0.14 2.04 1.25
8e-4 2.95 0.07 5.53 0.50
3.03 0.61 1.85 2.99 1.73
3.14 1e-5 1e-4 1e-3 0.02
3.16 1.73 0.26 2.02 0.89
3.41 2.92 2.32 1.81 0.35
3.10 2.91 3.20 5.01 0.02
3.61 3.45 4.66 1.31 1.35
2.10 1.66 3.14 1.69 3.60
2.89 4.18 5.34 7.13 7.52
0.41 0.51 1.08 3.22 1.73
2.91 3.35 5.17 3.15 6.63
2.42 3.24 4.15 8.37 7.16
2.48 2.42 0.25 3.10 1.33
3.60 3.92 5.27 0.97 3.82
1.65 0.29 3.88 0.02 4.69
3.14 1.49 0.44 0.69 0.66
1.50 3.68 4.52 4.02 1.76
5e-5 4e-9 8e-5 2.56 1e-4
2.27 3.46 3.92 2.49 2.98
3.10 2.04 2.85 1.15 1.33
'''
LOGS=[line.split() for line in LOGS.strip().splitlines()]
MERITS=[line.split() for line in MERITS.strip().splitlines()]


def rounded_interval(s):
    """Exact rational interval for rounding to the displayed final digit."""
    mant,exponent=(s.split('e')+[None])[:2] if 'e' in s else (s,'0')
    digits=len(mant.split('.')[1]) if '.' in mant else 0
    unit=Q(10)**(int(exponent)-digits)
    mid=Q(s)
    return mid-unit/2,mid+unit/2


def compare_rounding(value,s):
    lo,hi=rounded_interval(s)
    if isinstance(value,int):return lo<=value<=hi
    return mp.mpf(lo.numerator)/lo.denominator<=value<=mp.mpf(hi.numerator)/hi.denominator


def save(result):
    OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')


def run(resume):
    result=json.loads(OUT.read_text()) if resume and OUT.exists() else {'rows':{}}
    for line,(a,m) in enumerate(PAIRS,1):
        key=str(line);row=result['rows'].setdefault(key,dict(a=a,m=m,dimensions={}))
        if row.get('complete'):continue
        start=time.monotonic()
        if a is not None and 'S' not in row:
            row['S']=spectral_s(a,m,6,trace=(line==6))
            row['S']['values']={str(t):d for t,d in row['S']['values'].items()}
            save(result)
        for t in range(2,7):
            if str(t) in row['dimensions']:continue
            if a is None:
                basis=recurrence_basis(271828183,-314159269,2**31-1,t)
                book=reduced_box_minimum(basis,2**31-1)
            else:
                basis=lcg_basis(a,m,t)
                book=row['S']['values'][str(t)]
            independent=shortest_basis(basis)
            assert book['squared']==independent['squared'],(line,t,book,independent)
            if a is None:
                assert book['vectors']==independent['vectors']
            elif t>2:
                v=book['minimum_vectors']
                both=sorted(v+[[-x for x in w] for w in v])
                assert both==independent['vectors'],(line,t)
            squared=independent['squared']
            # Keep differences as evidence; do not turn a printed mismatch
            # into a failed computation or silently replace the input.
            expected=SQUARED[line-1][t-2]
            sq_ok=(squared==expected) if isinstance(expected,int) else compare_rounding(squared,expected)
            lg=mp.log(squared,2)/2
            merit=mp.pi**(mp.mpf(t)/2)*mp.mpf(squared)**(mp.mpf(t)/2)/(mp.gamma(1+mp.mpf(t)/2)*m)
            printed_lg=LOGS[line-1][t-2]
            corrected_lg='14.6' if (line,t)==(25,4) else printed_lg
            row['dimensions'][str(t)]=dict(squared=squared,independent=independent,
                printed_squared=expected,squared_matches=sq_ok,
                lg_nu=mp.nstr(lg,50),printed_lg=printed_lg,corrected_lg=corrected_lg,
                lg_matches=compare_rounding(lg,corrected_lg),
                merit=mp.nstr(merit,50),printed_merit=MERITS[line-1][t-2],
                merit_matches=compare_rounding(merit,MERITS[line-1][t-2]),
                generic_box=book if a is None else None)
            save(result)
            print('dimension',line,t,'squared',squared,'matches',sq_ok,
                  row['dimensions'][str(t)]['lg_matches'],row['dimensions'][str(t)]['merit_matches'],flush=True)
        row['complete']=True;row['seconds']=time.monotonic()-start;save(result)
    result['complete']=True
    result['rounding_scope']='Exact integer squared minima and rational comparison for approximate squared entries; logarithms/merits evaluated at100 decimal digits, not interval-certified yet.'
    save(result)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--resume',action='store_true');args=ap.parse_args()
    run(args.resume)
