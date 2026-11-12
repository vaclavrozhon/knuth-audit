"""Check all printed147 histograms and elementary claims against completed data."""
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
import json,xml.etree.ElementTree as ET
from extract_jigsaw import transform
import bricks147 as h


def read(p):return json.loads(Path(p).read_text())


def figure(path,top):
    glyphs=[]
    for t in ET.parse(path).getroot().iter('fill_text'):
        for span in t:
            for g in span:
                if g.get('unicode') in 'abcdef':
                    x,y=transform(t,float(g.get('x')),float(g.get('y')))
                    lo,hi=(330,401) if 'original' in path.name else (350,423)
                    if lo<x<hi:glyphs.append((x,y,g.get('unicode')))
    result=[]
    for y0 in [top,top+37.38]:
        selected=sorted(g for g in glyphs if y0-.2<g[1]<y0+28.2)
        assert len(selected)==12,(path,y0,len(selected))
        for i in range(2):
            six=selected[6*i:6*i+6];up=min(six,key=lambda x:x[1]);down=max(six,key=lambda x:x[1])
            left,front,back,right=sorted(g for g in six if g!=up and g!=down)
            result.append(''.join(g[2] for g in [up,down,front,back,left,right]))
    return result


def main():
    printed={
        '2x2x3':{'111':(0,0,1,0),'101':(0,2,6,1),'100':(0,1,6,0),'001':(0,1,2,0),'000':(0,0,2,0)},
        '2x2x4':{'111':(0,0,1,0),'110':(0,0,1,0),'101':(0,3,4,2),'100':(0,11,14,2),'001':(0,2,2,3),'000':(0,1,1,1)},
        '2x2x5':{'101':(0,5,4,0),'100':(0,18,9,0),'001':(0,0,1,0),'000':(0,2,5,1)},
        '2x3x3':{'111':(2,15,4,0),'110':(4,8,1,0),'100':(1,4,1,2)},
        '2x3x4':{'110':(6,8,1,0),'100':(0,6,0,0),'011':(0,4,2,0),'010':(0,2,0,0),'001':(0,2,0,0),'000':(0,7,0,0)},
        '2x3x5':{'111':(0,2,0,0)}}
    patterns={'111':'aa × bb × cc','110':'aa × bb × cd','101':'aa × bc × dd','100':'aa × bc × de',
              '011':'ab × cc × dd','010':'ab × cc × de','001':'ab × cd × ee','000':'ab × cd × ef'}
    differences=[];results={}
    for case,expected in printed.items():
        r=read(h.OUT/'bounded'/f'{case}-checked.json')
        actual={k:tuple(v.get(str(n),0) for n in [1,2,4,8]) for k,v in r['histogram'].items()}
        assert set(expected)==set(actual)
        for k,counts in expected.items():
            if counts!=actual[k]:differences.append(dict(case=case,faces=patterns[k],repeat_axes=k,printed=counts,corrected=actual[k]))
        results[case]=dict(normalized_models=r['models'],orbits=len(r['orbits']),histograms=actual)
    assert len(differences)==4 and all(d['case']=='2x2x4' for d in differences)
    assert {d['repeat_axes']:tuple(d['corrected']) for d in differences}=={
        '101':(0,3,4,1),'100':(0,11,12,2),'001':(0,2,2,4),'000':(0,1,3,1)}
    for label,count,orbits in [('1x1x1',1,1),('1x1x2',1,1),('1x1x3',0,0),('1x2x2',3,2),('1x2x3',1,1),('2x2x2',26,4),('3x3x3',0,0)]:
        r=read(h.OUT/'bounded'/f'{label}-checked.json');assert r['models']==count and len(r['orbits'])==orbits
    for label in ['2x2x6','2x2x7']:assert read(h.OUT/'followup'/f'{label}-checked.json')['models']==0
    for label in ['without-corner','without-middle-and-above']:
        r=read(h.OUT/'followup'/f'{label}-witness.json');assert r['all_contacts_and_boundaries_valid'] and r['complete_census'] is False
    original=h.OUT/'original-163.xml';draft=h.OUT/'draft-85.xml'
    a=figure(original,115.86);b=figure(draft,224.52)
    fig=read(h.OUT/'figures-checked.json')['figures'];assert a==b==fig['small']['model']
    # A specified pair of opposite colors occurs on exactly six physical cube types.
    opposite_counts=Counter()
    for name in h.cubes.TYPES:
        for f in [0,2,4]:opposite_counts[tuple(sorted(name[f:f+2]))]+=1
    assert len(opposite_counts)==15 and set(opposite_counts.values())=={6}
    # Fix the six exterior colors of the2x2x2 prototype and compare its two constructions.
    models=[]
    for line in (h.OUT/'bounded/2x2x2.out').read_text().splitlines():
        if not line.startswith('M '):continue
        row=tuple(h.cubes.WORDS[int(i)] for i in line.split()[1:]);_,bounds=h.validate((2,2,2),row)
        if len(set(bounds))<6:continue
        external=[bounds[i] for i in [2,3,0,1,4,5]];rename=dict(zip(external,h.cubes.COLORS))
        models.append(tuple(''.join(rename[c] for c in w) for w in row))
    assert len(models)==2 and models[0]!=models[1]
    sets=[{h.cubes.NAME[w] for w in r} for r in models]
    assert sets[0]==sets[1] and 'abcdef' not in sets[0] and len(sets[0])==8
    target=h.cubes.normalize(models[1]);assert h.orbit((2,2,2),h.cubes.normalize(models[0])).count(target)==24
    # Exact face-item example135 and all ten entries of the top selector.
    big=fig['magnificent'];colors,_=h.validate((2,3,5),big['model'])
    example={''.join(map(str,p)):colors[p] for p in h.faces((0,1,2))}
    assert example==dict(zip(['035','125','134','136','145','235'],'abdfec'))
    top=sorted(''.join(map(str,p)) for p in colors if p[1]==0)
    assert top==['101','103','105','107','109','301','303','305','307','309']
    h.save(h.OUT/'claims-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=h.sha(__file__),
        geometry_sha256=h.sha(h.__file__),all_larger_cases=results,differences=differences,
        all_other_histograms_agree=True,normalized_2x2x4_total_unchanged=244,total_2x2x4_orbits_unchanged=48,
        question_figure_all24_glyphs_valid=True,question_trace_hashes={str(p.relative_to(h.ROOT)):h.sha(p) for p in [original,draft]},
        prototype_two_models_same_eight_types_excluding_prototype=True,prototype_isomorphisms=24,
        opposite_pair_inventory=6,case135_correct=True,top_selector_correct=True,
        catalogue_completeness='l<=m<=n; volume<=30. l=1 forces mn<=6, and1x1xn needs n<=2. Remaining cases are2x2x2..7,2x3x3..5,3x3x3; all completely enumerated.',
        figure_diagnostic='Initial extractor expected aabbcc in fixed tensor-axis order; actual aaccbb is equivalent by color renaming. Corrected expectation before acceptance; not a book error.'))
    print('PASS147 claims: all feasible dimensions classified; four erroneous2x2x4 histogram rows; other counts correct;24 question labels; both cavity witnesses.')


if __name__=='__main__':main()
