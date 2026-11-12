"""Extend prior153 evidence to original/draft paths and terminal markers."""
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
import json,math
import check_path153 as old
from extract_chain150 import paths
from extract_paths151 import strokes
from paths151 import PORTS
from puzzle_xcc import save,sha
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/path153'

def decode(rect,curves):
    x0,x1,y0,y1=rect;unit=min(x1-x0,y1-y0);vertical=y1-y0>x1-x0
    assert abs(max(x1-x0,y1-y0)/unit-2)<.001
    ports=[(2-y,x) for x,y in PORTS] if vertical else PORTS
    ports=[(x0+x*unit/2,y0+y*unit/2) for x,y in ports]
    local=[c for c in curves if all(x0-.005<=x<=x1+.005 and y0-.005<=y<=y1+.005 for x,y in c['control'])]
    dots=[c['start'] for c in local if c['start']==c['end']]
    pairs=[];tip=-1;terminal=None;count=0
    for c in local:
        if c['start']==c['end']:continue
        ids=[];ends=[c['start'],c['end']]
        for p in ends:
            ds=[math.dist(p,q) for q in ports];i=min(range(6),key=ds.__getitem__)
            ids.append(i if ds[i]<.005 else -1)
        if -1 not in ids:pairs.append(tuple(sorted(ids)))
        else:
            assert ids.count(-1)==1 and tip==-1
            interior=ends[ids.index(-1)];tip=ids[1-ids.index(-1)];terminal=interior
            assert min(math.dist(interior,d) for d in dots)<.005
            assert abs(math.dist(ports[tip],interior)/unit-.2)<.001
        count+=1
    active=[p for pair in pairs for p in pair]+([] if tip<0 else [tip])
    assert len(active)==len(set(active))
    assert (tip<0 and not dots) or (tip>=0 and len(dots)==2)
    return dict(pairs=tuple(sorted(pairs)),tip=tip,vertical=vertical,stroke_count=count,terminal=terminal)

def question(path,y0,y1):
    rs,_=paths(path);cs=strokes(path);rs=sorted(r for r in rs if y0<r[2]<r[3]<y1);assert len(rs)==8
    result=[decode(r,cs) for r in rs]
    actual=[old.normalized(p['pairs'],p['tip']) for p in result]
    assert actual==[old.normalized(*p) for p in old.QUESTION]
    return dict(pieces=actual,normal_pieces=6,terminal_pieces=2,subpaths=sum(p['stroke_count'] for p in result))

def board(path,x0,y0,fig):
    unit=9.56;rs,_=paths(path);cs=strokes(path)
    rs=[r for r in rs if x0-.005<=r[0]<r[1]<=x0+5*unit+.005 and y0-.005<=r[2]<r[3]<=y0+4*unit+.005]
    assert len(rs)==8
    actual=[];total=0
    for r in rs:
        p=decode(r,cs);c=(r[0]-x0)/unit;row=(r[2]-y0)/unit
        assert abs(c-round(c))<.001 and abs(row-round(row))<.001
        actual.append((round(row),round(c),'V' if p['vertical'] else 'H',p['pairs'],p['tip']))
        total+=p['stroke_count']
    def normalize(f):return sorted((r,c,d,tuple(sorted(tuple(sorted(p)) for p in pairs)),tip) for r,c,d,pairs,tip in f)
    assert normalize(actual)==normalize(fig)
    pieces=old.inventory(fig);opts=old.options(pieces);picture=old.picture_options(fig,pieces,opts)
    assert old.verify(picture,pieces)
    result=dict(figure=normalize(actual),all_eight_pieces=True,blank_cells=4,single_path=True,subpaths=total)
    return result

def main():
    configs=[('original','original-164.xml',80,120,'original-480.xml',151.68,367.6,310.36),
             ('draft','draft-86.xml',190,230,'draft-170.xml',260.22,377.26,320.02)]
    data={};hashes={}
    for name,qfile,y1,y2,afile,y0,ax,cx in configs:
        qp=OUT/qfile;ap=OUT/afile
        print('Checking153',name,flush=True)
        data[name]=dict(question=question(qp,y1,y2),a=board(ap,ax,y0,old.FIG_A),c=board(ap,cx,y0,old.FIG_C))
        for p in [qp,ap]:hashes[str(p.relative_to(ROOT))]=sha(p)
    assert data['original']==data['draft']
    saved={};prior_hashes={}
    for name,fig in [('153a',old.FIG_A),('153c',old.FIG_C)]:
        p=ROOT/'results/path_dominoes'/name;d=json.loads(p.with_suffix('.json').read_text())
        assert d['matching_solutions']==d['single_path_solutions']==d['dlx2_solutions']==2 and d['symmetry_classes']==1
        assert 'Altogether 2 solutions' in p.with_suffix('.dlx2.txt').read_text()
        pieces=old.inventory(fig);opts=old.options(pieces);full=set()
        for m in d['solutions']:
            selected=[opts[i-1] for i in m['ids']];assert old.verify(selected,pieces);full.add(old.sig(selected))
        assert len(full)==2 and old.sig(old.picture_options(fig,pieces,opts)) in full
        assert {old.transformed([opts[i-1] for i in d['solutions'][0]['ids']],False,False,opts),old.transformed([opts[i-1] for i in d['solutions'][0]['ids']],True,True,opts)}==full
        for ext in ['.json','.xcc','.dlx2.txt']:prior_hashes[str(p.with_suffix(ext).relative_to(ROOT))]=sha(p.with_suffix(ext))
        saved[name]=dict(full_count=2,symmetry_classes=1,printed_witness_in_saved_models=True,all_saved_models_valid=True)
    dependencies={p:sha(ROOT/p) for p in ['check_path153.py','check_path_dominoes.py','extract_paths151.py','extract_chain150.py','paths151.py']}
    save(OUT/'figures-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),dependencies=dependencies,
        traces=hashes,figures=data,prior_hashes=prior_hashes,prior_counts=saved,all_original_draft_equal=True,
        terminal_types=30,terminal_type_proof='Choose3 of6 boundary points, choose1 as terminal, divide by2. No odd subset is invariant under a half-turn;20*3/2=30.',
        solver_calls=0,prior_censuses_not_restarted=True))
    print('PASS153:all24 original pieces and all24 draft pieces match previous transcription; terminals and paths valid; saved2+2 counts accepted without new search.')

if __name__=='__main__':main()
