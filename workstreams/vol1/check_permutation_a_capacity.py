"""A valid two-cycle input whose disjoint-cycle answer needs more than1200 words."""
from pathlib import Path
import json,time
from mixal import Assembly,CHARACTERS
from mix_io import IOMachine
from mixal_permutation_a import program,LINES,cycle_tokens,cards_from_tokens
ROOT=Path(__file__).resolve().parent
started=time.monotonic();t=320
anames=[f'A{i:04d}' for i in range(1,t+1)];bnames=[f'B{i:04d}' for i in range(1,t+1)]
first=anames
second=[anames[0]]
for j in range(t-1,-1,-1):
    second.append(bnames[j])
    if j:second.append(anames[j])
# Independent composition of full mappings, before any MIX execution.
names=anames+bnames;perm={x:x for x in names}
for cycle in (first,second):
    mapping=dict(zip(cycle,cycle[1:]+cycle[:1]))
    perm={x:mapping.get(y,y) for x,y in perm.items()}
assert all(perm[a]==b and perm[b]==a for a,b in zip(anames,bnames))
tokens=cycle_tokens([first,second]);assert len(tokens)==3*t+4<1200
cards=cards_from_tokens(tokens);assert len(cards)==61
assembly=Assembly(program(),64);machine=IOMachine(64,0);assembly.load(machine)
machine.inputs[16].extend(cards);machine.pc=assembly.start
line_at={loc:k for k,loc in zip(sorted(LINES),assembly.locations)}
first_overrun=None;tail=[];exception=None;core_started=False
try:
    while not machine.halted and machine.steps<10000000:
        line=line_at.get(machine.pc)
        core_started |= line==23
        if line in (64,65,72,82) and machine.reg[1].value(64)>=2400 and first_overrun is None:
            first_overrun=dict(line=line,address=machine.reg[1].value(64),steps=machine.steps)
        tail.append((machine.steps,machine.pc,line,machine.reg[1].value(64)))
        if len(tail)>20:tail.pop(0)
        machine.step()
    machine.finish_io()
except Exception as exc:exception=repr(exc)
result=dict(t=t,input_nonblank_words=len(tokens),cards=len(cards),expected_answer_words=4*t,
    answer_allocation=[1200,2399],first_overrun=first_overrun,halted=machine.halted,
    instructions=machine.steps,exception=exception,tail=tail,output_blocks=len(machine.outputs[18]),
    expected_answer_rows=(4*t+23)//24,elapsed_seconds=time.monotonic()-started,
    named_addresses={k:assembly.symbols[k].value(64) for k in ['ANS','OUTBUF','BEGIN','OPEN','DONE','GO','START','SIZE']})
(ROOT/'results/permutation-a-capacity.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
