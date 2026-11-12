"""Decode the seven source matrices; do not repeat accepted matching searches."""
from datetime import datetime, timezone
from pathlib import Path
import json, time, xml.etree.ElementTree as ET
from extract_jigsaw import transform
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/matching199_201'
OPTIONS = [(0,0,1,'t'),(0,1,0,'u'),(1,2,1,'v'),(1,2,2,'w'),
           (2,0,2,'x'),(2,1,0,'y'),(2,1,1,'z')]
EXCLUDED = [set(),{2},{1},{1,2},{0},{0,2},{0,1}]


def matrices(path, shift, baselines):
    # Column intervals accommodate the sums y+z and v+w, whose glyphs are
    # deliberately not assigned to the nearest single-character center.
    groups = [85,137,185,226,264,311,349,386]
    cuts = [(97,114),(154,172),(202,212),(242,252),(281,290),(327,336),(365,374)]
    cells = [[[[] for _ in range(3)] for _ in range(3)] for _ in range(7)]
    glyph_count = 0
    for text in ET.parse(path).iter('fill_text'):
        for span in text:
            for g in span:
                x,y = transform(text,float(g.get('x')),float(g.get('y')))
                x -= shift
                if not groups[0] <= x < groups[-1]: continue
                r = min(range(3),key=lambda i:abs(y-baselines[i]))
                if abs(y-baselines[r]) > .12: continue
                char = g.get('unicode')
                if char not in '0tuvwxyz+': continue
                m = next(i for i in range(7) if groups[i] <= x < groups[i+1])
                c = sum(x >= cut for cut in cuts[m])
                cells[m][r][c].append((x,char)); glyph_count += 1
    decoded = [[[''.join(c for x,c in sorted(gs)) for gs in row] for row in mat] for mat in cells]
    expected = []
    for excluded in EXCLUDED:
        mat = [[[] for _ in range(3)] for _ in range(3)]
        for i,j,k,var in OPTIONS:
            if k not in excluded: mat[i][j].append(var)
        expected.append([['+'.join(vs) if vs else '0' for vs in row] for row in mat])
    assert decoded == expected,(path,decoded,expected)
    return dict(matrices=decoded,source_cells=63,source_glyphs=glyph_count,
                excluded_c_indices_1_based=[sorted(i+1 for i in s) for s in EXCLUDED],
                header_sets_checked_visually=True)


def main():
    assert not (OUT/'source-checked.json').exists()
    start=time.monotonic()
    traces=['results/matching193_198/original-169.xml','results/matching193_198/draft-91.xml']
    decoded={
        'book':matrices(ROOT/traces[0],0,[339.58,348.52,357.52]),
        'author_draft':matrices(ROOT/traces[1],22.08,[448.2,457.2,466.08])}
    dependencies=['extract_jigsaw.py','puzzle_xcc.py','results/unsat_3d_matching.json',
                  'results/determinant_matching.json','results/circular_matching.json',
                  'results/algorithm_x_validation.json']
    old=json.loads((ROOT/'results/determinant_matching.json').read_text())
    assert old['zero_test_equality_examples'][1]['Pr(s=0_given_S_nonzero)']=='9/25'
    save(OUT/'source-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),
        checker_sha256=sha(__file__),dependencies={p:sha(ROOT/p) for p in dependencies},
        trace_hashes={p:sha(ROOT/p) for p in traces},matrices=decoded,
        wall_seconds=time.monotonic()-start,solver_calls=0,old_censuses_rerun=0,
        general_proofs='MATCHING199_201_SOURCE_NOTES.md'))
    print('PASS: all 63 matrix cells agree with the seven options in each source; no census rerun.')


if __name__=='__main__':main()
