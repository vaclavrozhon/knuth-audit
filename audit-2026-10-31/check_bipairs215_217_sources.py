"""Read every printed pentomino exchange; compare to accepted catalogs without regeneration."""
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
import json,os,time,xml.etree.ElementTree as ET
from extract_chain150 import points
from extract_jigsaw import inside
from check_exchanges208_214_sources import polygon
from check_pentomino_bipairs import SHAPES,orientations,normalized,canonical_pair,hole_free
from puzzle_xcc import save,sha

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/bipairs215_217'

def freeze(x):return tuple(freeze(v) for v in x) if isinstance(x,list) else x

def shapes_from_source(path,unit,inset):
    polys=[]
    for t in ET.parse(path).iter('fill_path'):
        if t.get('colorspace')!='DeviceRGB':continue
        ps=[v for q in t for v in points(t,q)]
        assert ps;polys.append((polygon(t),tuple(round(float(c),2) for c in t.get('color').split())))
    assert len(polys)%2==0;result=[]
    for k in range(0,len(polys),2):
        pair=polys[k:k+2];x0=min(x for p,color in pair for x,y in p)-inset;y0=min(y for p,color in pair for x,y in p)-inset
        xmax=max(x for p,color in pair for x,y in p)+inset;ymax=max(y for p,color in pair for x,y in p)+inset
        nr,nc=round((ymax-y0)/unit),round((xmax-x0)/unit)
        assert abs((ymax-y0)/unit-nr)<.01 and abs((xmax-x0)/unit-nc)<.01
        parts=[]
        for p,color in pair:
            cells=frozenset((r,c) for r in range(nr) for c in range(nc) if inside(x0+(c+.5)*unit,y0+(r+.5)*unit,p))
            assert len(cells)==5
            names=[n for n,s in SHAPES.items() if normalized(cells) in orientations(s)]
            assert len(names)==1;parts.append(dict(name=names[0],cells=sorted(cells),color=color))
        parts.sort(key=lambda p:p['name']);a,b=map(lambda q:set(map(tuple,q['cells'])),parts)
        assert a.isdisjoint(b) and len(a|b)==10 and parts[0]['name']!=parts[1]['name']
        result.append(dict(parts=parts,bounds=[x0,xmax,y0,ymax],grid=[nr,nc]))
    return result

def partsets(q):return [frozenset(map(tuple,p['cells'])) for p in q['parts']]

def main():
    assert not (OUT/'source-checked.json').exists();assert os.nice(0)>=15;start=time.monotonic()
    accepted=json.loads((ROOT/'results/pentomino_bipairs/catalog.json').read_text())
    catalog={(tuple(q['pieces']),freeze(q['covers'])):i for i,q in enumerate(accepted['catalog'])}
    reports={};traces=[]
    for version,ap,qp in [('book',OUT/'original-494.xml',ROOT/'results/exchanges208_214/original-171.xml'),
                         ('draft',OUT/'draft-184.xml',ROOT/'results/exchanges208_214/draft-93.xml')]:
        traces += [ap,qp];answer=shapes_from_source(ap,5.9964,.18);question=shapes_from_source(qp,7.9967,.24)
        assert len(answer)==36 and len(question)==2
        entries=[]
        for k,q in enumerate(answer[:32]):
            a,b=partsets(q);region=a|b
            if k<18:
                w=max(c for r,c in region);flip=lambda s:frozenset((r,w-c) for r,c in s);kind='left-right'
            else:flip=lambda s:frozenset((c,r) for r,c in s);kind='transpose'
            aa,bb=flip(a),flip(b);assert aa|bb==region and (aa,bb)!=(a,b)
            names=tuple(p['name'] for p in q['parts']);key=canonical_pair(a,b,aa,bb)
            assert (names,key) in catalog,(version,k,names)
            entries.append(dict(source_index=k,catalog_index=catalog[names,key],symmetry=kind,pieces=names))
        for i,j in [(32,33),(34,35)]:
            q,z=answer[i],answer[j];a,b=partsets(q);aa,bb=partsets(z)
            assert a|b==aa|bb and (a,b)!=(aa,bb)
            names=tuple(p['name'] for p in q['parts']);assert names==tuple(p['name'] for p in z['parts'])
            key=canonical_pair(a,b,aa,bb);assert (names,key) in catalog
            # No nontrivial symmetry of the ten-cell region.
            assert len(orientations(a|b))==8
            entries.append(dict(source_indices=[i,j],catalog_index=catalog[names,key],symmetry='none',pieces=names))
        assert {q['catalog_index'] for q in entries}==set(range(34)) and len(entries)==34
        qa,qb=partsets(question[0]);qc,qd=partsets(question[1]);assert qa|qb==qc|qd
        assert [p['name'] for p in question[0]['parts']]==[p['name'] for p in question[1]['parts']]==['S','Y']
        assert qa=={(0,0),(0,1),(1,1),(1,2),(1,3)} and qb=={(0,2),(0,3),(0,4),(0,5),(1,4)}
        assert qc=={(0,4),(0,5),(1,2),(1,3),(1,4)} and qd=={(0,0),(0,1),(0,2),(0,3),(1,1)}
        assert (('S','Y'),canonical_pair(qa,qb,qc,qd)) in catalog
        colors={}
        for q in answer+question:
            for p in q['parts']:
                if p['name'] in colors:assert colors[p['name']]==p['color']
                colors[p['name']]=p['color']
        assert set(colors)==set(SHAPES)
        reports[version]=dict(answer_diagrams=answer,question_diagrams=question,catalog_matches=entries,colors=colors,
            diagrams=38,pieces=76,cells=380)
    for field in ['catalog_matches','colors']:
        assert reports['book'][field]==reports['draft'][field]
    for field in ['answer_diagrams','question_diagrams']:
        assert [q['parts'] for q in reports['book'][field]]==[q['parts'] for q in reports['draft'][field]]
    # New four-case example at the top of p474, not a repeated full delta census.
    P=frozenset((0,c) for c in range(4));N=frozenset((2,c) for c in range(4));four=[];clean=set();holed=set()
    for qi in [0,3]:
        for yj in [1,2]:
            a=P|{(1,qi)};b=N|{(1,yj)};c=N|{(1,qi)};d=P|{(1,yj)}
            assert normalized(a) in orientations(SHAPES['Q']) and normalized(c) in orientations(SHAPES['Q'])
            assert normalized(b) in orientations(SHAPES['Y']) and normalized(d) in orientations(SHAPES['Y'])
            key=canonical_pair(a,b,c,d);ok=hole_free(a|b);(clean if ok else holed).add(key)
            four.append(dict(q_cancelled_cell=[1,qi],y_cancelled_cell=[1,yj],hole_free=ok))
    assert len(clean)==len(holed)==1 and sum(q['hole_free'] for q in four)==2
    assert (('Q','Y'),next(iter(clean))) in catalog
    # Consume the accepted matching profiles and samples; do not regenerate them.
    native=json.loads((ROOT/'results/matching_bipairs/native.json').read_text())
    old=json.loads((ROOT/'results/matching_bipairs/verified.json').read_text());assert native==old['native_cases']
    samples=old['random_samples'];assert len(native)==40 and len(samples)==500
    result=dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),nice=os.nice(0),wall_seconds=time.monotonic()-start,
        dependencies={p:sha(ROOT/p) for p in ['extract_chain150.py','extract_jigsaw.py','check_exchanges208_214_sources.py','check_pentomino_bipairs.py','puzzle_xcc.py']},
        source_hashes={str(p.relative_to(ROOT)):sha(p) for p in traces},
        accepted_data_hashes={p:sha(ROOT/p) for p in ['results/pentomino_bipairs/catalog.json','results/pentomino_bipairs/independent.json','results/pentomino_bipairs/examples.json','results/matching_bipairs/native.json','results/matching_bipairs/verified.json']},
        source_diagrams=reports,new_four_case_example=four,accepted_native_profiles=40,accepted_random_samples=500,
        accepted_levelwise_counterexamples=sum(q['exceeds_levelwise'] for q in samples),
        accepted_total_counterexamples=sum(q['exceeds_total'] for q in samples),
        old_censuses_rerun=0,new_solver_searches=0,status='PASS')
    save(OUT/'source-checked.json',result)
    print(json.dumps({k:v for k,v in result.items() if k in ['at_utc','nice','wall_seconds','old_censuses_rerun','new_solver_searches','status']}))

if __name__=='__main__':main()
