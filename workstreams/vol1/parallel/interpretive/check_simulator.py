"""Differential checks of the literal MIX simulator; finite evidence, not proof."""
import json
from pathlib import Path
import random
from programs import simulator
from mix_machine import Machine, Word, number, instruction, Undefined, OPS

ROOT = Path(__file__).resolve().parent
RNG = random.Random(20261101)
ERRORS = ('INDEXERROR','ADDRERROR','OPERROR','MEMERROR','FERROR','SIZEERROR')
NAMES = {v[0]: k for k,v in OPS.items()}
FIELDS = [8*l+r for l in range(6) for r in range(l,6)]
ASM = {}
COUNTS = {}
TIMINGS = []


def random_regs(b):
    return [number(RNG.choice((-1,1))*RNG.randrange(b**(2 if 1<=r<=6 else 5)), b)
            for r in range(8)]


def one(b, w, regs=None, memory=None, comparison=0, overflow=False,
        pc=100, expect_error=None, tag='ordinary'):
    if b not in ASM: ASM[b] = simulator(b)
    asm, lines = ASM[b]
    sy = {k:v.value(b) for k,v in asm.symbols.items()}
    native, host = Machine(b), Machine(b)
    native.reg = list(regs or random_regs(b))
    native.j, native.pc, native.comparison, native.overflow = 234,pc,comparison,overflow
    native.mem[pc] = w
    for k,v in (memory or {1000:number(17,b)}).items(): native.mem[k]=v
    host.mem[:3500] = native.mem[:3500]
    asm.load(host)
    for r in range(8):
        host.mem[sy['AREG']+r] = number(native.reg[r].magnitude(b),b)
        host.mem[sy['SIGNA']+r] = number(native.reg[r].sign,b)
    for name,value in [('JREG',native.j),('COMPI',comparison),('OVTOG',int(overflow)),('CLOCK',17)]:
        host.mem[sy[name]] = number(value,b)
    host.reg[6],host.pc = number(pc,b),sy['CYCLE']
    native_error = None
    try: native.step()
    except Undefined as e: native_error=str(e)
    if native_error and 'division overflow' in native_error: return
    # Stop at the next CYCLE, or at an explicitly omitted diagnostic.
    reached = None
    for _ in range(100000):
        if host.steps and host.pc==sy['CYCLE']: break
        reached = next((name for name in ERRORS if host.pc==sy[name]),None)
        if reached: break
        host.step()
        if host.halted: break
    else: raise AssertionError(('host step limit',b,w))
    if expect_error:
        assert reached==expect_error,(b,w,reached,expect_error)
        COUNTS['diagnostics']=COUNTS.get('diagnostics',0)+1
        return
    if native_error:
        if reached or 'division overflow' in native_error: return
        raise AssertionError(('unexpected native undefined',b,w,native_error))
    assert not reached,(b,w,reached)
    actual_regs = [number(host.mem[sy['SIGNA']+r].value(b)*host.mem[sy['AREG']+r].magnitude(b),
                          b,host.mem[sy['SIGNA']+r].value(b)) for r in range(8)]
    assert actual_regs==native.reg,('registers',b,w,native.reg,actual_regs)
    assert host.reg[6].value(b)==native.pc,('pc',b,w,native.pc,host.reg[6])
    assert host.mem[sy['JREG']].value(b)==native.j,('J',b,w)
    assert host.mem[sy['COMPI']].value(b)==native.comparison,('comparison',b,w)
    assert bool(host.mem[sy['OVTOG']].value(b))==native.overflow,('overflow',b,w)
    assert host.mem[:3500]==native.mem[:3500],('memory',b,w)
    pending = host.mem[sy['TIME']]
    simulated_time = host.mem[sy['CLOCK']].value(b)+pending.sign*(pending.digits[0]*b+pending.digits[1])-17
    assert simulated_time==native.time,('time',b,w,simulated_time,native.time)
    COUNTS[tag]=COUNTS.get(tag,0)+1
    if w.digits[4] in (8,48) and tag=='timings':
        TIMINGS.append({'radix':b,'instruction':str(w),'host_u':host.time,'simulated_u':native.time})


def main():
    # Every legal field, all arithmetic/load/store/compare opcode families;
    # both signs and negative zero; full-size values and index-size cases.
    for b in (64,100):
        for c in list(range(1,5))+list(range(8,34))+list(range(56,64)):
            for f in FIELDS:
                for sign in (-1,1):
                    for value in (0,37,b*b-1,b**5-1):
                        regs=[number(sign*(b*b-1 if 1<=r<=6 else b**5-1),b) for r in range(8)]
                        if c==4: regs[0]=number(0,b,sign)
                        one(b,instruction(b,NAMES[c],1000,f=f),regs,
                            {1000:number(sign*value,b,sign)},tag='fields_and_signs')
        for c in range(39,48):
            for f in range(10 if c==39 else 6):
                for comparison in (-1,0,1):
                    for overflow in (False,True):
                        for value in (-1,0,1):
                            regs=[number(value,b,-1 if value==0 else 1)]*8
                            one(b,instruction(b,NAMES[c],120,f=f),regs,
                                comparison=comparison,overflow=overflow,tag='branches')
        for c in range(48,56):
            for f in range(4):
                for sign in (-1,1):
                    for value in (0,1,b*b-1):
                        regs=[number(0,b,sign)]*8
                        one(b,instruction(b,NAMES[c],sign*value,f=f,sign_zero=sign),regs,
                            tag='address_transfer')
        for c in (1,2,8,16,24,32,33,56,63):
            for f in set(range(b))-set(FIELDS):
                one(b,instruction(b,NAMES[c],1000,f=f),expect_error='FERROR')
        for i in range(7,b):
            one(b,instruction(b,'LDA',1000,index=i),expect_error='INDEXERROR')
        for c in range(64,b):
            one(b,Word(1,(0,0,0,0,c)),expect_error='OPERROR')
        for m in (-1,3500,b*b-1):
            one(b,instruction(b,'LDA',m),expect_error='MEMERROR')
        regs=[number(0,b)]*8; regs[1]=number(b*b-1,b)
        one(b,instruction(b,'LDA',1,index=1),regs,expect_error='ADDRERROR')
        one(b,instruction(b,'LD1',1000),memory={1000:number(b*b,b)},expect_error='SIZEERROR')
        for c in range(39,56):
            maxf=9 if c==39 else 5 if c<48 else 3
            one(b,instruction(b,NAMES[c],120,f=maxf+1),expect_error='FERROR')
    # All 37 legal byte radices: operation families, indexing and flag state.
    supported=[0,1,2,3,5,6,7]+list(range(8,34))+list(range(39,64))
    for b in range(64,101):
        for c in supported:
            for repeat in range(3):
                regs=random_regs(b)
                f=RNG.choice(FIELDS) if c in (1,2,3) or 8<=c<=33 or c>=56 else 0
                m=1000
                if c==5: f=repeat%2; m=0
                if c==6: f=RNG.randrange(6); m=RNG.choice((0,1,5,10,11,27))
                if c==7: f=RNG.randrange(10); regs[1]=number(1001,b)
                if 39<=c<=47: f=RNG.randrange(10 if c==39 else 6); m=120
                if 48<=c<=55: f=RNG.randrange(4); m=RNG.randrange(-20,21)
                index=repeat%2
                if index:
                    regs[1]=number(-7,b)
                    if c==7: index=2; regs[2]=number(-7,b); regs[1]=number(1001,b)
                one(b,instruction(b,NAMES[c],m+(7 if index else 0),index,f),regs,
                    {1000:Word(RNG.choice((-1,1)),tuple(RNG.randrange(b) for _ in range(5)))},
                    comparison=repeat-1,overflow=repeat==1,tag='all_radices')
        # Full range shift/rotation and overlapping MOVE, including -0 destination.
        for f in range(6):
            for m in (0,1,5,10,b*b-1):
                one(b,instruction(b,'SLA',m,f=f),tag='shift_boundaries')
        for sign in (-1,1):
            for length in (0,1,5,b-1):
                regs=random_regs(b);regs[1]=number(0,b,sign)
                one(b,instruction(b,'MOVE',1000,f=length),regs,tag='move_zero_destination')
    # The exact answer-5 cases use M!=0 and then the stated special branches.
    for op,f,m,i in [('LDA',5,1000,0),('LDA',13,1000,0),('LDA',5,1000,1),
                     ('ENTA',2,7,0),('ENTA',2,0,0),('ENTA',2,7,1)]:
        regs=[number(0,64)]*8;regs[1]=number(3,64)
        one(64,instruction(64,op,m,i,f),regs,{1000:number(13,64),1003:number(13,64)},tag='timings')
    # The published answer-8 edge: fallthrough fetches BEGIN, then MEMERROR.
    b=64;asm,lines=ASM[b];sy={k:v.value(b) for k,v in asm.symbols.items()}
    h=Machine(b);asm.load(h);h.reg[6]=number(3499,b);h.pc=sy['CYCLE']
    seen=[]
    for _ in range(200):
        if h.pc==lines[10]: seen.append(h.reg[6].value(b))
        if h.pc==sy['MEMERROR']:break
        h.step()
    assert seen==[3499,3500] and h.pc==sy['MEMERROR'],seen
    result={'counts':COUNTS,'total_success':sum(v for k,v in COUNTS.items() if k!='diagnostics'),
            'timings':TIMINGS,'answer8_fetches':seen,
            'assembly_last_word':{str(b):max(a.memory) for b,(a,_) in ASM.items()},
            'limits':['integer MIX only','DIV overflow yields unspecified A/X and is excluded',
                      'original I/O absent; tested separately','timing excludes BEGIN initialization',
                      'Own exercise9 extension credits HLT explicitly; NUM/CHAR use known corrected table cost 10']}
    (ROOT/'results/simulator.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
