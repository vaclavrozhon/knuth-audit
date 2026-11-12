#!/usr/bin/env python3
"""Decode Hansson's original1935 coordinates and give all rectangle witnesses."""
import json
import re
from prepare_pentomino_main import OUT,SHAPES,normalized,orientations,connected_components,placements,instance
from dlx1_audit_tools import sha


def first_solution(rows,np):
    by_item=[set() for _ in range(np)]
    sets=list(map(set,rows))
    for i,row in enumerate(rows):
        for j in row:by_item[j-1].add(i)
    def rec(items,active,path):
        if not items:return path
        i=min(items,key=lambda j:len(by_item[j-1]&active))
        for row in sorted(by_item[i-1]&active):
            forbidden=set().union(*(by_item[j-1] for j in sets[row]))
            answer=rec(items-sets[row],active-forbidden,path+[row])
            if answer is not None:return answer
        return None
    return rec(set(range(1,np+1)),set(range(len(rows))),[])


def main():
    # Visual transcription of original page135, not its imperfect OCR.
    strings=['a123bc3','cdef1e2','e3f23g12','i12j23k2','klmn3n2','mnopq1','q2r123s2']
    board=['.']*60;details=[]
    for s in strings:
        cells=sorted((3-int(d))*20+ord(c)-97 for cols,rows in re.findall(r'([a-t]+)([123]+)',s) for c in cols for d in rows)
        assert len(cells)==5
        names=[p for p,shape in SHAPES.items() if normalized([divmod(v,20) for v in cells]) in orientations(shape)]
        assert len(names)==1
        for v in cells:assert board[v]=='.';board[v]=names[0]
        details.append(dict(text=s,cells=cells,piece=names[0]))
    for cs in connected_components({i for i,p in enumerate(board) if p=='.'},3,20):
        names=[p for p,shape in SHAPES.items() if normalized([divmod(v,20) for v in cs]) in orientations(shape)]
        assert len(cs)==5 and len(names)==1
        for v in cs:board[v]=names[0]
    b=''.join(board)
    d=json.loads((OUT/'pdf-diagrams.json').read_text());assert b==d['equation36']['board']
    # Braces in4B delimit exactly the same b..n file interval as Hansson.
    assert d['equation36']['region_columns']==[1,13]
    result=dict(source='sources/pentomino_main/FCR_032.pdf',printed_page=135,file_page=3,
      source_sha256=sha(OUT.parent.parent/'sources/pentomino_main/FCR_032.pdf'),
      checker_sha256=sha(__file__),transcription=strings,expanded=details,
      complete_board=b,agrees_with_equation36=True)
    (OUT/'hansson1935.json').write_text(json.dumps(result,indent=2)+'\n')
    rects={}
    for h,w in ((6,10),(5,12),(4,15)):
        moves=placements(h,w);names,rows,np=instance(moves,h,w)
        sol=first_solution(rows,np);assert sol is not None
        board=['.']*60
        for i in sol:
            p,cs=moves[i]
            assert len(cs)==5 and normalized([divmod(v,w) for v in cs]) in orientations(SHAPES[p])
            for v in cs:assert board[v]=='.';board[v]=p
        assert sorted(moves[i][0] for i in sol)==sorted(SHAPES) and '.' not in board
        rects[f'{h}x{w}']=dict(h=h,w=w,placements=len(moves),witness=[moves[i] for i in sol],
                               board=[''.join(board[r*w:(r+1)*w]) for r in range(h)])
    (OUT/'rectangle-witnesses.json').write_text(json.dumps(dict(source_sha256=sha(__file__),
        scope='Existence witnesses only; not a census of all rectangle solutions.',rectangles=rects),indent=2)+'\n')
    print('PASS: exact1935 source matches diagram36; three additional rectangular packings verified')


if __name__=='__main__':main()
