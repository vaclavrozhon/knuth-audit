"""Exact linear-code distributions for TAOCP2 exercise3.6-14.

A phase experiment draws a fresh uniformly random k-bit initial state.
It is distinguished from the book's single adaptively consumed stream.
"""
from pathlib import Path
from math import comb
from fractions import Fraction
from collections import Counter
import json,mpmath as mp
from functools import lru_cache
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/discarded-bits.json'


def linear_masks(k,l,last):
    a=[1<<j for j in range(k)]
    for j in range(k,last+1):a.append(a[j-k]^a[j-l])
    return a


def dependencies(rows):
    basis={};null=[]
    for i,row in enumerate(rows):
        v,c=row,1<<i
        while v:
            b=v.bit_length()-1
            if b not in basis:basis[b]=(v,c);break
            u,d=basis[b];v^=u;c^=d
        if not v:null.append(c)
    allnull=[0]
    for x in null:allnull += [y^x for y in allnull]
    return basis,allnull


def solve(basis,target):
    v,c=target,0
    while v:
        b=v.bit_length()-1
        if b not in basis:return None
        u,d=basis[b];v^=u;c^=d
    return c


@lru_cache(None)
def character_ball(k,h,w):
    # Sum (-1)^dot(v,x) over strings x of weight at most h, |v|=w.
    return sum((-1)**j*comb(w,j)*comb(k-w,i-j)
               for i in range(h+1) for j in range(max(0,i-k+w),min(i,w)+1))


def exact_phase(k,l,quality,phase,h):
    indices=[((phase+j)//k)*quality+(phase+j)%k for j in range(k+1)]
    masks=linear_masks(k,l,indices[-1]);rows=[masks[x] for x in indices]
    basis,dual=dependencies(rows[:k]);_,dualplus=dependencies(rows)
    relation=solve(basis,rows[-1]);chars=[character_ball(k,h,w) for w in range(k+1)]
    q=Fraction(sum(chars[d.bit_count()] for d in dual),1<<k)
    joint=Fraction(sum((-1 if d>>k else 1)*chars[(d&((1<<k)-1)).bit_count()] for d in dualplus),1<<(k+1))
    return dict(rank=len(basis),relation=relation,q=q,joint=joint,p=joint/q if q else None,rows=rows,dual=dual)


def brief(x):
    return {'exact':str(x),'decimal':str(mp.mpf(x.numerator)/x.denominator)}


def main():
    mp.mp.dps=45;data=json.loads(OUT.read_text()) if OUT.exists() else {}
    if 'independent_small_models' not in data:
        # Validate character/dual calculations by full independent state enumeration.
        cases=states=0
        for k,l in [(5,2),(7,3),(8,3),(9,4)]:
            for quality in [2*k,3*k,4*k,10*k+9]:
                for p in range(k):
                    h=2*k//5;x=exact_phase(k,l,quality,p,h);q=joint=0
                    for state in range(1<<k):
                        vals=[(state&v).bit_count()%2 for v in x['rows']]
                        if sum(vals[:k])<=h:q+=1;joint+=vals[-1]
                    assert x['q']==Fraction(q,1<<k) and x['joint']==Fraction(joint,1<<k)
                    cases+=1;states+=1<<k
        data['independent_small_models']={'phase_cases':cases,'complete_state_cases':states}
        OUT.write_text(json.dumps(data,indent=2)+'\n');print('PASS small_models',flush=True)
    results=data.get('linear_models',{})
    for quality in [200,300,400,1009]:
        if str(quality) in results:continue
        rows=[];counts=Counter();minimal=Counter()
        for phase in range(100):
            x=exact_phase(100,37,quality,phase,40)
            relation=x['relation'];key=f"rank{x['rank']}/k{relation.bit_count() if relation is not None else 'independent'}"
            counts[key]+=1
            minterms=min((relation^v).bit_count() for v in x['dual']) if relation is not None else None
            minimal[str(minterms)]+=1
            rows.append({'phase':phase,'rank':x['rank'],'relation_hex':None if relation is None else hex(relation),'terms':None if relation is None else relation.bit_count(),'minimum_terms':minterms,'trigger':str(x['q']),'joint_one':str(x['joint']),'one_given_trigger':str(x['p']),'dual_hex':[hex(v) for v in x['dual']]})
        results[str(quality)]={'census':dict(counts),'minimum_terms_census':dict(minimal),'phases':rows}
        data['linear_models']=results;OUT.write_text(json.dumps(data,indent=2)+'\n')
    expected={2:26,3:11,4:26,6:11,9:11,12:4,20:4,28:3,47:1,74:1,99:1}
    c=results['200']['census']
    assert c=={**{f'rank100/k{k}':v for k,v in expected.items()},'rank99/kindependent':1},c
    for quality,prefix in [(300,{5:26,6:22,10:19}),(400,{3:15,6:37,9:15}),(1009,{7:17,11:10,12:2})]:
        c=results[str(quality)]['minimum_terms_census']
        assert all(c.get(str(k))==v for k,v in prefix.items()),(quality,c)
    # Literal missing-n witness in the recursive expansion, first case k=2.
    init=[int(i==27) for i in range(100)];seq=init[:]
    for i in range(100,202):seq.append(seq[i-100]^seq[i-37])
    assert seq[201]==1 and seq[1]^seq[126]==0 and seq[1]^seq[127]==1
    data['linear_models']=results;data['index_witness']={'initial_one_index':27,'n':1,'X201':seq[201],'printed_X1_xor_X126':seq[1]^seq[126],'correct_X1_xor_X127':seq[1]^seq[127]}
    OUT.write_text(json.dumps(data,indent=2)+'\n');print('PASS linear_models',flush=True)
    phases1009=results['1009']['phases']
    reference=next(x for x in phases1009 if x['minimum_terms']==7 and x['rank']==100)
    p7=Fraction(reference['one_given_trigger'])
    witness=min((x for x in phases1009 if x['minimum_terms']==7 and x['rank']<100 and Fraction(x['one_given_trigger'])!=p7),key=lambda x:x['rank'])
    data['conditional_counterexample']={'quality':1009,'phase':witness['phase'],'rank':witness['rank'],'minimum_relation_terms':7,'iid_seven_term_probability':str(p7),'actual_uniform_state_probability':witness['one_given_trigger'],'scope':'Same sparse relation length does not imply same conditional law when previous100 values are dependent.'}
    q=Fraction(sum(comb(100,i) for i in range(41)),1<<100)
    phases=results['200']['phases']
    avgp=sum(Fraction(x['one_given_trigger']) for x in phases)/100
    fixedq=sum(Fraction(x['trigger']) for x in phases)/100
    fixedjoint=sum(Fraction(x['joint_one']) for x in phases)/100
    assert avgp>Fraction(49,100) and avgp<Fraction(1,2)
    assert round(10**6*q)==28444 and round(10**6*q*avgp)==14043
    # Exact fair-coin tail, evaluated without a Gaussian approximation.
    n=28482;r=13955;c=1;s=1
    for j in range(1,r+1):c=c*(n-j+1)//j;s+=c
    tail=mp.mpf(s)/(1<<n)
    assert mp.mpf('0.0003575')<tail<mp.mpf('0.0003585')
    q25=Fraction(sum(comb(100,i) for i in range(26)),1<<100)
    data['probabilities']={'iid_trigger':brief(q),'mean_conditional_one':brief(avgp),'printed_expression_without_factor':brief(10**6*avgp),'expression_with_factor_q':brief(10**6*q*avgp),'iid_expected_outputs':brief(10**6*q),'iid_expected_zeros_with_avgp':brief(10**6*q*(1-avgp)),'fresh_uniform_phase_trigger':brief(fixedq),'fresh_uniform_phase_joint_one':brief(fixedjoint),'fair_coin_tail_28482_13955':str(tail),'threshold75_iid_outputs_per_million':brief(10**6*q25),'scope':'Fresh uniform state at each fixed phase only; not an exact mean of the book adaptive-million-trial process.'}
    OUT.write_text(json.dumps(data,indent=2)+'\n');print('PASS probabilities',flush=True)
if __name__=='__main__':main()
