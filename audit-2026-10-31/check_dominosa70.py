#!/usr/bin/env python3
"""DLX70--71: original bitmap glyphs, all solutions, and 3DM reduction."""
from collections import Counter,defaultdict
from datetime import datetime,timezone
import hashlib
import json
import re
from PIL import Image,ImageDraw
import pikepdf
import extract_jigsaw as geo
from dlx1_audit_tools import ROOT,sha,run,input_text,decode_rows

OUT=ROOT/'results/convex68'
PIPS={'/BC':0,'/BD':1,'/BE':2,'/BF':3,'/BG':4,'/BH':5,'/BI':6,
      '/EY':2,'/EZ':3,'/F2':6}
# Connecting strokes: right, left, below, above, respectively.
JOINS={'/BO':(0,1),'/BQ':(0,-1),'/CM':(1,0),'/DA':(-1,0)}
MATRICES={'a':'06521412/14535336/11560044/44562223/00561336/66203251/15044032',
          'b':'33651515/65612324/24333620/41614460/30301144/26250500/25054216'}


def font_info(pdf,page,fontname):
    font=next(f for _,f in pdf.pages[page+19].Resources.Font.items() if f.get('/Name')=='/'+fontname)
    code=0;mapping={};details={}
    for item in font.Encoding.Differences:
        if isinstance(item,int):code=item;continue
        name=str(item);mapping[code]=name;code+=1
        stream=font.CharProcs[item].read_bytes()
        w=int(re.search(rb'/W (\d+)',stream)[1]);h=int(re.search(rb'/H (\d+)',stream)[1])
        pixels=stream.split(b'ID\n',1)[1][:(w+7)//8*h]
        im=Image.frombytes('1',(w,h),pixels)
        details[name]=dict(width=w,height=h,charproc_sha256=hashlib.sha256(stream).hexdigest())
        if name in PIPS:
            assert w==h==168
            unseen={(x,y) for x in range(12,156) for y in range(12,156) if im.getpixel((x,y))}
            components=[]
            while unseen:
                q=[unseen.pop()]
                for x,y in q:
                    for v in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                        if v in unseen:unseen.remove(v);q.append(v)
                components.append(q)
            assert all(len(q)>80 for q in components)
            assert len(components)==PIPS[name]
            details[name]['spot_centers']=sorted([round(sum(p[a] for p in q)/len(q),3) for a in (0,1)] for q in components)
            details[name]['spots']=len(components)
        im.save(OUT/f'{fontname}-{name[1:]}.png')
    return mapping,details


def diagram(page,fontname,mapping,x0,y0):
    symbols=defaultdict(list);glyphs=[]
    for t in geo.trace(page).iter('fill_text'):
        for span in t:
            if span.get('font')!=fontname:continue
            for g in span:
                x,y=geo.transform(t,float(g.get('x')),float(g.get('y')))
                c=round((x-x0)/10.58);r=round((y-y0)/10.59)
                if not(0<=r<7 and 0<=c<8):continue
                assert abs(x-x0-c*10.58)<.12 and abs(y-y0-r*10.59)<.12
                name=mapping[int(g.get('glyph'))];symbols[8*r+c].append(name)
                glyphs.append(dict(cell=8*r+c,name=name,origin=[x,y]))
    assert len(symbols)==56 and all(len(s)==2 for s in symbols.values())
    board=[];mates=[];orientations=[]
    for v in range(56):
        s=symbols[v];dots=[x for x in s if x in PIPS];joins=[x for x in s if x in JOINS]
        assert len(dots)==len(joins)==1
        board.append(PIPS[dots[0]]);r,c=divmod(v,8);dr,dc=JOINS[joins[0]]
        rr,cc=r+dr,c+dc;assert 0<=rr<7 and 0<=cc<8
        mates.append(8*rr+cc)
        orient='vertical' if dr else 'horizontal'
        orientations.append(orient if board[-1] in (2,3,6) else None)
        if board[-1] in (2,3,6):
            assert (dots[0] in ('/EY','/EZ','/F2'))==(orient=='vertical')
    assert all(mates[mates[v]]==v for v in range(56))
    pairs=sorted((v,mates[v]) for v in range(56) if v<mates[v])
    assert len(pairs)==28
    assert {tuple(sorted((board[u],board[v]))) for u,v in pairs}=={(x,y) for x in range(7) for y in range(x,7)}
    return dict(page=page,font=fontname,glyphs=glyphs,board=board,pairs=pairs,orientations=orientations)


def matrix(page,x0,y0):
    cells={}
    for t in geo.trace(page).iter('fill_text'):
        for span in t:
            for g in span:
                ch=g.get('unicode')
                if ch not in '0123456':continue
                x,y=geo.transform(t,float(g.get('x')),float(g.get('y')))
                c=round((x-x0)/13.82);r=round((y-y0)/10.97)
                if not(0<=r<7 and 0<=c<8):continue
                if abs(x-x0-c*13.82)>.15 or abs(y-y0-r*10.97)>.15:continue
                assert (r,c) not in cells;cells[r,c]=int(ch)
    assert len(cells)==56
    return [cells[r,c] for r in range(7) for c in range(8)]


def coordinate_models(board):
    full=(1<<56)-1;models=set();nodes=0
    def visit(occupied,used,chosen):
        nonlocal nodes
        nodes+=1
        if occupied==full:
            assert len(used)==28;models.add(tuple(sorted(chosen)));return
        v=((full^occupied)&-(full^occupied)).bit_length()-1;r,c=divmod(v,8)
        for w in ([v+1] if c<7 else [])+([v+8] if r<6 else []):
            pair=tuple(sorted((board[v],board[w])))
            if not(occupied>>w&1) and pair not in used:
                visit(occupied|(1<<v)|(1<<w),used|{pair},chosen+[(v,w)])
    visit(0,set(),[])
    return models,nodes


def main():
    OUT.mkdir(exist_ok=True);geo.OUT=OUT;pdf=pikepdf.open(geo.BOOK)
    qmap,qfont=font_info(pdf,131,'T42');amap,afont=font_info(pdf,431,'T35')
    assert qfont==afont
    d={'question-a':diagram(131,'T42',qmap,67.25,354.48),
       'answer-a':diagram(431,'T35',amap,124.25,242.4),
       'answer-b':diagram(431,'T35',amap,254.51,242.4)}
    result=dict(source_sha256=sha(__file__),book_sha256=sha(geo.BOOK),
         geometry_helper_sha256=sha(ROOT/'extract_jigsaw.py'),font_bitmaps=qfont,diagrams=d,cases={})
    for label,x0,y0 in [('a',262.74,350.34),('b',179.11,460.41)]:
        board=matrix(131,x0,y0)
        assert board==[int(c) for c in MATRICES[label] if c!='/']==d['answer-'+label]['board']
        assert Counter(board)=={k:8 for k in range(7)}
        if label=='a':assert d['question-a']['board']==board
        independent,nodes=coordinate_models(board)
        dominoes=[(x,y) for x in range(7) for y in range(x,7)]
        names=[f'D{x}{y}' for x,y in dominoes]+[f'p{r}{c}' for r in range(7) for c in range(8)]
        placements=[(8*r+c,8*r+c+1) for r in range(7) for c in range(7)]
        placements += [(8*r+c,8*(r+1)+c) for r in range(6) for c in range(8)]
        assert len(placements)==97
        rows=[[dominoes.index(tuple(sorted((board[u],board[v]))))+1,u+29,v+29] for u,v in placements]
        stats,text=run(OUT,'dominosa-'+label,input_text(names,rows),models=True)
        (OUT/f'dominosa-{label}.models').write_text(text)
        native={tuple(sorted(placements[i] for i in model)) for model in decode_rows(text,names,rows)}
        assert native==independent and stats['solutions']==len(native)
        for model in native:
            assert sorted(v for p in model for v in p)==list(range(56))
            assert sorted(tuple(sorted((board[u],board[v]))) for u,v in model)==dominoes
        printed=tuple(map(tuple,d['answer-'+label]['pairs']));assert printed in native
        if label=='b':assert len(native)==1
        else:
            question=tuple(map(tuple,d['question-a']['pairs']));assert question in native
            assert len(set(printed)-set(question))==len(set(question)-set(printed))==4
            survivors=[]
            for model in native:
                orientation={v:('horizontal' if b-a==1 else 'vertical') for a,b in model for v in (a,b)}
                if all(o is None or o==orientation[v] for v,o in enumerate(d['question-a']['orientations'])):
                    survivors.append(model)
            assert survivors==[question]
            result['orientation_clue_unique']=True;result['changed_dominoes']=4
        # Every adjacent pair has one endpoint in each checkerboard class.
        assert sum((v//8+v%8)%2==0 for v in range(56))==28
        assert all((u//8+u%8)%2 != (v//8+v%8)%2 for u,v in placements)
        examples=[placements[i] for i in (0,1,48,49,50,96)]
        triples=[(tuple(sorted((board[u],board[v]))),divmod(u,8),divmod(v,8)) for u,v in examples]
        if label=='a':assert [p[0] for p in triples]==[(0,6),(5,6),(2,3),(0,1),(4,6),(1,2)]
        result['cases'][label]=dict(board=board,solutions=len(native),all_models=sorted(native),
          independent_nodes=nodes,native=stats,full_sets_equal=True,
          three_dimensional_matching=dict(class_sizes=[28,28,28],horizontal=49,vertical=48,examples=triples))
        print(label,len(native),'complete model sets agree',flush=True)
    result.update(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat())
    (OUT/'dominosa70.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS:112 numeric cells,168 pip cells,84 original dominoes,3DM reduction')


if __name__=='__main__':main()
