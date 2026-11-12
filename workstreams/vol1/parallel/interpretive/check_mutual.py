"""A fully specified pair of the printed tracers, exercise1.4.3.2-5.

All mutable cells, registers, PC, J and flags are included in the repeated
state. Time is excluded because this example has no I/O or time input.
Thus an equal state certifies the subsequent periodic execution.
"""
from pathlib import Path
import json
from programs import tracer
from mix_machine import Machine,instruction,number

ROOT=Path(__file__).resolve().parent
results=[]
for b in range(64,101):
    a,z=tracer(b,1000),tracer(b,2000)
    sa={k:v.value(b) for k,v in a.symbols.items()}
    sz={k:v.value(b) for k,v in z.symbols.items()}
    m=Machine(b);a.load(m);z.load(m)
    # Outer A traces the entry to B. The two jumps arrange J=A.ENTER
    # when B starts, so that B in turn traces A.ENTER.
    m.mem[1998]=instruction(b,'ENTX',sa['LEAVEX'])
    m.mem[1999]=instruction(b,'JMP',999)
    m.mem[999]=instruction(b,'JMP',sz['ENTER'])
    m.j=1998;m.reg[7]=number(sz['LEAVEX'],b);m.pc=sa['ENTER']
    seen={};cycles=[];cross=[];outcome=None
    for k in range(10000):
        if m.pc==sa['CYCLE']:
            cycles.append(m.reg[0].value(b))
            key=(m.pc,tuple(m.reg),m.j,m.overflow,m.comparison,
                 tuple(m.mem[999:1047]),tuple(m.mem[1998:2047]))
            if key in seen:
                outcome={'period_steps':k-seen[key],'first':seen[key],'end':k};break
            seen[key]=k
        if m.pc==sa['INST']:
            w=m.mem[m.pc];addr=w.sign*(w.digits[0]*b+w.digits[1])
            if w.digits[2]:addr+=m.reg[w.digits[2]].value(b)
            if 24<=w.digits[4]<=33 and 1000<=addr<1047:
                p=m.mem[sa['PREG']]
                cross.append({'step':k,'outer_guest_pc':p.digits[0]*b+p.digits[1],
                              'target':addr,'op':w.digits[4]})
        m.step()
    assert outcome=={'period_steps':82,'first':2539,'end':2621},(b,outcome)
    assert cross[0]=={'step':486,'outer_guest_pc':2030,'target':1006,'op':31}
    assert m.writes<=set(range(1000,1047))|set(range(2000,2047)),m.writes
    results.append({'b':b,'outcome':outcome,'crosswrites':cross,
                    'outer_guest_pcs_first100':cycles[:100]})
(ROOT/'results/mutual_trace.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({'radices':len(results),'outcome':results[0]['outcome'],
                  'first_crosswrite':results[0]['crosswrites'][0]},indent=2))
