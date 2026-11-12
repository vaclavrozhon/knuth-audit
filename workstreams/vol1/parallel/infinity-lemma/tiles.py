"""Literal p385 Wang tiles. Every tuple is (north,south,west,east)."""
import sys
sys.dont_write_bytecode = True
from itertools import product

GREEK = {
 'A':('1','2','1','2'), 'B':('3','4','2','1'),
 'C':('2','1','3','4'), 'D':('4','3','4','3'),
}
BASIC = {
 'a':('Q','D','P','R'), 'b':('','','L','P'),
 'c':('U','Q','T','S'), 'd':('','','S','T'),
 'N':('Y','','X',''), 'J':('D','U','','X'), 'K':('','Y','R','L'),
 '_':('','','',''),
 **{x:('','',x,x) for x in 'RLPSTX'},
 **{x:(x,x,'','') for x in 'YUDQ'},
}

def expand(words):
    return {w:tuple(''.join(sorted(GREEK[w[0]][i]+''.join(BASIC[c][i] for c in w[1:])))
                    for i in range(4)) for w in words}

WORDS = []
def add(prefix,*groups):
    WORDS.extend(prefix+''.join(p).replace('_','') for p in product(*groups))
add('A','abcd')
add('BY','_UQ','PT')
add('B','_UDQ','PST')
add('BK','_UQ')
add('C','X_','LPST','_Q')
add('CR','_Q')
add('CJ','LPST')
add('DX','LPST','_Q')
add('DY','_UQ','PT')
add('DN','abcd')
add('DJ','LPST')
add('DK','_UQ')
add('D','RLPST','_UDQ')
TILES = expand(WORDS)
assert len(WORDS) == len(TILES) == len(set(TILES.values())) == 92

def valid(grid,tiles=TILES,wrap=False):
    h,w=len(grid),len(grid[0])
    for y in range(h):
        for x in range(w):
            t=tiles[grid[y][x]]
            if (wrap or x+1<w) and t[3]!=tiles[grid[y][(x+1)%w]][2]: return False
            if (wrap or y+1<h) and t[1]!=tiles[grid[(y+1)%h][x]][0]: return False
    return True

def rectangles(w,h,tiles=TILES,wrap=False):
    """Complete, finite row-major backtracking; no bound on caller's dimensions."""
    a=[None]*(w*h)
    ns={}; nw={}
    for name,t in tiles.items():
        ns.setdefault(t[0],[]).append(name)
        nw.setdefault(t[2],[]).append(name)
    def rec(i):
        if i==len(a):
            yield [a[j:j+w] for j in range(0,len(a),w)]; return
        y,x=divmod(i,w)
        cand=ns.get(tiles[a[i-w]][1],[]) if y else tiles
        if x:
            west=tiles[a[i-1]][3]
            cand=[t for t in cand if tiles[t][2]==west]
        for name in cand:
            t=tiles[name]
            if wrap and x==w-1 and t[3] != (tiles[a[i-x]][2] if x else t[2]):continue
            if wrap and y==h-1 and t[1] != (tiles[a[x]][0] if y else t[0]):continue
            a[i]=name; yield from rec(i+1)
    yield from rec(0)

def decide_under_periodicity_assumption(tiles):
    """Exercise4: total only if its stated (false in general) premise holds."""
    n=1
    while True:
        if next(rectangles(n,n,tiles),None) is None:return False,n
        if next(rectangles(n,n,tiles,wrap=True),None) is not None:return True,n
        n+=1

if __name__=='__main__':
    import json
    from pathlib import Path
    base=Path(__file__).parent
    counts={c:sum(w[0]==c for w in WORDS) for c in 'ABCD'}
    (base/'results/tiles92.json').write_text(json.dumps({'orientation':['N','S','W','E'],'classes':counts,'tiles':TILES},indent=2)+'\n')
    print(counts)
