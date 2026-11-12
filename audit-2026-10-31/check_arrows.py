"""Read arrow polygons from PDF, then audit the answer's propagation routine."""
from pathlib import Path
from itertools import product
from math import prod
import xml.etree.ElementTree as ET
import subprocess, tempfile, hashlib, json, random, time

ROOT=Path(__file__).resolve().parent
RESULT=ROOT/'results/factor_puzzles'
PDF=ROOT.parent/'books/taocp-vol4b-ed1-print2-2022.pdf'

def extract():
    boards=[]
    with tempfile.TemporaryDirectory(prefix='knuth-vol4b-arrow-') as directory:
        for page,scale in [(60,7.1982),(410,4.5592)]:
            path=Path(directory)/f'{page}.xml'
            subprocess.run(['mutool','draw','-F','trace','-o',str(path),str(PDF),str(page+20)],
                           check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            root=ET.parse(path).getroot();arrows=[]
            for p in root.iter('stroke_path'):
                points=[(float(n.get('x')),float(n.get('y'))) for n in p if n.tag in ('moveto','lineto')]
                if len(points)!=5:continue
                a,b,c,d,e,f=map(float,p.get('transform').split())
                points=[(a*x+c*y+e,b*x+d*y+f) for x,y in points]
                cx=sum(x for x,y in points[1:])/4;cy=sum(y for x,y in points[1:])/4
                if max(abs(x-cx)+abs(y-cy) for x,y in points)>=15:continue
                vx,vy=points[0][0]-cx,points[0][1]-cy
                dx=0 if abs(vx)<.01 else (1 if vx>0 else -1)
                dy=0 if abs(vy)<.01 else (1 if vy>0 else -1)
                arrows.append((cx,cy,dx,dy))
            assert len(arrows)==100
            arrows.sort(key=lambda p:(round(p[1],1),p[0]));digits=[None]*100
            for ft in root.iter('fill_text'):
                a,b,c,d,e,f=map(float,ft.get('transform').split())
                for span in ft.findall('span'):
                    if abs(float(span.get('trm').split()[0])-scale)>1e-4:continue
                    for g in span:
                        u=g.get('unicode')
                        if not u.isdigit():continue
                        x=float(g.get('x'));y=float(g.get('y'));x,y=a*x+c*y+e,b*x+d*y+f
                        i=min(range(100),key=lambda i:(arrows[i][0]-x)**2+(arrows[i][1]-y)**2)
                        assert abs(arrows[i][0]-x)<3 and abs(arrows[i][1]-y)<3
                        assert digits[i] is None;digits[i]=int(u)
            boards.append(dict(printed_page=page,pdf_ordinal=page+20,directions_xy=[p[2:] for p in arrows],
                               digits=digits,centers=[[x,y] for x,y,_,_ in arrows]))
    assert boards[0]['directions_xy']==boards[1]['directions_xy']
    assert ''.join(str(x) for x in boards[0]['digits'] if x is not None)=='31415926535897932384626433832795'
    assert all(x==y for x,y in zip(boards[0]['digits'],boards[1]['digits']) if x is not None)
    out=dict(source=str(PDF.relative_to(ROOT.parent)),source_sha256=hashlib.sha256(PDF.read_bytes()).hexdigest(),
             method='MuPDF trace: five-vertex outlines and positioned glyphs, row-major; directions use screen xy',boards=boards)
    (RESULT/'arrows-extracted.json').write_text(json.dumps(out,indent=2)+'\n')
    return boards

def bits(mask):
    while mask:
        bit=mask&-mask;yield bit;mask-=bit

def refine(a):
    """Literal prefix-union and backward goal sets from answer 68."""
    n=len(a)-1;g=[0]*(n+1);g[n]=a[0]
    for l in range(n-1,0,-1):g[l]=(g[l+1]|g[l+1]>>1)&((1<<l)-1)
    b=[0]*(n+1);chosen=[0]*(n+1);visits=0
    def dfs(l,union):
        nonlocal visits
        visits+=1
        if l>n:
            b[0]|=1<<(union.bit_count()-1)
            for j in range(1,n+1):b[j]|=chosen[j]
            return
        for x in bits(a[l]):
            s=union|x
            if (1<<(s.bit_count()-1))&g[l]:
                chosen[l]=x;dfs(l+1,s)
    dfs(1,0)
    return b,visits

def brute_refine(a):
    n=len(a)-1;b=[0]*(n+1)
    for chosen in product(*(list(bits(x)) for x in a[1:])):
        count=len(set(chosen));mask=1<<(count-1)
        if mask&a[0]:
            b[0]|=mask
            for j,x in enumerate(chosen,1):b[j]|=x
    return b

def local_checks():
    rng=random.Random(20261101068)
    for _ in range(1000):
        n=rng.randrange(1,7);a=[rng.randrange(1,1<<n)]+[rng.randrange(1,1<<rng.randrange(1,6)) for _ in range(n)]
        b,_=refine(a);assert b==brute_refine(a),(a,b)
        if all(b):assert refine(b)[0]==b
    return 1000

def neighbors(directions):
    result=[]
    for i,(dx,dy) in enumerate(directions):
        x,y=i%10,i//10;ray=[];x+=dx;y+=dy
        while 0<=x<10 and 0<=y<10:
            ray.append(y*10+x);x+=dx;y+=dy
        assert ray
        result.append(ray)
    return result

def propagate(clues,rays,mode='dynamic',snapshot='after'):
    domains=[1<<(d-1) if d is not None else (1<<len(ray))-1 for d,ray in zip(clues,rays)]
    previous=[None]*100;rounds=[];calls=visits=0
    def args(v):return tuple(domains[u] for u in [v]+rays[v])
    def cost(v):return prod(domains[u].bit_count() for u in rays[v])
    while any(x.bit_count()!=1 for x in domains):
        pending={v for v in range(100) if args(v)!=previous[v]};changed=set();round_calls=0
        if not pending:break
        order=sorted(pending,key=lambda v:(cost(v),v))
        while pending:
            v=min(pending,key=lambda v:(cost(v),v)) if mode=='dynamic' else order.pop(0)
            pending.remove(v);a=args(v);b,nodes=refine(a);visits+=nodes;calls+=1;round_calls+=1
            assert all(b),(v,a,b)
            for u,mask in zip([v]+rays[v],b):
                if domains[u]!=mask:changed.add(u);domains[u]=mask
            previous[v]=args(v) if snapshot=='after' else a
        rounds.append(dict(refinements=round_calls,changed_vertices=sorted(changed),
                           unresolved=sum(x.bit_count()!=1 for x in domains)))
        print(mode,snapshot,'round',len(rounds),'calls',calls,'unresolved',rounds[-1]['unresolved'],flush=True)
        if len(rounds)>100:raise RuntimeError('nontermination')
    return dict(mode=mode,snapshot=snapshot,rounds=rounds,refinements=calls,search_nodes=visits,domains=domains)

def main():
    started=time.monotonic();boards=extract();local=local_checks();rays=neighbors(boards[0]['directions_xy'])
    printed=boards[1]['digits'];assert all(d==len({printed[u] for u in ray}) for d,ray in zip(printed,rays))
    runs=[]
    for mode,snapshot in [('static','before'),('dynamic','before'),('static','after'),('dynamic','after')]:
        result=propagate(boards[0]['digits'],rays,mode,snapshot)
        assert result['domains']==[1<<(x-1) for x in printed]
        runs.append(result)
    out=dict(status='pass',independent_local_checks=local,printed_solution=printed,clues=boards[0]['digits'],
             rays=rays,runs=runs,elapsed_seconds=time.monotonic()-started)
    (RESULT/'arrows-verified.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS',[(x['mode'],x['snapshot'],len(x['rounds']),x['refinements']) for x in runs],flush=True)

if __name__=='__main__':main()
