"""Reproduce the empty-cycle input issue, stopping before the first ANS overrun.

This certifies the execution prefix, not the eventual behavior after code/data
corruption. Whether () is admitted by the input contract remains a review point.
"""
from pathlib import Path
import json
from mixal import Assembly
from mix_io import IOMachine
from mixal_permutation_a import program,LINES,cycle_tokens,cards_from_tokens
ROOT=Path(__file__).resolve().parent
runs=[]
for b in (64,65,100):
    a=Assembly(program(),b);m=IOMachine(b,17);a.load(m)
    m.inputs[16].extend(cards_from_tokens(cycle_tokens([[]])))
    line_at={loc:k for k,loc in zip(sorted(LINES),a.locations)}
    m.pc=a.start;seen_done=False
    while not m.halted:
        line=line_at.get(m.pc)
        seen_done |= line==48
        if line==72 and m.reg[1].value(b)>=2400:break
        m.step()
        assert m.steps<200000
    assert not m.halted and not seen_done
    assert line_at[m.pc]==72 and m.reg[1].value(b)==2400
    assert m.mem[0].sign==-1 and m.mem[1].sign==-1
    assert all(m.mem[k].digits==a.memory[a.symbols['EQUALS'].value(b)].digits for k in range(1202,2400))
    runs.append({'radix':b,'steps':m.steps,'time':m.time,'line':72,'next_write':2400,'answer_range':[1200,2399],
                 'output_phase_reached':False,'scope':'Stopped before overwriting OUTBUF; first1198 output names are equals signs.'})
(ROOT/'results/permutation-a-empty-cycle.json').write_text(json.dumps({'runs':runs,'status':'candidate pending input-domain interpretation','errata':'All four Volume1 layers searched by pages164-172 and ProgramA/identity/empty/parentheses; no applicable correction found.'},indent=2)+'\n')
print(json.dumps(runs))
