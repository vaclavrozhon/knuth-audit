"""Independent factor/orientation checks and exact disk/card puzzle solutions."""
from pathlib import Path
from itertools import product, permutations
from collections import Counter
from fractions import Fraction
from math import factorial
import json, random, time
from check_letter_cubes import rotations, transform, SIDES

R=Path(__file__).resolve().parent/'results/factor_puzzles'

def factor_data(cubes):
    n=len(cubes);factors=[]
    for choice in product(range(3),repeat=n):
        edges=[cubes[i][c] for i,c in enumerate(choice)]
        if Counter(a for edge in edges for a in edge)!=Counter({i:2 for i in range(n)}):continue
        adj=[set() for _ in range(n)]
        for a,b in edges:adj[a].add(b);adj[b].add(a)
        unseen=set(range(n));components=0
        while unseen:
            stack=[unseen.pop()];components+=1
            for a in stack:
                for b in adj[a]&unseen:unseen.remove(b);stack.append(b)
        factors.append((choice,components))
    pairs=[];orientation_count=0
    for i,(a,ca) in enumerate(factors):
        for j,(b,cb) in enumerate(factors[:i]):
            if all(x!=y for x,y in zip(a,b)):
                pairs.append((j,i));orientation_count+=2**(ca+cb+1)
    return factors,pairs,orientation_count

def orientations(cubes):
    normals=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    result=[]
    for cube in cubes:
        colors=[a for edge in cube for a in edge];choices=[]
        for m in rotations():
            placed={transform(m,n):c for n,c in zip(normals,colors)}
            choices.append(tuple(placed[n] for n in SIDES))
        result.append(choices)
    return result

def physical_count(cubes):
    choices=orientations(cubes);n=len(cubes)
    def search(i,masks):
        if i==n:return 1
        total=0
        for colors in choices[i]:
            if all(not(mask>>c&1) for mask,c in zip(masks,colors)):
                total+=search(i+1,tuple(mask|1<<c for mask,c in zip(masks,colors)))
        return total
    return search(0,(0,0,0,0))

def cube_checks():
    main=[[(0,3),(0,1),(3,2)],[(0,0),(0,2),(3,1)],[(2,2),(3,1),(0,1)],[(3,1),(3,2),(0,2)]]
    example=[[(1,2),(1,3),(3,4)],[(0,2),(0,3),(1,4)],[(0,1),(1,4),(2,4)],[(0,4),(1,3),(2,3)],[(0,1),(1,2),(3,4)]]
    out=[]
    for cubes in [main,example]:
        f,p,count=factor_data(cubes);physical=physical_count(cubes)
        assert len(f)==3 and len(p)==1 and count==physical==8
        assert all(f[i][1]==1 for i in p[0])
        out.append({'factors':f,'disjoint_pairs':p,'physical_orientations':physical,'color_counts':dict(Counter(a for c in cubes for e in c for a in e))})
    assert min(out[1]['color_counts'].values())>=5
    rng=random.Random(20261101062);checked=0
    for n,cases in [(2,50),(3,100),(4,200),(5,100)]:
        for _ in range(cases):
            cubes=[[(rng.randrange(n),rng.randrange(n)) for _ in range(3)] for _ in range(n)]
            assert factor_data(cubes)[2]==physical_count(cubes);checked+=1
    # Three disjoint factors necessarily arise when all colors occur six times:
    # the complement of two 2-factors has degree 6-2-2=2, one edge per cube.
    exact_six=0
    for _ in range(200):
        colors=list(range(4))*6;rng.shuffle(colors)
        cubes=[[tuple(colors[6*i+2*j:6*i+2*j+2]) for j in range(3)] for i in range(4)]
        f,p,count=factor_data(cubes)
        if p:assert len(p)>=3;exact_six+=1
    return {'examples':out,'random_graph_vs_physical_checks':checked,'exact_six_solvable_examples':exact_six}

def disks():
    rings=[[5,1,5,3,4,3,2,4],[3,4,5,3,3,2,2,1],
           [2,1,3,4,2,5,1,3],[3,4,1,3,4,5,3,2]]
    solutions=[]
    for shifts in product(range(8),repeat=3):
        shifts=(0,)+shifts
        if all(sum(rings[i][(ray-shifts[i])%8] for i in range(4))==12 for ray in range(8)):
            solutions.append(shifts)
    assert solutions==[(0,3,4,5)]
    # Explicit successive quotient constraints: mod angular 2, then 4, then 8.
    parity=[]
    for bits in product(range(2),repeat=3):
        shifts=(0,)+bits
        if sum(rings[i][(r-shifts[i])%8] for i in range(4) for r in [0,2,4,6])==48:parity.append(shifts)
    assert parity==[(0,0,0,0),(0,1,0,1)]
    quarters=[]
    for base in parity:
        for bits in product([0,2],repeat=3):
            shifts=tuple(a+b for a,b in zip(base,(0,)+bits))
            if sum(rings[i][(r-shifts[i])%8] for i in range(4) for r in [0,4])==24:quarters.append(shifts)
    assert quarters==[(0,2,0,2),(0,2,2,2),(0,3,0,1),(0,3,2,1)]
    opposite_sums=[[sum(rings[i][(r-shifts[i])%8] for i in range(4) for r in [j,j+4])
                    for j in range(4)] for shifts in quarters]
    assert opposite_sums==[[24,19,24,29],[24,20,24,28],[24,24,24,24],[24,25,24,23]]
    surviving=[s for s,sums in zip(quarters,opposite_sums) if sums==[24]*4]
    assert surviving==[(0,3,0,1)]
    # The book incorrectly rejects the first parity case from N+S alone.
    # It is NE+SW (19 or 20 rather than 24) that rejects its two possibilities.
    return {'rings_N_clockwise':rings,'solutions_clockwise_eighth_turns':solutions,'parity_stage':parity,
            'quarter_stage':quarters,'opposite_sums_at_quarter_stage':opposite_sums,
            'surviving_quarter_stage':surviving,'search_space':8**3}

def cards():
    cards=[(1,5,2,5),(5,1,1,3),(4,7,2,5),(4,5,4,2),(5,2,7,4),
           (5,5,7,7),(7,3,8,4),(5,4,3,4),(3,7,5,5)]
    oriented=[(i,rot,c if rot==0 else c[2:]+c[:2]) for i,c in enumerate(cards) for rot in [0,1]]
    rows=[]
    for a,b,c in permutations(oriented,3):
        if len({a[0],b[0],c[0]})<3:continue
        if a[2][0]+b[2][0]+c[2][0]==13 and a[2][2]+b[2][2]+c[2][2]==13:
            rows.append((a,b,c))
    masks=[sum(1<<x[0] for x in row) for row in rows];by_mask={}
    for row,mask in zip(rows,masks):by_mask.setdefault(mask,[]).append(row)
    solutions=[]
    for a,ma in zip(rows,masks):
        for b,mb in zip(rows,masks):
            if ma&mb:continue
            for c in by_mask.get(511^ma^mb,[]):
                if all(a[j][2][k]+b[j][2][k]+c[j][2][k]==13 for j in range(3) for k in [1,3]):
                    solutions.append((a,b,c))
    printed=['8473','2515','3454','4245','2547','7452','7755','1351','5537']
    assert any([''.join(map(str,x[2])) for row in s for x in row]==printed for s in solutions)
    assert len(solutions)==72
    return {'cards_NESW':cards,'valid_rows':len(rows),'all_solutions':len(solutions),'printed_solution':printed}

def summary():
    d=json.loads((R/'strong-exact.json').read_text())
    restricted=sum(factorial(24)//(factorial(a)*factorial(b)*factorial(c)*factorial(24-a-b-c))
                   for a,b,c in product(range(5,10),repeat=3) if 5<=24-a-b-c<=9)
    p=Fraction(d['strong_face_colorings'],d['all_face_colorings']);q=Fraction(d['strong_restricted_face_colorings'],restricted)
    factor_p=Fraction(factorial(8),2**4*4**8)
    return {'strong_probability_exact':str(p),'strong_probability':float(p),
            'strong_restricted_probability_exact':str(q),'strong_restricted_probability':float(q),
            'restricted_face_colorings':restricted,'expected_factors_exact':str(3**4*factor_p),
            'expected_disjoint_pairs_exact':str(Fraction(6**4,2)*factor_p**2),
            'markov_upper_bound_at_least10_pairs':float(Fraction(6**4,20)*factor_p**2),
            'printed_unrestricted_percent_sum':str(sum(map(Fraction,['74.4','4.3','8.7','1.3','6.2','.2','1.5','.1','2.0','0.0','12.2'])))}

if __name__=='__main__':
    start=time.monotonic();out={'status':'pass','cubes':cube_checks(),'disks':disks(),'cards':cards(),'probabilities':summary(),'elapsed_seconds':time.monotonic()-start}
    (R/'verified.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
