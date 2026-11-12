"""Original trace and answer-1/2 modifications, against direct MIX execution."""
from pathlib import Path
from collections import deque
import json
import random
from programs import tracer
from mix_machine import Machine, Word, number, instruction, Undefined, OPS, field
from mix_io import IOMachine

ROOT=Path(__file__).resolve().parent
RNG=random.Random(214531)
NAMES={v[0]:k for k,v in OPS.items()}
FIELDS=[8*l+r for l in range(6) for r in range(l,6)]
CACHE={}
COUNTS={}


def one(b,c,f,regs,memvalue,address=1000,index=0,overflow=False,comparison=0,tape=False,
        restore_j=False,original_erratum=False):
    key=b,tape,restore_j,original_erratum
    if key not in CACHE:CACHE[key]=tracer(b,tape=tape,restore_j=restore_j,original_erratum=original_erratum)
    asm=CACHE[key];sy={k:v.value(b) for k,v in asm.symbols.items()}
    d=Machine(b);d.pc=100;d.j=100;d.reg=list(regs);d.comparison=comparison;d.overflow=overflow
    d.mem[100]=instruction(b,'LDX',700)
    d.mem[101]=instruction(b,NAMES[c],address,index,f)
    d.mem[700]=regs[7];d.mem[1000]=memvalue
    before=d.mem[:]
    states=[]
    try:
        for _ in range(2):
            states.append((d.pc,d.j,d.comparison,d.overflow,d.mem[d.pc],d.reg[:]))
            d.step()
    except Undefined:return False
    stop=d.pc
    if stop in (100,101) or not 0<=stop<3500:return False
    h=IOMachine(b) if tape else Machine(b)
    h.mem=before[:];asm.load(h);h.reg=list(regs);h.reg[7]=number(stop,b)
    states[0][5][7]=number(stop,b)
    h.j=100;h.comparison=comparison;h.overflow=overflow
    h.run(sy['ENTER'],stop=stop,limit=10000)
    assert h.reg==d.reg,('regs',b,c,f,index,tape,restore_j,original_erratum,h.reg,d.reg)
    assert h.comparison==d.comparison,('comparison',b,c,f)
    assert h.overflow==d.overflow,('overflow',b,c,f)
    assert h.mem[:3500]==d.mem[:3500],('memory',b,c,f)
    if restore_j:assert h.j==d.j,('J',b,c,f,h.j,d.j)
    if tape:
        # Two records remain in the unflushed buffer; compare every byte/sign.
        start=sy['BUF']-99
        for rec,state in enumerate(states):
            p,j,comp,ov,w,rr=state
            expected=[Word(1,(p//b,p%b,comp+1+(0 if ov else 8),j//b,j%b)),w]+rr
            assert h.mem[start+10*rec:start+10*rec+10]==expected,('record',b,c,f,rec)
    tag='tape' if tape else 'restore_j' if restore_j else 'original'
    COUNTS[tag]=COUNTS.get(tag,0)+1
    return True


def main():
    for b in range(64,101):
        for mode in ('original','restore_j','tape'):
            for c in [0,1,2,3,4,5,6,7]+list(range(8,34))+list(range(39,64)):
                ff=(FIELDS if c in (1,2,3,4) or 8<=c<34 or c>=56 else
                    range(2) if c==5 else range(6) if c==6 or 40<=c<48 else
                    range(4) if 48<=c<56 else range(10) if c==39 else (0,1,5) if c==7 else (0,))
                # Every field at both radix boundaries; sampled field elsewhere.
                if b not in (64,100):ff=[RNG.choice(list(ff))]
                for f in ff:
                    regs=[number(RNG.randrange(-70,71),b) for _ in range(8)]
                    regs[1]=number(1001,b) if c==7 else number(3,b)
                    if c==4:regs[0]=number(0,b,RNG.choice((-1,1)))
                    m=RNG.randrange(16) if c==6 else 17 if 48<=c<56 else 120 if 39<=c<48 else 1000
                    idx=0 if c in (6,7) else RNG.randrange(2)
                    address=m-(3 if idx else 0)
                    one(b,c,f,regs,number(-37,b),address,idx,
                        overflow=RNG.choice((False,True)),comparison=RNG.choice((-1,0,1)),
                        tape=mode=='tape',restore_j=mode=='restore_j')
    # All negative-zero/sign/condition combinations for branches and stores.
    for b in (64,100):
        for v in (-1,0,1):
            for sign in (-1,1):
                regs=[number(v,b,sign)]*8
                for ov in (False,True):
                    for comp in (-1,0,1):
                        for c in range(39,48):
                            for f in range(10 if c==39 else 6):
                                one(b,c,f,regs,number(0,b,sign),120,
                                    overflow=ov,comparison=comp,tape=True)
    # Reproduce the 2008 correction using indexed STJ, then verify correction.
    regs=[number(0,64)]*8;regs[1]=number(3,64)
    old_failure=False
    try:one(64,32,2,regs,number(0,64),997,1,tape=True,original_erratum=True)
    except AssertionError as e:old_failure=str(e)
    assert old_failure
    one(64,32,2,regs,number(0,64),997,1,tape=True)
    # A complete ten-record tape block plus two records in the next block.
    b=64;asm=tracer(b,tape=True);sy={k:v.value(b) for k,v in asm.symbols.items()}
    h=IOMachine(b);asm.load(h);h.pc=sy['ENTER'];h.j=100;h.reg[7]=number(112,b)
    h.run(sy['ENTER'],stop=112,limit=10000)
    h.finish_io()
    block=h.outputs[0][0]
    assert len(block)==100
    assert [field(block[i],2).value(b) for i in range(0,100,10)]==list(range(100,110))
    assert field(h.mem[sy['BUF']-99],2).value(b)==110
    # Self tracing: the first attempt to trace CYCLE (line7) returns to ENTER+1.
    asm=tracer(b);sy={k:v.value(b) for k,v in asm.symbols.items()}
    h=Machine(b);asm.load(h);h.reg[7]=number(sy['LEAVEX'],b);h.j=sy['ENTER'];h.pc=sy['ENTER']
    seen=[]
    for _ in range(1000):
        if h.pc==sy['CYCLE']:
            seen.append(h.reg[0].value(b))
            if len(seen)==9:break
        h.step()
    expected=list(range(sy['ENTER'],sy['CYCLE']+1))+[sy['ENTER']+1]
    assert seen[:len(expected)]==expected,seen
    result={'counts':COUNTS,'total_success':sum(COUNTS.values()),
            'known_2008_original_failure':old_failure,'tape_full_block_records':10,
            'self_trace_locations':seen,'original_trace_words':47,'limits':[
                'No floating point; no device-dependent timing equivalence claimed',
                'Trace variants have documented output-device and private-memory restrictions',
                'Answer2 partial buffer inspected directly; final flushing is explicitly supplementary',
                'Trace exercise5/6/7 have separate structural arguments']}
    (ROOT/'results/trace.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
