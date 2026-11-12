"""Read every printed queen from the actual grids in both source versions."""
from collections import Counter
from pathlib import Path
from datetime import datetime,timezone
from itertools import combinations
import xml.etree.ElementTree as ET
import json,time
from extract_chain150 import paths
from extract_jigsaw import transform
from puzzle_xcc import save,sha

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/queen230_236'
SIZES=[38.3631,32.2298,30.7065,38.3737,38.3831,38.3915,22.2455,11.1271,5.5646]


def decode(path):
    _,segments=paths(path);groups=[]
    for s in segments:
        if len(s['points'])!=2:continue
        (x,y),(u,v)=s['points']
        if abs(y-v)>.001 or abs(x-u)<50:continue
        a,b=sorted([x,u])
        for g in groups:
            if abs(a-g[0][0])<.1 and abs(b-g[0][1])<.1:g.append((a,b,y));break
        else:groups.append([(a,b,y)])
    glyphs=[]
    for t in ET.parse(path).getroot().iter('fill_text'):
        for s in t:
            size=abs(float(s.get('trm').split()[0]))
            if not any(abs(size-v)<.001 for v in SIZES):continue
            for q in s:
                assert q.get('unicode') in ['q','\ufffd'],q.attrib
                glyphs.append(transform(t,float(q.get('x')),float(q.get('y'))))
    decoded=[];assigned=0
    for lines in groups:
        if len(lines)<17:continue
        yy=sorted(y for a,b,y in lines);n=len(yy)-1
        x0=min(a for a,b,y in lines);x1=max(b for a,b,y in lines);unit=(x1-x0)/n
        if abs((yy[-1]-yy[0])/unit-n)>.07:continue
        found=[(x,y) for x,y in glyphs if x0-.4*unit<x<x1+.4*unit and yy[0]<y<yy[-1]+.4*unit]
        if not found:continue
        cells=[];errors=[]
        for x,y in found:
            bottom=min(range(n+1),key=lambda i:abs(y-yy[i]));col=(x-x0)/unit
            cells.append((bottom-1,round(col)));errors.append((abs(y-yy[bottom])/unit,abs(col-round(col))))
        assert all(0<=a<n and 0<=b<n for a,b in cells)
        assert len(set(cells))==len(cells)
        assert max(a for a,b in errors)<.36 and max(b for a,b in errors)<.08,(path,n,max(errors))
        rows={a for a,b in cells};cols={b for a,b in cells}
        assert len(rows)==len(cols)==len(cells)
        assert len({a+b for a,b in cells})==len({a-b for a,b in cells})==len(cells)
        decoded.append(dict(n=n,bounds=[x0,x1,yy[0],yy[-1]],horizontal_grid_lines=n+1,queens=sorted(cells),queen_count=len(cells),
            missing_rows=sorted(set(range(n))-rows),missing_columns=sorted(set(range(n))-cols),max_origin_error_cells=[max(a for a,b in errors),max(b for a,b in errors)]))
        assigned+=len(cells)
    assert assigned==len(glyphs),(path,assigned,len(glyphs),[(q['n'],q['queen_count'],q['bounds']) for q in decoded])
    bands=[]
    for q in sorted(decoded,key=lambda q:q['bounds'][2]):
        if bands and q['bounds'][2]-bands[-1][0]['bounds'][2]<15:bands[-1].append(q)
        else:bands.append([q])
    return [q for band in bands for q in sorted(band,key=lambda q:q['bounds'][0])]


def permutation(cells,n):
    by=dict(cells);return [by.get(i,-1)+1 for i in range(n)]
def valid(q):
    n=len(q);return sorted(q)==list(range(1,n+1)) and len({i+v for i,v in enumerate(q)})==len({i-v for i,v in enumerate(q)})==n
def norms(q):
    n=len(q);return sorted(((2*r-n-1)**2+(2*c-n-1)**2 for r,c in enumerate(q,1)),reverse=True)


def tilts(q):
    n=len(q);points={(r,c-1) for r,c in enumerate(q)};found=set()
    for (r,c),(s,t) in combinations(points,2):
        # The pair is one diagonal of the square; rotate its half-vector by90 degrees.
        a,b=r+s+c-t,c+t+s-r;d,e=r+s-c+t,c+t-s+r
        if any(v%2 for v in [a,b,d,e]):continue
        other={(a//2,b//2),(d//2,e//2)}
        if len(other)==2 and other<=points:
            square=frozenset({(r,c),(s,t)}|other)
            if len(square)==4:found.add(square)
    result=[]
    for square in sorted(found,key=lambda s:sorted(s)):
        sx=sum(r for r,c in square);sy=sum(c for r,c in square)
        assert sx%2==sy%2==0
        flipped={(r,sy//2-c) for r,c in square}
        assert flipped!=square and len(flipped)==4
        assert {r for r,c in square}=={r for r,c in flipped} and {c for r,c in square}=={c for r,c in flipped}
        assert {r+c for r,c in square}=={r+c for r,c in flipped} and {r-c for r,c in square}=={r-c for r,c in flipped}
        candidate=permutation((points-square)|flipped,n);assert valid(candidate) and norms(candidate)==norms(q)
        result.append(dict(before=sorted(square),after=sorted(flipped),center_twice=[sx//2,sy//2]))
    assert sum(len(v['before']) for v in result)==len({tuple(p) for v in result for p in v['before']})
    # Every combination is checked directly; this is at most4096 explicit constructions.
    allq=set();target=norms(q)
    for mask in range(1<<len(result)):
        p=set(points)
        for i,v in enumerate(result):
            if mask>>i&1:p-=set(map(tuple,v['before']));p|=set(map(tuple,v['after']))
        candidate=tuple(permutation(p,n));assert valid(candidate) and norms(candidate)==target;allq.add(candidate)
    assert len(allq)==1<<len(result)
    return dict(squares=result,distinct_constructed_models=len(allq),all_nonattacking=True,same_distance_multiset=True)


def main():
    start=time.monotonic();assert not (OUT/'figures-checked.json').exists()
    names=['original-132','original-172','original-497','draft-54','draft-94','draft-187']
    data={name:decode(OUT/(name+'.xml')) for name in names}
    for a,b in zip(names[:3],names[3:]):assert [q['queens'] for q in data[a]]==[q['queens'] for q in data[b]],(a,b)
    old=json.loads((ROOT/'results/queen_costs/figures-verified.json').read_text())
    for name,key in [('original-132','112'),('original-172','152'),('original-497','477')]:assert [permutation(q['queens'],16) for q in data[name] if q['n']==16]==old[key]
    large={q['n']:permutation(q['queens'],q['n']) for q in data['draft-187'] if q['n']>16}
    assert set(large)=={17,18,19,32,64,128}
    for n,q in large.items():
        if n!=128:assert valid(q)
    assert large[128][-1]==0 and large[128].count(0)==1 and set(range(1,129))-set(large[128])=={65}
    repaired=large[128][:-1]+[65];assert valid(repaired)
    # Exact original primary-paper table, not a new optimizer.
    text=(ROOT/'sources/fischetti-salvagnin-1907.08246v1.txt').read_text().split('And these are some most-beautiful solutions')[1]
    import re
    paper={}
    matches=list(re.finditer(r'(?m)^\s+(16|32|48|64|80|96|112|128|144|160|176)\s+\d+\.\d+\s+',text))
    for i,m in enumerate(matches):
        n=int(m[1]);end=matches[i+1].start() if i+1<len(matches) else len(text)
        values=list(map(int,re.findall(r'\d+',text[m.end():end])))[:n]
        assert valid(values),(n,values);paper[n]=values
    assert repaired==paper[128] and norms(large[32])==norms(paper[32]) and norms(large[64])==norms(paper[64])
    tilt={str(n):tilts(q) for n,q in [(64,large[64]),(128,repaired)]}
    assert [len(tilt[str(n)]['squares']) for n in [64,128]]==[6,12]
    assert [tilt[str(n)]['distinct_constructed_models'] for n in [64,128]]==[64,4096]
    save(OUT/'figures-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),wall_seconds=time.monotonic()-start,
        dependencies={p:sha(ROOT/p) for p in ['extract_chain150.py','extract_jigsaw.py','puzzle_xcc.py']},
        trace_hashes={name+'.xml':sha(OUT/(name+'.xml')) for name in names},figures=data,printed_queen_occurrences_per_version=389,
        old_seven_figures_exactly_preserved=True,original_draft_equal=True,large_permutations=large,repaired128=repaired,paper_permutations=paper,tilts=tilt,
        accepted_source_hashes={p:sha(ROOT/p) for p in ['results/queen_costs/figures-verified.json','sources/fischetti-salvagnin-1907.08246v1.txt','sources/fischetti-salvagnin-1907.08246v1.pdf']},
        new_optimization_searches=0,old_censuses_repeated=0,missing_queen=dict(row_one_based=128,column_one_based=65,count=127,n=128)))
    print('PASS:13figures,389queens per version;128 figure missing(128,65), other127 exactly match primary paper.6/12tilts give64/4096 models.')


if __name__=='__main__':main()
