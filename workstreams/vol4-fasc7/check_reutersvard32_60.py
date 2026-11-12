#!/usr/bin/env python3
"""Native32 and complete boundary/interior count certificate for60."""
from fractions import Fraction as F
from collections import Counter
from itertools import product
from math import prod
import json
import xml.etree.ElementTree as ET
from check_clasp_projection import ROOT
from check_cubie_junctions import path_points
from check_hc_drawings26_27 import network
from check_hc_realizability28_29 import fit
from check_hc_free_boundaries import boundary_certificate,tiny_interior_count
from check_line_csp22 import ORDER,propagate
from check_polyhedra_fixed import encode


def main():
    paths=[p.attrib for p in ET.parse(ROOT/'sources/file-031.svg').findall('.//{http://www.w3.org/2000/svg}path')]
    raw={i:path_points(paths[i]) for i in range(18,215)}
    origin=(F('196.87109375'),F('96.17578125'))
    unit=(F('23.90625')/8,F('27.60546875')/16)
    mapped={i:[tuple(F(round((p[k]-origin[k])/unit[k])) for k in (0,1)) for p in ps] for i,ps in raw.items()}
    affine=[fit([(q[k],p[k]) for i,ps in raw.items() for p,q in zip(ps,mapped[i])]) for k in (0,1)]
    residuals=[sum((p[k]-affine[k][0]*q[k]-affine[k][1])**2 for k in (0,1)) for i,ps in raw.items() for p,q in zip(ps,mapped[i])]
    assert max(residuals)<F(1,10000),float(max(residuals))
    p,ns,rs,lines,faces,boundary=network(mapped,paths)
    boundary_lines=[]
    for a,b in zip(boundary,boundary[1:]+boundary[:1]):
        boundary_lines.append({'variable':'_'.join(sorted((a,b))),'label':'>' if a<b else '<'})
    pic={'name':'Reutersvard32','points':p,'junctions':ns,'relations':{j:{'variables':es,'tuples':rows} for j,(es,rows) in rs.items()},
         'lines':lines,'faces':faces,'boundary':boundary,'boundary_lines':boundary_lines,
         'native_path_range':[18,215],'source_affine':affine,'source_max_residual_squared':max(residuals),'native_integer_paths':mapped}
    bc=boundary_certificate(pic)
    ic=tiny_interior_count(pic,bc)
    assert (bc['boundary_labeling_count'],ic['count'])==(1728,8)
    assert len(ic['tree'])==1
    free=ic['tree'][0]['independent_free_variables']
    assert len(free)==3 and all(len(d)==2 for d in free.values())
    # Isolate the nine small boundary factors printed in answer60. The
    # transfer certificate above already fixes every interior port.
    brs={j:rs[j] for j in boundary}
    variables=set(bc['boundary_variables'])|set(bc['fixed_interior_ports'])
    initial={v:{bc['fixed_interior_ports'][v]} if v in bc['fixed_interior_ports'] else set(ORDER) for v in variables}
    ds,btrace=propagate(brs,initial);assert ds is not None
    uncertain={v for v in variables if len(ds[v])>1};adj={v:set() for v in uncertain};reduced=[]
    for j,(es,rows) in brs.items():
        live=[r for r in rows if all(s in ds[e] for e,s in zip(es,r))]
        active=[e for e in es if e in uncertain]
        projected_rows=sorted({''.join(r[es.index(e)] for e in active) for r in live})
        if len(projected_rows)<prod(len(ds[e]) for e in active):
            for e in active:adj[e].update(set(active)-{e})
        reduced.append({'junction':j,'variables':active,'rows':projected_rows})
    components=[];remaining=set(uncertain)
    while remaining:
        component={min(remaining)};todo=list(component)
        while todo:
            for e in adj[todo.pop()]-component:component.add(e);todo.append(e)
        remaining-=component;es=sorted(component)
        assert prod(len(ds[e]) for e in es)<=4096
        local=[r for r in reduced if set(r['variables'])<=component and r['variables']]
        assert all(not(set(r['variables'])&component) or set(r['variables'])<=component or len(r['rows'])==prod(len(ds[e]) for e in r['variables']) for r in reduced)
        solutions=[]
        for values in product(*[''.join(s for s in ORDER if s in ds[e]) for e in es]):
            a=dict(zip(es,values))
            if all(''.join(a[e] for e in r['variables']) in r['rows'] for r in local):solutions.append(''.join(values))
        components.append({'variables':es,'constraints':local,'solutions':solutions,'count':len(solutions)})
    assert sorted(x['count'] for x in components)==[2]*6+[3]*3
    pic['boundary_factor_certificate']={'propagation':btrace,'domains':{v:''.join(s for s in ORDER if s in ds[v]) for v in sorted(variables)},
                                         'reduced_relations':reduced,'components':components}
    pic['boundary_certificate']=bc;pic['interior_certificate']=ic
    pic['total_count']=1728*8
    (ROOT/'results/reutersvard32-60.json').write_text(json.dumps(pic,indent=2,default=encode)+'\n')
    print(json.dumps({'junctions':len(p),'types':dict(Counter(x['type'] for x in ns.values())),
                      'lines':len(lines),'boundary':len(boundary),'inner_free':free,
                      'boundary_count':bc['boundary_labeling_count'],'standard_count':ic['count'],'total':pic['total_count']}))


if __name__=='__main__':main()
