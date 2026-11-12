"""Finite local lemmas used in the general desubstitution proof of exercise5."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from collections import Counter
from itertools import product
import json
from tiles import TILES, GREEK, BASIC, expand, rectangles, valid, decide_under_periodicity_assumption

BASE=Path(__file__).parent
REV={t:w for w,t in TILES.items()}
H=dict(zip('abcd','badc')); V=dict(zip('abcd','cdab'))
def macro(block):
    g=dict(zip('abcd','ABCD'))[block[0][0][1]]
    suffix=block[1][1][2:] if g=='A' else block[1][1][1:]
    w=g+suffix
    return REV.get(expand([w])[w])

def inflate(grid,sub):
    out=[[None]*(2*len(grid[0])+1) for _ in range(2*len(grid)+1)]
    for y,row in enumerate(grid):
        for x,t in enumerate(row):
            for j,r in enumerate(sub[t]):
                for i,q in enumerate(r):
                    old=out[2*y+j][2*x+i]
                    assert old is None or old==q
                    out[2*y+j][2*x+i]=q
    assert valid(out)
    return out

def main():
    candidates=[]
    for a in rectangles(3,3):
        if not a[0][0].startswith('A'):continue
        z=a[0][0][1]
        if [a[0][2],a[2][0],a[2][2]]!=['A'+H[z],'A'+V[z],'A'+V[H[z]]]:continue
        candidates.append(a)
    assert len(candidates)==104
    (BASE/'results/blocks3.json').write_text(json.dumps(candidates,indent=2)+'\n')
    good=[a for a in candidates if macro(a) is not None]
    bad=[a for a in candidates if macro(a) is None]
    assert len(good)==92 and len(bad)==12
    sub={macro(a):a for a in good}
    assert len(sub)==92 and set(sub)==set(TILES)
    forbidden=[]
    for a in bad:
        counts=[sum([r[-1] for r in b]==[r[0] for r in a] for b in candidates),
                sum([r[-1] for r in a]==[r[0] for r in b] for b in candidates),
                sum(b[-1]==a[0] for b in candidates),sum(a[-1]==b[0] for b in candidates)]
        assert 0 in counts
        forbidden.append({'corner':a[0][0],'center':a[1][1],'neighbor_counts_W_E_N_S':counts})
    pairs=0
    for a in good:
        for b in good:
            for d in ['h','v']:
                match=([r[-1] for r in a]==[r[0] for r in b]) if d=='h' else a[-1]==b[0]
                ca,cb=TILES[macro(a)],TILES[macro(b)]
                eq=ca[3]==cb[2] if d=='h' else ca[1]==cb[0]
                assert match==eq,(macro(a),macro(b),d)
                pairs+=1
    # A second validator uses raw four strings, not the backtracking constraints.
    inflation=[]
    for seed in TILES:
        grid=[[seed]]
        for level in range(1,5):
            grid=inflate(grid,sub)
            assert valid(grid)
        inflation.append({'seed':seed,'side':len(grid)})
    grid=[['Aa']]
    for _ in range(7):grid=inflate(grid,sub)
    closed={'Aa'}
    while True:
        nxt=closed|{t for p in closed for row in sub[p] for t in row}
        if nxt==closed:break
        closed=nxt
    omitted=sorted(set(TILES)-closed)
    assert len(closed)==86
    # Exercise6 exact finite number W(2,3)=9.
    good_colorings={}
    for n in range(10):
        cs=[]
        for c in product(range(2),repeat=n):
            if not any(c[a]==c[a+d]==c[a+2*d] for d in range(1,n) for a in range(n-2*d)):
                cs.append(''.join(map(str,c)))
        good_colorings[n]=cs
    assert good_colorings[8] and not good_colorings[9]
    # Main-text six types and three impossible types, transcribed from images.
    six={str(i):t for i,t in enumerate([
        ('1','2','3','1'),('11','12','1','2'),('21','22','2','3'),
        ('2','1','13','11'),('12','11','11','12'),('22','21','12','13')])}
    three={str(i):t for i,t in enumerate([('1','2','3','1'),('1','1','1','2'),('2','2','2','3')])}
    assert valid([['0','1','2'],['3','4','5']],six,True)
    assert len(list(rectangles(3,2,three)))==0
    verdicts={'six':decide_under_periodicity_assumption(six),'three':decide_under_periodicity_assumption(three)}
    assert verdicts=={'six':(True,6),'three':(False,3)}
    # Known repaired7x7 figure; compare every literal side.
    fig=[
        'Aa BKQ Ab BQP Aa BK Ab',
        'CJP DNa CR DKQ CJL DNb CP',
        'Ac BDS Ad BYQT Ac BS Ad',
        'CPQ DJP CXP DNa CRQ DR CR',
        'Aa BKU Ab BDP Aa BK Ab',
        'CJT DNc CS DSD CJS DNd CT',
        'Ac BQS Ad BDT Ac BS Ad']
    canon=lambda w:REV[expand([w])[w]]
    fig=[[canon(w) for w in r.split()] for r in fig]
    assert valid(fig)
    (BASE/'results/substitution-blocks.json').write_text(json.dumps(sub,indent=2)+'\n')
    (BASE/'results/inflated-255.json').write_text(json.dumps(grid)+'\n')
    (BASE/'results/tiles92.json').write_text(json.dumps({'orientation':['N','S','W','E'],'tiles':TILES},indent=2)+'\n')
    result={'candidate_blocks':len(candidates),'allowed_blocks':len(good),'forbidden':forbidden,
            'edge_equivalence_checks':pairs,'all_seeds_inflated':inflation,'largest_square':len(grid),
            'W23_counts':{n:len(cs) for n,cs in good_colorings.items()},'W23_length8':good_colorings[8],
            'main_example_decisions':verdicts,'corrected_figure_valid':True}
    result['closed_inflation_alphabet']=sorted(closed)
    result['six_omittable']=omitted
    (BASE/'results/tiles-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['all_seeds_inflated','forbidden']},indent=2))

if __name__=='__main__':main()
