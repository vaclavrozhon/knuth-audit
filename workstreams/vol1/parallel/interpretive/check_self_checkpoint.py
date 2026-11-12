"""A reachable checkpoint demonstrates a third trace level without replaying
the expensive already-correct outer interpretation prefix.
"""
from pathlib import Path
import json
from selftrace_program import assembly
from check_selftrace import record
from mix_io import IOMachine
from mix_machine import number

ROOT=Path(__file__).resolve().parent
results=[]
for b in (64,100):
    asm=assembly(b);sy={k:v.value(b) for k,v in asm.symbols.items()}
    d=IOMachine(b);asm.load(d)
    # OUT+19 is the physical OUT OUTBUF(18), after incrementing a nested tag.
    for _ in range(1000000):
        if d.pc==sy['OUT']+19:
            row=tuple(d.mem[sy['OUTBUF']:sy['OUTBUF']+24])
            if record(row,b)[0]==1:break
        d.step()
    else:raise AssertionError('checkpoint not reached')
    prefix_steps=d.steps;assert not d.devices
    m=IOMachine(b);asm.load(m)
    keys=sorted(d.writes);assert 2*len(keys)<=2000
    for i,k in enumerate(keys):
        m.mem[2*i]=number(k,b);m.mem[2*i+1]=d.mem[k]
    m.mem[sy['USED']]=number(2*len(keys),b)
    for r in range(8):
        m.mem[sy['AREG']+r]=number(d.reg[r].magnitude(b),b)
        m.mem[sy['SIGNA']+r]=number(d.reg[r].sign,b)
    for label,value in [('JREG',d.j),('COMPI',d.comparison),('OVTOG',int(d.overflow)),('CLOCK',d.time)]:
        m.mem[sy[label]]=number(value,b)
    m.reg[6]=number(d.pc,b);m.pc=sy['CYCLE']
    d.step();d._finish_input()
    m.step();m.run(m.pc,stop=sy['CYCLE'],limit=100000)
    records=[record(row,b) for row in m.outputs[18]]
    forwarded=[r for r in records if r[0]==2]
    assert len(forwarded)==1 and forwarded[0][1]==sy['BEGIN'],records
    ref=record(d.outputs[18][-1],b)
    assert forwarded[0]==(ref[0]+1,ref[1],ref[2])
    rr=[number(m.mem[sy['SIGNA']+r].value(b)*m.mem[sy['AREG']+r].magnitude(b),b,
               m.mem[sy['SIGNA']+r].value(b)) for r in range(8)]
    assert rr==d.reg and m.reg[6].value(b)==d.pc
    assert m.mem[sy['JREG']].value(b)==d.j
    results.append({'b':b,'checkpoint_reached_after_direct_steps':prefix_steps,
                    'checkpoint_dictionary_words':2*len(keys),'actual_MIX_steps_after_checkpoint':m.steps,
                    'third_level_record':{'level':2,'pc':forwarded[0][1],'word':str(forwarded[0][2])},
                    'note':'Reachable checkpoint constructed by direct execution of the identical MIX load image; no instruction hooks'})
(ROOT/'results/selftrace-checkpoint.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
