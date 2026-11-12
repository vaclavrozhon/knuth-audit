"""Reconstruct only explicitly documented generator inputs for TAOCP 3.3.1 figures."""
from fractions import Fraction as F
from pathlib import Path
import json
import mpmath as mp
from verify_ks import statistics,probability,mm
ROOT=Path(__file__).resolve().parent
mp.mp.dps=70
PARAMS={'B':(0,3141592653,2718281829,2**35),'C':(0,2**7+1,1,2**35),'D':(47594118,23,0,10**8+1),'F':(314159265,2**18+1,1,2**35)}
FIG2={'B':['..o','...','s..','o..','...'],'C':['...','o..','...','.ro','...'],'D':['...','...','oo.','...','...'],'F':['.rr','ssr','rrr','rrs','rrr']}
FIG5P={'B':['...','...','.o.','...','...'],'C':['...','...','.s.','.r.','.o.'],'D':['..r','.oo','.s.','.o.','...'],'F':['ss.','srr','srr','..o','r..']}
FIG5M={'B':['...']*5,'C':['...','..o','...','s..','o.o'],'D':['o..','s..','s..','...','..s'],'F':['.o.','...','...','rrs','rrr']}

def save(out):
    (ROOT/'results/general-test-figures.json').write_text(json.dumps(out,indent=2)+'\n')

def stream(params,length):
    x,a,c,m=params;out=[]
    for _ in range(length):out.append(x);x=(a*x+c)%m
    return out

def transformed_maxima(data,m,t):
    assert len(data)%t==0
    return [F(max(data[i:i+t]),m)**t for i in range(0,len(data),t)]

def chi(data):
    counts=[0]*10
    for x in data:counts[min(9,int(10*x))]+=1
    n=len(data);v=sum((F(y)-F(n,10))**2/F(n,10) for y in counts)
    return counts,v

def code(p):
    tail=min(p,1-p)
    return 'r' if tail<mp.mpf('.01') else 's' if tail<mp.mpf('.05') else 'o' if tail<mp.mpf('.10') else '.'

def main():
    out={'status':'partial','conventions':['include X_0 (offset0)','start X_1 (offset1)'],'figure4_trials':[]}
    for name in ['B','F']:
        params=PARAMS[name];m=params[-1];raw=stream(params,1001)
        for offset in [0,1]:
            data=transformed_maxima(raw[offset:offset+1000],m,5)
            counts,v=chi(data);direct=statistics(data)
            inner=[statistics(data[i:i+10])[0] for i in range(0,200,10)]
            cdfvalues=[probability(10,10*d) for d in inner]
            outer=statistics(cdfvalues)
            row=dict(generator=name,offset=offset,KS200=[mp.nstr(mm(d)*mp.sqrt(200),25) for d in direct],KS20_of_KS10plus=[mp.nstr(mm(d)*mp.sqrt(20),25) for d in outer],chi_square=str(v),counts=counts)
            out['figure4_trials'].append(row);save(out);print('FIG4',row,flush=True)
    out['figure2_5_trials']=[]
    for name,params in PARAMS.items():
        raw=stream(params,3001);m=params[-1]
        for offset in [0,1]:
            for stride_type in ['200t','1000']:
                rows=[];mismatches=0
                for t in range(1,6):
                    got=['','',''];tests=[]
                    for block in range(3):
                        start=offset+block*(200*t if stride_type=='200t' else 1000)
                        data=transformed_maxima(raw[start:start+200*t],m,t)
                        counts,v=chi(data);plus,minus=statistics(data)
                        probs=[mp.gammainc(mp.mpf('4.5'),0,mm(v)/2)/mp.gamma(mp.mpf('4.5')),probability(200,200*mm(plus)),probability(200,200*mm(minus))]
                        for j,p in enumerate(probs):got[j]+=code(p)
                        tests.append(dict(block=block,chi=str(v),counts=counts,KS200=[mp.nstr(mm(d)*mp.sqrt(200),20) for d in [plus,minus]],CDF=[mp.nstr(p,25) for p in probs]))
                    expected=[z[name][t-1] for z in [FIG2,FIG5P,FIG5M]]
                    mismatches+=sum(a!=b for x,y in zip(got,expected) for a,b in zip(x,y))
                    rows.append(dict(t=t,observed_codes=got,printed_codes=expected,tests=tests))
                result=dict(generator=name,offset=offset,stride=stride_type,mismatches=mismatches,total_codes=45,rows=rows)
                out['figure2_5_trials'].append(result);save(out);print('FIG25',name,offset,stride_type,mismatches,flush=True)
    out['status']='completed_comparisons_not_assumed_reproductions';save(out)

if __name__=='__main__':main()
