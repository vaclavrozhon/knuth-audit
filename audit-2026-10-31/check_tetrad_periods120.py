"""Finite certificates proving the complete infinite-plane classification."""
from collections import deque
from datetime import datetime,timezone
import json
from graph_native import ROOT,sha,save

OUT=ROOT/'results/graphs117_120'

def propagate(forced,anchor,targets):
    known={(0,0):anchor};queue=deque([(0,0)]);proof=[]
    while not targets<=known.keys():
        assert queue,'Forced rules do not prove all target cells'
        r,c=queue.popleft()
        for dr,dc,t in forced[known[r,c]]:
            pos=(r+dr,c+dc)
            if max(map(abs,pos))>30:continue
            if pos in known:assert known[pos]==t
            else:
                known[pos]=t;queue.append(pos)
                proof.append(dict(position=pos,tile=t,parent=[r,c],offset=[dr,dc]))
    return known,proof

def main():
    finite=json.loads((OUT/'tetrads120-finite-checked.json').read_text())
    vectors=json.loads((OUT/'tetrads120-vectors.json').read_text());results=[]
    for f,display in zip(finite['families'],vectors['printed_arrays']):
        a=f['family']=='a';tiles=f['tiles'];anchor=5 if a else 0
        rules={k:[(i//5-2,i%5-2,int(t)) for i,t in enumerate(p) if t!='?'] for k,p in enumerate(f['forced_neighborhoods'])}
        # Bases for a lattice with index12 or13, and explicit coset representatives.
        generators=[(0,3),(4,-1)] if a else [(0,13),(1,-9)]
        representatives=[(r,c) for r in range(4) for c in range(3)] if a else [(0,c) for c in range(13)]
        index=abs(generators[0][0]*generators[1][1]-generators[0][1]*generators[1][0])
        translations=generators+[(-r,-c) for r,c in generators]
        known,proof=propagate(rules,anchor,set(representatives+translations))
        assert all(known[p]==anchor for p in translations)
        def reduce(r,c):
            if a:
                q,r=divmod(r,4);return r,(c+q)%3
            return 0,(c+9*r)%13
        pattern={p:known[p] for p in representatives}
        assert len(pattern)==index and sum(t==anchor for t in pattern.values())==1
        value=lambda r,c:pattern[reduce(r,c)]
        for r,c in representatives:
            t=tiles[value(r,c)]
            assert t[1]==tiles[value(r,c+1)][3] and t[2]==tiles[value(r+1,c)][0]
        # Independent reconstruction of each derivation from its explicit parent.
        replay={(0,0):anchor}
        for step in proof:
            parent=tuple(step['parent']);pos=tuple(step['position']);dr,dc=step['offset'];t=step['tile']
            assert (dr,dc,t) in rules[replay[parent]]
            assert pos==(parent[0]+dr,parent[1]+dc) and pos not in replay
            assert value(*pos)==t;replay[pos]=t
        assert set(representatives+translations)<=replay.keys()
        # The book's entire336-cell strip is a translate of this valid infinite pattern.
        shifts=[(rr,cc) for rr,cc in representatives if all(value(r+rr,c+cc)==display[r][c] for r in range(6) for c in range(56))]
        assert len(shifts)==1
        forces_anchor={anchor};rounds=[]
        while True:
            new={k for k in rules if any(t in forces_anchor for dr,dc,t in rules[k])}-forces_anchor
            if not new:break
            rounds.append(sorted(new));forces_anchor|=new
        extra={}
        if a:
            # Even the exceptional ambiguous tile types occur only in5x5 boards containing5.
            assert all(anchor in b for b in f['boards'])
            extra['every_5x5_contains_anchor']=True
            classes=1
        else:
            assert forces_anchor=={0,2,4,6,7,8,9}
            remaining=sorted(set(range(10))-forces_anchor);assert remaining==[1,3,5]
            successor={1:3,3:5,5:1}
            for k in remaining:
                east=[j for j in remaining if tiles[k][1]==tiles[j][3]]
                south=[j for j in remaining if tiles[k][2]==tiles[j][0]]
                assert east==south==[successor[k]]
            period3=[[remaining[(r+c)%3] for c in range(3)] for r in range(3)]
            for r in range(3):
                for c in range(3):
                    t=tiles[period3[r][c]]
                    assert t[1]==tiles[period3[r][(c+1)%3]][3]
                    assert t[2]==tiles[period3[(r+1)%3][c]][0]
            extra=dict(types_forcing_anchor=sorted(forces_anchor),forcing_rounds=rounds,anchor_free_types=remaining,
                east_and_south_successor=successor,period3_counterexample=period3,
                period3_formula='tile(r,c)=[1,3,5][(r+c) mod3], all integer r,c, zero-based tile numbers',
                period3_generators=[[1,-1],[0,3]],period3_lattice_index=3)
            classes=2
        results.append(dict(family=f['family'],anchor=anchor,lattice_generators=generators,lattice_index=index,
            representative_tiles=[dict(position=p,tile=t) for p,t in pattern.items()],forced_derivation=proof,
            opposite_generator_anchors_proved=True,printed_336_cells_match_translation=shifts[0],
            complete_translation_classes=classes,**extra))
    save(OUT/'tetrads120-plane-checked.json',dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),script_sha256=sha(__file__),
        finite_neighborhoods_sha256=sha(OUT/'tetrads120-finite-checked.json'),families=results,
        proof='Each anchor forces anchors at both signs of a lattice basis and one complete set of coset representatives. Translation of the finite derivation then covers Z^2 by induction. Every output pattern matches all edges. Unique occurrence of the anchor per fundamental domain proves its exact minimal period index. Family b also has an anchor-free3-cell pattern; all other types force the anchor, so the classification is exhaustive.'))
    # Exact vector drawing of the counterexample, with original type numbers.
    colors={'W':'#ffffff','R':'#ffbfbf','B':'#8080ff','K':'#333333'};tiles=finite['families'][1]['tiles'];parts=[]
    parts.append('<svg xmlns="http://www.w3.org/2000/svg" width="720" height="580" viewBox="0 0 720 580">')
    parts.append('<rect width="720" height="580" fill="#f6f7fa"/><g font-family="sans-serif" fill="#172033">')
    parts.append('<text x="40" y="42" font-size="22" font-weight="bold">Exercise 120(b): a second infinite tiling</text>')
    parts.append('<text x="40" y="73" font-size="16">Use the 2nd, 4th and 6th printed tiles; repeat this 3 × 3 block.</text>')
    shapes=[[(0,0),(1,0),(.5,.5)],[(1,0),(1,1),(.5,.5)],[(1,1),(0,1),(.5,.5)],[(0,1),(0,0),(.5,.5)]]
    for r in range(3):
        for c in range(3):
            k=[1,3,5][(r+c)%3];x=55+125*c;y=105+125*r
            for color,shape in zip(tiles[k],shapes):
                points=' '.join(f'{x+125*dx},{y+125*dy}' for dx,dy in shape)
                parts.append(f'<polygon points="{points}" fill="{colors[color]}" stroke="#172033" stroke-width="1"/>')
            parts.append(f'<circle cx="{x+62.5}" cy="{y+62.5}" r="16" fill="white" stroke="#172033"/><text x="{x+62.5}" y="{y+68}" text-anchor="middle" font-size="16">{k+1}</text>')
    parts.append('<text x="455" y="160" font-size="16">Rows and columns cycle:</text><text x="455" y="195" font-size="22">2 → 4 → 6 → 2</text>')
    parts.append('<text x="40" y="520" font-size="16">All touching edge colors match, including across the repeated boundaries.</text>')
    parts.append('<text x="40" y="549" font-size="16">The minimal periodic cell has area 3; the book displays a different area-13 tiling.</text></g></svg>')
    (ROOT/'images/tetrads120-counterexample.svg').write_text('\n'.join(parts)+'\n')
    print('120: complete plane classification; a has one12-cell class, b has13-cell AND3-cell classes. Finite propagation certificates saved.')

if __name__=='__main__':main()
