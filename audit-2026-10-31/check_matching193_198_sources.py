"""Read new source details only. Reuse every accepted matching census unchanged."""
from datetime import datetime, timezone
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import json, time, xml.etree.ElementTree as ET
from extract_chain150 import points
from extract_jigsaw import transform
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/matching193_198'


def graph89(path, low, high):
    root = ET.parse(path)
    vertices, segments = [], []
    for tag in ['fill_path', 'stroke_path']:
        for t in root.iter(tag):
            ps = [p for q in t for p in points(t, q)]
            if not ps or not low < min(y for x,y in ps) <= max(y for x,y in ps) < high:
                continue
            if tag == 'fill_path' and t.get('color') == '1 1 1':
                x0,x1 = min(x for x,y in ps),max(x for x,y in ps)
                y0,y1 = min(y for x,y in ps),max(y for x,y in ps)
                if 2.99 < x1-x0 < 3.01 and 2.99 < y1-y0 < 3.01:
                    vertices.append(((x0+x1)/2, (y0+y1)/2))
            if tag == 'stroke_path' and [q.tag for q in t] == ['moveto','lineto']:
                segments.append(ps)
    assert len(vertices) == 18 and len(segments) == 65
    # One printed segment goes through the middle vertex, representing two edges.
    edges = set()
    for a,b in segments:
        dx,dy = b[0]-a[0],b[1]-a[1]
        norm = dx*dx+dy*dy
        on = []
        for i,(x,y) in enumerate(vertices):
            z = ((x-a[0])*dx+(y-a[1])*dy)/norm
            if -.001 < z < 1.001 and abs((x-a[0])*dy-(y-a[1])*dx)/norm**.5 < .003:
                on.append((z,i))
        on.sort()
        assert len(on) in [2,3] and abs(on[0][0]) < .001 and abs(on[-1][0]-1) < .001
        for (_,i),(_,j) in zip(on,on[1:]):
            e=tuple(sorted([i,j]));assert e not in edges;edges.add(e)
    degree = [sum(i in e for e in edges) for i in range(18)]
    middle, = [i for i,d in enumerate(degree) if d == 2]
    left = [i for i,(x,y) in enumerate(vertices) if x < vertices[middle][0]-.01]
    right = [i for i,(x,y) in enumerate(vertices) if x > vertices[middle][0]+.01]
    assert len(left)==9 and len(right)==8
    expected={tuple(sorted(e)) for group in [left,right] for e in combinations(group,2)}
    bridges = [e for e in edges if middle in e]
    assert len(bridges)==2 and sum(any(i in left for i in e) for e in bridges)==1
    assert edges == expected | set(bridges) and len(edges)==66
    return dict(vertices=vertices,edges=sorted(edges),middle=middle,left=left,right=right,
                straight_source_segments=65,clique_sizes=[9,8],edges_including_two_bridges=66)


def matrix198(path, xshift, yshift):
    centers=[302.37,316.29,330.21,344.13,358.05,371.97,384.03,394.35,404.61]
    centers=[x+xshift for x in centers]
    cells=[[[] for _ in range(9)] for _ in range(9)]
    for t in ET.parse(path).iter('fill_text'):
        for span in t:
            for g in span:
                x,y=transform(t,float(g.get('x')),float(g.get('y')))
                c=g.get('unicode')
                if not (295+xshift < x < 409+xshift and 459+yshift < y < 559+yshift):
                    continue
                assert c.isdigit(),(x,y,c)
                row=round((y-yshift-464.7)/11.25)
                col=min(range(9),key=lambda j:abs(x-centers[j]))
                assert 0<=row<9 and abs(x-centers[col])<4.3
                cells[row][col].append((x,y,c))
    decoded=[];glyph_count=0
    for i,row in enumerate(cells):
        values=[]
        for gs in row:
            glyph_count+=len(gs)
            if len(gs)==1:
                assert gs[0][2]=='0'
                values.append('0');continue
            mid=464.7+yshift+i*11.25
            top=sorted((x,c) for x,y,c in gs if y<mid)
            bottom=sorted((x,c) for x,y,c in gs if y>mid)
            assert ''.join(c for x,c in top)=='1' and len(bottom) in [1,2]
            values.append(str(Fraction(1,int(''.join(c for x,c in bottom)))))
        decoded.append(values)
    expected=json.loads((ROOT/'results/matching_probabilities.json').read_text())['book_example']['matrix']
    assert decoded==expected
    return dict(matrix=decoded,cells=81,source_digit_glyphs=glyph_count,
                reused_oracle='results/matching_probabilities.json')


def main():
    assert not (OUT/'source-checked.json').exists()
    start=time.monotonic()
    graphs={v:graph89(OUT/(v+'.xml'),lo,hi) for v,lo,hi in
            [('original-123',295,355),('draft-45',403,464)]}
    matrices={v:matrix198(OUT/(v+'.xml'),dx,dy) for v,dx,dy in
              [('original-490',0,0),('draft-180',9.66,108.66)]}
    dependencies=['extract_chain150.py','extract_jigsaw.py','puzzle_xcc.py',
                  'results/matching_probabilities.json','results/complete_matching.json',
                  'results/bounded_updates.json','results/bounded_permutations.json',
                  'results/algorithm_x_validation.json']
    traces=[str(p.relative_to(ROOT)) for p in sorted(OUT.glob('*.xml'))]
    save(OUT/'source-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),
        checker_sha256=sha(__file__),dependencies={p:sha(ROOT/p) for p in dependencies},
        trace_hashes={p:sha(ROOT/p) for p in traces},graphs=graphs,matrices=matrices,
        wall_seconds=time.monotonic()-start,solver_calls=0,old_censuses_rerun=0))
    print('PASS: both graphs have 18 vertices and 66 edges; all 81 matrix cells match in both versions.')


if __name__=='__main__':main()
