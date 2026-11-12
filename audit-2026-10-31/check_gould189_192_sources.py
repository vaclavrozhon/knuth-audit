"""New source details only: exact rational signs in figure190 and printed191.

Never recompute the accepted n=4000..4100 census or the old quadratures.
The interval for g uses rational series and the DLMF5.11(ii) remainder bound.
"""
from collections import Counter
from datetime import datetime,timezone
from decimal import Decimal,localcontext
from fractions import Fraction as Q
from math import comb,factorial
from pathlib import Path
import json,time,xml.etree.ElementTree as ET
from extract_chain150 import points
from puzzle_xcc import save,sha

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/gould189_192'


def bernoulli(n):
    b=[Q(1)]
    for m in range(1,n+1):
        b.append(-sum((comb(m+1,j)*b[j] for j in range(m)),Q())/(m+1))
    assert b[1:5]==[Q(-1,2),Q(1,6),Q(0),Q(-1,30)]
    return b


def constant_interval():
    # log2=2 atanh(1/3); positive tail bounded by a geometric series.
    jmax=100
    log2lo=2*sum((Q(1,(2*j+1)*3**(2*j+1)) for j in range(jmax)),Q())
    log2hi=log2lo+Q(9,4*(2*jmax+1)*3**(2*jmax+1))
    n,m=64,32
    b=bernoulli(2*m+2)
    h=sum((Q(1,k) for k in range(1,n+1)),Q())
    correction=sum((b[2*k]/(2*k*n**(2*k)) for k in range(1,m+1)),Q())
    next_term=b[2*m+2]/((2*m+2)*n**(2*m+2))
    base=h-Q(1,2*n)+correction
    # psi(N)=H_(N-1)-gamma; DLMF5.11.2, remainder has sign of first omitted term.
    gamma_lo=base-6*log2hi+min(0,next_term)
    gamma_hi=base-6*log2lo+max(0,next_term)
    # E1(1)=-gamma-sum((-1)^k/(k*k!)); alternating-series bound.
    partial=sum((Q((-1)**k,k*factorial(k)) for k in range(1,101)),Q())
    sum_lo=partial-Q(1,101*factorial(101));sum_hi=partial
    e1lo=-gamma_hi-sum_hi;e1hi=-gamma_lo-sum_lo
    elo=sum((Q(1,factorial(k)) for k in range(101)),Q())
    ehi=elo+Q(1,100*factorial(100))
    lo,hi=elo*e1lo,ehi*e1hi
    assert 0<lo<hi<1 and hi-lo<Q(1,10**75)
    return lo,hi,dict(log2_terms=100,gamma_N=n,gamma_Bernoulli_terms=m,
                     exponential_terms=101,E1_terms=100,
                     lower=str(lo),upper=str(hi),width=str(hi-lo),
                     basis=['DLMF5.11.2 and5.11(ii)','DLMF6.6.2','g=e*E1(1)'])


def triangle(gould=False):
    rows={1:[0 if gould else 1]}
    for n in range(2,101):
        row=[0]*n
        row[-1]=1 if gould and n==2 else rows[n-1][0]
        for k in range(n-2,-1,-1):row[k]=rows[n-1][k]+row[k+1]
        rows[n]=row
    return rows


def source_cells(path):
    root=ET.parse(path).getroot()
    strokes=list(root.iter('stroke_path'));assert len(strokes)==1
    t=strokes[0];ps=[p for q in t for p in points(t,q)]
    x0=min(x for x,y in ps);y0=min(y for x,y in ps)
    width=max(x for x,y in ps)-x0;height=max(y for x,y in ps)-y0
    assert abs(width-60)<.002 and abs(height-60)<.002
    unit=width/100
    # Rectangular black source fills may merge adjacent cells in the book PDF.
    # The PS draft retains individual cells. Decode both independently.
    black=set();rectangles=0
    for t in root.iter('fill_path'):
        if t.get('color')!='0 0 0':continue
        ps=[p for q in t for p in points(t,q)]
        assert len(ps)==4
        xs=sorted({round(x,4) for x,y in ps});ys=sorted({round(y,4) for x,y in ps})
        assert len(xs)==len(ys)==2
        assert x0-.002<=xs[0]<xs[1]<=x0+width+.002
        assert y0-.002<=ys[0]<ys[1]<=y0+height+.002
        grid=[(xs[0]-x0)/unit,(xs[1]-x0)/unit,(ys[0]-y0)/unit,(ys[1]-y0)/unit]
        assert all(abs(a-round(a))<.003 for a in grid)
        a,b,c,d=map(round,grid);rectangles+=1
        for n0 in range(c,d):
            for k0 in range(a,b):
                cell=(n0+1,k0+1)
                assert 1<=cell[1]<=cell[0]<=100 and cell not in black,cell
                black.add(cell)
    return black,dict(origin=[x0,y0],unit=unit,rectangles=rectangles,black_cells=len(black),
                      rows=[''.join('+' if (n,k) in black else '-' for k in range(1,n+1)) for n in range(1,101)])


def main():
    assert not (OUT/'source-checked.json').exists()
    started=time.monotonic();lo,hi,certificate=constant_interval()
    bell,gould=triangle(),triangle(True)
    expected=set();gaps=[]
    for n in range(1,101):
        for k in range(1,n+1):
            ratio=Q(gould[n][k-1],bell[n][k-1])
            assert ratio<lo or ratio>hi,(n,k)
            if ratio>hi:expected.add((n,k));gaps.append(ratio-hi)
            else:gaps.append(lo-ratio)
    figures={}
    for name in ['original-489','draft-179']:
        actual,data=source_cells(OUT/(name+'.xml'))
        assert actual==expected,(name,len(actual^expected),sorted(actual^expected)[:10])
        figures[name]=data
    old=json.loads((ROOT/'results/gould_constants.json').read_text())
    probabilities=['.59635','.26597','.09678','.03009','.00823','.00202','.00045','.00009','.00002']
    comparisons=[]
    for k,(printed,saved) in enumerate(zip(probabilities,old['probabilities_1_to_12']),1):
        with localcontext() as ctx:
            ctx.prec=60
            assert Decimal(saved).quantize(Decimal('.00001'))==Decimal(printed)
        comparisons.append(dict(k=k,printed=printed,saved_accepted=saved))
    # Exact counterexamples for both independent domain restrictions in F142.
    assert 1-Q(1,2)==Q(1,2) and Q(2)**2==4 and 1-Q(2)==-1
    assert 1-Q(2)==-1 and Q(1,2)**(-1)==2 and 1-Q(2)==-1
    counterexamples=[dict(a='4',b='1/2',x='1',exponent='1/2',power='2',F='-1'),
                     dict(a='1/2',b='2',x='1',exponent='-1',power='2',F='-1')]
    dependencies=['results/gould_constants.json','results/gould_signs.json','results/extreme_cover.json',
                  'check_gould_constants.py','check_gould_signs.py','extract_chain150.py','extract_jigsaw.py',
                  'sources/gould189_192/dlmf5-11.html','sources/gould189_192/dlmf6-6.html']
    with localcontext() as ctx:
        ctx.prec=12;gap=Decimal(min(gaps).numerator)/Decimal(min(gaps).denominator)
        width=Decimal((hi-lo).numerator)/Decimal((hi-lo).denominator)
    data=dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),
              constant_certificate=certificate,interval_width_decimal=str(width),
              minimum_ratio_separation_lower_bound=str(min(gaps)),minimum_separation_decimal=str(gap),
              exact_signs=5050,black_positive=len(expected),white_negative=5050-len(expected),
              figures=figures,printed191=comparisons,F142=counterexamples,
              trace_hashes={f'results/gould189_192/{n}.xml':sha(OUT/(n+'.xml')) for n in figures},
              dependencies={p:sha(ROOT/p) for p in dependencies},
              accepted_high_n_sign_runs_repeated=0,accepted_quadratures_repeated=0,solver_calls=0,
              wall_seconds=time.monotonic()-started,
              scope='All5050 figure cells in both versions certified with rational bounds. General190 sign research problem not solved; old4000..4100 signs retained as stable numerical evidence, not an interval proof.')
    save(OUT/'source-checked.json',data)
    print('PASS:5050 exact signs per version;',len(expected),'black;',data['wall_seconds'],'seconds')


if __name__=='__main__':main()
