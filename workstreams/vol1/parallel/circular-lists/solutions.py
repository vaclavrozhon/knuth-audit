"""Independently written executable MIX solutions to exercises 11,13--15.

COPY2 allocates a head first, then appends copies; ZERO2 does not use MOVE.
MULT2 caches the multiplier term and avoids multiplying the sentinel. As
required by exercise 15 it calls the printed ADD through its three switches.
Input/source and destination polynomials are disjoint; P=M is also allowed.
"""
import sys
sys.dont_write_bytecode=True
from programs import rows,assembly,symbols,number


OWN=rows('''
ZERO2|STJ|Z2RET
|LD2|AVAIL
|J2Z|OVERFLOW
|LDX|1,2(LINK)
|STX|AVAIL
|STZ|0,2
|LDA|Z2SENT
|STA|1,2
|ST2|1,2(LINK)
Z2RET|JMP|*
Z2SENT|CON|-1(ABC)
COPY2|STJ|C2RET
|JMP|ZERO2
|ENT3|0,2
|LD4|1,1(LINK)
C2LOOP|LDA|1,4(ABC)
|JAN|C2END
|LD6|AVAIL
|J6Z|OVERFLOW
|LDX|1,6(LINK)
|STX|AVAIL
|LDA|0,4
|STA|0,6
|LDA|1,4
|STA|1,6
|ST6|1,3(LINK)
|ENT3|0,6
|LD4|1,4(LINK)
|JMP|C2LOOP
C2END|ST2|1,3(LINK)
C2RET|JMP|*
ERASE2|STJ|E2RET
|LD2|1,1(LINK)
|LDX|AVAIL
|ST2|AVAIL
|STX|1,1(LINK)
E2RET|JMP|*
MULT2|STJ|M2RET
|LDA|M2NEW1
|STA|SW1
|LDA|M2NEW2
|STA|SW2
|STA|SW3
M2NEXT|LD4|1,4(LINK)
|LDA|1,4(ABC)
|JAN|M2END
|STA|M2EXP
|LDA|0,4
|STA|M2COEF
|JMP|ADD
|JMP|M2NEXT
M2END|LDA|MOLD1
|STA|SW1
|LDA|MOLD2
|STA|SW2
|STA|SW3
M2RET|JMP|*
M2BUILD|LDA|1,1(ABC)
|JAN|M2SENT
|ADD|M2EXP
|SLA|2
|STA|M2ABC
|LDA|0,1
|MUL|M2COEF
|STX|M2PROD
|LDA|M2ABC
|JMP|SW1+1
M2SENT|SLA|2
|JMP|SW1+1
M2NEW1|JMP|M2BUILD
M2NEW2|LDA|M2PROD
M2EXP|CON|0
M2COEF|CON|0
M2ABC|CON|0
M2PROD|CON|0
''')


def run():
    from check_mix import Fixture,add,mul
    import json,random
    from pathlib import Path
    rng=random.Random(224)
    counts={'copy':0,'erase':0,'zero':0,'mult':0,'pm_alias':0,'refill':0}
    for b in range(64,101):
        for k in range(21):
            polys=[{e:rng.choice([-3,-1,1,3]) for e in rng.sample(range(8),k%6)} for j in range(3)]
            p,q,m=polys
            f=Fixture(b,extra=OWN);ph=f.polynomial(p);qh=f.polynomial(q);mh=f.polynomial(m)
            original=f.m.mem[:]
            f.call('COPY2',[(1,ph)]);ch=f.m.reg[2].value(b)
            assert f.read(ch)[0]==p and f.m.reg[1].value(b)==ph
            f.partition([ph,qh,mh,ch]);counts['copy']+=1
            f.call('ERASE2',[(1,ch)]);f.partition([ph,qh,mh]);counts['erase']+=1
            f.call('ZERO2');zh=f.m.reg[2].value(b)
            assert f.read(zh)[0]=={};f.partition([ph,qh,mh,zh]);counts['zero']+=1
            f.call('MULT2',[(1,ph),(2,qh),(4,mh)])
            assert [f.m.reg[r].value(b) for r in [1,2,4]]==[ph,qh,mh]
            assert f.read(qh)[0]==add(q,mul(p,m));f.partition([ph,qh,mh,zh]);counts['mult']+=1
            for sw in ['SW1','SW2','SW3']:assert f.m.mem[f.s[sw]]==original[f.s[sw]]
            for h in [ph,mh]:
                for a in f.read(h)[1]:assert f.m.mem[a:a+2]==original[a:a+2]
            f.call('MULT2',[(1,ph),(2,qh),(4,ph)])
            assert f.read(qh)[0]==add(add(q,mul(p,m)),mul(p,p));counts['pm_alias']+=1
            f.partition([ph,qh,mh,zh])
        for op in ['COPY2','ZERO2','MULT2']:
            f=Fixture(b,overflow='refill',pool_count=0,extra=OWN)
            ph=f.polynomial({0:1,1:-1});qh=f.polynomial({});mh=f.polynomial({0:2})
            f.pool=list(range(3000,3020,2));f.chain(f.pool);f.m.mem[51]=number(3000,b)
            f.call(op,[(1,ph),(2,qh),(4,mh)])
            assert not f.m.halted
            if op=='MULT2':assert f.read(qh)[0]=={0:2,1:-2};f.partition([ph,qh,mh])
            else:
                nh=f.m.reg[2].value(b)
                assert f.read(nh)[0]==({0:1,1:-1} if op=='COPY2' else {})
                f.partition([ph,qh,mh,nh])
            counts['refill']+=1
    out=Path(__file__).resolve().parent/'results'
    (out/'own-solutions.json').write_text(json.dumps({'counts':counts,'radices':list(range(64,101))},indent=2)+'\n')
    # Complete symbolic listings are reviewable independently of Python.
    for b in [64,100]:
        a=assembly(b,extra=OWN)
        listing='\n'.join(f'{label:12} {op:6} {operand}' for label,op,operand in OWN)+'\n'
        (out/f'own-solutions-{b}.mixal').write_text(listing)
        (out/f'combined-words-{b}.json').write_text(json.dumps({
            'symbols':symbols(a),'words':{k:[v.sign,*v.digits] for k,v in a.memory.items()}
        },indent=2)+'\n')
    print(json.dumps(counts))


if __name__=='__main__':run()
