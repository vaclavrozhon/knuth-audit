"""Geometric validation of every original solution figure in108--112."""
from collections import Counter
from itertools import product
import json
from layout_native import ROOT,OUT,save,sha
from wordcross109 import WORDS
from word_puzzles import orbit
from torto112 import paths,validate_path

PRESIDENTS='ADAMS ARTHUR BUCHANAN BUSH CARTER CLEVELAND CLINTON COOLIDGE EISENHOWER FILLMORE FORD GARFIELD GRANT HARDING HARRISON HAYES HOOVER JACKSON JEFFERSON JOHNSON KENNEDY LINCOLN MADISON MCKINLEY MONROE NIXON OBAMA PIERCE POLK REAGAN ROOSEVELT TAFT TAYLOR TRUMAN TYLER VANBUREN WASHINGTON WILSON'.split()


def components(sets):
    groups=[{i} for i in range(len(sets))]
    for i in range(len(sets)):
        for j in range(i):
            if sets[i]&sets[j]:
                merged=groups[i]|groups[j]
                for k in merged:groups[k]=merged
    return len({tuple(sorted(g)) for g in groups})


def wordcross(grid,expected):
    m,n,b=grid['m'],grid['n'],grid['board'];found=[]
    for direction in [0,1]:
        dr,dc=[(0,1),(1,0)][direction]
        for r,c in product(range(m),range(n)):
            if b[r*n+c]=='.':continue
            if r-dr>=0 and c-dc>=0 and b[(r-dr)*n+c-dc]!='.':continue
            cells=[];rr,cc=r,c
            while rr<m and cc<n and b[rr*n+cc]!='.':
                cells.append(rr*n+cc);rr+=dr;cc+=dc
            if len(cells)>1:found.append(dict(word=''.join(b[k] for k in cells),direction=direction,cells=cells))
    assert Counter(p['word'] for p in found)==Counter(expected),(m,n,Counter(p['word'] for p in found)-Counter(expected),Counter(expected)-Counter(p['word'] for p in found))
    assert set().union(*(set(p['cells']) for p in found))=={k for k,c in enumerate(b) if c!='.'}
    return dict(m=m,n=n,placements=found,components=components([set(x['cells']) for x in found]))


def main():
    original=json.loads((OUT/'original-figures.json').read_text());pres=[]
    assert len(PRESIDENTS)==38==len(set(PRESIDENTS))
    for g in original['presidential']:
        m,n,b=g['m'],g['n'],g['board'];allpositions=[]
        for word in PRESIDENTS:
            for r,c in product(range(m),range(n)):
                for dr,dc in product([-1,0,1],repeat=2):
                    if dr==dc==0:continue
                    rr,cc=r+dr*(len(word)-1),c+dc*(len(word)-1)
                    if not (0<=rr<m and 0<=cc<n):continue
                    cells=tuple((r+dr*k)*n+c+dc*k for k in range(len(word)))
                    if ''.join(b[k] for k in cells)==word:allpositions.append((word,cells))
        printed=[]
        for oval in g['ovals']:
            matched=[(w,c) for w,c in allpositions if set(c)==set(oval)]
            assert len(matched)==1,(oval,matched)
            printed.append(dict(word=matched[0][0],cells=matched[0][1]))
        assert Counter(x['word'] for x in printed)==Counter(PRESIDENTS)
        assert components([set(x['cells']) for x in printed])==1
        pres.append(dict(m=m,n=n,placements=printed,connected=True))
    cross=[]
    for i,g in enumerate(original['wordcross']):
        expected=WORDS if i<6 else [w for p in PRESIDENTS for w in (['VAN','BUREN'] if p=='VANBUREN' else [p])]
        result=wordcross(g,expected)
        if 0<i<6:
            d=json.loads((OUT/f"wordcross109-{g['m']}x{g['n']}-decoded.json").read_text())
            assert any(p['board']==g['board'] for p in d['placements'])
        cross.append(result)
    assert [x['components'] for x in cross]==[3,1,1,1,1,2,1]
    diagram=[]
    for i,g in enumerate(original['diagrams']):
        b=g['board'];case='a' if i<2 else 'b'
        target={3:12,4:12,5:4} if case=='a' else {2:8,5:12,8:4}
        expected=['A'*length for length,count in target.items() for _ in range(count)]
        result=wordcross(dict(m=8,n=8,board=b),expected)
        independent=json.loads((OUT/f'diagrams111-{case}.json').read_text())
        bits=sum((c=='A')<<k for k,c in enumerate(b))
        assert bits in independent['boards']
        diagram.append(dict(case=case,board=b,components=result['components'],canonical=min(orbit(b,8))))
    for case in ['a','b']:
        independent=json.loads((OUT/f'diagrams111-{case}.json').read_text())
        classes={min(orbit(''.join('A' if bits>>k&1 else '.' for k in range(64)),8)) for bits in independent['boards']}
        assert classes=={x['canonical'] for x in diagram if x['case']==case}
    boards=[g['board'] for g in original['torto']]
    requested=[
        'THE MATURE ART OF COMPUTER PROGRAMMING IMMATURE MATURING COMMUTER GROUPING TROUPING AUTHORING THRUMMING'.split(),
        'DANCING LINKS TORTO WORDS SOLVER LOVER ROSIN SALVO TOADS TROVE ASKING DOSING LOSING ORDAIN SAILOR SIGNAL SILVER LANCING LOANING SOAKING ORTOLAN'.split(),
        'ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN'.split(),
        'ZERO ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT'.split(),
        'FIRST SECOND THIRD FOURTH FIFTH SIXTH'.split()
    ]
    torto=[]
    for board,words in zip(boards,requested):
        checked={w:paths(board,w) for w in words}
        assert all(checked.values()),[w for w,ps in checked.items() if not ps]
        for word,allpaths in checked.items():
            for path in allpaths:validate_path(board,word,path)
        torto.append(dict(board=board,paths=checked))
    assert len(torto[1]['paths']['TORTO'])==2
    dictionary=(ROOT/'sources/sgb-words.txt').read_text().split();assert len(dictionary)==5757
    extras={w.upper():paths(boards[1],w.upper()) for w in dictionary};extras={w:p for w,p in extras.items() if p}
    assert len(extras)==24,len(extras)
    corrected='YTE'+boards[4][3:]
    corrections={w:paths(corrected,w) for w in requested[4]+['FIFTY','SIXTY']}
    assert all(corrections.values())
    save(OUT/'figures-checked.json',dict(script_sha256=sha(__file__),source_figure_hash=sha(OUT/'original-figures.json'),
        presidential=pres,wordcross=cross,diagrams=diagram,torto=torto,torto_five_letter_words=extras,
        corrected_ordinal_board=corrected,corrected_ordinal_paths=corrections,
        known_erratum='Rightmost Torto first rowETV becomesYTE, April8,2023.'))
    print('All76 presidential ovals connected;7 wordcross grids,6 complete diagram classes,5 Torto grids valid;24 dictionary words.')


if __name__=='__main__':main()
