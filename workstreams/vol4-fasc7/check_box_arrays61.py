#!/usr/bin/env python3
"""All four native arrays61 and small-component standard-label certificates.

Geometry is cached after one pass. The counting phase joins the small
local relations exactly; no intermediate may exceed4096 partial rows.
"""
from fractions import Fraction as F
from collections import Counter
from itertools import product
from math import prod
import json
import xml.etree.ElementTree as ET
from check_clasp_projection import ROOT,sub,cross2,solve,path_segments
from check_cubie_junctions import path_points
from check_hc_drawings26_27 import network
from check_line_csp22 import ORDER,propagate
from check_polyhedra_fixed import encode


def native(paths,tag,start,stop):
    raw={i:path_points(paths[i]) for i in range(start,stop)}
    origin=raw[start][0];a=sub(raw[start][1],origin);c=sub(raw[start+2][1],origin);b=tuple(-a[k]-c[k] for k in (0,1))
    determinant=cross2(a,b);assert determinant>0
    mapped={i:[(F(round(4*cross2(sub(p,origin),b)/determinant)),F(round(4*cross2(a,sub(p,origin))/determinant))) for p in ps] for i,ps in raw.items()}
    observations=[(q,p) for i,ps in raw.items() for p,q in zip(ps,mapped[i])]
    gram=[[sum((*q,1)[i]*(*q,1)[j] for q,p in observations) for j in range(3)] for i in range(3)]
    affine=[solve(gram,[sum((*q,1)[j]*p[k] for q,p in observations) for j in range(3)]) for k in (0,1)]
    residuals=[sum((p[k]-sum(x*y for x,y in zip(affine[k],(*q,1))))**2 for k in (0,1)) for q,p in observations]
    assert max(residuals)<F(1,10000),(tag,float(max(residuals)))
    # Native lines are printed in both endpoint directions. Deduplicate
    # exact segments before checking every possible crossing.
    segments=sorted({tuple(sorted(ab)) for i,ps in mapped.items() for ab in path_segments(paths[i],ps)})
    synthetic=[{'d':'M 0 0 L 1 1'} for e in segments]
    p,ns,rs,lines,faces,boundary=network(dict(enumerate(segments)),synthetic)
    return {'picture':tag,'source_path_range':[start,stop],'source_grid_affine':affine,
            'source_maximum_residual_squared':max(residuals),'all_native_integer_paths':mapped,
            'points':p,'junctions':ns,'relations':rs,'lines':lines,'faces':faces,'boundary':boundary}


def small_components(pic):
    rs=pic['relations'];variables=pic['lines'];initial={e:set(ORDER) for e in variables}
    boundary=pic['boundary']
    for a,b in zip(boundary,boundary[1:]+boundary[:1]):initial['_'.join(sorted((a,b)))]={'>' if a<b else '<'}
    ds,trace=propagate(rs,initial);assert ds is not None
    uncertain={v for v in variables if len(ds[v])>1};adj={v:set() for v in uncertain};reduced=[]
    for j,(es,rows) in rs.items():
        live=[r for r in rows if all(s in ds[e] for e,s in zip(es,r))]
        active=[e for e in es if e in uncertain]
        pr=sorted({''.join(r[es.index(e)] for e in active) for r in live})
        assert pr
        if len(pr)<prod(len(ds[e]) for e in active):
            for e in active:adj[e].update(set(active)-{e})
        reduced.append({'junction':j,'variables':active,'rows':pr})
    components=[];remaining=set(uncertain)
    while remaining:
        component={min(remaining)};todo=list(component)
        while todo:
            for e in adj[todo.pop()]-component:component.add(e);todo.append(e)
        remaining-=component;es=sorted(component)
        candidates=prod(len(ds[e]) for e in es)
        local=[r for r in reduced if r['variables'] and set(r['variables'])<=component]
        assert all(not(set(r['variables'])&component) or set(r['variables'])<=component or len(r['rows'])==prod(len(ds[e]) for e in r['variables']) for r in reduced)
        joined=[{}];join_steps=[]
        for r in sorted(local,key=lambda r:(len(r['rows']),r['junction'])):
            extended={}
            for a in joined:
                for row in r['rows']:
                    b=dict(zip(r['variables'],row))
                    if all(e not in a or a[e]==s for e,s in b.items()):
                        d={**a,**b};extended[tuple(sorted(d.items()))]=d
            joined=list(extended.values())
            assert 0<len(joined)<=4096,(pic['picture'],len(es),len(joined))
            join_steps.append({'junction':r['junction'],'number_of_partial_rows':len(joined)})
        assert all(set(a)==set(es) for a in joined)
        solutions=sorted(''.join(a[e] for e in es) for a in joined)
        assert solutions
        components.append({'variables':es,'constraints':local,'unpruned_cartesian_size':candidates,
                           'exact_relation_join_steps':join_steps,'solutions':solutions,'count':len(solutions)})
    witness={v:next(iter(d)) for v,d in ds.items() if len(d)==1}
    for c in components:witness.update(zip(c['variables'],c['solutions'][0]))
    assert all(''.join(witness[e] for e in es) in rows for es,rows in rs.values())
    return {'standard_propagation':trace,'standard_domains':{v:''.join(s for s in ORDER if s in ds[v]) for v in variables},
            'reduced_relations':reduced,'components':components,'one_complete_witness':witness,'total':prod(x['count'] for x in components)}


def main():
    cache=ROOT/'results/box-arrays61-native-cache.json'
    if cache.exists():pics=json.loads(cache.read_text())['pictures']
    else:
        paths=[p.attrib for p in ET.parse(ROOT/'sources/file-134.svg').findall('.//{http://www.w3.org/2000/svg}path')]
        pics=[]
        for tag,start,stop in [('i',37,775),('ii',775,1579),('iii',1579,2321),('iv',2321,3089)]:
            pic=native(paths,tag,start,stop);pics.append(pic)
            print('native',tag,len(pic['points']),len(pic['lines']),flush=True)
        cache.write_text(json.dumps({'pictures':pics},indent=2,default=encode)+'\n')
    expected=[1,2**25,5**5*2**6*9**5,2**20*5]
    for p,e in zip(pics,expected):
        p['standard_certificate']=small_components(p)
        assert p['standard_certificate']['total']==e,(p['picture'],p['standard_certificate']['total'],e)
        print('count',p['picture'],e,dict(Counter(c['count'] for c in p['standard_certificate']['components'])),flush=True)
    (ROOT/'results/box-arrays61.json').write_text(json.dumps({'pictures':pics},indent=2,default=encode)+'\n')


if __name__=='__main__':main()
