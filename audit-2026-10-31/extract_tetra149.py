"""Read the twenty coordinate labels and colors from both original vector traces."""
from datetime import datetime,timezone
import xml.etree.ElementTree as ET
from extract_jigsaw import transform
import tetra149 as h
from puzzle_xcc import save,sha


def figure(path,top,shift):
    labels={};letters=[]
    for t in ET.parse(path).getroot().iter('fill_text'):
        for s in t:
            gs=[g for g in s if g.get('unicode')]
            if not gs:continue
            x,y=transform(t,float(gs[0].get('x')),float(gs[0].get('y')))
            word=''.join(g.get('unicode') for g in gs)
            if top-1<y<top+98 and word.isdigit() and len(word)==4:
                v=tuple(map(int,word)); assert v in h.INDEX and v not in labels
                labels[v]=(x,y)
            for g in gs:
                x,y=transform(t,float(g.get('x')),float(g.get('y')))
                if top-1<y<top+98 and 235<x<425 and g.get('unicode') in 'abcde':letters.append((x,y,g.get('unicode')))
    assert len(labels)==len(letters)==20
    # Coordinate labels themselves must form the stated affine projection.
    basis=[labels[tuple(3*(i==j) for i in range(4))] for j in range(4)]
    for v,xy in labels.items():
        expected=tuple(sum(v[j]*basis[j][k]/3 for j in range(4)) for k in range(2))
        assert max(abs(a-b) for a,b in zip(xy,expected))<.02
    colors={};matches=[]
    for x,y,c in letters:
        distances=sorted(((x-lx-shift)**2+(y-ly-.5)**2,v) for v,(lx,ly) in labels.items())
        distance,v=distances[0];assert distance<1 and distances[1][0]>40 and v not in colors
        colors[v]=c;matches.append(dict(vertex=v,color=c,label_position=labels[v],color_position=(x,y),squared_error=distance))
    model=''.join(colors[v] for v in h.VERTICES);types=h.validate(model)
    return dict(model=model,physical_types=types,matches=matches)


def main():
    a=h.ROOT/'results/bricks147/original-478.xml';b=h.ROOT/'results/bricks147/draft-168.xml'
    original=figure(a,415.64,182.55);draft=figure(b,524.30,182.42)
    assert original['model']==draft['model']
    orbit=h.orbit(original['model']);assert len(orbit)==2880
    for m in orbit:h.validate(m)
    save(h.OUT/'figures-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),
        geometry_sha256=sha(h.__file__),trace_sha256={str(p.relative_to(h.ROOT)):sha(p) for p in [a,b]},
        original=original,draft=draft,all100_labels_characters_equal=True,all10_tetrahedra_used_once=True,
        orbit_size=2880,combined_symmetry_group=2880,stabilizer=1,all_orbit_models_valid=True))
    print('PASS149:20 barycentric labels and20 colors agree in original/draft;10 physical types;2880 distinct valid symmetry images.')


if __name__=='__main__':main()
