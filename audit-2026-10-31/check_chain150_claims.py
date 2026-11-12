"""Bind parity and corrected counts; distinguish paths with/without the frame."""
from collections import Counter
from datetime import datetime,timezone
import json,re
import chain150 as h
from verify_f139 import PORTS,LENGTHS


def frame_key(graph):
    keys=[]
    for k in range(4):
        mapped=[]
        def turn(p):
            for _ in range(k):p=7-p[1],p[0]
            return p
        for p,ns in graph.items():mapped.append((turn(p),tuple(sorted(turn(q) for q in ns))))
        keys.append(tuple(sorted(mapped)))
    return min(keys)


def illustration(pieces):
    unit=25;parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1150" height="330" viewBox="0 0 1150 330">',
        '<rect width="1150" height="330" fill="#f7f9fc"/>',
        '<g font-family="Arial,sans-serif" fill="#17243a">',
        '<text x="30" y="34" font-size="22" font-weight="bold">F139: the printed inventory cannot close</text>',
        '<text x="30" y="62" font-size="15">Only strips 3, 14 and 17 have an odd number of horizontal path ends.</text>']
    for row in range(2):
        x=30;y=105+100*row
        for i in range(9*row,9*row+9):
            p=pieces[i];n=LENGTHS[i];odd=i in [2,13,16];color='#b85a00' if odd else '#243950'
            parts.append(f'<rect x="{x}" y="{y}" width="{n*unit}" height="{unit}" fill="'+('#fff0cc' if odd else '#fff')+f'" stroke="{color}" stroke-width="1.5"/>')
            for xx in range(1,n):parts.append(f'<path d="M {x+xx*unit},{y} v {unit}" stroke="#dde3ed"/>')
            for (a,b),v in p.items():
                cx=x+(a+.5)*unit;cy=y+(b+.5)*unit
                for j,c in enumerate(v):
                    if c:
                        dx,dy=h.DIRS[j];dash=' stroke-dasharray="3 2"' if c==2 else ''
                        parts.append(f'<path d="M {cx},{cy} l {dx*unit/2},{dy*unit/2}" stroke="{color}" stroke-width="2.5"{dash}/>')
            H=sum(c in 'WE' for c in PORTS[i]);V=sum(c in 'NS' for c in PORTS[i])
            parts.append(f'<text x="{x}" y="{y-10}" font-size="14">{i+1}</text><text x="{x}" y="{y+45}" font-size="12">H={H}, V={V}</text>')
            x+=n*unit+20
    parts+=['<text x="30" y="285" font-size="15">A quarter turn swaps H and V; their parity is equal on every strip. The total stays odd.</text>',
        '<text x="30" y="311" font-size="13">Center paths shown. Each join pairs two ends. Dashed ends are the unique special connection.</text></g></svg>']
    (h.ROOT/'images/f139-parity.svg').write_text('\n'.join(parts)+'\n')


def main():
    pieces,_=h.inventory();ex=json.loads((h.OUT/'strips-extracted.json').read_text())
    assert ex['extractor_sha256']==h.sha(h.ROOT/'extract_chain150.py')
    assert [sorted(c['side'] for c in p['contacts']) for p in ex['pieces']]==[sorted(s) for s in PORTS]
    odd=[];turns=0
    for i,p in enumerate(pieces):
        parities=[]
        for k in range(4):
            q=h.rotate(p,k)
            ends=[j for (x,y),v in q.items() for j,(dx,dy) in enumerate(h.DIRS) if v[j] and (x+dx,y+dy) not in q]
            parities.append(sum(j in [1,3] for j in ends)%2)
        assert len(set(parities))==1
        if parities[0]:odd.append(i+1)
        for v in p.values():
            nz=[i for i,c in enumerate(v) if c]
            if len(nz)==2 and (nz[0]-nz[1])%2:turns+=1
    assert odd==[3,14,17] and turns==21
    data=json.loads((h.OUT/'corrected-census/checked.json').read_text());assert data['count']==43 and data['all_models_valid']
    assert data['geometry_sha256']==h.sha(h.__file__) and data['checker_sha256']==h.sha(h.ROOT/'check_chain150_census.py')
    assert data['terminal_sha256']==h.sha(h.OUT/'corrected-census/corrected-all.json')
    figs=json.loads((h.OUT/'figures-checked.json').read_text());_,options=h.placements(corrected=True)
    hist=Counter();maps={};translation=Counter()
    for m in data['models']:
        graph,components=h.validate([options[i] for i in m],corrected=True);assert components==[34]
        fk=frame_key(graph);hist[fk]+=1;maps[tuple(m)]=fk;translation[h.path_key(graph)]+=1
    occurrences=[hist[maps[tuple(figs['figures']['original'+str(i)]['normalized_model'])]] for i in range(4)]
    assert len(hist)==8 and occurrences==[1,15,9,3] and sorted(hist.values())==[1,1,2,3,5,7,9,15]
    assert len(translation)==7
    previous=json.loads((h.ROOT/'results/polygons143/errata-check.json').read_text());contexts=[]
    pattern=r'(?:[Pp]age\s+|(?:4b|4f5)\.)(?:143|458|459|141|266|267)\b|(?:answer|exercise|exer ise)\s+150\b|Endless|super.piece|43 solutions|18 positions'
    for p,d in previous['files'].items():
        source=h.ROOT.parent/p;assert h.sha(source)==d
        lines=source.read_text(errors='replace').splitlines()
        for i,line in enumerate(lines):
            if re.search(pattern,line,re.I):contexts.append(dict(file=p,line=i+1,context='\n'.join(lines[max(0,i-1):i+5])))
    h.save(h.OUT/'errata-check.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),files=previous['files'],pattern=pattern,contexts=contexts,
        latest_remote_retrieval='2026-11-03T05:37:34Z; six unchanged hashes from143',conclusion='No matching correction to150 inventory. Adjacent151/152 errata are separate.'))
    illustration(pieces)
    h.save(h.OUT/'claims-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=h.sha(__file__),
        geometry_sha256=h.sha(h.__file__),standalone_sha256=h.sha(h.ROOT/'verify_f139.py'),odd_strips_one_based=odd,
        literal_count_proved_zero=True,literal_searches=0,total_turn_cells=turns,corrected_count=43,
        frame_path_classes=8,figure_occurrences=occurrences,path_histogram=[dict(path=k,count=v) for k,v in sorted(hist.items())],
        translation_classes=7,translation_explanation='Two frame positions of the same path shape are separate in the book. Suppressing translations gives7 and merges3+1 occurrences of pathiv. This is not a numerical erratum.',
        all43_single_loops_of_length34=True,corrected_census_sha256=h.sha(h.OUT/'corrected-census/checked.json'),
        figures_sha256=h.sha(h.OUT/'figures-checked.json'),errata_sha256=h.sha(h.OUT/'errata-check.json'),illustration_sha256=h.sha(h.ROOT/'images/f139-parity.svg')))
    print('PASS150:literal0 by parity; corrected43,8 frame paths,[1,15,9,3];7 translation classes are a different convention. F139 only.')


if __name__=='__main__':main()
