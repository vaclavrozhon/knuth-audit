#!/usr/bin/env python3
"""All15 edges of the printed matching graph; contrast the14-edge2019 source."""
from datetime import datetime, timezone
import json
import math
import pikepdf
from check_sudoku_basics import BOOK, OUT
from dlx1_audit_tools import ROOT, sha


def compose(m, n):
    a,b,c,d,e,f = m; A,B,C,D,E,F = n
    return (a*A+c*B,b*A+d*B,a*C+c*D,b*C+d*D,a*E+c*F+e,b*E+d*F+f)


def segments(path, page):
    pdf = pikepdf.open(path); matrix = (1,0,0,1,0,0); stack = []; position = None; found = []
    def point(x,y):
        a,b,c,d,e,f = matrix; return a*x+c*y+e,b*x+d*y+f
    for ins in pikepdf.parse_content_stream(pdf.pages[page-1]):
        op = str(ins.operator)
        v = list(map(float,ins.operands)) if op in {'cm','m','l'} else []
        if op == 'q': stack.append(matrix)
        elif op == 'Q': matrix = stack.pop()
        elif op == 'cm': matrix = compose(matrix,v)
        elif op == 'm': position = point(*v)
        elif op == 'l':
            dest = point(*v)
            if 10 < abs(position[1]-dest[1]) < 20 and abs(position[0]-dest[0]) < 100:
                found.append((position,dest))
            position = dest
    assert not stack
    return found


def decode(lines):
    xs = sorted({round(p[0],2) for line in lines for p in line})
    # Separate draws can differ by <=.001pt: cluster the five column centers.
    groups = []
    for x in xs:
        if groups and x-groups[-1][-1] < .02: groups[-1].append(x)
        else: groups.append([x])
    centers = [sum(g)/len(g) for g in groups]
    assert len(centers) == 5, centers
    top, bottom = [3,8,1,2,7], [7,1,4,5,8]
    edges = []
    for a,b in lines:
        assert a[1] > b[1]
        i = min(range(5),key=lambda k:abs(a[0]-centers[k]))
        j = min(range(5),key=lambda k:abs(b[0]-centers[k]))
        assert abs(a[0]-centers[i]) < .02 and abs(b[0]-centers[j]) < .02
        edges.append((top[i],bottom[j]))
    assert len(edges) == len(set(edges))
    return set(edges)


def main():
    lines = segments(BOOK,148); old_lines = segments(ROOT/'sources/fasc5c.pdf',70)
    actual, old = decode(lines), decode(old_lines)
    chart = json.loads((OUT/'pdf-grids.json').read_text())['sources']['33']['cells']
    expected = {(j,k) for j in range(9) if len(chart[9*4+j]) > 1 for k in chart[9*4+j]}
    assert actual == expected and len(actual) == 15
    assert old == expected-{(7,1)} and len(old) == 14
    result = dict(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  source_sha256=sha(__file__),book_sha256=sha(BOOK),author_source_sha256=sha(ROOT/'sources/fasc5c.pdf'),
                  labels_top=[3,8,1,2,7], labels_bottom=[7,1,4,5,8],
                  edges=sorted(actual),old_edges=sorted(old),book_vector_segments=lines,old_vector_segments=old_lines,
                  known_erratum='2021-08-09 F5p126/ex49: add u7-v1. Incorporated in4B128.',
                  scope='Every straight edge extracted from PDF content streams and compared to the entire row4 candidate graph; vertex labels visually checked.')
    (OUT/'diagram.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','edges','old_edges','known_erratum')},indent=2))


if __name__ == '__main__':
    main()
