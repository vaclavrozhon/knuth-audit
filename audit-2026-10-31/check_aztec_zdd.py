"""Validate X262(a) via explicit families, canonical ZDDs and determinants."""
from functools import lru_cache
from pathlib import Path
import argparse,json,subprocess,time
import sympy as sp

ROOT=Path(__file__).parent
BINARY='/tmp/knuth-aztec-zdd'


def cells(height,width,corner):
    return {(r,c) for r in range(height) for c in range(width)
            if min(r+c,height-1-r+c,r+width-1-c,height+width-2-r-c)>=corner}


def explicit(height,width,corner):
    board=cells(height,width,corner)
    edges=[]
    for r,c in board:
        for b in [(r+1,c),(r,c+1)]:
            if b in board:edges.append(((r,c),b))
    edges.sort(key=lambda e:(e[0][1]*height+e[0][0],-(e[1][1]*height+e[1][0])))
    options=[frozenset(e) for e in edges]
    def search(remaining,chosen):
        if not remaining:
            yield frozenset(chosen);return
        a=min(remaining)
        for j,edge in enumerate(options):
            if a in edge and edge<=remaining:
                yield from search(remaining-edge,chosen+[j])
    family=frozenset(search(board,[]));nodes={}
    @lru_cache(None)
    def zdd(family):
        if not family:return 0
        if family==frozenset([frozenset()]):return 1
        var=min(v for solution in family for v in solution)
        lo=zdd(frozenset(s for s in family if var not in s))
        hi=zdd(frozenset(s-{var} for s in family if var in s))
        if hi==0:return lo
        key=(var,lo,hi)
        if key not in nodes:nodes[key]=len(nodes)+2
        return nodes[key]
    root=zdd(family)
    return len(family),len(nodes)+2 if root>1 else 1


def run(height,width,corner):
    out=subprocess.check_output([BINARY,str(height),str(width),str(corner)],text=True)
    return json.loads(out)


def determinant(height,width,corner):
    board=cells(height,width,corner)
    black=sorted(p for p in board if sum(p)%2==0)
    white=sorted(p for p in board if sum(p)%2==1)
    if len(black)!=len(white):return 0
    lookup={p:i for i,p in enumerate(white)}
    matrix=[[0]*len(white) for _ in black]
    for i,(r,c) in enumerate(black):
        for rr,cc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
            if (rr,cc) in lookup:matrix[i][lookup[rr,cc]]=(-1)**c if c==cc else 1
    return abs(int(sp.Matrix(matrix).det(method='domain-ge')))


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--validate-only',action='store_true')
    args=parser.parse_args();start=time.monotonic();cases=0
    for height in range(1,6):
        for width in range(1,8):
            if height*width>30:continue
            for corner in range(min(height,width)):
                expected,nodes=explicit(height,width,corner)
                got=run(height,width,corner)
                assert (int(got['solutions']),got['zdd_nodes'])==(expected,nodes),(height,width,corner,expected,nodes,got)
                assert determinant(height,width,corner)==expected
                cases+=1
    validation=dict(exact_cover_families_and_canonical_zdds=cases,determinant_comparisons=cases,
                    seconds=time.monotonic()-start)
    (ROOT/'results/aztec_zdd_validation.json').write_text(json.dumps(validation,indent=2)+'\n')
    print(json.dumps(validation),flush=True)
    if args.validate_only:return
    results=[]
    for width in [16,28,29,30,31,32,33,34,40]:
        got=run(16,width,7)
        if width>=30:assert got['zdd_nodes']==154440*width-2655855,got
        if width==16:assert int(got['solutions'])==2**36
        if width==32:assert int(got['solutions'])==152326556015596771390830202722034115329
        if width in (16,32):
            start=time.monotonic();independent=determinant(16,width,7)
            assert int(got['solutions'])==independent
            got['determinant_verified']=True;got['determinant_seconds']=time.monotonic()-start
        results.append(got)
        (ROOT/'results/aztec_zdd.json').write_text(json.dumps(results,indent=2)+'\n')
        print(json.dumps(got),flush=True)


if __name__=='__main__':main()
