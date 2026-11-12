"""Short arithmetic and source-edge certificates; no enumeration or solver."""
from pathlib import Path
from datetime import datetime, timezone
import json
import math
import os
import re
import time
import xml.etree.ElementTree as ET
from puzzle_xcc import save, sha

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/usa239_246'
SRC=ROOT/'sources/usa239_246'


def line_segments(trace):
    result=[]
    for e in ET.parse(trace).getroot().iter('stroke_path'):
        a,b,c,d,tx,ty=map(float,e.get('transform').split())
        current=None
        for p in e:
            if p.tag not in ['moveto','lineto']:
                current=None;continue
            x,y=float(p.get('x')),float(p.get('y'))
            point=(a*x+c*y+tx,b*x+d*y+ty)
            if p.tag=='lineto' and current is not None:
                result.append((current,point,e.get('color')))
            current=point
    return result


def main():
    start=time.monotonic()
    assert os.nice(0)>=15 and not (OUT/'f148-f149-witness.json').exists()
    vertices=re.findall(r'^"([A-Z]{2})",A\d+,"([^"]+)",(\d+)$',(SRC/'contiguous-usa.gb').read_text(),re.M)
    pop={a:int(n) for a,name,n in vertices};fullnames={a:name for a,name,n in vertices}
    northwest='AZ ID KS MN MT ND NE NV OK OR WA WY'.split()
    england='CT MA ME NH RI VT'.split()
    assert sum(pop[s] for s in northwest)==37177055
    assert sum(pop[s] for s in england)==14445438
    assert sum(pop[s] for s in england+['NY'])==33823525
    census=(SRC/'census-2015-pepannres.txt').read_text()
    primary={}
    for s in northwest+england+['NY']:
        match=re.search(r'^'+re.escape(fullnames[s])+r'\s+[\d,]+\s+([\d,]+)',census,re.M)
        assert match
        primary[s]=int(match.group(1).replace(',',''))
        assert primary[s]==pop[s]
    figures=json.loads((OUT/'figures.json').read_text())
    edge_claims=[('116-right','AL TN MS'.split()),('246-ext-left','SD NE WY'.split()),
                 ('246-int-left','SD NE WY'.split()),('246-int-right','IN IL KY'.split())]
    evidence=[]
    for version in ['original','draft']:
        left=figures['versions'][version]['116-left']
        assert sorted(northwest) in left['sets']
        assert min(p for q,p in zip(left['sets'],left['populations']) if 'NY' not in q)==37177055
        for title,route in edge_claims:
            page=(136 if title.startswith('116') else 499) if version=='original' else (58 if title.startswith('116') else 189)
            trace=OUT/f'{version}-{page}.xml';segs=line_segments(trace)
            geometry=figures['versions'][version][title]['circle_geometry']
            def check(a,b,color):
                aa=(geometry[a]['x'],geometry[a]['y']);bb=(geometry[b]['x'],geometry[b]['y'])
                found=[(x,y) for x,y,c in segs if c==color and min(max(math.dist(aa,x),math.dist(bb,y)),max(math.dist(aa,y),math.dist(bb,x)))<.03]
                assert len(found)==1,(version,title,a,b,color)
                return dict(states=[a,b],color=color,endpoints=found[0])
            records=[check(route[0],route[-1],'0 0 1')]+[check(a,b,'0 0 0') for a,b in zip(route,route[1:])]
            evidence.append(dict(version=version,title=title,black_path=route,segments=records,trace_sha256=sha(trace)))
        q=figures['versions'][version]['246-ext-left']
        assert q['twice_drawn_dashed']==92 and q['exterior']==90
    save(OUT/'f148-f149-witness.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),nice=os.nice(0),
        wall_seconds=time.monotonic()-start,source_hashes={str(p.relative_to(ROOT)):sha(p) for p in [SRC/'contiguous-usa.gb',SRC/'census-2015-pepannres.txt',OUT/'figures.json']},
        F148=dict(northwest={s:pop[s] for s in northwest},northwest_total=37177055,new_england={s:pop[s] for s in england},new_england_total=14445438,ny_plus_new_england=33823525,
                  old_rounded_millions=[37.3,14.3,33.7],correct_rounded_millions=[37.2,14.4,33.8],same_values_in_official_2015_base=True),
        F149=dict(edge_witnesses=evidence,drawn_cut_edges_246_left=46,actual_cut_edges_246_left=45,partition_cost=90),global_optimality_verified=False))
    print('PASS F148/F149: exact population sums, eight source-edge witnesses; no search.')


if __name__=='__main__':main()
