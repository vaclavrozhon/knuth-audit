"""Finite path-domino catalogue and parity certificates; no placement search."""
from collections import Counter
from itertools import combinations
from pathlib import Path
from puzzle_xcc import save, sha

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/paths151_152'
# Clockwise boundary points on a horizontal 2-by-1 domino, doubled coordinates.
PORTS=((1,0),(3,0),(4,1),(3,2),(1,2),(0,1))

def pairings(v):
    if not v:
        yield ();return
    a=v[0]
    for b in v[1:]:
        for tail in pairings(tuple(x for x in v if x not in (a,b))):
            yield tuple(sorted(((a,b),)+tail))

def rotate(p):
    return tuple(sorted(tuple(sorted(((a+3)%6,(b+3)%6))) for a,b in p))

def canonical(p):
    p=tuple(sorted(tuple(sorted(pair)) for pair in p))
    return min(p,rotate(p))

def crossing(p):
    return any(a<c<b<d or c<a<d<b for (a,b),(c,d) in combinations(p,2))

def catalogue(k):
    raw={p for s in combinations(range(6),2*k) for p in pairings(s)}
    return raw,{canonical(p) for p in raw}

def mask(p):return tuple(sorted(x for pair in p for x in pair))
def mask_type(v):return min(tuple(sorted(v)),tuple(sorted((x+3)%6 for x in v)))

def main():
    records=[];noncross=[]
    for k,expected in enumerate([(1,1,1,1),(15,3,9,9),(45,9,27,18),(15,7,11,4)]):
        raw,reps=catalogue(k);fixed=sum(rotate(p)==p for p in raw)
        nc={p for p in reps if not crossing(p)}
        assert (len(raw),fixed,len(reps),len(nc))==expected
        assert len(reps)==(len(raw)+fixed)//2
        counts=Counter(mask_type(mask(p)) for p in reps)
        assert set(counts.values())=={[1,1,3,11][k]}
        odd=sum(sum(x in (0,4,5) for pair in p for x in pair)%2 for p in nc)
        records.append(dict(subpaths=k,raw=len(raw),half_turn_fixed=fixed,types=len(reps),noncrossing=len(nc),
            noncrossing_odd_cell_endpoint_types=odd,mask_multiplicities=[dict(mask=v,count=c) for v,c in sorted(counts.items())],
            catalogue=sorted(reps),noncrossing_catalogue=sorted(nc)))
        noncross+=list(nc)
    assert len(noncross)==32
    paths=sum(len(p) for p in noncross)
    odd=sum(sum(x in (0,4,5) for pair in p for x in pair)%2 for p in noncross)
    assert paths==57 and odd==16 and paths%2!=odd%2
    # Every domino covers one black and one white cell. Its two cell endpoint
    # parities agree, because its total endpoint count is even. Therefore the
    # parity of black endpoints is fixed under every placement. Every joined
    # boundary endpoint pairs black with white, so black endpoints must equal
    # half the total number of endpoints, i.e. the number of printed subpaths.
    # Here the former is even, the latter57 odd. No placement search is needed.
    save(OUT/'catalogue-checked.json',dict(checker_sha256=sha(__file__),records=records,
        single_and_double_types=36,all_types=48,noncrossing_types=32,noncrossing_subpaths=paths,
        noncrossing_odd_cell_endpoint_types=odd,noncrossing_unsat_by_checkerboard_parity=True,placement_searches=0,
        maximum_horizontals_proof='Each of8 rows has odd width9, hence at least one vertical-domino cell. Thus at least4 vertical dominoes and at most32 horizontal. Equality forces one vertical cell per row, pairing rows0–1,2–3,4–5,6–7; no odd-height vertical placement. A printed witness proves attainability.'))
    print('PASS:9+27 types,12 extras,32 noncrossing; noncrossing UNSAT:57 subpaths versus16 odd cell-endpoint types. No search.')

if __name__=='__main__':main()
