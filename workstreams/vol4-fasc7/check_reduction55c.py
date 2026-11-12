#!/usr/bin/env python3
"""One exact trace-identity witness and a simple polygon realizing its word."""
from fractions import Fraction as F
import json
from check_boundary_matrix_bounds55 import A,B,X,I,multiply,tr
from check_hc_drawings26_27 import network
from check_polyhedra_fixed import encode
from check_clasp_projection import ROOT

def value(word):
    m=I
    for c in word:m=multiply(m,A if c=='A' else B)
    return m

def main():
    p=[-1,0,1,0,0,-1]
    c=multiply(multiply(A,X),A);inverse=((0,1),(1,-1));normal=I
    for power in p:
        normal=multiply(normal,c)
        normal=multiply(normal,inverse if power==-1 else value('A'*power))
    original='ABAABBBAABB';printed='ABBAABBBB';corrected='ABBBBAABBBB'
    assert normal==value(original)==((-2,1),(7,-3))
    assert value(printed)==((7,-4),(12,-7)) and value(corrected)==((12,-7),(29,-17))
    assert tr(normal)==tr(value(corrected))==-5 and tr(value(printed))==0
    # Five convex corners; the inward parabolic subdivisions give the
    # desired one, three and two consecutive reflex corners respectively.
    corners=[(0,0),(6,0),(8,6),(4,10),(-2,6)]
    subdivisions=[1,0,3,0,2]
    polygon=[]
    for k,a in enumerate(corners):
        b=corners[(k+1)%5];d=(b[0]-a[0],b[1]-a[1]);n=subdivisions[k]
        polygon.append(tuple(map(F,a)))
        for j in range(1,n+1):
            t=F(j,n+1);height=t*(1-t)/100
            polygon.append((a[0]+t*d[0]-height*d[1],a[1]+t*d[1]+height*d[0]))
    assert len(polygon)==11
    mapped={i:[a,polygon[(i+1)%11]] for i,a in enumerate(polygon)}
    paths={i:{'d':'M 0 0 L 1 1'} for i in mapped}
    pts,ns,rs,lines,faces,boundary=network(mapped,paths)
    names={point:j for j,point in pts.items()};order=[names[p] for p in polygon]
    assert len(pts)==len(lines)==11 and len(faces)==2
    pos=boundary.index(order[0]);assert boundary[pos:]+boundary[:pos]==order
    word=''
    for i,j in enumerate(order):
        assert ns[j]['type']=='V'
        prev,next=order[i-1],order[(i+1)%11]
        if ns[j]['neighbors']==(next,prev):word+='A'
        else:assert ns[j]['neighbors']==(prev,next);word+='B'
    assert word==original
    result={'m':6,'p':p,'q':11,'normal_form_matrix':normal,
            'original':{'word':original,'matrix':value(original),'trace':tr(value(original))},
            'printed_reduced':{'word':printed,'matrix':value(printed),'trace':tr(value(printed))},
            'corrected_reduced':{'word':corrected,'matrix':value(corrected),'trace':tr(value(corrected))},
            'realizable_boundary':{'polygon':polygon,'case_word':word.replace('A','V').replace('B','Λ'),
                                   'source_corners':corners,'inward_subdivisions':subdivisions,
                                   'points':pts,'junctions':ns,'faces':faces,'boundary':boundary}}
    (ROOT/'results/reduction55c.json').write_text(json.dumps(result,indent=2,default=encode)+'\n')
    print(json.dumps({'m':6,'p':p,'q':11,'traces':[-5,0,-5],'realizable_case_word':word},indent=2))

if __name__=='__main__':main()
