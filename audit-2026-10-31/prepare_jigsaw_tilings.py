#!/usr/bin/env python3
"""All box options by Algorithm R and independent normalized polyomino growth."""
from datetime import datetime,timezone
import gzip
import json
from check_connected import algorithm_r,grid
from dlx1_audit_tools import ROOT,sha,input_text

OUT=ROOT/'results/jigsaw/tilings'


def grown_shapes(limit):
    shapes={((0,0),)}
    for n in range(1,limit+1):
        yield n,shapes
        nxt=set()
        if n==limit:break
        for p in shapes:
            used=set(p)
            boundary={(x+dx,y+dy) for x,y in p for dx,dy in ((1,0),(-1,0),(0,1),(0,-1))}-used
            for v in boundary:
                s=used|{v};x0=min(x for x,y in s);y0=min(y for x,y in s)
                nxt.add(tuple(sorted((x-x0,y-y0) for x,y in s)))
        shapes=nxt


def placements(shapes,n):
    result=set()
    for p in shapes:
        w=1+max(x for x,y in p);h=1+max(y for x,y in p)
        if w==1 or h==1:continue
        for r in range(n-h+1):
            for c in range(n-w+1):
                result.add(tuple(sorted((r+y)*n+c+x for x,y in p)))
    return result


def r_options(n):
    adj=grid(n);tags=[0]*(n*n);result=set();raw=0
    for root in range(n*n):
        rows,tags=algorithm_r(adj,root,n=n,tag=tags)
        for row in rows:
            raw+=1
            straight=len({v//n for v in row})==1 or len({v%n for v in row})==1
            r0,c0=divmod(row[0],n);r1,c1=divmod(row[-1],n)
            endpoint=(r0==r1 and c1-c0==n-1) or (c0==c1 and r1-r0==n-1)
            assert straight==endpoint
            if not straight:
                t=tuple(sorted(row));assert t not in result;result.add(t)
        for u in adj[root]:tags[u]-=1
    return result,raw


def write_options(name,rows,n):
    rows=sorted(rows)
    p=OUT/(name+'.json.gz')
    with gzip.open(p,'wt') as f:json.dump(rows,f)
    names=[f'p{r}{c}' for r in range(n) for c in range(n)]
    dlx=OUT/(name+'.dlx');dlx.write_text(input_text(names,[[v+1 for v in row] for row in rows]))
    return dict(options=len(rows),json_sha256=sha(p),dlx_sha256=sha(dlx))


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    diagrams=json.loads((ROOT/'results/jigsaw/pdf-diagrams.json').read_text())['sources']
    reference=diagrams['35c']['cells']
    result=dict(status='running',source_sha256=sha(__file__),
                algorithm_r_sha256=sha(ROOT/'check_connected.py'),counts={},files={})
    for n,shapes in grown_shapes(9):
        if n<3:continue
        growth=placements(shapes,n)
        actual,raw=r_options(n)
        assert growth==actual,(n,len(growth),len(actual))
        result['counts'][str(n)]=dict(fixed_shapes=len(shapes),all_placements=raw,
                                     nonstraight=len(actual),complete_sets_equal=True)
        result['files']['n'+str(n)]=write_options('n'+str(n),actual,n)
        print('n',n,'options',len(actual),'both complete sets equal',flush=True)
        if n==9:
            rainbow={row for row in actual if len({reference[v] for v in row})==9}
            standard={tuple(9*(3*a+r)+3*b+c for r in range(3) for c in range(3))
                      for a in range(3) for b in range(3)}
            assert standard<=rainbow and len(rainbow)==3173
            without=rainbow-standard;assert len(without)==3164
            result['files']['rainbow']=write_options('rainbow',rainbow,9)
            result['files']['rainbow-no-sudoku']=write_options('rainbow-no-sudoku',without,9)
    assert [result['counts'][str(n)]['nonstraight'] for n in range(3,8)]==[16,105,561,2804,13602]
    result.update(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat())
    (OUT/'options.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
