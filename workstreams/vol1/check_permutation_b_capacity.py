"""Stop before Program B's first out-of-allocation answer write on valid input."""
from pathlib import Path
import json,time
from mixal import Assembly
from mix_io import IOMachine
from mixal_permutation_a import cycle_tokens,cards_from_tokens
from mixal_permutation_b import program,LINES
ROOT=Path(__file__).resolve().parent
started=time.monotonic();t=320
anames=[f'A{k:04d}' for k in range(1,t+1)];bnames=[f'B{k:04d}' for k in range(1,t+1)]
second=[anames[0]]
for k in range(t-1,-1,-1):
    second.append(bnames[k])
    if k:second.append(anames[k])
cards=cards_from_tokens(cycle_tokens([anames,second]));assert len(cards)==61
assembly=Assembly(program(),64);m=IOMachine(64);assembly.load(m);m.inputs[16].extend(cards);m.pc=assembly.start
line_at={p:k for k,p in zip(sorted(LINES),assembly.locations)}
while not m.halted:
    line=line_at[m.pc]
    if line in (60,61,66) and m.reg[1].value(64)>=3600:break
    m.step();assert m.steps<4000000
assert not m.halted and m.reg[1].value(64)==3600
result=dict(t=t,cards=61,input_nonblank_words=964,expected_answer_words=1280,
            allocated_answer=[2400,3599],line=line,next_write=3600,instructions=m.steps,
            cpu_time=m.time,output_blocks=len(m.outputs[18]),published_ENT3_correction_included=True,
            stopped_before_first_outside_write=True,elapsed_seconds=time.monotonic()-started)
(ROOT/'results/permutation-b-capacity.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
