#!/usr/bin/env python3
"""Small certificates for every63 chart row and its endpoint ambiguity.

Uses the saved, already proved Reutersvard32 geometry. It does not rerun
visibility, labeling counts, or any search. The general proofs are in
notes/hc-linear-system-exercise-063.md.
"""
from fractions import Fraction as F
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def main():
    # '<' means behind, '>' in front; these are relational symbols here,
    # not comparisons of z. Corrected22October2026 shadow entries included.
    rows={
      'T+':['j=B','j=C','j<A','l=B','l<A','l<C','r=C','r<A','r<B'],
      'T-':['j=B','j=C','j<A','l=B','l<A','l>C','r=C','r<A','r>B'],
      'T-arrow-down':['j=B','j<A','j>C','l=B','l<A','r=C','r<A','m=C','m<B'],
      'T-arrow-up':['j=C','j<A','j>B','l=B','l<A','r=C','r<A','m=B','m<C'],
      'V-I+':['j=A','j=B','l=A','l<B'],
      'V-IO':['j=B','j>A','l=A','l<B','r=A','r<B'],
      'V-+O':['j=A','j=B','r=A','r<B'],
      'V-O-':['j=A','j=B','l=B','l<A'],
      'V-OI':['j=A','j>B','l=B','l<A','r=B','r<A'],
      'V--I':['j=A','j=B','r=B','r<A'],
      'W-O+I':['j=A','j=B','l=C','r=C','l<A','r<B','a=A','b=B','a<B','b<A'],
      'W--+-':['j=A','j=B','j=C','a<B','b>C','c<A'],
      'W-+-+':['j=A','j=B','j=C','a>B','b<C','c>A'],
      'Y-arrow':['j=B','j=C','j>A','l=A','l<B','r=A','r<C'],
      'Y----':['j=A','j=B','j=C','a>C','b>B','c>A'],
      'Y-+++':['j=A','j=B','j=C','a<C','b<B','c<A'],
    }
    assert len(rows)==16 and all(len(v)<=10 for v in rows.values())
    p=json.loads((ROOT/'results/reutersvard32-60.json').read_text())
    q=json.loads((ROOT/'results/reutersvard59-spatial.json').read_text())
    from check_line_csp22 import TABLE,global_symbol
    d={k:next(iter(v)) for k,v in p['interior_certificate']['tree'][0]['fixed_point'].items()}
    for e in p['boundary_lines']: d[e['variable']]=e['label']
    for e,vs in p['interior_certificate']['tree'][0]['independent_free_variables'].items():
        d[e]=next(s for s in vs if s!='-')
    local={}
    for j in ('v10','v09'):
        ns=p['junctions'][j]['neighbors']; kind=p['junctions'][j]['type']
        es=p['relations'][j]['variables']; word=''.join(d[e] for e in es)
        local[j]=next(t for t in TABLE[kind] if ''.join(global_symbol(s,j,k) for s,k in zip(t,ns))==word)
    assert local['v10']=='O+I'
    assert p['junctions']['v09']['neighbors'][::2]==['v10','v02']
    f=p['faces'][2]['walk']
    assert f==['v00','v03','v10','v09','v02']
    # The other endpoint in the W chart is v09; its T bar continues
    # through to v02 along exactly the same foreground physical edge.
    assert tuple(p['points']['v09'])==tuple((a+b)/2 for a,b in zip(p['points']['v10'],p['points']['v02']))
    z=[]
    for ei in (6,104):
        a,b=q['edges'][ei];u,v=[tuple(map(F,q['vertices'][i])) for i in (a,b)]
        k=next(k for k in (0,1) if u[k]!=v[k]);t=(F((6,14)[k])-u[k])/(v[k]-u[k])
        pt=tuple(u[k]+t*(v[k]-u[k]) for k in range(3))
        assert pt[:2]==(6,14) and 0<t<1
        z.append(pt[2])
    assert z==[F(-14397,200),F(1441,80)] and z[1]-z[0]==F(35999,400)
    # The bounded central planar face is background: its center lies
    # in none of the nine projected cube hexagons.
    hole=(F(15),F(23)); rejected=[]
    for c in q['centers']:
        x,y=(hole[k]-F(c[k]) for k in (0,1))
        # Screen cube hexagon has |x|<=4, |y|<=8, |y+x|<=8,
        # |y-x|<=8, equivalently |x|<=4 and |y|+|x|<=8.
        assert abs(x)>4 or abs(y)+abs(x)>8
        rejected.append({'center':c,'offset':[x,y],'outside':True})
    # Exact winding parity at the saved face14 boundary.
    ps=[tuple(map(F,p['points'][j])) for j in p['faces'][14]['walk']]
    crossings=[]
    for a,b in zip(ps,ps[1:]+ps[:1]):
        if (a[1]>hole[1])!=(b[1]>hole[1]):
            x=a[0]+(hole[1]-a[1])*(b[0]-a[0])/(b[1]-a[1])
            assert x!=hole[0]
            if x>hole[0]:crossings.append(x)
    assert len(crossings)%2==1 and p['faces'][14]['area_twice']<0
    out={
      'chart_rows':rows,
      'row_scope':'W-O+I endpoint assertions require front points on the two outer carriers; their identification with neighboring J vertices is not generally valid.',
      'known_corrections':{'date':'2026-10-22','T-arrow-down':['m=C','m<B'],'T-arrow-up':['m=B','m<C']},
      'endpoint_counter_under_adjacent_vertex_reading':{
        'strong_witness_reused':'results/reutersvard59-spatial.json',
        'W':'v10','W_point':p['points']['v10'],'W_neighbors':p['junctions']['v10']['neighbors'],
        'T':'v09','T_point':p['points']['v09'],'T_neighbors':p['junctions']['v09']['neighbors'],
        'local_words':local,'common_foreground_face':f,
        'contradictory_requirements':['z_v09=h_F(6,14)','z_v09>h_F(6,14)'],
        'front_physical_edge':6,'hidden_stem_edge':104,'front_depth':z[0],'artificial_T_depth':z[1],'gap':z[1]-z[0],
        'possible_repair':'Use independent front samples on the two arrow carriers, or follow barT subdivisions to a physical endpoint. The printed text does not define a,b explicitly.'},
      'bounded_background_face':{'walk':p['faces'][14]['walk'],'point':hole,'right_ray_crossings':crossings,'all_nine_hexagon_tests':rejected},
      'work_scope':'Only exact two-edge interpolation,16-row transcription,and9 point/hexagon tests; no realization/count rerun.'}
    (ROOT/'results/linear-chart63.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
    print(json.dumps({'chart_rows':len(rows),'endpoint_gap':str(z[1]-z[0]),'bounded_background_face':14,'status':'interpretation partial; no new finding'}))


if __name__=='__main__':main()
