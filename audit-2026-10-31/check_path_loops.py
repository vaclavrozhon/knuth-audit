"""Complete factored path-domino placements with distinct pieces and one loop."""
from collections import Counter,defaultdict
from pathlib import Path
import argparse,json
from pysat.card import CardEnc,EncType
from pysat.solvers import Solver
from check_path_dominoes import OUT,catalog,rotate_pairs


def components(vertices,arcs):
    neighbors=defaultdict(set)
    for a,b in arcs:neighbors[a].add(b);neighbors[b].add(a)
    remaining=set(vertices);out=[]
    while remaining:
        todo=[remaining.pop()];seen=set(todo)
        while todo:
            for b in neighbors[todo.pop()]:
                if b not in seen:seen.add(b);remaining.remove(b);todo.append(b)
        out.append(seen)
    return out


def complete(name):
    data=json.loads((OUT/f'{name}.json').read_text());placement=data['first_solution']
    assert placement
    catalog_all,_,_=catalog()
    pieces={piece for piece,mask in catalog_all.items() if str(mask) in data['inventory']}
    # For the noncrossing inventory, restrict to noncrossing pieces as well.
    if name=='planar32':pieces=set(catalog()[1])
    choices=[];by_tile=defaultdict(list);by_piece=defaultdict(list)
    vertices=set()
    for i,tile in enumerate(placement):
        mask=tile['mask'];ports=[tuple(p) for p in tile['ports']]
        vertices.update(ports[j] for j in range(6) if mask>>j&1)
        for piece in sorted(pieces):
            if catalog_all[piece]!=tile['pattern']:continue
            for pairs in sorted({piece,rotate_pairs(piece)}):
                if sum(1<<v for pair in pairs for v in pair)!=mask:continue
                arcs=[(ports[a],ports[b]) for a,b in pairs]
                choices.append(dict(tile=i,piece=piece,pairs=pairs,arcs=arcs))
                by_tile[i].append(len(choices));by_piece[piece].append(len(choices))
    clauses=[];top=len(choices)
    for variables in list(by_tile.values())+list(by_piece.values()):
        card=CardEnc.equals(variables,bound=1,top_id=top,encoding=EncType.seqcounter)
        clauses.extend(card.clauses);top=max(top,card.nv)
    iterations=0;cuts=0
    with Solver(name='g4',bootstrap_with=clauses) as solver:
        while solver.solve():
            iterations+=1
            model=[v for v in solver.get_model() if 1<=v<=len(choices)]
            selected=[choices[v-1] for v in model]
            arcs=[arc for c in selected for arc in c['arcs']]
            comps=components(vertices,arcs)
            if len(comps)==1:break
            for comp in comps:
                clause=[i+1 for i,c in enumerate(choices)
                        if any((a in comp)!=(b in comp) for a,b in c['arcs'])]
                solver.add_clause(clause);cuts+=1
        else:
            raise AssertionError(f'{name}: factored placement has no single-loop assignment')
    assert Counter(c['tile'] for c in selected)==Counter(range(len(placement)))
    assert Counter(c['piece'] for c in selected)==Counter(pieces)
    degrees=Counter(v for arc in arcs for v in arc)
    assert set(degrees)==vertices and set(degrees.values())=={2}
    assert len(components(vertices,arcs))==1
    out=dict(name=name,iterations=iterations,subtour_cuts=cuts,
             pieces=len(pieces),loop_vertices=len(vertices),
             assignment=[{k:v for k,v in c.items() if k!='arcs'} for c in selected])
    (OUT/f'{name}.loop.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='assignment'}),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('name');args=parser.parse_args()
    complete(args.name)
