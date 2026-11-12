"""Validate the actualMIX reentrant selftracer against direct native steps.

No instruction is replaced by Python. The reference runs the same load image
directly; the tested program performs every lookup/copy/print on nativeMIX.
"""
from pathlib import Path
import argparse
import json
import time
from selftrace_program import assembly
from mix_io import IOMachine
from mix_machine import number,Word

ROOT=Path(__file__).resolve().parent


def decimal(words):
    digits=[d-30 for w in words for d in w.digits]
    assert all(0<=d<=9 for d in digits),digits
    return int(''.join(map(str,digits)))


def record(row,b):
    depth=decimal(row[:2]);pc=decimal(row[2:4]);mag=decimal(row[4:6])
    sign=1 if row[6].digits[0]==44 else -1 if row[6].digits[0]==45 else None
    assert sign is not None,row[6]
    return depth,pc,number(sign*mag,b,sign)


def check(b,capacity=2000,guest_limit=100,step_limit=10000000):
    asm=assembly(b,capacity);sy={k:v.value(b) for k,v in asm.symbols.items()}
    m,d=IOMachine(b),IOMachine(b)
    asm.load(m);asm.load(d)
    d.pc=sy['BEGIN']
    guest_steps=0;expected_records=[];start=time.monotonic();checks=0
    failure_labels={sy[k]:k for k in ('INDEXERROR','ADDRERROR','OPERROR','MEMERROR','FERROR','SIZEERROR','MEMFULL')}
    for _ in range(step_limit):
        if m.pc in failure_labels:break
        if m.pc==sy['CYCLE']:
            # At CYCLE after a guest instruction, the reference has executed it.
            rr=[number(m.mem[sy['SIGNA']+r].value(b)*m.mem[sy['AREG']+r].magnitude(b),b,
                       m.mem[sy['SIGNA']+r].value(b)) for r in range(8)]
            assert rr==d.reg,('registers',b,guest_steps,rr,d.reg)
            assert m.reg[6].value(b)==d.pc,('pc',b,guest_steps,m.reg[6],d.pc)
            assert m.mem[sy['JREG']].value(b)==d.j,('J',b,guest_steps)
            assert m.mem[sy['COMPI']].value(b)==d.comparison,('comparison',b,guest_steps)
            assert bool(m.mem[sy['OVTOG']].value(b))==d.overflow,('overflow',b,guest_steps)
            used=m.mem[sy['USED']].value(b)
            shadow={m.mem[k].value(b):m.mem[k+1] for k in range(0,used,2)}
            assert len(shadow)==used//2
            assert set(shadow)==d.writes,('write keys',b,guest_steps,set(shadow)^d.writes)
            assert all(d.mem[k]==v for k,v in shadow.items()),('logical memory',b,guest_steps)
            # ROM has never been written by the real interpreter.
            assert all(m.mem[k]==asm.memory[k] for k in range(2000,3000))
            d._finish_input()
            checks+=1
            if guest_limit is not None and guest_steps>=guest_limit:break
            expected_records.append((d.pc,d.mem[d.pc]))
            d.step();guest_steps+=1
        m.step()
    else:raise AssertionError(('step budget before requested completion',b,capacity,guest_steps))
    logs=[record(row,b) for row in m.outputs[18]]
    direct=[(p,w) for level,p,w in logs if level==0]
    assert direct==expected_records[:len(direct)],('level0trace',b)
    # Every forwarded record has one more interpretation level than direct output.
    forwarded=[(level,p,w) for level,p,w in logs if level>0]
    d._finish_input()
    expected_forwarded=[(level+1,p,w) for level,p,w in (record(row,b) for row in d.outputs[18])]
    assert forwarded==expected_forwarded[:len(forwarded)],('forwarded trace',b)
    assert len(expected_forwarded)-len(forwarded)<=1
    levels={}
    for level,_,_ in logs:levels[level]=levels.get(level,0)+1
    stopped=failure_labels.get(m.pc,'prefix_complete')
    if guest_limit is None:
        assert stopped=='MEMFULL',(b,stopped)
        assert m.mem[sy['USED']].value(b)==capacity
        assert levels.get(1,0)>0,('nested trace not reached',b,levels)
    return {'b':b,'capacity_words':capacity,'guest_instructions_attempted':guest_steps,
            'state_checks':checks,'physical_steps':m.steps,'seconds':round(time.monotonic()-start,3),
            'stop':stopped,'used_words':m.mem[sy['USED']].value(b),'output_by_level':levels,
            'first_records':[(l,p,str(w)) for l,p,w in logs[:8]],
            'first_nested_records':[(l,p,str(w)) for l,p,w in forwarded[:8]],
            'code_last_word':max(k for k in asm.memory if k>=3000)}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--full',type=int)
    args=parser.parse_args()
    if args.full:
        result=check(args.full,128,None,15000000)
        path=ROOT/f'results/selftrace-full-{args.full}.json'
    else:
        result=[check(b) for b in range(64,101)]
        path=ROOT/'results/selftrace-radices.json'
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result if args.full else {'radices':len(result),'all_state_checks':sum(r['state_checks'] for r in result)},indent=2))
