"""Independent set-based memo solver, exact update counts, original DLX6."""
from pathlib import Path
from math import comb,factorial
from functools import lru_cache
import json,subprocess,re,random,os
from check_exact_preprocessing import solutions,data
R=Path(__file__).parent/'results/zdd_counts';R.mkdir(exist_ok=True);BIN=os.environ.get('KNUTH_DLX6_BIN','/tmp/knuth-vol4b-zdd/dlx6')
F=[0,1]
for i in range(100):F.append(F[-1]+F[-2])
def native(names,rows,name):
    source=' '.join(names)+'\n'+'\n'.join(' '.join(names[i] for i in range(len(names)) if s>>i&1) for s in rows)+'\n'
    p=subprocess.run([BIN,'v1','m1','d0'],input=source,text=True,capture_output=True,timeout=120)
    (R/(name+'.xcc')).write_text(source);(R/(name+'.log')).write_text(p.stderr);(R/(name+'.zdd')).write_text(p.stdout)
    assert 'Altogether ' in p.stderr and 'overflow' not in p.stderr.lower()
    return dict(count=int(re.search(r'Altogether (\d+) solution',p.stderr)[1]),updates=int(re.search(r'(\d+) updates',p.stderr)[1]),nodes=int(re.search(r'(\d+) ZDD node',p.stderr)[1]),signatures=sum(map(int,re.search(r'(\d+)\+(\d+) signatures',p.stderr).groups())))
def model(n,rows):
    cache={0:1};updates=branches=0
    def visit(S):
        nonlocal updates,branches
        if S in cache:return cache[S]
        active=[r for r in rows if r&S==r];i=min((i for i in range(n) if S>>i&1),key=lambda i:sum(bool(r>>i&1) for r in active));choices=[r for r in active if r>>i&1];base=[r for r in active if not r>>i&1];updates+=1+sum(r.bit_count()-1 for r in choices);count=0
        for r in choices:
            current=base[:]
            # All rows are stored in increasing item order; after choosing i,
            # cyclic commit walks larger then smaller indices.
            order=[j for j in list(range(i+1,n))+list(range(i)) if r>>j&1]
            for j in order:
                removed=[q for q in current if q>>j&1];updates+=1+sum(q.bit_count()-1 for q in removed);current=[q for q in current if not q>>j&1]
            c=visit(S^r);count+=c;branches+=bool(c)
        cache[S]=count;return count
    count=visit((1<<n)-1);return dict(count=count,updates=updates,nodes=branches+2 if count else 1,signatures=len(cache))
reports=[]
for n in range(2,21):
    rows=[(1<<i)|(1<<j) for i in range(n) for j in range(i+1,n)];name=f'matching-{n}';actual=native([f'v{i}' for i in range(n)],rows,name);direct=model(n,rows);assert actual==direct,(name,actual,direct)
    V=((n-5)*F[n+1]+2*(n+1)*F[n])//5;W=((5*n*n+7*n+25)*F[n+1]-6*(n+1)*F[n])//25
    assert actual['updates']==W-(n%2==0)
    assert actual['nodes']==(V+3 if n%2==0 else 1)
    assert actual['signatures']==F[n+1]+(n%2)
    reports.append(dict(case=name,actual=actual,printed_nodes=V+2 if n%2==0 else 1))
print('Perfect matching formulas checked; even ZDD size needs V+3.',flush=True)
for kind in ['full','bounded']:
 for n in range(1,11):
    rows=[(1<<i)|(1<<(n+j)) for i in range(n) for j in range(n if kind=='full' else min(i+2,n))];name=f'permutation-{kind}-{n}';actual=native([f'X{i}' for i in range(n)]+[f'Y{i}' for i in range(n)],rows,name);direct=model(2*n,rows);assert actual==direct,(name,actual,direct)
    expected=dict(count=factorial(n) if kind=='full' else 2**(n-1),updates=((n*n+3*n+4)*2**n-4)//4 if kind=='full' else (2*n**3+15*n*n+n)//6,nodes=n*2**(n-1)+2 if kind=='full' else n*n+2,signatures=2**n if kind=='full' else n*(n-1)//2+1)
    assert all(actual[k]==v for k,v in expected.items() if k!='signatures' or kind=='full')
    if kind=='bounded':assert actual['signatures']==n*(n+1)//2+1
    reports.append(dict(case=name,actual=actual,printed_formulas=expected))
    print(name,actual,'formula',expected,flush=True)
for n in range(1,10):
    rows=list(range(1,1<<n));name=f'extreme-{n}';actual=native([f'i{i}' for i in range(n)],rows,name);direct=model(n,rows);assert actual==direct,(name,actual,direct)
    V=((72*n-342)*5**n+(375*n-875)*4**n+600*3**n+1800*n*2**n+1550)//3600
    assert actual['updates']==V
    reports.append(dict(case=name,actual=actual,printed_updates=V));print(name,actual['updates'],'formula',V,flush=True)
(R/'formulas.json').write_text(json.dumps(reports,indent=2)+'\n')
# Exact semantics of colored free ZDDs on small arbitrary XCC inputs.
rng=random.Random(254);random_report=[]
for case in range(300):
 np=rng.randrange(1,5);ns=rng.randrange(4);rows=[]
 for _ in range(rng.randrange(1,10)):
  prim=[i for i in range(1,np+1) if rng.randrange(2)] or [rng.randrange(1,np+1)];sec=[(i,rng.randrange(3)) for i in range(np+1,np+ns+1) if rng.randrange(2)];row=[(i,0) for i in prim]+sec;rng.shuffle(row);rows.append(row)
 expected=solutions(set(range(1,np+1)),{i:dict(r) for i,r in enumerate(rows,1)})
 p=subprocess.run([BIN,'v1','m1','d0'],input=data(np,ns,rows),text=True,capture_output=True,timeout=10);nodes={}
 for a,b,c,d in re.findall(r'([0-9a-f]+): \(~([0-9a-f]+)\?([0-9a-f]+):([0-9a-f]+)\)',p.stdout):nodes[int(a,16)]=tuple(int(x,16) for x in [b,c,d])
 @lru_cache(None)
 def walk(v):
  if v==0:return frozenset()
  if v==1:return frozenset([()])
  var,lo,hi=nodes[v]
  if var==0:return walk(hi)
  assert all(var not in a for a in walk(hi))
  return walk(lo)|frozenset(tuple(sorted(a+(var,))) for a in walk(hi))
 actual=set(walk(max(nodes))) if nodes else set();assert actual==expected,(case,p.stdout,p.stderr,expected,actual)
 random_report.append(dict(case=case,solutions=len(expected)))
(R/'colored-random.json').write_text(json.dumps(random_report,indent=2)+'\n');print('300 colored ZDD families agree exactly.',flush=True)
