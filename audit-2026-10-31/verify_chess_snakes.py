"""Independent subset and geometric checks for the direct snake enumerator."""
from pathlib import Path
from collections import Counter
from itertools import combinations
import json,subprocess
ROOT=Path(__file__).parent;OUT=ROOT/'results/chess_snakes';OUT.mkdir(exist_ok=True)

def adjacency(n,piece):
    a=[0]*(n*n)
    for v in range(n*n):
        for w in range(n*n):
            dr,dc=abs(v//n-w//n),abs(v%n-w%n)
            yes=dict(king=max(dr,dc)==1,knight=sorted((dr,dc))==[1,2],bishop=dr==dc and dr>0,
                     rook=(dr==0) != (dc==0),queen=(dr==dc or dr==0 or dc==0) and v!=w)[piece]
            if yes:a[v]|=1<<w
    return a

def orbit(mask,n):
    q={(v//n,v%n) for v in range(n*n) if mask>>v&1};out=set()
    for flip in [False,True]:
        a={(r,n-1-c) if flip else (r,c) for r,c in q}
        for _ in range(4):
            out.add(sum(1<<(r*n+c) for r,c in a));a={(c,n-1-r) for r,c in a}
    return out

def classify(mask,a):
    vertices=[i for i in range(len(a)) if mask>>i&1];degrees=[(a[i]&mask).bit_count() for i in vertices]
    if all(d==2 for d in degrees):kind='cycle'
    elif degrees.count(1)==2 and all(d in [1,2] for d in degrees):kind='path'
    else:return None
    seen=1<<vertices[0];todo=seen
    while todo:
        bit=todo&-todo;todo-=bit;v=bit.bit_length()-1;new=a[v]&mask&~seen;seen|=new;todo|=new
    return kind if seen==mask else None

def small():
    cases=[]
    for n in [2,3,4]:
        for piece in ['king','knight','bishop','rook','queen']:
            a=adjacency(n,piece);expected={'path':set(),'cycle':set()}
            for mask in range(1<<(n*n)):
                if mask.bit_count()<3:continue
                kind=classify(mask,a)
                if kind:expected[kind].add(min(orbit(mask,n)))
            for kind in ['path','cycle']:
                file=OUT/f'validation-{n}-{piece}-{kind}.jsonl'
                p=subprocess.run(['/tmp/knuth-chess-snakes',str(n),piece,kind,'3','-1',str(file)],text=True,capture_output=True,check=True)
                rows=[json.loads(s) for s in file.read_text().splitlines()];actual={min(orbit(mask,n)) for start,length,mask in rows}
                assert actual==expected[kind],(n,piece,kind,len(actual),len(expected[kind]))
                for start,length,mask in rows:assert mask.bit_count()==length and classify(mask,a)==kind
                cases.append(dict(n=n,piece=piece,kind=kind,D4_classes=len(actual)))
    (OUT/'validation.json').write_text(json.dumps(cases,indent=2)+'\n');print('Validated',len(cases),'cases')

def large():
    results=[]
    for path in sorted(OUT.glob('*-start*.json')):
        if path.name.endswith('.verified.json'):continue
        d=json.loads(path.read_text())
        if 'status' in d:continue
        n=d['board_side'];a=adjacency(n,d['piece']);classes={};models=set();hist=Counter()
        for start,length,mask in map(json.loads,path.with_suffix('.jsonl').read_text().splitlines()):
            assert mask.bit_count()==length and classify(mask,a)==d['mode']
            if d['mode']=='path':assert (a[start]&mask).bit_count()==1
            models.add(mask);hist[length]+=1;classes.setdefault(length,set()).add(min(orbit(mask,n)))
        assert {str(k):v for k,v in hist.items()}==d['counts']
        result=dict(file=path.name,piece=d['piece'],mode=d['mode'],start=d['start'],models=len(models),D4_classes={k:len(v) for k,v in classes.items()})
        path.with_suffix('.verified.json').write_text(json.dumps(result,indent=2)+'\n');results.append(result)
    (OUT/'verified-summary.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(results,indent=2))

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--small',action='store_true');a=p.parse_args()
    if a.small:small()
    else:large()
