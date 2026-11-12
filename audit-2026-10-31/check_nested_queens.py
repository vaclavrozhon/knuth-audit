"""Exercise 162: explicit MCC and independent geometric verification."""
from pathlib import Path
from itertools import permutations
from collections import Counter
import argparse,json,re,subprocess,time
ROOT=Path(__file__).parent;OUT=ROOT/'results/nested_queens';OUT.mkdir(exist_ok=True)

def valid(q):
    return all(len({f(r,c) for r,c in q})==len(q) for f in
               [lambda r,c:r,lambda r,c:c,lambda r,c:r+c,lambda r,c:r-c])

def patterns(k):
    return [p for p in permutations(range(k)) if valid(list(enumerate(p)))]

def occurrences(p,k):
    return [(r,min(p[r:r+k])) for r in range(len(p)-k+1)
            if max(p[r:r+k])-min(p[r:r+k])==k-1]

def orbit(p):
    n=len(p);q=set(enumerate(p));out=set()
    for flip in [False,True]:
        a={(r,n-1-c) if flip else (r,c) for r,c in q}
        for _ in range(4):
            out.add(tuple(c for r,c in sorted(a)));a={(c,n-1-r) for r,c in a}
    return out

def overlap_check():
    results=[]
    for k in [4,5,6]:
        ps=patterns(k);tested=0;shared=0
        for p in ps:
            a=set(enumerate(p))
            for q in ps:
                for dr in range(-k+1,k):
                    for dc in range(-k+1,k):
                        if dr==dc==0:continue
                        b={(i+dr,q[i]+dc) for i in range(k)};tested+=1
                        if a&b:shared+=1;assert not valid(a|b),(k,p,q,dr,dc)
        results.append(dict(k=k,patterns=ps,translated_pairs=tested,shared_pairs=shared,compatible_overlaps=0))
    (OUT/'overlap.json').write_text(json.dumps(results,indent=2)+'\n');return results

def mcc(n,k,t):
    primary=[f'r{i}' for i in range(n)]+[f'c{i}' for i in range(n)]+[f'{t}|#']
    secondary=[f'a{i}' for i in range(2*n-1)]+[f'b{i}' for i in range(2*n-1)]
    lines=[' '.join(primary+['|']+secondary)]
    def queen(r,c):return [f'r{r}',f'c{c}',f'a{r+c}',f'b{r-c+n-1}']
    for r in range(n):
        for c in range(n):lines.append(' '.join(queen(r,c)))
    for p in patterns(k):
        for r in range(n-k+1):
            for c in range(n-k+1):lines.append(' '.join(['#']+[s for i in range(k) for s in queen(r+i,c+p[i])]))
    return '\n'.join(lines)+'\n'

def parse_models(out,n,k,t,problem):
    def cyclic_key(words):
        i=words.index('#') if '#' in words else next(i for i,s in enumerate(words) if s.startswith('r'))
        return tuple(words[i:]+words[:i])
    lookup={}
    for line in problem.splitlines()[1:]:
        words=line.split();isblock=words[0]=='#';body=words[1:] if isblock else words
        q=[]
        for i in range(0,len(body),4):
            r,c,a,b=body[i:i+4];r=int(r[1:]);c=int(c[1:])
            assert a==f'a{r+c}' and b==f'b{r-c+n-1}'
            q.append((r,c))
        key=cyclic_key(words);assert key not in lookup
        lookup[key]=(isblock,q)
    models=[];current=[]
    for line in out.splitlines()+['END']:
        if re.match(r'^\d+:$',line) or line=='END':
            if current:
                queens=[];blocks=0
                for option in current:
                    words=option.split(' (')[0].split()
                    isblock,q=lookup[cyclic_key(words)];blocks+=isblock;queens.extend(q)
                assert len(queens)==n and valid(queens) and blocks==t
                p=tuple(c for r,c in sorted(queens));assert len(occurrences(p,k))>=t
                models.append(p);current=[]
        elif line.strip():current.append(line)
    return models

def run(n,k,t,all_models=False,seconds=300):
    name=f'n{n}-q{k}-t{t}';base=OUT/name;problem=mcc(n,k,t);base.with_suffix('.mcc').write_text(problem)
    command=['/tmp/knuth-dlx3-sharp','v1','m1','d10000000000']+([] if all_models else ['t1'])
    start=time.monotonic();print('Starting',name,flush=True)
    try:
        p=subprocess.run(command,input=problem,text=True,capture_output=True,timeout=seconds)
        base.with_suffix('.log').write_text(p.stderr);base.with_suffix('.out').write_text(p.stdout)
        match=re.search(r'Altogether (\d+) solution',p.stderr);assert match,p.stderr
        count=int(match[1]);models=parse_models(p.stdout,n,k,t,problem);assert len(models)==count
        canonical={min(orbit(q)) for q in models}
        result=dict(n=n,k=k,t=t,solutions=count,distinct_models=len(set(models)),orbits=len(canonical),
                    complete=all_models or count==0,seconds=time.monotonic()-start,
                    occurrence_histogram=dict(Counter(len(occurrences(q,k)) for q in set(models))),models=models)
    except subprocess.TimeoutExpired as e:
        for data,suffix in [(e.stderr,'.log'),(e.stdout,'.out')]:
            data=data or b''
            if isinstance(data,bytes):data=data.decode()
            base.with_suffix(suffix).write_text(data)
        result=dict(n=n,k=k,t=t,status='timeout, not UNSAT',seconds=time.monotonic()-start)
    base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='models'}),flush=True);return result

def suite():
    results=[]
    for k,t,minimum,all_models in [(4,2,15,True),(4,3,17,True),(4,4,17,True),(4,5,22,False),
                                  (5,2,16,True),(5,3,19,True),(5,4,20,True),(6,2,22,True),(6,3,25,False)]:
        for n in range(k*t,minimum+1):
            path=OUT/f'n{n}-q{k}-t{t}.json'
            result=json.loads(path.read_text()) if path.exists() else run(n,k,t,all_models and n==minimum)
            results.append(result)
            (OUT/'suite.json').write_text(json.dumps(results,indent=2)+'\n')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--n',type=int);p.add_argument('--k',type=int);p.add_argument('--t',type=int)
    p.add_argument('--all',action='store_true');p.add_argument('--suite',action='store_true');a=p.parse_args()
    if a.suite:overlap_check();suite()
    else:run(a.n,a.k,a.t,a.all)
