"""Standalone F134 certificate; Python standard library only, no solver or data files.

Coordinates use basis (1,0),(1/2,sqrt(3)/2). A cell (x,y,0) is upward,
(x,y,1) downward. The three letters follow its corners counterclockwise.
Transcription: TAOCP 4B p454, answer140(c), third figure from the left.
Colors a,b,c,d are white,pink,blue,dark gray.
"""
from collections import defaultdict
from itertools import product
import json

TILES = [
    ((0,2,1),'aaa'), ((6,2,0),'bbb'), ((2,1,1),'ccc'), ((4,1,1),'ddd'),
    ((0,3,0),'aab'), ((1,2,0),'aca'), ((4,0,1),'daa'), ((6,1,1),'abb'),
    ((2,2,1),'bbc'), ((5,2,1),'bdb'), ((3,1,0),'cac'), ((2,2,0),'ccb'),
    ((5,0,1),'cdc'), ((4,1,0),'add'), ((5,2,0),'dbd'), ((5,1,0),'dcd'),
    ((6,1,0),'cab'), ((1,2,1),'bac'), ((1,3,0),'abd'), ((0,3,1),'dba'),
    ((5,0,0),'acd'), ((3,1,1),'dca'), ((3,2,0),'cdb'), ((5,1,1),'bdc'),
]


def check(tiles):
    canonical = lambda w: min(w,w[1:]+w[:1],w[2:]+w[:2])
    expected = {canonical(''.join(w)) for w in product('abcd',repeat=3)}
    assert len(expected)==24
    assert len(tiles)==24 and {canonical(w) for t,w in tiles}==expected
    assert len({t for t,w in tiles})==24
    colors = defaultdict(set)
    for (x,y,z),word in tiles:
        corners = [(x,y),(x+1,y),(x,y+1)] if z==0 else [(x+1,y+1),(x,y+1),(x+1,y)]
        for v,c in zip(corners,word):colors[v].add(c)
    return {v:sorted(cs) for v,cs in colors.items() if len(cs)>1}


def main():
    conflicts=check(TILES)
    assert conflicts=={(7,2):['a','b'],(7,1):['a','b']}
    fixes=[]
    for i,(cell,word) in enumerate(TILES):
        for shift in (1,2):
            changed=TILES.copy();changed[i]=(cell,word[shift:]+word[:shift])
            if not check(changed):fixes.append(dict(index=i,cell=cell,before=word,after=changed[i][1]))
    assert fixes==[dict(index=7,cell=(6,1,1),before='abb',after='bba')]
    print(json.dumps(dict(result='PASS',original_conflicts=[dict(vertex=v,colors=c) for v,c in sorted(conflicts.items())],
        all24_tile_types=True,tried_rotations=48,unique_fix=fixes[0],
        instruction='Rotate the rightmost downward-pointing triangle 120 degrees clockwise. White moves from its right corner to its bottom corner.'),indent=2))


if __name__=='__main__':main()
