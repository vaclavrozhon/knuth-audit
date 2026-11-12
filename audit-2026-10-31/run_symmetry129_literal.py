"""Literal paired options of answer129, for its previously untested0.5T cost.

The old compressed model and successful counts are reused as independent
evidence; this new48-primary/42-secondary input preserves both opposite cells.
"""
from datetime import datetime,timezone
from pathlib import Path
import gzip,json,os,re
import check_macmahon as g
import macmahon126 as mc
import graph_native

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/symmetries129'


def problem():
    edges=sorted(g.EDGE_TRIANGLES)
    header=[g.name(t) for t in g.TRIANGLES]+g.PIECES+['|']+[mc.edge_name(e) for e in edges]
    rows=[];placements=[]
    for t in g.HALF:
        u=g.opposite(t)
        for piece in g.PIECES:
            for cs in sorted({piece[i:]+piece[:i] for i in range(3)}):
                ds=''.join(g.complement(cs))
                rows.append([g.name(t),g.piece(cs)]+[mc.edge_name(e)+':'+c for e,c in zip(g.edges(t),cs)]+
                            [g.name(u),g.piece(ds)]+[mc.edge_name(e)+':'+c for e,c in zip(g.edges(u),ds)])
                placements.append([(t,cs),(u,ds)])
    assert len(rows)==768 and len({tuple(sorted(r)) for r in rows})==768
    # Independent correspondence with the old compressed768-option model.
    h,old,metadata=g.strong_options()
    assert {(tuple(m['triangle']),''.join(m['colors'])) for m in metadata}=={(t,cs) for [(t,cs),_] in placements}
    return dict(header=header,rows=rows,placements=placements,edges=edges)


def main():
    OUT.mkdir(exist_ok=True);native=OUT/'native';native.mkdir(exist_ok=True);graph_native.OUT=native
    enc=problem();built=mc.build()
    result=graph_native.run('literal-strong-rotation',mc.text(enc),binary=built['binaries']['original']['path'],every=100000)
    if result['status']!='completed':return
    assert result['solutions']==68024064
    lookup={tuple(sorted(row)):i for i,row in enumerate(enc['rows'])}
    models=[];selected=[]
    def validate():
        colors={};pieces=[];cells=set()
        for i in selected:
            for t,cs in enc['placements'][i]:
                assert t not in cells;cells.add(t);pieces.append(g.piece(cs))
                # Match actual geometric endpoints;edge labels are checked separately.
                u,v,w=g.vertices(t);a,b=(v,u) if t[2] else (u,v)
                for ends,c in zip([(w,a),(w,b),(u,v)],cs):
                    key=tuple(sorted(ends));assert key not in colors or colors[key]==c;colors[key]=c
        assert cells==set(g.TRIANGLES) and sorted(pieces)==g.PIECES and len(selected)==12
        for (u,v),c in colors.items():
            other=tuple(sorted([(4-u[0],4-u[1]),(4-v[0],4-v[1])]))
            assert colors[other]=='dcba'['abcd'.index(c)]
        return ''.join(colors[tuple(sorted([(e[1],e[2]),(e[1]+1,e[2])]))] if e[0]=='-' else
                       colors[tuple(sorted([(e[1],e[2]),(e[1],e[2]+1)]))] if e[0]=='/' else
                       colors[tuple(sorted([(e[1]+1,e[2]),(e[1],e[2]+1)]))] for e in enc['edges'])
    with gzip.open(native/'literal-strong-rotation.out.gz','rt') as f:
        for line in f:
            if re.fullmatch(r'\d+:\s*',line):
                if selected:models.append(validate());selected=[]
            elif line.strip():
                tokens=re.sub(r'\s*\(\d+ of \d+\)\s*$','',line).split();selected.append(lookup[tuple(sorted(tokens))])
    if selected:models.append(validate())
    assert len(models)==len(set(models))==680
    old=json.loads((ROOT/'results/macmahon/additional-bitset-counts.json').read_text())
    assert next(x for x in old if x['label']=='strong-0')['solutions']==result['solutions']
    models_file=OUT/'literal-strong-rotation-samples.txt';models_file.write_text('\n'.join(models)+'\n')
    mc.save(OUT/'literal-strong-rotation-checked.json',dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
        source_sha256=mc.sha(__file__),native_metadata_sha256=mc.sha(native/'literal-strong-rotation.json'),
        old_independent_metadata_sha256=mc.sha(ROOT/'results/macmahon/additional-bitset-counts.json'),
        solutions=result['solutions'],validated_samples=len(models),output_period=100000,
        net_search_mems=result['net_search_mems'],gross_search_mems=result['search_mems'],
        rounded_teramems=round(result['net_search_mems']/1e12,1),book_teramems=.5,
        models_file=models_file.name,models_sha256=mc.sha(models_file),
        scope='Literal paired-cell encoding, complete count and cost; every emitted sample independently validated. Earlier compressed count is reused, not rerun.'))
    print('PASS129 literal:',result['solutions'],'solutions;',len(models),'samples;',result['net_search_mems'],'net mems',flush=True)


if __name__=='__main__':main()
