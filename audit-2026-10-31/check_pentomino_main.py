#!/usr/bin/env python3
"""Independent row-bitset search versus native DLX1 for short pentomino cases."""
from collections import Counter
import json
import subprocess
import time
from dlx1_audit_tools import ROOT,sha,validated_binary,statistics,decode_rows
from prepare_pentomino_main import OUT,SHAPES,orientations,normalized


def bitset_search(rows,np,nomrv=False):
    n=max(max(row) for row in rows)
    itemrows=[0]*n; rowitems=[]
    for i,row in enumerate(rows):
        rowitems.append(sum(1<<(j-1) for j in row))
        for j in row:itemrows[j-1] |= 1<<i
    conflicts=[]
    for row in rows:
        mask=0
        for j in row:mask|=itemrows[j-1]
        conflicts.append(mask)
    profile=Counter();solutions=set()
    def rec(items,active,path):
        profile[len(path)]+=1
        if not items:
            solutions.add(tuple(sorted(path)));return
        remaining=items; best=len(rows)+1; candidates=0
        while remaining:
            b=remaining&-remaining;remaining-=b
            a=itemrows[b.bit_length()-1]&active
            if a.bit_count()<best:
                best=a.bit_count();candidates=a
                if not best:return
            if nomrv:break
        while candidates:
            b=candidates&-candidates;candidates-=b;r=b.bit_length()-1
            rec(items&~rowitems[r],active&~conflicts[r],path+[r])
    rec((1<<np)-1,(1<<len(rows))-1,[])
    return solutions,[profile[i] for i in range(13)]


def validate(models,c):
    boards=set()
    for sol in models:
        board=['.']*60;used=[]
        for i in sol:
            p,cs=c['moves'][i];used.append(p)
            assert len(cs)==5 and normalized([divmod(v,c['w']) for v in cs]) in orientations(SHAPES[p])
            for v in cs:assert board[v]=='.';board[v]=p
        assert sorted(used)==sorted(SHAPES) and '.' not in board
        boards.add(''.join(board))
    assert len(boards)==len(models)
    return boards


def main():
    data=json.loads((OUT/'instances.json').read_text())
    build=json.loads((ROOT/'results/dancing_links/dlx1-build.json').read_text())
    validated_binary()
    long={'full-cells-secondary','first-cell-3x20'}
    result={};boardsets={}
    for label,c in data['cases'].items():
        if label in long:continue
        name='dlx1-nomrv' if c['nomrv'] else 'dlx1'
        binary=build['binaries'][name];assert sha(binary['path'])==binary['sha256']
        inp=OUT/(label+'.dlx');assert sha(inp)==c['input_sha256']
        cmd=[binary['path'],'v129','m1'];start=time.monotonic()
        p=subprocess.run(cmd,input=inp.read_text(),text=True,capture_output=True,check=True,timeout=300)
        (OUT/(label+'.log')).write_text(p.stderr);(OUT/(label+'.out')).write_text(p.stdout)
        native=statistics(p.stderr);models=decode_rows(p.stdout,c['names'],c['rows'])
        expected,profile=bitset_search(c['rows'],c['primary_count'],c['nomrv'])
        assert models==expected and profile==native['profile']
        assert len(models)==c['expected_solutions']
        if c['expected_nodes'] is not None:assert native['nodes']==c['expected_nodes'],(label,native)
        boardsets[label]=validate(models,c)
        result[label]=dict(native=native,independent_nodes=sum(profile),independent_profile=profile,
            models=sorted(models),boards=sorted(boardsets[label]),command=cmd,
            binary_sha256=binary['sha256'],stdout_sha256=sha(OUT/(label+'.out')),
            stderr_sha256=sha(OUT/(label+'.log')),elapsed_seconds=time.monotonic()-start)
        print(label,native['solutions'],native['nodes'],native['search_mems'],flush=True)
    assert boardsets['full']==boardsets['pruned']==boardsets['full-pieces-secondary']
    assert boardsets['gamma']==boardsets['pruned-gamma']==boardsets['pruned-gamma-pieces-secondary']==boardsets['pruned-gamma-cells-secondary']
    # The rectangular symmetry group has4 elements; all8 solutions have trivial
    # stabilizers and split into precisely2 complete orbits.
    def orbit(s):
        return {''.join(s[(2-r if a else r)*20+(19-c if b else c)] for r in range(3) for c in range(20)) for a in (0,1) for b in (0,1)}
    groups={tuple(sorted(orbit(s))) for s in boardsets['full']}
    assert len(groups)==2 and all(len(g)==4 and set(g)<=boardsets['full'] for g in groups)
    assert all(len(set(g)&boardsets['gamma'])==len(set(g)&boardsets['pruned-xz'])==1 for g in groups)
    transposed={''.join(s[c*3+r] for r in range(3) for c in range(20)) for s in boardsets['first-cell-20x3']}
    assert transposed==boardsets['full']
    (OUT/'short-check.json').write_text(json.dumps(dict(source_sha256=sha(__file__),
       instances_sha256=sha(OUT/'instances.json'),cases=result,symmetry_orbits=sorted(groups)),indent=2)+'\n')
    print('PASS: all9 short full model sets, full profiles, symmetry and secondary-item formulations')


if __name__=='__main__':main()
