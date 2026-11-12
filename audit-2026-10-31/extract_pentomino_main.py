#!/usr/bin/env python3
"""Read the original rounded PDF outlines of all pentomino diagrams on80--81."""
from collections import Counter
import json
import math
import extract_jigsaw as ex
from dlx1_audit_tools import ROOT,sha
from prepare_pentomino_main import OUT,SHAPES,normalized,orientations,connected_components

COLORS={'.3 .4 .8':'V','.95 .95 .75':'Z','.25 1 .25':'Y','0 .5 0':'W',
 '1 .8 .8':'T','.9 .9 .95':'R','1 1 0':'S','.5 .2 0':'Q',
 '.85 .7 .7':'O','1 .75 .5':'P','1 0 .5':'X','.5 0 .8':'U'}
STEP=7.992


def polygon(p):
    """Flatten the tiny rounded corners; test points are cell centers."""
    result=[];last=None
    for v in p:
        if v.tag in ('moveto','lineto'):
            last=(float(v.get('x')),float(v.get('y')));result.append(ex.transform(p,*last))
        elif v.tag=='curveto':
            controls=[last]+[(float(v.get('x'+str(i))),float(v.get('y'+str(i)))) for i in (1,2,3)]
            for k in range(1,17):
                t=k/16
                q=tuple((1-t)**3*controls[0][i]+3*(1-t)**2*t*controls[1][i]+3*(1-t)*t*t*controls[2][i]+t**3*controls[3][i] for i in (0,1))
                result.append(ex.transform(p,*q))
            last=controls[-1]
        elif v.tag=='closepath':pass
        else:raise AssertionError(v.tag)
    return result


def rotate(poly,theta):
    c,s=math.cos(theta),math.sin(theta)
    return [(c*x-s*y,s*x+c*y) for x,y in poly]


def classify(poly,piece):
    matches=[]
    for angle in (0,math.pi/4):
        q=rotate(poly,angle)
        x0,x1=min(x for x,y in q),max(x for x,y in q)
        y0,y1=min(y for x,y in q),max(y for x,y in q)
        w,h=round((x1-x0)/STEP),round((y1-y0)/STEP)
        if max(abs(x1-x0-w*STEP),abs(y1-y0-h*STEP))>.8:continue
        cells=[]
        for r in range(h):
            for c in range(w):
                x=(x0+x1)/2+(c-(w-1)/2)*STEP;y=(y0+y1)/2+(r-(h-1)/2)*STEP
                if ex.inside(x,y,q):cells.append((r,c))
        if len(cells)==5 and normalized(cells) in orientations(SHAPES[piece]):
            matches.append(dict(angle=angle,cells=cells))
    assert matches,(piece,poly)
    return matches


def main():
    ex.OUT=OUT
    diagrams={}
    for page in (80,81):
        ps=[]
        for p in ex.trace(page).iter('fill_path'):
            if p.get('colorspace')!='DeviceRGB':continue
            piece=COLORS[p.get('color')];poly=polygon(p)
            ps.append(dict(piece=piece,color=p.get('color'),polygon=poly,shape_checks=classify(poly,piece)))
        diagrams[page]=ps
    assert len(diagrams[80])==29 and len(diagrams[81])==1
    assert ''.join(p['piece'] for p in diagrams[80][12:])=='TUVWXYZROQPSOPQRS'
    # Published equation36, origin inferred from complete corner endpoints.
    origin=(155.716,162.504)
    board=[]
    for r in range(3):
        for c in range(20):
            hits=[p['piece'] for p in diagrams[80][:12] if ex.inside(origin[0]+(c+.5)*STEP,origin[1]+(r+.5)*STEP,p['polygon'])]
            assert len(hits)==1,(r,c,hits)
            board.append(hits[0])
    board=''.join(board)
    assert all(v==5 for v in Counter(board).values()) and len(Counter(board))==12
    short=json.loads((OUT/'short-check.json').read_text())
    gammas=set(short['cases']['gamma']['boards']);assert board in gammas
    other=(gammas-{board}).pop()
    changed={p for p in SHAPES if {i for i,v in enumerate(board) if v==p}!={i for i,v in enumerate(other) if v==p}}
    assert changed==set('QRSTWYZ')
    region={i for i,p in enumerate(board) if p in changed}
    # The two braces delimit a centrally symmetric 35-cell region with bounding
    # columns1..13 and rows0..2. Rotating that region switches the two solutions.
    lo=min(v%20 for v in region);hi=max(v%20 for v in region)
    rotated=list(board)
    for v in region:
        r,c=divmod(v,20);u=(2-r)*20+lo+hi-c
        assert u in region;rotated[u]=board[v]
    assert ''.join(rotated)==other
    # Equation38, same scale and board origin reconstructed from its grid.
    vpoly=diagrams[81][0]['polygon'];origin38=(141.112,205.448)
    vcells=[r*20+c for r in range(3) for c in range(20)
            if ex.inside(origin38[0]+(c+.5)*STEP,origin38[1]+(r+.5)*STEP,vpoly)]
    assert vcells==[9,10,11,29,49],vcells
    result=dict(source_sha256=sha(__file__),book_sha256=sha(ex.BOOK),
        traces={str(p):sha(OUT/f'page{p}-trace.xml') for p in (80,81)},diagrams=diagrams,
        equation36=dict(board=board,rows=[board[r*20:(r+1)*20] for r in range(3)],
          other_board=other,rotated_pieces=sorted(changed),rotated_region=sorted(region),
          region_columns=[lo,hi],all_models_matched=True),
        equation38=dict(cells=vcells,components=connected_components(set(range(60))-set(vcells),3,20)))
    (OUT/'pdf-diagrams.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: 29 original shapes80, full equation36 and7-piece rotation, equation38')


if __name__=='__main__':main()
