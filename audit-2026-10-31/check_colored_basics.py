#!/usr/bin/env python3
"""Independent finite checks for DLX77--83 and the word-search/Algorithm C text."""
from collections import Counter
from datetime import datetime,timezone
from itertools import combinations,permutations,product
from pathlib import Path
import hashlib,json,random,time
from colored_dlx import ColoredDLX,brute

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/colored_basics'
NAMES='ABEL BERTRAND BOREL CANTOR CATALAN FROBENIUS GLAISHER GRAM HADAMARD HENSEL HERMITE HILBERT HURWITZ JENSEN KIRCHHOFF KNOPP LANDAU MARKOFF MELLIN MINKOWSKI NETTO PERRON RUNGE STERN STIELTJES SYLVESTER WEIERSTRASS'.split()
GRID='''OTHESCATALANDAU
TSEAPUSTHORSROF
TLSEEAYRRLYHAPA
EPEARELRGOUEMSI
NNARRCVLTRTAAMA
ITHUOTEKWIANDEM
LANTNBSIMICMAAW
LGDNARTREBLIHCE
ERECIZECEPTNEDY
MEARSHRHLIPKATH
EJENSENHRIEONET
HSUINEBORFEWNAR
TMARKOFFOFCSOKM
PLUTERPFROEKGRA
GMMINSEJTLEITSG'''.splitlines()
PACKED='CATALANDAUBOREL GRAMARKOFFKNOPP ABELWEIERSTRASS BERTRANDHERMITE CANTORFROBENIUS GLAISHERHURWITZ HADAMARDHILBERT HENSELKIRCHHOFF JENSENSYLVESTER MELLINSTIELTJES NETTORUNGESTERN MINKOWSKIPERRON'.split()
TOY=[((1,0),(2,0),(4,0),(5,1)),((1,0),(3,0),(4,1),(5,0)),
     ((1,0),(4,2)),((2,0),(4,1)),((3,0),(5,2))]


def table80():
    run=ColoredDLX(5,3,TOY)
    initial=run.snapshot()
    initial_printed={
      'L':[3,0,1,2,6,4,5], 'R':[1,2,3,0,5,6,4],
      'T':[None,3,2,2,4,3,0,1,2,4,5,-1,1,3,4,5,-2,1,4,-3,2,4,-4,3,5,-5],
      'U':[None,17,20,23,21,24,None,1,2,4,5,7,7,3,9,10,12,12,14,17,8,18,20,13,15,23],
      'D':[None,7,8,13,9,10,10,12,20,14,15,15,17,23,18,24,18,1,21,21,2,4,24,3,5,None],
      'C':[None]*6+[0,0,0,0,1,0,0,0,1,0,0,0,2,0,0,1,0,0,2,0]}
    assert initial==initial_printed,(initial,initial_printed)
    run.solve()
    final_printed={
      'L':[0,0,1,0,6,4,4], 'R':[0,3,3,0,6,6,4],
      'T':[None,1,2,1,2,0,0,1,2,4,5,-1,1,3,4,5,-2,1,4,-3,2,4,-4,3,5,-5],
      'U':[None,12,20,23,18,5,None,1,2,4,5,7,1,3,4,5,12,12,14,17,8,18,20,3,5,23],
      'D':[None,12,8,23,14,5,10,12,20,14,15,15,1,23,18,24,18,1,4,21,2,4,24,3,5,None],
      'C':[None]*6+[0,0,0,0,1,0,0,0,-1,0,0,0,2,0,0,1,0,0,2,0]}
    for field,values in final_printed.items():
        for i,v in enumerate(values):
            if v is not None:
                assert run.first['memory'][field][i]==v,(field,i,v,run.first['memory'][field][i])
    assert run.first['nodes']==[20,12]
    assert run.solutions==brute(3,TOY)=={(1,3)}
    return dict(initial=initial,first_solution=run.first,all_solutions=sorted(run.solutions),
                final_printed=final_printed,all_printed_fields_match=True,profile=dict(run.profile))


def graphs77():
    cases=[]; digest=hashlib.sha256()
    for n in range(5):
        edges=list(combinations(range(n),2)); graphs=[frozenset(edges[k] for k in range(len(edges)) if mask>>k&1) for mask in range(1<<len(edges))]
        count=0
        for g in graphs:
            for h in graphs:
                pairs=list(product(sorted(g),sorted(set(edges)-h)))
                rows=[]
                for v,w in product(range(n),repeat=2):
                    cols=[v+1,n+w+1]+[2*n+j+1 for j,(e,f) in enumerate(pairs) if v in e and w in f]
                    rows.append(tuple((i,0) for i in cols))
                got=ColoredDLX(2*n+len(pairs),2*n,rows).solve().solutions
                expected={tuple(v*n+p[v] for v in range(n)) for p in permutations(range(n))
                          if all(tuple(sorted((p[u],p[v]))) in h for u,v in g)}
                assert got==expected,(n,g,h,got,expected)
                digest.update(json.dumps([n,sorted(g),sorted(h),sorted(got)]).encode())
                count+=1
        cases.append(dict(vertices=n,graph_pairs=count))
    return dict(cases=cases,complete_model_digest=digest.hexdigest(),oracle='All vertex permutations vs literal Algorithm C with every color zero (Algorithm X).')


def words():
    assert len(GRID)==15 and all(len(row)==15 for row in GRID)
    assert len(PACKED)==12 and all(len(row)<=15 for row in PACKED)
    assert all(sum(name in row for row in PACKED)==1 for name in NAMES)
    directions=[(dr,dc) for dr,dc in product((-1,0,1),repeat=2) if dr or dc]
    hits={}; counts={}; occupied=Counter(); options={}
    for name in NAMES:
        choices=set(); matches=[]
        for r,c,(dr,dc) in product(range(15),range(15),directions):
            cells=tuple((r+k*dr,c+k*dc) for k in range(len(name)))
            if all(0<=a<15 and 0<=b<15 for a,b in cells):
                choice=tuple(sorted((a,b,ch) for (a,b),ch in zip(cells,name)))
                choices.add(choice)
                if ''.join(GRID[a][b] for a,b in cells)==name:
                    matches.append(dict(start=[r,c],direction=[dr,dc],cells=cells))
        assert len(matches)==1,(name,matches)
        counts[name]=len(choices); hits[name]=matches[0]; options[name]=choices
        occupied.update(matches[0]['cells'])
    lengths=Counter(map(len,NAMES)); distribution=[lengths[k] for k in range(4,12)]
    assert distribution==[2,5,6,5,3,5,0,1]
    per_length=[4*15*(16-k)+4*(16-k)**2 for k in range(4,12)]
    assert per_length==[1296,1144,1000,864,736,616,504,400]
    assert sum(counts.values())==24320
    assert all(counts[name]==per_length[len(name)-4] for name in NAMES)
    assert sum(map(len,NAMES))==184 and len(occupied)==135
    center=[name for name,v in hits.items() if (7,7) in v['cells']]
    left=[name for name,v in hits.items() if (7,6) in v['cells']]
    assert sorted(center)==sorted(['BERTRAND','GLAISHER','HERMITE','HILBERT','KIRCHHOFF','WEIERSTRASS'])
    assert len(left)==5
    message=''.join(GRID[r][c] for r,c in product(range(15),repeat=2) if (r,c) not in occupied)
    assert message=='THESEAUTHORSOFEARLYPAPERSINACTAMATHEMATICAWERECITEDYEARSLATERINTHEARTOFCOMPUTERPROGRAMMING'
    listed=[('ABEL',[(0,0,'A'),(0,1,'B'),(0,2,'E'),(0,3,'L')]),
      ('ABEL',[(0,0,'A'),(1,0,'B'),(2,0,'E'),(3,0,'L')]),
      ('ABEL',[(0,0,'A'),(1,1,'B'),(2,2,'E'),(3,3,'L')]),
      ('ABEL',[(0,0,'L'),(0,1,'E'),(0,2,'B'),(0,3,'A')]),
      ('WEIERSTRASS',[(14,c,ch) for c,ch in zip(range(4,15),'SSARTSREIEW')])]
    for name,choice in listed: assert tuple(sorted(choice)) in options[name],(name,choice)
    return dict(grid=GRID,packed_rows=PACKED,packed_widths=list(map(len,PACKED)),length_distribution=distribution,
                placements_by_length=per_length,placements_per_name=counts,placements=sum(counts.values()),
                matches=hits,letters=184,occupied_cells=135,center_names=center,left_names=left,hidden_message=message)


def validation():
    rng=random.Random(770083); cases=0; uncolored=0
    universe=[tuple([(i,0) for i in (1,2) if mask>>(i-1)&1]+([] if c is None else [(3,c)]))
              for mask,c in product(range(1,4),(None,0,1,2))]
    matrices=(rows for k in range(6) for rows in combinations(universe,k))
    larger=[]
    universe2=[tuple([(i,0) for i in (1,2) if mask>>(i-1)&1]+
                         [(i,c) for i,c in zip((3,4),(a,b)) if c is not None])
               for mask,a,b in product(range(1,4),(None,0,1,2),(None,0,1,2))]
    for _ in range(2000): larger.append(rng.sample(universe2,rng.randrange(11)))
    from itertools import chain
    for rows in chain(matrices,larger):
        n=max([2]+[i for row in rows for i,c in row]); expected=brute(2,rows)
        for mrv in (False,True):
            a=ColoredDLX(n,2,rows).solve(mrv=mrv)
            b=ColoredDLX(n,2,rows,secondary_lengths=False).solve(mrv=mrv)
            assert a.solutions==b.solutions==expected
            assert a.events==b.events and a.profile==b.profile
            if all(c==0 for row in rows for i,c in row):
                x=ColoredDLX(n,2,rows,colored=False).solve(mrv=mrv)
                assert x.solutions==expected and x.events==a.events and x.snapshot()==a.snapshot()
        uncolored+=all(c==0 for row in rows for i,c in row)
        cases+=1
    return dict(matrices=cases,uncolored_matrices=uncolored,policies=['first','MRV'],oracle='All row subsets; full model sets, traces, profiles and restoration checked. Secondary LEN omission leaves the entire trace unchanged.')


def prefix83():
    rng=random.Random(830083); cases=0
    # The terminal marker in each root row is uncolored, and root rows do not
    # themselves contain earlier markers. Nonroot rows may have colored markers.
    universe=[tuple([(i,0) for i in (2,3) if mask>>(i-2)&1]+
                    [(i,c) for i,c in zip((4,5),(a,b)) if c is not None])
              for mask,a,b in product(range(1,4),(None,0,1,2),(None,0,1,2))]
    for _ in range(1000):
        rows=[((1,0),(4,0)),((1,0),(5,0))]+rng.sample(universe,rng.randrange(9))
        expanded=[rows[0],((1,0),(4,0),(5,0))]+rows[2:]
        expected=brute(3,expanded)
        got=ColoredDLX(5,3,rows).solve(root=1,prefix83=True).solutions
        assert got==expected
        cases+=1
    # Explicit colors are permitted for secondary items by the general XCC
    # definition, but the printed extension tests color zero.
    colored=[((1,0),(3,1)),((1,0),(4,0)),((2,0),(3,1))]
    modified=ColoredDLX(4,2,colored).solve(root=1,prefix83=True).solutions
    allowed={model for model in brute(2,colored) if not (1 in model and any(i==3 for r in model for i,c in colored[r]))}
    assert modified=={(0,2),(1,2)} and allowed=={(0,2)}
    # A decisive all-uncolored counterexample: distinct terminal markers do
    # not prevent an earlier marker from also occurring in another root row.
    overlapping=[((1,0),(3,0)),((1,0),(3,0),(4,0)),((1,0),(5,0)),((2,0),(3,0))]
    expanded=[overlapping[0],overlapping[1],((1,0),(3,0),(4,0),(5,0)),overlapping[3]]
    broken=ColoredDLX(5,2,overlapping).solve(root=1,prefix83=True)
    assert broken.solutions=={(2,3)} and brute(2,expanded)==set()
    assert ColoredDLX(5,2,expanded).solve(root=1).solutions==set()
    # Direct requirement: every root option contains p, exactly one q row
    # must be added. First two conflict on a; third violates earlier a.
    assert brute(2,overlapping)=={(2,3)}
    return dict(uncolored_terminal_cases=cases,colored_terminal_case=dict(rows=colored,printed=sorted(modified),required=sorted(allowed)),
                uncolored_overlap_counterexample=dict(rows=overlapping,expanded=expanded,printed=sorted(broken.solutions),required=[],
                  first_solution=broken.first,events=broken.events),
                sufficient_repair='Require each distinguished terminal item to occur in exactly one root option and to have color zero there. The 1000 randomized tests obey this stronger hypothesis; see the general invariant proof in the notes.',
                limitation='Colored-tail ambiguity is not counted as a separate finding. The all-uncolored case disproves the stated result without relying on a color convention.')


def main():
    start=time.monotonic(); OUT.mkdir(parents=True,exist_ok=True)
    result={}
    for label,fn in [('table80',table80),('word_search',words),('graphs77',graphs77),('interpreter_validation',validation),('prefix83',prefix83)]:
        result[label]=fn(); print(label,'PASS',flush=True)
    result.update(status='pass',checked_at_utc=datetime.now(timezone.utc).isoformat(),seconds=time.monotonic()-start,
                  scripts={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),ROOT/'colored_dlx.py')})
    (OUT/'check.json').write_text(json.dumps(result,indent=2)+'\n')
    print('All checks passed in',round(result['seconds'],2),'seconds')


if __name__=='__main__': main()
