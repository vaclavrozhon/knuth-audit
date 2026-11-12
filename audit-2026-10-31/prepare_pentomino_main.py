#!/usr/bin/env python3
"""Complete pentomino placement sets for 4B pp.79--82, before solving."""
from collections import Counter
import json
from check_pentomino_bipairs import SHAPES, normalized, orientations, transform
from dlx1_audit_tools import ROOT, sha, input_text

OUT = ROOT/'results/pentomino_main'
DIGITS = '0123456789abcdefghij'


def connected_components(region, h, w):
    unseen = set(region); result = []
    while unseen:
        q = [min(unseen)]; unseen.remove(q[0])
        for u in q:
            r,c = divmod(u,w)
            for rr,cc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                v = rr*w+cc
                if 0<=rr<h and 0<=cc<w and v in unseen:
                    unseen.remove(v); q.append(v)
        result.append(sorted(q))
    return sorted(result)


def placements(h,w):
    result = []
    for p,s in SHAPES.items():
        for o in orientations(s):
            for r in range(h-max(x for x,y in o)):
                for c in range(w-max(y for x,y in o)):
                    result.append((p,tuple(sorted((r+x)*w+c+y for x,y in o))))
    assert len(set(result)) == len(result)
    return sorted(result)


def good_components(move,h=3,w=20):
    return all(len(c)%5==0 for c in connected_components(set(range(h*w))-set(move[1]),h,w))


def gamma(move):
    return move[0]!='V' or normalized([divmod(v,20) for v in move[1]]) == ((0,0),(0,1),(0,2),(1,0),(2,0))


def unflipped(move):
    return move[0]!='Z' or normalized([divmod(v,20) for v in move[1]]) in {
        normalized(transform(SHAPES['Z'],g)) for g in range(4)}


def instance(moves,h,w,primary='all'):
    cells = [DIGITS[r]+DIGITS[c] for r in range(h) for c in range(w)]
    names = list(SHAPES)+cells if primary=='pieces' else cells+list(SHAPES)
    index = {name:i+1 for i,name in enumerate(names)}
    # Cells precede the piece in each option, as in the p.82 example.
    rows = [[index[cells[v]] for v in cs]+[index[p]] for p,cs in moves]
    np = 72 if primary=='all' else 60 if primary=='cells' else 12
    return names,rows,np


def main():
    OUT.mkdir(exist_ok=True)
    # Independent grow-by-one enumeration: every finite connected set has a
    # spanning-tree leaf that can be deleted, so this generation is exhaustive.
    shapes = {((0,0),)}; census = {}
    for n in range(1,6):
        census[n] = dict(fixed=len(shapes),free=len({min(orientations(s)) for s in shapes}))
        if n==5:break
        nxt = set()
        for s in shapes:
            occupied = set(s)
            for r,c in s:
                for v in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                    if v not in occupied:nxt.add(normalized(occupied|{v}))
        shapes = nxt
    assert [census[n]['free'] for n in range(1,6)] == [1,1,2,5,12]
    assert {min(orientations(s)) for s in shapes} == {min(orientations(s)) for s in SHAPES.values()}
    full = placements(3,20)
    pruned = [m for m in full if good_components(m)]
    vg = [m for m in full if gamma(m)]
    pg = [m for m in pruned if gamma(m)]
    xz = [m for m in pruned if (m[0]!='X' or max(v%20 for v in m[1])<10) and unflipped(m)]
    assert [Counter(p for p,c in full)[p] for p in SHAPES] == [48,220,136,144,136,72,110,72,72,18,136,72]
    assert [Counter(p for p,c in pruned)[p] for p in SHAPES] == [48,156,132,28,128,16,44,16,12,4,128,16]
    assert len(pg)==716 and len(xz)==718
    assert [Counter(p for p,c in xz)[p] for p in 'VXZ']==[16,2,8]
    variants = {
      'full':(full,3,20,'all',False,32644),
      'gamma':(vg,3,20,'all',False,21805),
      'pruned':(pruned,3,20,'all',False,None),
      'pruned-gamma':(pg,3,20,'all',False,1243),
      'pruned-xz':(xz,3,20,'all',False,1128),
      'full-pieces-secondary':(full,3,20,'cells',False,61851),
      'pruned-gamma-pieces-secondary':(pg,3,20,'cells',False,19306),
      'pruned-gamma-cells-secondary':(pg,3,20,'pieces',False,11656),
      'full-cells-secondary':(full,3,20,'pieces',False,1086521921),
      'first-cell-3x20':(full,3,20,'cells',True,None),
      'first-cell-20x3':(placements(20,3),20,3,'cells',True,71191)}
    cases = {}
    for label,(moves,h,w,primary,nomrv,expected) in variants.items():
        names,rows,np = instance(moves,h,w,primary)
        inp = OUT/(label+'.dlx'); inp.write_text(input_text(names,rows,np))
        masks = OUT/(label+'.masks')
        masks.write_text(f'{primary} {int(nomrv)} {len(moves)}\n'+'\n'.join(
            f'{list(SHAPES).index(p)} {sum(1<<v for v in cs):x}' for p,cs in moves)+'\n')
        cases[label] = dict(h=h,w=w,primary=primary,nomrv=nomrv,expected_nodes=expected,
            expected_solutions=2 if label.startswith(('gamma','pruned-gamma','pruned-xz')) else 8,
            names=names,rows=rows,moves=moves,primary_count=np,
            piece_counts=dict(Counter(p for p,c in moves)),options=len(moves),
            input_sha256=sha(inp),masks_sha256=sha(masks))
    examples = [('O',(0,1,2,3,4)),('O',(55,56,57,58,59)),
                ('P',(0,1,2,20,21)),('Z',(19,37,38,39,57))]
    assert all(m in full for m in examples)
    bad = ('V',(9,10,11,29,49))
    comps = connected_components(set(range(60))-set(bad[1]),3,20)
    assert sorted(map(len,comps))==[27,28] and bad in full and bad not in pruned
    first = [m for m in full if 0 in m[1]]
    after = [m for m in full if 5 in m[1] and m[0]!='O' and not set(m[1])&set(range(5))]
    assert (len(first),len(after))==(29,49)
    # F120: literal coordinate alphabet, not the variable j in the bounds.
    order = [DIGITS[i]+DIGITS[j] for i in range(20) for j in range(3)]
    assert order[-1]=='j2' and '2j' not in order
    result = dict(source_sha256=sha(__file__),shape_source_sha256=sha(ROOT/'check_pentomino_bipairs.py'),
       free_polyomino_census=census,cases=cases,printed_options=examples,
       bad_V_components=comps,first_cell_branches=[len(first),len(after)],
       F120=dict(order20x3=order,printed_last='2j',correct_last=order[-1],printed_is_valid=False))
    (OUT/'instances.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: complete1..5 shapes, all placement counts, component exclusions, examples29/49 and F120')


if __name__=='__main__':main()
