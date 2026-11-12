#!/usr/bin/env python3
"""Compare every vector node and edge of Figure 68 with the 8-queens tree.

Uses the actual PDF content stream, not OCR or a raster approximation.
The page draws nodes as zero-length stroked segments and edges as lines.
"""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import math
import pikepdf

ROOT=Path(__file__).resolve().parent
BOOK=ROOT.parent/'books/taocp-vol4b-ed1-print2-2022.pdf'


def main():
    pdf=pikepdf.open(BOOK)
    page=pdf.pages[51]
    assert not page.Resources.get('/XObject',{})
    shift=(0.0,0.0);stack=[];dots=[];edges=[];position=None;line=None
    for instruction in pikepdf.parse_content_stream(page):
        op=str(instruction.operator)
        v=list(map(float,instruction.operands)) if op in {'cm','m','l'} else []
        if op=='q':stack.append(shift)
        elif op=='Q':shift=stack.pop()
        elif op=='cm':
            assert v[:4]==[1,0,0,1], 'This page should use translations only.'
            shift=(shift[0]+v[4],shift[1]+v[5])
        elif op=='m':
            position=(shift[0]+v[0],shift[1]+v[1]);line=None
        elif op=='l':
            assert line is None, 'Unexpected multi-segment stroke.'
            line=(position,(shift[0]+v[0],shift[1]+v[1]));position=line[1]
        elif op=='S':
            assert line is not None
            if line[0]==line[1]:dots.append(line[0])
            else:edges.append(line)
            line=None
        elif op in {'c','v','y','h','s','B','B*','b','b*','Do'}:
            raise ValueError('Unexpected unaccounted vector operation: '+op)
    assert not stack
    assert len(dots)==len(set(dots))==2057 and len(edges)==2056
    children=defaultdict(list);parents={};errors=[];second_distances=[]
    # The scanned endpoint and its separate dot can differ slightly because
    # of PDF coordinate rounding. The fixed tolerance is well separated from
    # all other dots; record both distances rather than silently snapping.
    tolerance=.1
    for edge in edges:
        ids=[]
        for endpoint in edge:
            nearest=sorted((math.dist(endpoint,dot),i) for i,dot in enumerate(dots))
            assert nearest[0][0]<tolerance and nearest[1][0]>2*tolerance
            errors.append(nearest[0][0]);second_distances.append(nearest[1][0])
            ids.append(nearest[0][1])
        u,v=ids
        if dots[u][1]<dots[v][1]:u,v=v,u
        assert dots[u][1]>dots[v][1] and v not in parents
        children[u].append(v);parents[v]=u
    roots=set(range(len(dots)))-set(parents)
    assert len(roots)==1
    root=roots.pop();profile=Counter();seen=set();labeled_nodes=[]

    def compare(u,prefix):
        assert u not in seen
        seen.add(u);r=len(prefix);profile[r]+=1
        legal=[c for c in range(8) if all(c!=a and abs(c-a)!=r-j
               for j,a in enumerate(prefix))] if r<8 else []
        ordered=sorted(children[u],key=lambda v:dots[v][0])
        assert len(ordered)==len(legal),(prefix,len(ordered),len(legal))
        labeled_nodes.append(dict(id=u,position_points=dots[u],
            assigned_prefix_zero_based=prefix,parent=parents.get(u),children=ordered))
        for v,c in zip(ordered,legal):compare(v,prefix+[c])

    compare(root,[])
    assert seen==set(range(2057))
    assert [profile[k] for k in range(9)]==[1,8,42,140,344,568,550,312,92]
    assert len({tuple(node['assigned_prefix_zero_based']) for node in labeled_nodes})==2057
    possibilities=8**8;placements=math.comb(64,8)
    assert possibilities==16777216 and placements==4426165368
    percentage_nodes=Fraction(100*2057,possibilities)
    percentage_tuples=Fraction(100*possibilities,placements)
    assert Fraction(5,1000)<percentage_nodes<Fraction(15,1000)
    assert Fraction(375,1000)<percentage_tuples<Fraction(385,1000)
    result=dict(verified=True,checked_at_utc=datetime.now(timezone.utc).isoformat(),
        book=str(BOOK.relative_to(ROOT.parent)),book_sha256=hashlib.sha256(BOOK.read_bytes()).hexdigest(),
        parser_version=pikepdf.__version__,printed_page=32,pdf_page=52,
        nodes=len(dots),edges=len(edges),root_id=root,
        endpoint_tolerance_points=tolerance,max_endpoint_error_points=max(errors),
        minimum_second_nearest_dot_distance_points=min(second_distances),
        profile=[profile[k] for k in range(9)],every_ordered_subtree_matches=True,
        page31_arithmetic=dict(tuples=possibilities,unrestricted_placements=placements,
            nodes_percentage_exact=str(percentage_nodes),tuples_percentage_exact=str(percentage_tuples),
            rounded_percentages=['0.01%','0.38%']),
        scope='All 2057 dots and 2056 edges match the ordered legal-prefix tree. '
              'Column labels are assigned by lexicographic order, not printed in Figure 68.',
        extracted_nodes=sorted(labeled_nodes,key=lambda node:node['id']))
    destination=ROOT/'results/backtrack_basics/figure68-verified.json'
    destination.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='extracted_nodes'},indent=2))


if __name__=='__main__':main()
