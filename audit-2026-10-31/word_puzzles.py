"""Word-placement and sudoku XCC inputs for DLX105--107; no search on import."""
from itertools import product
from puzzle_xcc import encode

WORDS105='ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN ELEVEN TWELVE'.split()
WORDS106='ONE TWO THREE FOUR FIVE'.split()
WORDS107='ACRE ART COMPARE COMPUTER CORPORATE CROP MACRO META MOTET PARAMETER ROAM TAME'.split()
ALPHABET107='ACEMOPRTU'
DIRECTIONS=[(di,dj) for di,dj in product([-1,0,1],repeat=2) if di or dj]


def placements(words,n,sudoku=False):
    result=[]
    for wi,word in enumerate(words):
        for i,j in product(range(n),repeat=2):
            for di,dj in DIRECTIONS:
                coords=[(i+di*k,j+dj*k) for k in range(len(word))]
                if not all(0<=r<n and 0<=c<n for r,c in coords):continue
                letters=tuple((r*n+c,letter) for (r,c),letter in zip(coords,word))
                if sudoku:
                    units=set();valid=True
                    for (r,c),letter in zip(coords,word):
                        for unit in [('r',r,letter),('c',c,letter),('b',3*(r//3)+c//3,letter)]:
                            if unit in units:valid=False
                            units.add(unit)
                    if not valid:continue
                result.append(dict(word=wi,start=[i,j],direction=[di,dj],letters=letters))
    return result


def instance(words,n,copies=1,sudoku=False):
    places=placements(words,n,sudoku)
    primary=[f'#{wi}c{copy}' for wi in range(len(words)) for copy in range(copies)]
    if sudoku:
        primary += [f'P{i}{j}' for i in range(9) for j in range(9)]
        primary += [f'{kind}{i}{letter}' for kind in 'RCB' for i in range(9) for letter in ALPHABET107]
    secondary=[f'c{cell}' for cell in range(n*n)]
    if copies>1:secondary += [f'm{k}' for k in range(len(places))]
    rows=[];row_info=[]
    for k,p in enumerate(places):
        for copy in range(copies):
            row=[(f'#{p["word"]}c{copy}',0)]
            row += [(f'c{cell}',ord(letter)-ord('A')+1) for cell,letter in p['letters']]
            if copies>1:row.append((f'm{k}',0))
            rows.append(row);row_info.append(dict(placement=k,copy=copy))
    if sudoku:
        for i,j,letter in product(range(9),range(9),ALPHABET107):
            b=3*(i//3)+j//3
            rows.append([(f'P{i}{j}',0),(f'R{i}{letter}',0),(f'C{j}{letter}',0),
                         (f'B{b}{letter}',0),(f'c{9*i+j}',ord(letter)-ord('A')+1)])
            row_info.append(dict(cell=9*i+j,letter=letter))
    enc=encode(primary,secondary,rows)
    return enc,places,row_info


def decode(model,places,row_info,n):
    board=['.']*(n*n);chosen=[]
    for ri in model:
        info=row_info[ri]
        if 'placement' in info:
            k=info['placement'];chosen.append(k);entries=places[k]['letters']
        else:entries=[(info['cell'],info['letter'])]
        for cell,letter in entries:
            assert board[cell] in ('.',letter)
            board[cell]=letter
    assert len(chosen)==len(set(chosen))
    return tuple(sorted(chosen)),''.join(board)


def orbit(board,n):
    def rotate(b):return ''.join(b[(n-1-j)*n+i] for i in range(n) for j in range(n))
    values=[]
    for b in [board,''.join(board[i*n+n-1-j] for i in range(n) for j in range(n))]:
        for _ in range(4):values.append(b);b=rotate(b)
    return set(values)


def components(chosen,places):
    unseen=set(chosen);number=0
    while unseen:
        stack=[unseen.pop()];number+=1
        while stack:
            cells={c for c,l in places[stack.pop()]['letters']}
            reached={k for k in unseen if cells & {c for c,l in places[k]['letters']}}
            unseen-=reached;stack.extend(reached)
    return number
