#!/usr/bin/env python3
"""Operation certificates for C/R with dense schoolbook multiplication.

The recurrence bypasses C2's constant-stop shortcut only for the extra D=1
check. All asymptotic certificates use D>=4; integer cost omits optional M2.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import json
import time
from verify_polynomial_division import add,mul,scale,trim,divide

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/polynomial-c-complexity.json'


def spread(coeffs,D):
    out=[0]*((len(coeffs)-1)*D+1)
    for j,c in enumerate(coeffs):out[j*D]=c
    return trim(out)
def family(D):
    W=[1]*D;A=spread([1,0,1,1,1],D);B=spread([1,-1,-1,1],D)
    u,v=mul(W,A),mul(W,B)
    C=mul(W,spread([-1,1,4],D));T=4**(D-1)
    E=scale(mul(W,spread([11,-7],D)),T)
    H=scale(W,32*(-7)**(D-1))
    return add(u,v),u,[v,C,E,H],W


def measured_pseudo(a,b,optimized,D=None):
    m,n=len(a)-1,len(b)-1;lc=b[-1];r=list(a);q=[0]*(m-n+1)
    costs={'nonzero_integer_products':0,'schoolbook_bit_products':0,'core_subset_products':0,'core_subset_bit_products':0,'peak_bits':0}
    if optimized:
        for j in range(m-n):r[j]*=lc**(m-n-j)
    for k in range(m-n,-1,-1):
        top=r[n+k];q[k]=top*lc**k
        for j in range(n+k-1,-1,-1):
            if optimized and j<k:continue
            x=r[j]
            if x:
                cost=abs(x).bit_length()*abs(lc).bit_length()
                costs['nonzero_integer_products']+=1;costs['schoolbook_bit_products']+=cost
                if D and 1<=k<=D//4 and (D+1)//2<=j<D:
                    assert top==0 and x==-lc**(D-k)
                    costs['core_subset_products']+=1;costs['core_subset_bit_products']+=cost
            r[j]=lc*x-(top*b[j-k] if j>=k else 0)
            costs['peak_bits']=max(costs['peak_bits'],abs(r[j]).bit_length())
        r[n+k]=0
    return trim(q),trim(r[:n]),costs


def run_C(a,b,optimized,D):
    u,v=a,b;g=h=1;seq=[];records=[]
    while v:
        delta=len(u)-len(v)
        selected=(len(u)==3*D and len(v)==2*D)
        q,r,cost=measured_pseudo(u,v,optimized,D if selected else None)
        assert add(mul(v,q),r)==scale(u,v[-1]**(delta+1))
        records.append({'m':len(u)-1,'n':len(v)-1,'delta':delta,'raw_bits':max((abs(c).bit_length() for c in r),default=0),'selected':selected,**cost})
        if not r:break
        den=g*h**delta;assert all(c%den==0 for c in r)
        u,v=v,[c//den for c in r];seq.append(v)
        oldh=h;g=u[-1];h=F(g)**delta*F(oldh)**(1-delta);assert h.denominator==1;h=int(h)
    return seq,records


def block():
    rows=[]
    for D in list(range(1,33))+[48,64,96]:
        U,V,expected,W=family(D);assert len(U)==len(V)==5*D and max(map(abs,U+V))<=2
        variants={}
        for optimized in [False,True]:
            seq,records=run_C(U,V,optimized,D);assert seq==expected
            selected=next(r for r in records if r['selected'])
            assert selected['core_subset_products']==(D//4)*(D//2)
            C,E=expected[1],expected[2]
            _,rr=divide(C,E)
            raw=scale(rr,E[-1]**(D+1))
            assert raw==scale(W,512*(-7)**(D-1)*4**(D*D-1))
            assert raw[0].denominator==1
            assert selected['raw_bits']==abs(raw[0].numerator).bit_length()
            if D>=4:
                assert selected['core_subset_bit_products']>=D**5//10
            variants['optimized' if optimized else 'literal']=selected
        rows.append({'D':D,'input_degree':5*D-1,'input_coefficient_bound':2,'variants':variants})
    return {'family_parameters':len(rows),'algorithm_runs':2*len(rows),'rows':rows,
            'cost_model':'Exact count of digit-pair iterations in dense binary schoolbook multiplication for the first product lc*r_j only. Zero operands omitted. Pre-scaling, second products, divisions, additions and quotient formation excluded from lower count.'}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--resume',action='store_true');args=ap.parse_args()
    if args.resume and OUT.exists():
        old=json.loads(OUT.read_text())
        if old.get('status')=='passed':print('REUSE family');return
    start=time.perf_counter();r=block();r.update(status='passed',seconds=time.perf_counter()-start)
    OUT.write_text(json.dumps(r,indent=2)+'\n');print('PASS family',r['family_parameters'],'runs',r['algorithm_runs'],'seconds',r['seconds'],flush=True)
    for row in r['rows'][-3:]:print(row,flush=True)


if __name__=='__main__':main()
