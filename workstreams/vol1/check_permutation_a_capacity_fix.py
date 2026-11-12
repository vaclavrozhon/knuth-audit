"""Check only the changed allocation on the valid large counterexample."""
from pathlib import Path
import json,time
from mixal import Assembly,CHARACTERS
from mix_io import IOMachine
from mixal_permutation_a import program,cycle_tokens,cards_from_tokens
ROOT=Path(__file__).resolve().parent
started=time.monotonic();t=320
anames=[f'A{i:04d}' for i in range(1,t+1)];bnames=[f'B{i:04d}' for i in range(1,t+1)]
second=[anames[0]]
for j in range(t-1,-1,-1):
    second.append(bnames[j])
    if j:second.append(anames[j])
cards=cards_from_tokens(cycle_tokens([anames,second]))
answer=cycle_tokens(list(zip(anames,bnames)))
expected=''.join(answer);expected+=' '*((-len(expected))%120)
for b in range(64,101):
    a=Assembly(program(True),b)
    assert max(a.memory)<4000 and a.symbols['OUTBUF'].value(b)==3623
runs=[]
for b in (64,100):
    a=Assembly(program(True),b);m=IOMachine(b,1000);a.load(m);m.inputs[16].extend(cards)
    m.run(a.start,limit=10000000);cpu=m.time;m.finish_io()
    output=[''.join(CHARACTERS[d] for w in block for d in w.digits) for block in m.outputs[18]]
    assert len(output)==61+54
    assert ''.join(output[61:])==expected
    assert not m.overflow and not m.inputs[16] and not m.devices
    runs.append(dict(radix=b,instructions=m.steps,cpu_time=cpu,output_blocks=len(output),answer_words=len(answer)))
result=dict(runs=runs,elapsed_seconds=time.monotonic()-started,allocation='MAXANS EQU 2*MAXWDS+23; ANS ORIG *+MAXANS',all37_radices_fit_memory=True)
(ROOT/'results/permutation-a-capacity-fix.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
