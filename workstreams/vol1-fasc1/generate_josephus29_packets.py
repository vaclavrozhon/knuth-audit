#!/usr/bin/env python3
"""Generate immutable per-person MMIX packets with mutable global successors.

The already proved complete Fenwick formatter is copied unchanged.
No assembly or execution is performed by this generator.
"""
from pathlib import Path

BASE=Path(__file__).resolve().parent


def generate(n=24,m=11):
    assert 1<=n<=219 and 1<=m<2**64
    lines=[
        '% Immutable Ingalls-style MMIX packets; successors live in distinct GREG0 registers.',
        '% The emitted program supports its chosen1<=N<=219 and unsigned1<=M<2^64.',
        f'N       IS      {n}',f'M       IS      {m}',
        '        LOC     Data_Segment','Order   GREG    @',
        '        LOC     @+4*N','Buf     GREG    @',
        '        LOC     @+11*N+1','n       GREG    N','m       GREG    M',
    ]
    lines += [f'Next{i} GREG 0' for i in range(1,n+1)]
    names=['zero','left','step','count','prev','successor','victim','tmp',
           'off','width','person','outoff','end','digits','char','value','t']
    lines += [f'{name:<9} IS      ${i}' for i,name in enumerate(names)]
    lines += ['        LOC     #100','Main    SET     zero,0']
    lines += [f'        GETA    Next{i},Entry{i%n+1}' for i in range(1,n+1)]
    lines += [
        '        SET     left,n','        SET     step,1','        SET     count,m',
        f'        GETA    prev,Update{n}','        JMP     Entry1',
        'Remove  SUB     tmp,victim,1','        SLU     off,tmp,2',
        '        STTU    step,Order,off','        SUB     left,left,1',
        '        BZ      left,Done','        INCL    step,1','        SET     count,m',
        '        GO      $255,prev,0',
    ]
    template=(BASE/'sources/josephus29-fenwick.mms').read_text().splitlines()
    start=next(i for i,line in enumerate(template) if line.startswith('Done '))
    lines += template[start:]
    for i in range(1,n+1):
        lines += [
            f'Entry{i} SUBU count,count,1',f'        PBNZ    count,Continue{i}',
            f'        SET     successor,Next{i}',f'        SET     victim,{i}',
            '        JMP     Remove',f'Continue{i} GO prev,Next{i},0',
            f'Update{i} SET Next{i},successor',f'        JMP     Continue{i}',
        ]
    return '\n'.join(lines)+'\n'


if __name__=='__main__':
    (BASE/'sources/josephus29-packets.mms').write_text(generate())
