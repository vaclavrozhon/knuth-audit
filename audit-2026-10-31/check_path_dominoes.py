"""Path-domino inventory and factored edge-matching problems, TAOCP X151--153.

Ports are clockwise 0..5 around a horizontal domino; half-turn adds 3 mod 6.
The SAT problem chooses placements and on/off port masks. It deliberately
forgets pairing of active ports, as does the first stage in the book.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
from pathlib import Path
import argparse, hashlib, json, subprocess, threading, time
from pysat.card import CardEnc, EncType
from pysat.solvers import Solver

ROOT = Path(__file__).parent
OUT = ROOT / 'results/path_dominoes'


def half(mask):
    return ((mask << 3) | (mask >> 3)) & 63


def key(mask):
    return min(mask, half(mask))


def matchings(points):
    if not points:
        yield (); return
    a, *rest = points
    for b in rest:
        for tail in matchings([p for p in rest if p != b]):
            yield tuple(sorted(((a,b),) + tail))


def rotate_pairs(pairs):
    return tuple(sorted(tuple(sorted(((a+3)%6,(b+3)%6))) for a,b in pairs))


def noncrossing(pairs):
    return not any(a < c < b < d or c < a < d < b
                   for (a,b),(c,d) in combinations(pairs,2))


def catalog():
    all_patterns = {}; flat_patterns = {}; stats = {}
    for length in range(4):
        raw = set()
        for points in combinations(range(6),2*length):
            raw.update(matchings(list(points)))
        orbits = {min(p,rotate_pairs(p)) for p in raw}
        flat = {p for p in orbits if noncrossing(p)}
        stats[length] = dict(raw=len(raw),fixed=sum(p==rotate_pairs(p) for p in raw),
                             orbits=len(orbits),noncrossing=len(flat))
        for p in orbits:
            mask = sum(1 << v for pair in p for v in pair)
            all_patterns[p] = key(mask)
        for p in flat:
            mask = sum(1 << v for pair in p for v in pair)
            flat_patterns[p] = key(mask)
    assert [stats[k]['orbits'] for k in range(4)] == [1,9,27,11]
    assert [stats[k]['noncrossing'] for k in range(4)] == [1,9,18,4]
    # One terminal and one internal pair: choose three ports, then terminal.
    terminal = set()
    for ports in combinations(range(6),3):
        for tip in ports:
            pair = tuple(x for x in ports if x != tip)
            original = (tip,pair)
            rotated = ((tip+3)%6,tuple(sorted((x+3)%6 for x in pair)))
            terminal.add(min(original,rotated))
    assert len(terminal)==30
    # Three ports touch each half of the domino. Any closed placement must
    # have equal numbers of active ports on black and white board cells.
    left={0,4,5};imbalances=Counter()
    for pairs in flat_patterns:
        active={v for pair in pairs for v in pair}
        imbalance=abs(len(active&left)-len(active-left))
        imbalances[imbalance]+=1
    assert imbalances=={0:23,2:9}
    return all_patterns,flat_patterns,dict(by_subpaths=stats,terminal_patterns=len(terminal),
        noncrossing_absolute_checkerboard_imbalances=dict(imbalances),
        noncrossing_tiling_impossible='Nine signed contributions of2 cannot sum to0.')


def placements(height,width):
    for r in range(height):
        for c in range(width):
            if c+1 < width:
                yield {'cells':((r,c),(r,c+1)), 'orientation':'H',
                       'ports':((2*r,2*c+1),(2*r,2*c+3),(2*r+1,2*c+4),
                                (2*r+2,2*c+3),(2*r+2,2*c+1),(2*r+1,2*c))}
            if r+1 < height:
                yield {'cells':((r,c),(r+1,c)), 'orientation':'V',
                       'ports':((2*r+1,2*c+2),(2*r+3,2*c+2),(2*r+4,2*c+1),
                                (2*r+3,2*c),(2*r+1,2*c),(2*r,2*c+1))}


def boundary(port,height,width):
    return port[0] in (0,2*height) or port[1] in (0,2*width)


def options_for(height,width,inventory):
    options=[]
    for placement in placements(height,width):
        for mask in range(64):
            if not inventory.get(key(mask),0): continue
            if any(mask >> j & 1 and boundary(port,height,width)
                   for j,port in enumerate(placement['ports'])): continue
            options.append(dict(placement,mask=mask,pattern=key(mask)))
    return options


def encode(height,width,inventory,horizontals=None,geometry=None):
    options=options_for(height,width,inventory)
    if geometry is not None:options=[o for o in options if o['cells'] in geometry]
    clauses=[]; top=len(options)
    groups=defaultdict(list)
    ports={port for opt in options for port in opt['ports'] if not boundary(port,height,width)}
    edge={port:top+i+1 for i,port in enumerate(sorted(ports))};top+=len(edge)
    for var,opt in enumerate(options,1):
        for cell in opt['cells']:groups[('cell',cell)].append(var)
        groups[('pattern',opt['pattern'])].append(var)
        groups[('direction',opt['orientation'])].append(var)
        groups[('placement',opt['cells'])].append(var)
        for j,port in enumerate(opt['ports']):
            if port in edge:
                clauses.append([-var,edge[port] if opt['mask']>>j&1 else -edge[port]])
    def equal(literals,count):
        nonlocal top
        if count > len(literals):clauses.append([]);return
        if not literals:return
        card=CardEnc.equals(lits=literals,bound=count,top_id=top,encoding=EncType.seqcounter)
        clauses.extend(card.clauses);top=max(top,card.nv)
    for cell in product(range(height),range(width)):equal(groups['cell',cell],1)
    for pattern,count in inventory.items():equal(groups['pattern',pattern],count)
    if horizontals is not None:
        # Count geometric placements, not every alternative port mask.
        horizontal_vars=[]
        for placement in placements(height,width):
            if placement['orientation']!='H':continue
            alternatives=groups['placement',placement['cells']]
            if not alternatives:continue
            top+=1;selector=top;horizontal_vars.append(selector)
            clauses.extend([[-v,selector] for v in alternatives])
            clauses.append([-selector]+alternatives)
        equal(horizontal_vars,horizontals)
    return top,clauses,options


def signature(selected):
    return tuple(sorted((tuple(o['cells']),o['mask']) for o in selected))


def verify(selected,height,width,inventory,horizontals):
    cells=Counter(cell for o in selected for cell in o['cells'])
    assert cells==Counter(product(range(height),range(width)))
    assert Counter(o['pattern'] for o in selected)==inventory
    assert horizontals is None or sum(o['orientation']=='H' for o in selected)==horizontals
    edge=defaultdict(list)
    for o in selected:
        for j,port in enumerate(o['ports']):edge[port].append(o['mask']>>j&1)
    for port,values in edge.items():
        if boundary(port,height,width):assert values==[0]
        else:assert len(values)==2 and values[0]==values[1]


def direct_small(height,width):
    """Enumerate geometric tilings and all grid-edge subsets, without SAT."""
    place=list(placements(height,width));by_cell=defaultdict(list)
    for p in place:
        for cell in p['cells']:by_cell[cell].append(p)
    board=set(product(range(height),range(width)))
    def tilings(remaining,prefix):
        if not remaining:yield prefix;return
        cell=min(remaining)
        for p in by_cell[cell]:
            if set(p['cells'])<=remaining:
                yield from tilings(remaining-set(p['cells']),prefix+[p])
    answer=defaultdict(set)
    for tiling in tilings(board,[]):
        ports=sorted({port for p in tiling for port in p['ports'] if not boundary(port,height,width)})
        for bits in product((0,1),repeat=len(ports)):
            state=dict(zip(ports,bits));selected=[]
            for p in tiling:
                mask=sum(state.get(port,0)<<j for j,port in enumerate(p['ports']))
                if mask.bit_count()%2:break
                selected.append(dict(p,mask=mask,pattern=key(mask)))
            else:
                inventory=tuple(sorted(Counter(o['pattern'] for o in selected).items()))
                answer[inventory].add(signature(selected))
    return answer


def validate():
    counts={};total=0;orientation_queries=0
    for height,width in [(2,2),(2,3),(2,4)]:
        cases=direct_small(height,width)
        for items,expected in cases.items():
            inventory=Counter(dict(items));_,clauses,options=encode(height,width,inventory)
            actual=set()
            with Solver(name='g4',bootstrap_with=clauses) as solver:
                while solver.solve():
                    indices=[v for v in solver.get_model() if 1<=v<=len(options)]
                    selected=[options[v-1] for v in indices]
                    verify(selected,height,width,inventory,None)
                    sig=signature(selected);assert sig not in actual;actual.add(sig)
                    solver.add_clause([-v for v in indices])
            assert actual==expected,(height,width,items,len(actual),len(expected))
            total+=len(actual)
            for hcount in range(height*width//2+1):
                _, constrained,opts=encode(height,width,inventory,hcount)
                direct=any(sum(cells[0][0]==cells[1][0] for cells,mask in sig)==hcount
                           for sig in expected)
                with Solver(name='g4',bootstrap_with=constrained) as solver:
                    assert solver.solve()==direct
                orientation_queries+=1
        counts[f'{height}x{width}']=len(cases)
    return {'inventory_cases':counts,'matching_solutions':total,
            'orientation_queries':orientation_queries}


def save_cnf(path,top,clauses):
    with path.open('w') as stream:
        stream.write(f'p cnf {top} {len(clauses)}\n')
        for clause in clauses:stream.write(' '.join(map(str,clause))+' 0\n')


def reflections(selected,height,width,options):
    """All four rectangular reflections, expressed in the existing option IDs."""
    lookup={(tuple(sorted(o['cells'])),frozenset(p for j,p in enumerate(o['ports'])
                if o['mask']>>j&1)):i for i,o in enumerate(options,1)}
    answer=set()
    for flip_r,flip_c in product((False,True),repeat=2):
        ids=[]
        for o in selected:
            cells=tuple(sorted((height-1-r if flip_r else r,
                                width-1-c if flip_c else c) for r,c in o['cells']))
            active=frozenset((2*height-r if flip_r else r,
                              2*width-c if flip_c else c)
                             for j,(r,c) in enumerate(o['ports']) if o['mask']>>j&1)
            ids.append(lookup[cells,active])
        answer.add(tuple(sorted(ids)))
    return answer


def solve_problem(name,height,width,inventory,horizontals,limit,enumerate_all,
                  resume=False,symmetry=False,blank_corner=False):
    top,clauses,options=encode(height,width,inventory,horizontals)
    if (height,width,horizontals)==(8,9,32):
        # Equality in the row-parity bound forces four vertical dominoes,
        # one in each pair of rows, in an even column (zero-based).
        clauses.extend([[-i] for i,o in enumerate(options,1)
                        if o['orientation']=='V' and
                        (o['cells'][0][0]%2 or o['cells'][0][1]%2)])
    if blank_corner:
        # This is a restricted search for a witness, never an impossibility proof.
        clauses.append([i for i,o in enumerate(options,1)
                        if o['pattern']==0 and o['cells']==((0,0),(0,1))])
    print(f'{name}: {len(options)} options, {top} variables, {len(clauses)} clauses',flush=True)
    base=OUT/name;save_cnf(base.with_suffix('.cnf'),top,clauses)
    start=time.monotonic(); count=0; first=None; blocks=[];answer=None;seen=set()
    model_path=base.with_suffix('.models.jsonl')
    if resume:
        for line in model_path.read_text().splitlines():
            ids=tuple(sorted(json.loads(line)))
            assert ids not in seen
            selected=[options[v-1] for v in ids]
            verify(selected,height,width,inventory,horizontals)
            seen.add(ids);blocks.append([-v for v in ids]);first=first or selected
        count=len(seen)
        print(f'{name}: resumed {count} independently rechecked models',flush=True)
    with Solver(name='g4',bootstrap_with=clauses+blocks,with_proof=True) as solver:
        timer=threading.Timer(limit,solver.interrupt);timer.start()
        try:
            with model_path.open('a' if resume else 'w') as stream:
                def add_ids(ids):
                    nonlocal count,first
                    ids=tuple(sorted(ids))
                    if ids in seen:return
                    selected=[options[v-1] for v in ids]
                    verify(selected,height,width,inventory,horizontals)
                    seen.add(ids);count+=1;first=first or selected
                    stream.write(json.dumps(ids)+'\n');stream.flush()
                    if enumerate_all:
                        block=[-v for v in ids];blocks.append(block);solver.add_clause(block)
                if symmetry:
                    for ids in list(seen):
                        for reflected in reflections([options[v-1] for v in ids],height,width,options):
                            add_ids(reflected)
                    print(f'{name}: reflection closure has {count} models',flush=True)
                while True:
                    answer=solver.solve_limited(expect_interrupt=True)
                    if answer is not True:break
                    indices=[v for v in solver.get_model() if 1<=v<=len(options)]
                    selected=[options[v-1] for v in indices]
                    verify(selected,height,width,inventory,horizontals)
                    add_ids(indices)
                    if symmetry:
                        for reflected in reflections(selected,height,width,options):add_ids(reflected)
                    if not enumerate_all:break
                    if count%100==0:print(f'{name}: {count} solutions, {time.monotonic()-start:.1f}s',flush=True)
        finally:timer.cancel()
        out=dict(name=name,height=height,width=width,horizontals=horizontals,
                 inventory=dict(inventory),solutions_found=count,
                 status='EXHAUSTED' if answer is False else 'SAT' if answer else 'TIMEOUT',
                 seconds=time.monotonic()-start,first_solution=first,
                 variables=top,clauses=len(clauses),options=len(options),limit_seconds=limit,
                 resumed=resume,reflection_closure=symmetry,blank_fixed_at_corner=blank_corner,
                 solver_statistics=solver.accum_stats())
        if answer is False:
            proof=base.with_suffix('.drat');proof.write_text('\n'.join(solver.get_proof())+'\n')
            final=base.with_suffix('.final.cnf');save_cnf(final,top,clauses+blocks)
            out['proof_bytes']=proof.stat().st_size
            out['final_cnf_sha256']=hashlib.sha256(final.read_bytes()).hexdigest()
            out['proof_sha256']=hashlib.sha256(proof.read_bytes()).hexdigest()
            result=subprocess.run(['/tmp/knuth-drat-trim/drat-trim',str(final),str(proof),'-t','1800'],
                                  text=True,capture_output=True,timeout=1830)
            base.with_suffix('.verification.txt').write_text(result.stdout+result.stderr)
            out['proof_verified']=result.returncode==0 and 's VERIFIED' in result.stdout
            assert out['proof_verified'],result.stdout+result.stderr
    base.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='first_solution'}),flush=True)
    return out


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--limit',type=float,default=1800)
    parser.add_argument('--mode',choices=['validate','max36','balanced36','all48','planar32'],default='validate')
    parser.add_argument('--resume',action='store_true')
    parser.add_argument('--symmetry',action='store_true')
    parser.add_argument('--blank-corner',action='store_true')
    parser.add_argument('--label')
    args=parser.parse_args();OUT.mkdir(exist_ok=True)
    all_patterns,flat_patterns,stats=catalog()
    (OUT/'catalog.json').write_text(json.dumps(stats,indent=2)+'\n')
    if args.mode=='validate':
        stats=validate();(OUT/'validation.json').write_text(json.dumps(stats,indent=2)+'\n')
        print(json.dumps(stats));return
    if args.mode in ('max36','balanced36'):
        inventory=Counter(v for p,v in all_patterns.items() if len(p) in (1,2))
        height,width,horizontals=8,9,32 if args.mode=='max36' else 18
    elif args.mode=='all48':
        inventory=Counter(all_patterns.values());height,width,horizontals=8,12,None
    else:
        inventory=Counter(flat_patterns.values());height,width,horizontals=8,8,None
    solve_problem(args.label or args.mode,height,width,inventory,horizontals,args.limit,
                  args.mode=='max36',args.resume,args.symmetry,args.blank_corner)


if __name__=='__main__':main()
