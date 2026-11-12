#!/usr/bin/env python3
"""DLX68: independent convexity predicates and complete placement sets."""
from collections import defaultdict
from datetime import datetime, timezone
import gzip
from itertools import combinations
import json
from dlx1_audit_tools import ROOT, sha, input_text
from prepare_jigsaw_tilings import grown_shapes

OUT = ROOT/'results/convex68'


def convex(shape):
    for axis in (0, 1):
        lines = defaultdict(list)
        for p in shape:
            lines[p[axis]].append(p[1-axis])
        if any(max(v)-min(v)+1 != len(v) for v in lines.values()):
            return False
    return True


def perimeter_convex(shape):
    s = set(shape)
    perimeter = sum((x+dx,y+dy) not in s for x,y in s
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)))
    w = max(x for x,y in s)-min(x for x,y in s)+1
    h = max(y for x,y in s)-min(y for x,y in s)+1
    return perimeter == 2*(w+h)


def bounded(shape, side):
    return all(max(p[a] for p in shape)-min(p[a] for p in shape) < side
               for a in (0,1))


def placements(shapes, n):
    return {tuple(sorted((r+y)*n+c+x for x,y in p))
            for p in shapes for r in range(n-max(y for x,y in p))
            for c in range(n-max(x for x,y in p))}


def canonical(shape):
    reps = []
    for swap in (False, True):
        for sx in (-1,1):
            for sy in (-1,1):
                s = [(sx*(y if swap else x), sy*(x if swap else y)) for x,y in shape]
                a,b = min(x for x,y in s),min(y for x,y in s)
                reps.append(tuple(sorted((x-a,y-b) for x,y in s)))
    return min(reps)


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    old = json.loads((ROOT/'results/jigsaw/tilings/options.json').read_text())
    result = dict(source_sha256=sha(__file__), growth_sha256=sha(ROOT/'prepare_jigsaw_tilings.py'),
                  prior_archive_sha256=sha(ROOT/'results/jigsaw/tilings/options.json'), cases={})
    expected_shapes = [1,2,6,19,59,176,502]
    expected_options = [1,4,22,113,523,2196,8438]
    for n, shapes in grown_shapes(9):
        assert all(convex(s)==perimeter_convex(s) for s in shapes)
        if n == 5:
            free = {canonical(s) for s in shapes}
            nonconvex = {s for s in free if not convex(s)}
            assert len(free)==12 and nonconvex=={canonical(((0,0),(0,1),(1,1),(2,0),(2,1)))}
            result['pentominoes'] = dict(free=12, convex=11, unique_nonconvex=sorted(nonconvex))
        if n == 8:
            continue
        good = {s for s in shapes if convex(s) and (n!=9 or bounded(s,4))}
        rows = placements(good,n)
        if n <= 2:
            independent = {tuple(c) for c in combinations(range(n*n),n)
                           if n==1 or abs(c[0]//n-c[1]//n)+abs(c[0]%n-c[1]%n)==1}
        else:
            oldpath=ROOT/f'results/jigsaw/tilings/n{n}.json.gz'
            assert sha(oldpath)==old['files'][f'n{n}']['json_sha256']
            connected=set(map(tuple,json.loads(gzip.decompress(oldpath.read_bytes()))))
            connected |= {tuple(r*n+c for c in range(n)) for r in range(n)}
            connected |= {tuple(r*n+c for r in range(n)) for c in range(n)}
            independent = {t for t in connected if perimeter_convex([(v%n,v//n) for v in t])
                           and (n!=9 or bounded([(v%n,v//n) for v in t],4))}
        assert rows==independent
        if n<=7:
            assert len(good)==expected_shapes[n-1] and len(rows)==expected_options[n-1]
        else:
            assert len(good)==325 and len(rows)==12097
        variants = {f'n{n}': rows}
        if n==9:
            squares={tuple(9*(r+y)+c+x for y in range(3) for x in range(3))
                     for r in range(7) for c in range(7)}
            assert squares<=rows and len(squares)==49
            variants['n9-no-square'] = rows-squares
        for label,tiles in variants.items():
            p=OUT/(label+'.json.gz')
            with gzip.open(p,'wt') as stream:json.dump(sorted(tiles),stream)
            dlx=OUT/(label+'.dlx')
            dlx.write_text(input_text([f'p{r}{c}' for r in range(n) for c in range(n)],
                                      [[v+1 for v in t] for t in sorted(tiles)]))
            result['cases'][label]=dict(n=n,all_fixed_shapes=len(shapes),convex_shapes=len(good),
                 options=len(tiles),json_sha256=sha(p),dlx_sha256=sha(dlx),
                 complete_placement_sets_equal=True,all_convexity_predicates_agree=True)
            print(label,len(good),len(tiles),'complete sets agree',flush=True)
    result.update(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat())
    (OUT/'options.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
