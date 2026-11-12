"""Independent encodings and geometry for DLX87--90; ranks are zero-based here."""
from pathlib import Path

ROOT=Path(__file__).resolve().parent
DATA=ROOT/'sources/wordlists'
OUT=ROOT/'results/double_words'


def dictionary(n,ospd=False):
    name=f'words{n}-from-'+('sgb' if n==5 and not ospd else 'OSPD4')
    words=(DATA/name).read_text().upper().splitlines()
    assert len(set(words))==len(words) and all(len(w)==n for w in words)
    return words


def down_words(rows,kind):
    p,n=len(rows),len(rows[0])
    if kind=='square':return [''.join(row[j] for row in rows) for j in range(n)]
    return [''.join(rows[(i+j)%p][j if kind=='left' else n-1-j] for j in range(n)) for i in range(p)]


def orbit(rows,kind):
    rows=tuple(rows);p=len(rows);down=down_words(rows,kind)
    if kind=='square':return {rows,tuple(down)}
    other=tuple(down[-i%p] for i in range(p)) if kind=='left' else tuple(down)
    return {r[s:]+r[:s] for r in (rows,other) for s in range(p)}


def validate(rows,words,kind):
    p,n=len(rows),len(words[0]);rank={w:i for i,w in enumerate(words)}
    assert all(len(w)==n and w in rank for w in rows)
    if kind=='square':assert p==n
    down=down_words(rows,kind)
    assert all(w in rank for w in down),(rows,down)
    assert len(set(rows+down))==2*p,(rows,down)
    return max(rank[w] for w in rows+down)+1


def encoding(words,kind='square',period=None,symmetry=True):
    n=len(words[0]);p=n if kind=='square' else period
    primary=[f'a{i}' for i in range(p)]+[f'd{i}' for i in range(p)]
    cells=[f'{i}.{j}' for i in range(p) for j in range(n)]
    names=primary+cells+list(words)+([w+'@' for w in words] if symmetry else [])
    assert len(set(names))==len(names)
    number={name:i+1 for i,name in enumerate(names)}
    rows=[];info=[]
    for rank,w in enumerate(words):
        for slot in range(2*p):
            i=slot%p
            row=[(slot+1,0)]
            for j in range(n):
                if slot<p:cell=(i,j);c=w[j]
                elif kind=='square':cell=(j,i);c=w[j]
                else:cell=((i+j)%p,j);c=w[j] if kind=='left' else w[n-1-j]
                row.append((number[f'{cell[0]}.{cell[1]}'],ord(c)))
            row.append((number[w],0))
            if symmetry and (kind!='square' or slot in (0,p)):
                row.append((number[w+'@'],0))
            rows.append(tuple(row));info.append((slot,rank))
    return dict(names=names,primary=2*p,rows=rows,info=info,words=words,kind=kind,period=p)


def input_text(enc):
    names=enc['names'];p=enc['primary']
    return ' '.join(names[:p]+['|']+names[p:])+'\n'+''.join(
        ' '.join(names[i-1]+(':'+chr(c) if c else '') for i,c in row)+'\n'
        for row in enc['rows'])


def model_rows(model,enc):
    p=enc['period'];rows=[None]*p;down=[None]*p
    for r in model:
        slot,rank=enc['info'][r]
        (rows if slot<p else down)[slot%p]=enc['words'][rank]
    if enc['kind']=='right':
        # In the printed right-stair formula, across labels decrease as one
        # moves physically down the diagram. Convert both orientations.
        n=len(enc['words'][0])
        rows=[rows[-i%p] for i in range(p)]
        down=[down[(-i-n+1)%p] for i in range(p)]
    assert all(rows) and down==down_words(rows,enc['kind'])
    return rows


def geometric_models(words,kind,period):
    """Every ordered tuple of across words; used only on tiny test dictionaries."""
    from itertools import permutations
    wordset=set(words)
    for rows in permutations(words,period):
        down=down_words(rows,kind)
        if all(w in wordset for w in down) and len(set(rows+tuple(down)))==2*period:
            yield rows


SQUARES={2:'IS TO',3:'MAY AGE NOT',4:'SHOW NONE OPEN WEST',
  5:'START THREE ROOFS ASSET PEERS',6:'CHESTS LUSTRE OBTAIN ARENAS CIRCLE ASSESS',
  7:'HERTZES OPERATE MIMICAL ACERATE GENETIC ENDMOST RESENTS'}
LEFT=['WRITE WHOLE','MAKES LIVED WAXES','THERE SHARE WHOLE WHOSE',
  'STOOD THANK SHARE SHIPS STORE','WHERE SHEEP SMALL STILL WHOLE SHARE',
  'MAKES BASED TIRED WORKS LANDS LIVES GIVES','WATER MAKES LOVED GIVEN LAKES BASED NOTES TONES',
  'WHERE SHEET STILL SHALL WHITE SHAPE STARS WHOLE SHORE',
  'THERE SHOES SHIRT STONE SHOOK START WHILE SHELL STEEL SHARP']
RIGHT=['SPOTS','STALL SPIES','STOOD HOLES LEAPS','MIXED TEARS SLEPT SALAD',
  'YEARS STEAM SALES MARKS DRIED','STEPS SEALS DRAWS KNOTS TRAPS DROPS',
  'TRIED FEARS SLIPS SEAMS DRAWS ERECT TEARS',
  'YEARS STOPS HOOKS FRIED TEARS SLANT SWORD SWEEP',
  'START SPEAR SALES TESTS STEER SPEAK SKIES SLEPT SPORT',
  'YEARS STOCK HORNS FUELS BEETS SPEED TEARS PLANT SWORD SWEEP']
