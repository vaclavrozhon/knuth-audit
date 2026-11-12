"""Exercises 168--170,175--178: independent arithmetic and MCC checks."""
from pathlib import Path
from itertools import product,combinations
from functools import cache
from math import comb
import json,random,re,subprocess,time
ROOT=Path(__file__).parent;OUT=ROOT/'results/mcc_arithmetic';OUT.mkdir(exist_ok=True)

@cache
def bell(n):return 1 if n==0 else sum(comb(n-1,k)*bell(k) for k in range(n))

@cache
def recurrence(s,t,distinct):
    if not t:return bell(s)
    sign=-1 if distinct else 1
    value=recurrence(s+2,t-1,distinct)+recurrence(s+1,t-1,distinct)+sign*sum(comb(t-1,k)*recurrence(s,k,distinct) for k in range(t))
    assert value%2==0;return value//2

def coefficient(s,t,distinct):
    """Coefficient in product (1+x^v), or product 1/(1-x^v)."""
    bounds=(1,)*s+(2,)*t;states=list(product(*(range(b+1) for b in bounds)))
    index={v:i for i,v in enumerate(states)};dp=[0]*len(states);dp[0]=1
    for part in states[1:]:
        origins=product(*(range(b-v+1) for b,v in zip(bounds,part)))
        # A descending mixed-radix order is a 0/1 knapsack update; ascending
        # allows repeated parts. The two products count the actual objects.
        if distinct:origins=reversed(list(origins))
        for v in origins:
            if dp[index[v]]:
                target=tuple(a+b for a,b in zip(v,part));dp[index[target]]+=dp[index[v]]
    return dp[-1]

def solve(primary,secondary,options,name=None):
    text=' '.join([f'{a}|{v}' for v,a in primary.items()]+(['|']+secondary if secondary else []))+'\n'
    text+='\n'.join(' '.join(o) for o in options)+'\n'
    p=subprocess.run(['/tmp/knuth-dlx3','v1','d0'],input=text,text=True,capture_output=True)
    match=re.search(r'Altogether (\d+) solution',p.stderr);assert match,p.stderr
    if name:(OUT/(name+'.mcc')).write_text(text);(OUT/(name+'.log')).write_text(p.stderr)
    return int(match[1])

def matrix_model(matrix,targets):
    primary={};secondary=[];rows=[[] for _ in matrix];fill=[]
    for j,target in enumerate(targets):
        h=target//2;A=f'A{j}';B=f'B{j}';primary[A]=target
        if h:primary[B]=h
        for i,row in enumerate(matrix):
            if row[j]:rows[i].append(A)
            if row[j]==2:rows[i].append(B)
        for z in range(h):
            sharp=f'Q{j}_{z}';primary[sharp]=1
            xprev=[f'x{j}_{z-1}'] if z else []
            xnext=[f'x{j}_{z}'] if z<h-1 else []
            fill.extend([[sharp,A]+xprev,[sharp,B]+xnext])
            if xnext:secondary.extend(xnext)
    return primary,secondary,rows,fill

def repeat(alpha,maximum,tag,primary,secondary):
    if maximum==1:return [alpha]
    a=maximum-1;xs=[f'x{tag}_{j}' for j in range(a)];secondary.extend(xs)
    out=[alpha+[xs[0]]]
    for j in range(a):
        q=f'Q{tag}_{j}';primary[q]=1;out.append([q,xs[j]])
        out.append([q]+alpha+([xs[j+1]] if j<a-1 else []))
    return out

def factorization_models():
    factors=[v for v in range(2,361) if 360%v==0];exponents=[]
    for v in factors:
        row=[]
        for prime in [2,3,5]:
            a=0
            while v%prime==0:a+=1;v//=prime
            row.append(a)
        exponents.append(row)
    # The exponent-3 column has the specialized A,B,C gadget of answer178.
    primary={'A':3,'B':1,'C':1,'Q':1,'R':1,'D':2,'E':1,'S':1,'F':1};secondary=['x']
    rows=[]
    for a,b,c in exponents:rows.append(['A','B','C'][:a]+['D','E'][:b]+(['F'] if c else []))
    fill=[['Q','A'],['Q','B','x'],['R','A','x'],['R','C'],['S','D'],['S','E']]
    strict=solve(primary,secondary,rows+fill,'factor360-distinct');assert strict==34
    repeated=[]
    for v,row in zip(factors,rows):repeated+=repeat(row,3 if v==2 else 2 if v in [3,6] else 1,str(v),primary,secondary)
    general=solve(primary,secondary,repeated+fill,'factor360-repeated');assert general==52
    def direct(rest,minimum,distinct):
        total=1 if rest>=minimum else 0
        for v in range(minimum,int(rest**.5)+1):
            if rest%v==0:total+=direct(rest//v,v+distinct,distinct)
        return total
    assert direct(360,2,True)==strict and direct(360,2,False)==general
    return dict(distinct=strict,repeated=general,distinct_options=len(rows+fill),repeated_options=len(repeated+fill),repeated_primary=len(primary),repeated_secondary=len(secondary))

def main():
    start=time.monotonic();cases=[]
    for s in range(6):
        for t in range(6):
            for distinct in [False,True]:
                value=coefficient(s,t,distinct);assert value==recurrence(s,t,distinct)
                cases.append(dict(s=s,t=t,distinct=distinct,count=value))
    rng=random.Random(177);matrix_cases=[]
    for target in [2,3,4,11]:
        for j in range(40):
            N=1+j%3;M=2+j%7
            matrix=[]
            for i in range(M):
                row=tuple(rng.randrange(3) for _ in range(N))
                if not any(row):row=(1,)+row[1:]
                matrix.append(row)
            expected=sum(all(sum(matrix[i][q] for i in range(M) if mask>>i&1)==target for q in range(N)) for mask in range(1<<M))
            primary,secondary,rows,fill=matrix_model(matrix,[target]*N)
            actual=solve(primary,secondary,rows+fill);assert actual==expected,(matrix,target,actual,expected)
            matrix_cases.append(dict(matrix=matrix,target=target,count=actual))
    repetition=[]
    for maximum in range(1,9):
        for wanted in range(maximum+2):
            # A zero multiplicity is handled by omitting the all-zero choice
            # from DLX's input: use an offset mandatory option of multiplicity1.
            primary={'A':wanted+1};secondary=[];options=repeat(['A'],maximum,'r',primary,secondary)
            primary['force']=1;options.append(['force','A'])
            actual=solve(primary,secondary,options);assert actual==(wanted<=maximum)
            repetition.append(dict(maximum=maximum,wanted=wanted,count=actual))
    result=dict(partition_cases=cases,matrix_cases=matrix_cases,repetition_cases=repetition,
                factor360=factorization_models(),seconds=time.monotonic()-start)
    (OUT/'arithmetic.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(partition_cases=len(cases),matrix_cases=len(matrix_cases),repetition_cases=len(repetition),factor360=result['factor360'],seconds=result['seconds'])))

if __name__=='__main__':main()
