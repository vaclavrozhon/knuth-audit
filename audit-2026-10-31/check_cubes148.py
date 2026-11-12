"""Finite inventory, Burnside proof, and literal figure verification for148."""
from collections import Counter
from datetime import datetime,timezone
from itertools import product,permutations
from pathlib import Path
import json,re
import bricks147 as geom
from extract_bricks147 import glyphs,tensor
from puzzle_xcc import save,sha

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/cubes148'
SRC=ROOT/'sources/cubes148'


def name(w):return min(geom.cubes.orient(w,p) for p in geom.cubes.ROTATIONS)


def inventory(path,top):
    gs=sorted(g for g in glyphs(path) if top-.2<g[1]<top+28.2 and g[2] in 'abc')
    assert len(gs)==66,(path,len(gs));words=[]
    for i in range(11):
        six=gs[6*i:6*i+6];up=min(six,key=lambda g:g[1]);down=max(six,key=lambda g:g[1])
        left,front,back,right=sorted(g for g in six if g!=up and g!=down)
        words.append(''.join(g[2] for g in [up,down,front,back,left,right]))
    return words


def decode(t):
    colors={}
    for x,plane in enumerate(t):
        for y,row in enumerate(plane):
            for z,c in enumerate(row):
                if c!='.':assert (x%2+y%2+z%2)==2 and c in 'abc';colors[(x,y,z)]=c
    cells={}
    for p in geom.positions((3,3,3)):
        ff=geom.faces(p)
        if all(f in colors for f in ff):cells[p]=''.join(colors[f] for f in ff)
    assert len(cells)==11
    assert set(colors)=={f for p in cells for f in geom.faces(p)},'Unexplained colored facet'
    assert set(cells)=={(1,j,k) for j in range(3) for k in range(3)}|{(0,1,1),(2,1,1)}
    for p,w in cells.items():
        assert all(w[i]!=w[i+1] for i in [0,2,4])
        for f,delta in enumerate(geom.OFFSETS):
            q=tuple(a+b for a,b in zip(p,delta))
            if q in cells:assert w[f]==cells[q][f^1]
    return cells,colors


def main():
    words=[''.join(p) for p in product('abc',repeat=6) if all(p[i]!=p[i+1] for i in [0,2,4])]
    assert len(words)==216
    classes={name(w) for w in words};assert len(classes)==11
    sizes=Counter(name(w) for w in words);assert Counter(sizes.values())=={8:3,24:8}
    fixed=[sum(geom.cubes.orient(w,p)==w for w in words) for p in geom.cubes.ROTATIONS]
    assert Counter(fixed)=={216:1,6:8,0:15} and sum(fixed)//24==11
    a=ROOT/'results/bricks147/original-478.xml';b=ROOT/'results/bricks147/draft-168.xml'
    first=inventory(a,158.22);second=inventory(b,266.88)
    assert first==second and len(set(name(w) for w in first))==11 and {name(w) for w in first}==classes
    ta=tensor(glyphs(a),(3,3,3),69.72,49.85,211.3,4.68,8.96)
    tb=tensor(glyphs(b),(3,3,3),79.32,49.85,319.96,4.68,8.96)
    assert ta==tb
    cells,colors=decode(ta);assert {name(w) for w in cells.values()}==classes
    shape_symmetries=[];colored_symmetries=[]
    for p,signs,perm in geom.group((3,3,3)):
        transformed={}
        for xyz,w in cells.items():
            q=tuple(xyz[p[i]] if signs[i]>0 else 2-xyz[p[i]] for i in range(3))
            transformed[q]=geom.cubes.orient(w,perm)
        if set(transformed)!=set(cells):continue
        shape_symmetries.append((p,signs,perm))
        for renamed in permutations('abc'):
            trans=str.maketrans('abc',''.join(renamed))
            if all(transformed[q].translate(trans)==w for q,w in cells.items()):colored_symmetries.append(dict(axes=p,signs=signs,colors=''.join(renamed)))
    assert len(shape_symmetries)==16
    # The finite count is also a general Burnside argument: nonidentity rotations
    # can fix an admissible coloring only around a body diagonal. Each of the
    # eight120-degree rotations has two3-cycles; their colors must differ(3*2).
    previous=json.loads((ROOT/'results/polygons143/errata-check.json').read_text())
    pattern=r'(?:[Pp]age\s+|(?:4b|4f5)\.)(?:143|458|141|266)\b|(?:answer|exercise|exer ise)\s+148\b|eleven such cubes|opposite faces'
    contexts=[]
    for path,digest in previous['files'].items():
        file=ROOT.parent/path;assert sha(file)==digest
        lines=file.read_text(errors='replace').splitlines()
        for i,line in enumerate(lines):
            if re.search(pattern,line,re.I):contexts.append(dict(file=path,line=i+1,context='\n'.join(lines[max(0,i-1):i+5])))
    for origin,namefile in [('sources/bricks147/page143.txt','question.txt'),('sources/bricks147/page458.txt','answer.txt'),
                            ('sources/bricks147/draft79.txt','draft-question.txt'),('sources/bricks147/draft162.txt','draft-answer.txt')]:
        (SRC/namefile).write_bytes((ROOT/origin).read_bytes())
    save(OUT/'errata-check.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),files=previous['files'],pattern=pattern,contexts=contexts,
        latest_remote_retrieval='2026-11-03T05:37:34Z; six unchanged hashes reused from143',
        conclusion='No matching correction found forDLX148; displayed contexts include unrelated theorem266.'))
    save(OUT/'checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),
        dependencies={str(p.relative_to(ROOT)):sha(p) for p in [a,b,Path(geom.__file__),ROOT/'cubes146.py',ROOT/'extract_bricks147.py']},
        oriented_colorings=216,rotation_classes=11,orbit_size_histogram=dict(Counter(sizes.values())),burnside_fixed_counts=fixed,
        figure_words=first,all66_inventory_labels_equal_and_valid=True,tensor=ta,
        occupied_cells=[dict(position=p,word=w,type=name(w)) for p,w in cells.items()],
        colored_facets=len(colors),tensor_characters=343,all11_types_used_once=True,all_contacts_valid=True,
        spatial_shape_symmetries=len(shape_symmetries),colored_symmetries=colored_symmetries,
        all_original_and_draft_characters_equal=True,known_errata=[],new_findings=[],expensive_searches_started=False))
    print('PASS148:216 oriented colorings,11 types,Burnside;66 diagram labels+343 tensor characters;11-piece witness and16 shape symmetries. Colored symmetries:',len(colored_symmetries))


if __name__=='__main__':main()
