#!/usr/bin/env python3
"""Both native30 diagrams, both red-line repeats, exact3D witness and determinant."""
from fractions import Fraction as F
import json
import xml.etree.ElementTree as ET
from check_clasp_projection import ROOT,sub,dot,cross2,parameter
from check_polyhedra_fixed import cross,normal,encode
from check_cubie_junctions import path_points
from check_hc_realizability28_29 import native,canonical_junction,spatial,fit

def line(a,b):return cross((*a,F(1)),(*b,F(1)))
def det3(rows):return dot(rows[0],cross(rows[1],rows[2]))
def interval_add(a,b):return(a[0]+b[0],a[1]+b[1])
def interval_neg(a):return(-a[1],-a[0])
def interval_sub(a,b):return interval_add(a,interval_neg(b))
def interval_mul(a,b):
    v=[x*y for x in a for y in b];return(min(v),max(v))
def interval_cross(a,b):return tuple(interval_sub(interval_mul(a[(i+1)%3],b[(i+2)%3]),interval_mul(a[(i+2)%3],b[(i+1)%3])) for i in range(3))

def repeat(paths,start,redstart,pic,concurrent):
    pairs=[[],[]]
    for i,word in [(start,'abca'),(start+1,'defd')]:
        raw=path_points(paths[i]);assert len(raw)==len(word)
        for p,j in zip(raw,word):
            for k in (0,1):pairs[k].append((pic['points'][j][k],p[k]))
    transforms=[fit(ps) for ps in pairs]
    tosource=lambda p:tuple(transforms[k][0]*p[k]+transforms[k][1] for k in (0,1))
    errors=[]
    for i,word in [(start,'abca'),(start+1,'defd')]:
        for p,j in zip(path_points(paths[i]),word):errors.append(dot(sub(p,tosource(pic['points'][j])),sub(p,tosource(pic['points'][j]))))
    assert max(errors)<F(1,10000)
    segments=[]
    for i,(u,v) in enumerate([('a','d'),('b','e'),('c','f')],redstart):
        raw=path_points(paths[i]);assert len(raw)==2
        a,b=map(tosource,[pic['points'][u],pic['points'][v]]);delta=sub(b,a)
        residuals=[cross2(sub(p,a),delta)**2/dot(delta,delta) for p in raw]
        assert max(residuals)<F(1,10000)
        assert dot(sub(raw[0],a),sub(raw[0],a))<F(1,10000)
        if concurrent:
            o=tosource((F(24),F(-6)))
            assert 0<dot(sub(o,raw[0]),sub(raw[1],raw[0]))<dot(sub(raw[1],raw[0]),sub(raw[1],raw[0]))
        segments.append({'native_path':i,'corresponding_crease':u+v,'endpoints':raw,'perpendicular_residual_squared':residuals})
    return {'source_paths':[start,start+1],'coordinate_affine':transforms,
            'maximum_vertex_residual_squared':max(errors),'all_three_red_lines':segments}

def main():
    paths=[p.attrib for p in ET.parse(ROOT/'sources/file-030.svg').findall('.//{http://www.w3.org/2000/svg}path')]
    left=dict(zip('abcdef',[(F(0),F(0)),(F(60),F(0)),(F(20),F(-16)),(F(16),F(-4)),(F(42),F(-3)),(F(112,5),F(-10))]))
    aa,bb,cc,_=path_points(paths[43]);dd,ee,ff,_=path_points(paths[44]);unit=(bb[0]-aa[0])/60
    right={j:tuple((p[k]-aa[k])/unit for k in (0,1)) for j,p in zip('abcdef',[aa,bb,cc,dd,ee,ff])}
    words=['abca','defd','ad','be','cf']
    p=native(paths,'30-left',38,left,words);q=native(paths,'30-right',43,right,words)
    assert {j:canonical_junction(x) for j,x in p['junctions'].items()}=={j:canonical_junction(x) for j,x in q['junctions'].items()}
    for pic in (p,q):
        assert all(pic['standard_domains'][e]=='+' for e in ['ad','be','cf'])
        assert all(len(s)==1 for s in pic['standard_domains'].values())
        assert all(''.join(pic['standard_domains'][e] for e in vs) in ts for vs,ts in pic['relations'].values())
        ls=[line(pic['points'][u],pic['points'][v]) for u,v in [('a','d'),('b','e'),('c','f')]]
        pic['three_crease_lines']=ls;pic['concurrency_determinant']=det3(ls)
    assert p['concurrency_determinant']==0 and q['concurrency_determinant']>0
    assert all(dot(l,(F(24),F(-6),F(1)))==0 for l in p['three_crease_lines'])
    # Concurrency failure remains true under every0.01pt source-coordinate
    # perturbation of all six points, not only a preferred rational fit.
    eps=F(1,100)/unit
    boxes={j:tuple((x-eps,x+eps) for x in pt)+((F(1),F(1)),) for j,pt in right.items()}
    ilines=[interval_cross(boxes[u],boxes[v]) for u,v in [('a','d'),('b','e'),('c','f')]]
    terms=[interval_mul(ilines[0][i],interval_cross(ilines[1],ilines[2])[i]) for i in range(3)]
    interval=(F(0),F(0))
    for term in terms:interval=interval_add(interval,term)
    assert interval[0]>0
    q['determinant_interval_for_source_coordinate_error_0_01pt']=interval
    raw={j:(*xy,F(0)) for j,xy in left.items()}
    for j,z in [('d',-F(2,3)),('e',-F(1,2)),('f',-F(3,5))]:raw[j]=(*left[j],z)
    face_words=['acb','abed','bcfe','cadf','def']
    p['spatial_witness']=spatial(p,raw,face_words,lambda v:v[:2],(0,0,-1),expected_counts=(6,9,5))
    support=[]
    for face in face_words:
        n=normal([raw[j] for j in face]);values={j:dot(n,sub(v,raw[face[0]])) for j,v in raw.items()}
        assert all(value==0 if j in face else value<0 for j,value in values.items())
        support.append({'face':face,'outward_normal':n,'all_vertex_signed_distances':values,'camera_dot':-n[2]})
    p['spatial_witness']['strict_convex_facet_support']=support
    p['red_line_repeat']=repeat(paths,48,50,p,True)
    q['red_line_repeat']=repeat(paths,53,55,q,False)
    out={'pictures':[p,q],'untruncated_apex':(F(24),F(-6),F(-1)),
         'truncation_fractions':{'ad':F(2,3),'be':F(1,2),'cf':F(3,5)},
         'nearby_perturbation':{'moved_vertex':'d','new_image_point':[F(16),'-4+epsilon'],
                                'determinant_d_with_common_point_of_other_two_lines':'-24*epsilon'}}
    (ROOT/'results/truncated-tetrahedron30.json').write_text(json.dumps(out,indent=2,default=encode)+'\n')
    print(json.dumps({'source_right_det':float(q['concurrency_determinant']),
                      'robust_interval':list(map(float,interval)),
                      'left_visible_edges':len(p['spatial_witness']['every_edge_visibility']),
                      'left_hidden_edges':p['spatial_witness']['hidden_edges'],
                      'junctions':p['junctions']},indent=2))

if __name__=='__main__':main()
