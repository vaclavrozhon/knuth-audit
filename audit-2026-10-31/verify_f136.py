"""Solver-free lower-bound certificate for the cylindrical count in DLX142(ii).

Only the standard library is used. Each line gives 24 cyclic four-sector words
in column-major order, starting at the lower left. Bottom two rows are corner
oriented, upper two rows edge oriented. Optional argument: another certificate.
"""
from itertools import product
from pathlib import Path
import gzip
import json
import sys


def canonical_colors(word):
    names={};result=[]
    for color in word:
        if color not in names:
            names[color]=chr(97+len(names))
        result.append(names[color])
    return ''.join(result)


def cyclic(word):
    return min(word[i:]+word[:i] for i in range(4))


def reflect(word):
    result=[]
    for x in range(6):
        for y in range(4):
            old=word[4*((5-x)*4+y):4*((5-x)*4+y+1)]
            order=[1,0,3,2] if y<2 else [0,3,2,1]
            result.extend(old[i] for i in order)
    return canonical_colors(''.join(result))


def main():
    path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent/'results/octagons142/f136-5981-classes.txt.gz'
    inventory={cyclic(''.join(word)) for word in product('abc',repeat=4)}
    assert len(inventory)==24
    seen=set()
    with gzip.open(path,'rt') as source:
        for line in source:
            word=line.strip()
            assert len(word)==96 and set(word)==set('abc') and canonical_colors(word)==word
            tiles=[word[i:i+4] for i in range(0,96,4)]
            assert {cyclic(tile) for tile in tiles}==inventory
            sides={}
            for x in range(6):
                for y in range(4):
                    a,b,c,d=tiles[4*x+y]
                    # bottom/right/top/left, all read in increasing coordinates.
                    sides[x,y]=((a,b),(b,c),(d,c),(a,d)) if y<2 else ((a,a),(b,b),(c,c),(d,d))
            for x in range(6):
                for y in range(4):
                    bottom,right,top,left=sides[x,y]
                    assert right==sides[(x+1)%6,y][3]
                    if y<3:
                        assert top==sides[x,y+1][0]
            mate=reflect(word)
            assert mate!=word and reflect(mate)==word
            assert word<mate and word not in seen
            seen.add(word)
    # This proves only a lower bound. Exhaustiveness belongs to the two censuses.
    assert len(seen)>=5981 and 2*len(seen)>2*5980
    print(json.dumps(dict(status='PASS',geometric_classes=len(seen),
        proven_lower_bound_after_color_permutations=2*len(seen),
        printed_bound=2*5980,strict_counterexample=True,search_performed=False,
        exhaustive_upper_bound_claimed=False),indent=2))


if __name__=='__main__':
    main()
