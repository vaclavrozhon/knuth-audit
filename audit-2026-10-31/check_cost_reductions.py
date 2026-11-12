"""Exact subset oracle for DLX5, online lower bounds, and 243 counterexample."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,random,subprocess,re
from check_exact_preprocessing import solutions,data
R=Path(__file__).parent/'results/cost_reductions';R.mkdir(exist_ok=True)
rng=random.Random(249);summary=[]
for case in range(1000):
    np=rng.randrange(1,6);ns=rng.randrange(4);rows=[];weights=[]
    for z in range(rng.randrange(1,12)):
        primary=[i for i in range(1,np+1) if rng.randrange(2)] or [rng.randrange(1,np+1)]
        secondary=[(i,rng.randrange(3)) for i in range(np+1,np+ns+1) if rng.randrange(2)]
        row=[(i,0) for i in primary]+secondary;rng.shuffle(row);rows.append(row);weights.append(rng.randrange(21))
    sol=solutions(set(range(1,np+1)),{i:dict(row) for i,row in enumerate(rows)})
    prices=sorted(sum(weights[i] for i in s) for s in sol);K=rng.randrange(1,9)
    raw=data(np,ns,rows).splitlines();raw=[raw[0]]+[line+' |'+str(w) for line,w in zip(raw[1:],weights)]
    p=subprocess.run(['/tmp/knuth-dlx5',f'k{K}','v17','d0'],input='\n'.join(raw)+'\n',text=True,capture_output=True,timeout=10)
    assert 'TIMEOUT' not in p.stderr
    found=[]
    if 'The optimum costs are:' in p.stderr:
        for cost,repeat in re.findall(r'^ \$(\d+)(?: \(repeated (\d+) times\))?$',p.stderr,re.M):found.extend([int(cost)]*int(repeat or 1))
    if 'The optimum cost is' in p.stderr:found=[int(re.search(r'The optimum cost is \$(\d+)',p.stderr).group(1))]
    assert found==prices[:K],(case,raw,prices[:K],found,p.stderr)
    summary.append(dict(case=case,solutions=len(sol),K=K))
# Literal answer249: after each prefix, unseen values are zero.
checks=0
for trial in range(10000):
    d=rng.randrange(1,9);k=rng.randrange(1,7);N=d*k;a=[rng.randrange(40) for _ in range(N)];b=[0]*N;t=l=0
    for c in a:
        p=t;y=0;r=1
        while r*p>0:
            x=b[N-p]
            if c<=x:r=0
            else:
                if p%k==0:l+=x-y
                y=x;b[N-p-1]=x;p-=1
        b[N-p-1]=c;t+=1
        if p%k==0:l+=c-y
        expected=sum(sorted([0]*(N-t)+a[:t])[k-1::k])
        assert l==expected,(trial,t,l,expected);checks+=1
# F078, positive unit weights, two primary items a,b and optional s.
raw='a b | s\na |1\na s |4\nb |1\n'
p=subprocess.run(['/tmp/knuth-dlx5','k2','v17','m1','d0'],input=raw,text=True,capture_output=True,timeout=10)
(R/'243.xcc').write_text(raw);(R/'243.log').write_text(p.stdout+p.stderr)
assert re.findall(r'^ \$(\d+)$',p.stderr,re.M)==['2','5']
report=dict(random_cases=summary,online_prefix_checks=checks,counterexample243=dict(primary=['a','b'],secondary=['s'],weights=[1,1,1],options=[['a'],['a','s'],['b']],d=2,r=2,solutions=[dict(options=[0,2],sum_of_squares=2,squared_deviation=2),dict(options=[1,2],sum_of_squares=5,squared_deviation=1)]))
(R/'verified.json').write_text(json.dumps(report,indent=2)+'\n');print('1000 DLX5 cases agree; online prefix checks:',checks)
