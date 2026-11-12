"""Read all216 face labels of the30-cube inventory and the six-cube witness."""
from datetime import datetime,timezone
import xml.etree.ElementTree as ET
from extract_jigsaw import transform
import cubes146 as h


def decode(path,rows,example):
    glyphs=[]
    for text in ET.parse(path).getroot().iter('fill_text'):
        for span in text:
            for g in span:
                if g.get('unicode') in list('abcdef'):
                    x,y=transform(text,float(g.get('x')),float(g.get('y')))
                    glyphs.append(dict(letter=g.get('unicode'),x=x,y=y))
    def read_row(top,n):
        selected=sorted((g for g in glyphs if top-.15<g['y']<top+28.15),key=lambda g:g['x'])
        assert len(selected)==6*n,(top,n,len(selected))
        cubes=[]
        for i in range(n):
            six=selected[6*i:6*i+6]
            up=min(six,key=lambda g:g['y']);down=max(six,key=lambda g:g['y'])
            remaining=sorted((g for g in six if g is not up and g is not down),key=lambda g:g['x'])
            left,front,back,right=remaining
            assert abs(up['x']-down['x'])<.2
            assert abs(left['y']-right['y'])<.2
            assert abs((front['y']+back['y'])/2-left['y'])<.2
            word=''.join(g['letter'] for g in [up,down,front,back,left,right])
            assert sorted(word)==list(h.COLORS)
            cubes.append(dict(word=word,name=h.NAME[word],glyphs=six))
        return cubes
    inventory=sum((read_row(top,10) for top in rows),[]);witness=read_row(example,6)
    assert sorted(c['name'] for c in inventory)==h.TYPES
    placement=[c['word'] for c in witness];h.validate(placement)
    names=[c['name'] for c in witness]
    assert names==['aebfcd','acbfde','acbdef','afbdec','abcedf','aebcfd']
    return dict(inventory=inventory,witness=witness,witness_names=names,witness_row=placement,
                all_30_distinct_types=True,all_216_face_labels_valid=True)


def main():
    original=h.ROOT/'results/hexagons144/page142-trace.xml'
    draft=h.ROOT/'results/hexagons144/draft78-trace.xml'
    a=decode(original,[393.0,433.32,473.7],562.62)
    b=decode(draft,[501.6,541.92,582.24],671.28)
    for field in ['inventory','witness']:
        assert [r['word'] for r in a[field]]==[r['word'] for r in b[field]],field
    h.save(h.OUT/'figures-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),
        checker_sha256=h.sha(__file__),geometry_sha256=h.sha(h.__file__),
        trace_hashes={str(p.relative_to(h.ROOT)):h.sha(p) for p in [original,draft]},
        original=a,draft=b,all_216_original_and_draft_labels_equal=True))
    print('PASS146 figures:30 distinct cube types and valid six-cube witness;216 face labels; original/draft equal.')


if __name__=='__main__':main()
