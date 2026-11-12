#!/usr/bin/env python3
"""Exhaustive nontrivial symmetry census by exact covers of whole tile orbits."""
from collections import Counter
from datetime import datetime,timezone
import gzip
import json
from dlx1_audit_tools import ROOT,sha,run,input_text
from check_sudoku_trios57 import bitset_covers

OUT=ROOT/'results/jigsaw/tilings'


def maps(n):
    return [tuple(f(r,c)[0]*n+f(r,c)[1] for r in range(n) for c in range(n))
            for f in [lambda r,c:(r,c),lambda r,c:(c,n-1-r),
                      lambda r,c:(n-1-r,n-1-c),lambda r,c:(n-1-c,r),
                      lambda r,c:(n-1-r,c),lambda r,c:(r,n-1-c),
                      lambda r,c:(c,r),lambda r,c:(n-1-c,n-1-r)]]


def moved(tiles,mapping):
    return tuple(sorted(tuple(sorted(mapping[v] for v in t)) for t in tiles))


def symmetry_orbits(tiles,group):
    available=set(tiles);orbits=[];rejected=0
    for first in sorted(tiles):
        if first not in available:continue
        orbit={tuple(sorted(g[v] for v in first)) for g in group}
        assert orbit<=available
        available-=orbit
        union=set(v for t in orbit for v in t)
        if len(union)!=sum(map(len,orbit)):
            rejected+=1;continue
        orbits.append((tuple(sorted(union)),tuple(sorted(orbit))))
    return sorted(orbits),rejected


def solve_group(n,tiles,group,label):
    orbits,rejected=symmetry_orbits(tiles,group)
    rows=[[v+1 for v in union] for union,_ in orbits]
    names=[f'p{r}{c}' for r in range(n) for c in range(n)]
    native,_=run(OUT/'symmetry',label,input_text(names,rows),timeout=600)
    covers,profile=bitset_covers(rows,n*n)
    actual=set()
    for cover in covers:
        tiling=tuple(sorted(t for row in cover for t in orbits[row][1]))
        assert len(tiling)==n and set(v for t in tiling for v in t)==set(range(n*n))
        assert sum(map(len,tiling))==n*n and all(t in tiles for t in tiling)
        assert all(moved(tiling,g)==tiling for g in group)
        assert tiling not in actual;actual.add(tiling)
    assert native['solutions']==len(actual)
    assert native['profile']==[profile.get(i,0) for i in range(len(native['profile']))]
    return actual,dict(orbits=len(orbits),overlapping_orbits_rejected=rejected,
                       native=native,independent_profile=profile,full_tilings_validated=len(actual))


def main():
    diagrams=json.loads((ROOT/'results/jigsaw/pdf-diagrams.json').read_text())['sources']
    result=dict(status='running',source_sha256=sha(__file__),helper_sha256=sha(ROOT/'check_sudoku_trios57.py'),cases={})
    expected={4:{1:2,2:3,4:2,8:1},5:{1:256,2:7,4:3},6:{1:39791,2:439,4:7},
              7:{1:16550986,2:2660}}
    totals={4:33,5:2082,6:320098,7:132418528}
    for n in range(4,8):
        tiles=set(map(tuple,json.loads(gzip.decompress((OUT/f'n{n}.json.gz').read_bytes()))))
        transformations=maps(n);nontrivial=set();groups={}
        for g in range(1,8):
            group={transformations[0],transformations[g]}
            while True:
                closed=group|{tuple(a[b[v]] for v in range(n*n)) for a in group for b in group}
                if closed==group:break
                group=closed
            models,stats=solve_group(n,tiles,sorted(group),f'n{n}-g{g}')
            nontrivial.update(models);groups[str(g)]=stats
            print(n,'symmetry',g,'fixed',len(models),flush=True)
        representatives={min(moved(t,g) for g in transformations) for t in nontrivial}
        stabilizers={r:tuple(i for i,g in enumerate(transformations) if moved(r,g)==r) for r in representatives}
        census=Counter(len(s) for s in stabilizers.values())
        assert (totals[n]-len(nontrivial))%8==0
        census[1]=(totals[n]-len(nontrivial))//8
        assert dict(census)==expected[n],(n,census)
        assert sum(8//k*v for k,v in census.items())==totals[n]
        pictures=[]
        for label,d in diagrams.items():
            if not label.startswith(f'62n{n}-'):continue
            t=tuple(sorted(map(tuple,d['regions'])))
            assert all(piece in tiles for piece in t)
            stabilizer=[i for i,g in enumerate(transformations) if moved(t,g)==t]
            pictures.append(dict(label=label,stabilizer=stabilizer,canonical=min(moved(t,g) for g in transformations)))
        if n==4:
            assert [len(p['stabilizer']) for p in pictures]==[1,1,2,2,2,4,4,8]
            assert len({tuple(map(tuple,p['canonical'])) for p in pictures})==8
        if n==7:
            kinds=Counter('rotation180' if 2 in s else 'axis' if 4 in s or 5 in s else 'diagonal' for s in stabilizers.values())
            assert dict(kinds)=={'rotation180':2265,'axis':354,'diagonal':41}
            assert [len(p['stabilizer']) for p in pictures]==[2,2,2]
        result['cases'][str(n)]=dict(groups=groups,symmetric_tilings=len(nontrivial),
                                     class_census=dict(census),pictures=pictures,
                                     total_used_for_asymmetric_classes=totals[n])
        with gzip.open(OUT/f'n{n}-symmetric-models.json.gz','wt') as f:json.dump(sorted(nontrivial),f)
        result['cases'][str(n)]['models_sha256']=sha(OUT/f'n{n}-symmetric-models.json.gz')
        (OUT/'symmetry.json').write_text(json.dumps(result,indent=2)+'\n')
    # The n8 pictures are examples, not an assertion of a complete census.
    pictures=[]
    for label,d in diagrams.items():
        if label.startswith('62n8-'):
            t=tuple(sorted(map(tuple,d['regions'])))
            n8=set(map(tuple,json.loads(gzip.decompress((OUT/'n8.json.gz').read_bytes()))))
            assert all(p in n8 for p in t)
            pictures.append(dict(label=label,stabilizer=[i for i,g in enumerate(maps(8)) if moved(t,g)==t]))
    assert [len(p['stabilizer']) for p in pictures]==[4,8,8]
    result['n8_examples']=pictures
    tiles=set(map(tuple,json.loads(gzip.decompress((OUT/'n9.json.gz').read_bytes()))))
    models,stats=solve_group(9,tiles,maps(9),'n9-allD4')
    standard=tuple(sorted(tuple(9*(3*a+r)+3*b+c for r in range(3) for c in range(3)) for a in range(3) for b in range(3)))
    printed={tuple(sorted(map(tuple,diagrams[label]['regions']))) for label in ['62n9-b','62n9-c']}
    assert models==printed|{standard} and len(models)==3
    result['n9_allD4']=dict(stats=stats,models=sorted(models),exactly_two_nonstandard=True)
    result.update(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat())
    (OUT/'symmetry.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: all symmetry classes and all16 exercise62 tiling diagrams',flush=True)


if __name__=='__main__':main()
