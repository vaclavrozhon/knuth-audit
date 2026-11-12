#!/usr/bin/env python3
"""All seven native T2–T8 polygon diagrams and the exact forbidden57 picture."""
from fractions import Fraction as F
from collections import defaultdict
import json
import xml.etree.ElementTree as ET
from check_clasp_projection import ROOT,sub,dot,cross2,path_segments,cuts
from check_cubie_junctions import path_points
from check_hc_picture_networks import ordered_neighbors
from check_hc_drawings26_27 import network
from check_line_csp22 import TABLE,global_symbol,propagate,ORDER
from check_boundary_matrix_bounds55 import A,B,I,X,multiply,tr,det
from check_polyhedra_fixed import encode

def sign(k):
    while k%2==0:k//=2
    return 'A' if k%4==1 else 'B'

def matrix(word):
    ans=I
    for s in word:ans=multiply(ans,A if s=='A' else B)
    return ans

def main():
    paths=[p.attrib for p in ET.parse(ROOT/'sources/file-133.svg').findall('.//{http://www.w3.org/2000/svg}path')]
    ds=['']
    for n in range(7):ds.append(ds[-1]+'A'+''.join('B' if c=='A' else 'A' for c in ds[-1][::-1]))
    assert ds[:4]==['','A','AAB','AABAABB']
    rows=[]
    for n in range(2,9):
        raw=path_points(paths[133+n]);origin=raw[0]
        unit={2:F('12.8'),3:F('1.6'),4:F('1.6'),5:F('.8'),6:F('.8'),7:F('.4'),8:F('.4')}[n]
        qs=[tuple(F(round((p[k]-origin[k])/unit)) for k in (0,1)) for p in raw]
        errors=[sum((p[k]-origin[k]-unit*q[k])**2 for k in (0,1)) for p,q in zip(raw,qs)]
        assert max(errors)<F(1,10000) and qs[0]==qs[-1] and len(qs)==2**n+1
        pts,ns,rs,lines,faces,boundary=network({133+n:qs},paths)
        assert len(pts)==len(lines)==2**n and len(faces)==2
        names={p:j for j,p in pts.items()};order=[names[p] for p in qs[:-1]]
        pos=boundary.index(order[0]);assert boundary[pos:]+boundary[:pos]==order
        word=''
        for i,j in enumerate(order):
            assert ns[j]['type']=='V'
            prev,next=order[i-1],order[(i+1)%len(order)]
            if ns[j]['neighbors']==(next,prev):word+='A'
            else:assert ns[j]['neighbors']==(prev,next);word+='B'
        half=''.join(sign(k) for k in range(1,2**(n-1)+1));expected=half*2
        assert half==ds[n-1]+'A'
        offset=0 if n==2 else 2
        assert word[offset:]+word[:offset]==expected
        d=matrix(ds[n-1]);h=multiply(d,A);m=multiply(h,h)
        assert det(h)==1 and tr(m)==(7 if n==2 else -1)
        lucas=[2,1]
        for k in range(2,2**n+1):lucas.append(lucas[-1]+lucas[-2])
        count=tr(m)+lucas[-1]
        rows.append({'n':n,'source_path':133+n,'source_origin':origin,'grid_unit':unit,
                     'maximum_source_residual_squared':max(errors),'source_polygon_grid':qs,
                     'junctions':ns,'points':pts,'faces':faces,'boundary':boundary,
                     'native_word':word,'rotation_to_printed_numbering':offset,'case_word':expected,
                     'D_n_minus_1':d,'half_product':h,'full_trace':tr(m),
                     'Lucas_2_power_n':lucas[-1],'labelings':count})
    (ROOT/'results/twindragons56-native-cache.json').write_text(json.dumps(rows,indent=2,default=encode)+'\n')
    p57=[p.attrib for p in ET.parse(ROOT/'sources/file-186.svg').findall('.//{http://www.w3.org/2000/svg}path')]
    originals={i:path_points(p57[i]) for i in (18,19)}
    allpoints=[p for qs in originals.values() for p in qs]
    origin=tuple(min(p[k] for p in allpoints) for k in (0,1));units=tuple((max(p[k] for p in allpoints)-origin[k])/u for k,u in enumerate((6,2)))
    mapped={};errors=[]
    for i,qs in originals.items():
        mapped[i]=[]
        for p in qs:
            q=tuple(F(round((p[k]-origin[k])/units[k])) for k in (0,1));mapped[i].append(q)
            errors.append(sum((p[k]-origin[k]-units[k]*q[k])**2 for k in (0,1)))
    assert max(errors)<F(1,10000)
    points={'L':(F(0),F(1)),'Y':(F(2),F(1)),'V':(F(4),F(0)),'W':(F(4),F(2)),'R':(F(6),F(1))}
    names={p:j for j,p in points.items()};adj=defaultdict(set);segments=[]
    for i,qs in mapped.items():
        for a,b in path_segments(p57[i],qs):
            u,v=names[a],names[b];adj[u].add(v);adj[v].add(u);segments.append((a,b))
    for a,b in segments:
        for c,d in segments:assert set(cuts(a,b,c,d))<={F(0),F(1)}
    wanted={'Y':('V','W','L'),'V':('W','Y'),'W':('Y','V','R')};relations={}
    for j,ns in wanted.items():
        actual=ordered_neighbors(j,j,ns,points)
        assert set(ns)==adj[j]
        assert tuple(ns)==actual or (j=='Y' and any(tuple(ns[k:]+ns[:k])==actual for k in range(3)))
        vs=[''.join(sorted((j,k))) for k in ns]
        rows57=[''.join(global_symbol(s,j,k) for s,k in zip(t,ns)) for t in TABLE[j]]
        relations[j]=(vs,rows57)
    assert len(adj['L'])==len(adj['R'])==1
    lines=sorted({v for vs,ts in relations.values() for v in vs})
    fixed,proof=propagate(relations,{e:set(ORDER) for e in lines});assert fixed is None
    result={'scope':'Every native T2–T8 point and junction, and all57 geometry; all-n matrix proof is separate. Jacobi convention and fractal convergence are not silently inferred from these seven drawings.',
            'twindragons':rows,'forbidden57':{'source_paths':[18,19],'source_origin':origin,'source_units':units,
             'maximum_source_residual_squared':max(errors),'source_grid_paths':mapped,'points':points,
             'junctions':wanted,'relations':relations,'lines':lines,'unlabelability_propagation':proof}}
    (ROOT/'results/twindragons56-subpicture57.json').write_text(json.dumps(result,indent=2,default=encode)+'\n')
    print(json.dumps({'twindragons':[{'n':r['n'],'junctions':len(r['points']),'trace':r['full_trace'],'count':r['labelings']} for r in rows],
                      'forbidden57_final_step':proof[-1]},indent=2))

if __name__=='__main__':main()
