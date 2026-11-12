"""Literal options for DLX126 and isolated primary-color eligibility build.

The earlier symmetry122 sources/binaries remain untouched while Q8 runs.
"""
from pathlib import Path
from datetime import datetime, timezone
from itertools import product
from collections import Counter
import difflib, gzip, json, re, shutil, subprocess, tempfile
import check_macmahon as geom
import graph_native
from dlx1_audit_tools import ROOT, sha
from native_symmetry122 import save

OUT = ROOT/'results/triangles124_126'


def edge_name(e):
    return f'{e[0]}{e[1]}{e[2]}'


def problem(mode='anchored'):
    cells = geom.TRIANGLES
    pieces = geom.PIECES
    edges = sorted(geom.EDGE_TRIANGLES)
    boundary = [e for e in edges if len(geom.EDGE_TRIANGLES[e]) == 1]
    names = [geom.name(t) for t in cells] + pieces + ['*']
    header = names + ['|'] + [edge_name(e) for e in edges]
    fixed = {} if mode == 'full' else {'aaa': (2,0,0)}
    if mode == 'center-up':
        fixed.update(bbb=(1,2,0), ccc=(2,1,0), ddd=(2,2,0))
    elif mode == 'center-down':
        fixed.update(bbb=(1,1,1), ccc=(2,1,1), ddd=(1,2,1))
    else:
        assert mode in ('full', 'anchored')
    rows, placements = [], []
    for t in cells:
        for tile in pieces:
            if tile in fixed and t != fixed[tile]:
                continue
            for cs in sorted({tile[i:]+tile[:i] for i in range(3)}):
                rows.append([geom.name(t), tile] + [edge_name(e)+':'+c for e,c in zip(geom.edges(t),cs)])
                placements.append(dict(cell=t, colors=cs, tile=tile))
    rows.append(['*']+[edge_name(e)+':a' for e in boundary])
    placements.append(None)
    return dict(mode=mode, header=header, rows=rows, placements=placements,
                primary_names=names, edges=edges, fixed=fixed)


def text(enc):
    return ' '.join(enc['header'])+'\n'+'\n'.join(' '.join(row) for row in enc['rows'])+'\n'


def build():
    dest=OUT/'native';dest.mkdir(parents=True,exist_ok=True)
    manifest=dest/'build.json'
    if manifest.exists():
        data=json.loads(manifest.read_text())
        for name,entry in data['sources'].items(): assert sha(entry['path'])==entry['sha256'],name
        for name,entry in data['binaries'].items(): assert sha(entry['path'])==entry['sha256'],name
        return data
    base=ROOT/'results/symmetry121_123/native/dlx2-symmetry122.w'
    original=base.read_text()
    replacements=[
      ('int theta=49;', 'int tile_mode=2; /* 126:1 waits for all colors,2 waits for tile colors */\nint theta=49;'),
      ("case 'y': k|=", "case 'W': k|=(sscanf(argv[j]+1,\"\"O\"d\",&tile_mode)-1);@+break;\ncase 'y': k|="),
      ('  @<Input the options@>;', '''  @<Input the options@>;
  if (tile_mode!=1 && tile_mode!=2) panic("Invalid tile threshold mode");
  for (i=1;i<second;i++) {
    if (strlen(cl[i].name)==3 && strspn(cl[i].name,"abcd")==3) {
      if (tile_mode==1) cl[i].cth='e';
      else {
        cl[i].cth='a';
        for (j=0;j<3;j++) if (cl[i].name[j]>=cl[i].cth)
          cl[i].cth=cl[i].name[j]+1;
      }
    }
  }''')]
    code=original
    for old,new in replacements:
        assert code.count(old)==1,old
        code=code.replace(old,new)
    source=dest/'dlx2-macmahon126.w';source.write_text(code)
    patch=''.join(difflib.unified_diff(original.splitlines(True),code.splitlines(True),fromfile=base.name,tofile=source.name))
    (dest/'dlx2-macmahon126.patch').write_text(patch)
    tmp=Path(tempfile.mkdtemp(prefix='knuth-vol4b-macmahon126-native-'))
    sources={}
    for name in ['gb_flip.w','gb_flip.ch','boilerplate.w']:
        path=ROOT/'sources/knuth-programs'/name;shutil.copy2(path,tmp/name)
        sources[name]=dict(path=str(path),sha256=sha(path))
    shutil.copy2(source,tmp/source.name)
    commands=[['ctangle','gb_flip.w','gb_flip.ch'],['ctangle',source.name],
              ['cc','-O2','-Wno-implicit-int','-Wno-implicit-function-declaration','dlx2-macmahon126.c','gb_flip.c','-o','dlx2-macmahon126'],
              ['c++','-O3','-std=c++17',str(ROOT/'xcc_bitset.cpp'),'-o','xcc-bitset']]
    with (dest/'build.log').open('w') as log:
        for cmd in commands:subprocess.run(cmd,cwd=tmp,stdout=log,stderr=log,check=True)
    previous=json.loads((base.parent/'build.json').read_text())
    original_bin=Path(previous['binaries']['original']['binary'])
    assert sha(original_bin)==previous['binaries']['original']['sha256']
    for p in [base,source,ROOT/'xcc_bitset.cpp',Path(__file__)]:sources[p.name]=dict(path=str(p),sha256=sha(p))
    binaries={k:dict(path=str(p),sha256=sha(p)) for k,p in [('original',original_bin),('threshold',tmp/'dlx2-macmahon126'),('bitset',tmp/'xcc-bitset')]}
    result=dict(built_at_utc=datetime.now(timezone.utc).isoformat(),commands=commands,sources=sources,binaries=binaries,
                scope='Original DLX2; previously validated122 changes plus primary CTH initialization prescribed in126; separate immutable-conflict bitset solver.')
    save(manifest,result);return result


def native(label,enc,variant='original',*,every=1):
    built=build();graph_native.OUT=OUT/'native'
    if variant=='original':
        binary=built['binaries']['original']['path'];source=ROOT/'sources/knuth-programs/dlx2.w';extra=()
    else:
        assert variant in ('all-colors','tile-colors')
        binary=built['binaries']['threshold']['path'];source=OUT/'native/dlx2-macmahon126.w'
        extra=('y98','W1' if variant=='all-colors' else 'W2')
    return graph_native.run(label,text(enc),binary=binary,source=source,every=every,extra=extra)


def models(label,enc):
    lookup={tuple(sorted(row)):i for i,row in enumerate(enc['rows'])}
    assert len(lookup)==len(enc['rows'])
    model=None
    with gzip.open(OUT/'native'/(label+'.out.gz'),'rt') as f:
        for line in f:
            if re.fullmatch(r'\d+:\s*',line):
                if model is not None:yield tuple(sorted(model))
                model=[]
            elif line.strip():
                tokens=re.sub(r'\s*\(\d+ of \d+\)\s*$','',line).split()
                assert model is not None;model.append(lookup[tuple(sorted(tokens))])
    if model is not None:yield tuple(sorted(model))


def validate(model,enc):
    assert len(model)==25 and len(set(model))==25
    colors={};cells=set();pieces=[];border=0
    for i in model:
        p=enc['placements'][i]
        if p is None:
            border+=1;continue
        t=tuple(p['cell']);assert t not in cells;cells.add(t)
        cs=p['colors'];tile=min(cs[j:]+cs[:j] for j in range(3));pieces.append(tile)
        if tile in enc['fixed']:assert t==tuple(enc['fixed'][tile])
        # Geometric edge endpoints are independently shared by neighboring cells.
        v=geom.vertices(t)
        a,b=(v[1],v[0]) if t[2] else (v[0],v[1])
        pairs=(tuple(sorted([v[2],a])),tuple(sorted([v[2],b])),tuple(sorted([v[0],v[1]])))
        for edge,c in zip(pairs,cs):
            assert edge not in colors or colors[edge]==c
            colors[edge]=c
    assert border==1 and cells==set(geom.TRIANGLES) and sorted(pieces)==geom.PIECES
    edge_colors={}
    for edge,ts in geom.EDGE_TRIANGLES.items():
        t=ts[0];v=geom.vertices(t);j=geom.edges(t).index(edge)
        a,b=(v[1],v[0]) if t[2] else (v[0],v[1])
        ends=[(v[2],a),(v[2],b),(v[0],v[1])][j]
        c=colors[tuple(sorted(ends))];edge_colors[edge]=c
        if len(ts)==1:assert c=='a'
    return ''.join(edge_colors[tuple(e)] for e in enc['edges'])


def orbit_key(colors):
    names={};out=[]
    for c in colors:
        if c=='a':out.append(c)
        else:
            if c not in names:names[c]=chr(98+len(names))
            out.append(names[c])
    return ''.join(out)
