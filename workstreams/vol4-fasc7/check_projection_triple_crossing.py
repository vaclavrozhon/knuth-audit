#!/usr/bin/env python3
"""One explicit12-vertex counterexample to the corrected answer40 conditions."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib,json
from check_polyhedra_fixed import ROOT,sub,dot,cross,encode

VERTICES=[(-3,0,0),(3,0,0),(0,4,1),(1,3,-1),
          (-2,-2,10),(2,2,10),(-4,1,11),(-3,2,9),
          (-2,4,20),(2,-4,20),(5,2,21),(3,3,19)]
EDGES=[(4*t+i,4*t+j) for t in range(3) for i,j in combinations(range(4),2)]
TARGETS={(0,1),(4,5),(8,9)}
def cross2(a,b):return a[0]*b[1]-a[1]*b[0]

def check():
    volumes=[]
    for t in range(3):
        a,b,c,d=VERTICES[4*t:4*t+4]
        det=dot(sub(b,a),cross(sub(c,a),sub(d,a)));assert det
        volumes.append(det)
    assert volumes==[-42,-40,-84]
    first=[]
    for i,p in enumerate(VERTICES):
        for a,b in EDGES:
            A,B=VERTICES[a],VERTICES[b];d=sub(B,A);u=sub(p,A)
            assert d[:2]!=(0,0)
            collinearity=cross2(d,u)
            entry={'vertex':i,'edge':[a,b],'projected_orientation':collinearity}
            if collinearity==0:
                k=next(k for k in range(2) if d[k]);s=F(u[k],d[k])
                on_segment=0<=s<=1
                delta=F(A[2])+s*d[2]-p[2]
                assert not on_segment or delta==0
                entry.update(parameter=s,on_projected_segment=on_segment,depth_difference=delta)
            first.append(entry)
    second=[]
    for e,f in combinations(EDGES,2):
        a,b=e;c,d=f;A,B,C,D=[VERTICES[k] for k in (a,b,c,d)]
        u,v=sub(B,A),sub(D,C)
        direction=cross2(u,v);offset=cross2(sub(C,A),u)
        assert direction or offset
        second.append({'edges':[e,f],'projected_direction_determinant':direction,'offset_determinant':offset})
    lines=[]
    for a,b in EDGES:
        A,B=VERTICES[a],VERTICES[b];dx,dy=B[0]-A[0],B[1]-A[1]
        # dy*x-dx*y+c=0. Non-target supporting lines stay outside radius1/10.
        c=dx*A[1]-dy*A[0]
        if (a,b) in TARGETS:
            assert c==0
            assert A[0]*B[0]+A[1]*B[1]<0
            assert min(A[0]**2+A[1]**2,B[0]**2+B[1]**2)>F(1,100)
        else:assert 100*c*c>dx*dx+dy*dy
        lines.append({'edge':[a,b],'line_coefficients':[dy,-dx,c],
                      'squared_distance_of_supporting_line_from_origin':F(c*c,dx*dx+dy*dy)})
    support=[]
    for t,(a,b) in enumerate([(0,1),(4,5),(8,9)]):
        coefs=[(0,1),(-1,1),(2,1)][t]
        vals=[dot(coefs,v[:2]) for v in VERTICES[4*t:4*t+4]]
        assert vals[:2]==[0,0] and min(vals[2:])>0
        support.append({'tetrahedron':t,'halfplane_coefficients':coefs,'vertex_evaluations':vals})
    source_files=['errata/originals/err4f7.textxt','errata/pdf/err4f7.pdf',
                  'errata/pdf/all4f7.pdf','errata/text/err4f7.txt','errata/text/all4f7.txt']
    repo=ROOT.parents[1]
    return {'status':'candidate_pending_independent_review','scope':'Sufficiency of the quantitative conditions in corrected answer40; not the qualitative stability definition onp11.',
            'vertices':VERTICES,'edges':EDGES,'tetrahedron_scalar_triples':volumes,
            'disjoint_depth_slabs':[[-1,1],[9,11],[19,21]],
            'all216_vertex_edge_checks':first,'all153_edge_pair_checks':second,
            'projected_edge_supporting_lines':lines,'local_radius':'1/10',
            'local_projection_support_halfplanes':support,
            'exact_visible_rays':[[1,0],[-1,0],[-1,-1],[1,-2]],
            'occlusion_proof':'notes/F7-C0005.md',
            'errata_files':[{'file':f,'sha256':hashlib.sha256((repo/f).read_bytes()).hexdigest()} for f in source_files],
            'relevant_correction':{'date':'2026-09-13','page':167,'answer':40,'effect':'Replaces projected parallel-direction prohibition by collinearity of projected supporting lines; no triple-concurrence prohibition added.'},
            'no_other_relevant_correction_found':'The full current primary TeX, short and cumulative layers have no additional40 correction or restriction excluding the three-component witness.'}

if __name__=='__main__':
    result=check()
    (ROOT/'results/F7-C0005-evidence.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,default=encode)+'\n')
    print(json.dumps({'tetrahedra':3,'vertices':12,'edges':18,'vertex_edge_checks':216,
                      'edge_pair_checks':153,'conditions_pass':True,'local_visible_degree':4}))
