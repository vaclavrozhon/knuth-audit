"""Run transcribed MIX instructions against exact rational arithmetic.

The model compares independent machine instructions with Algorithms A/N/M,
whose nearest-neighbor property has already been checked separately. It also
checks the 2002 timing expression and records an original-code counterexample.
Successful blocks are checkpointed and never rerun automatically.
"""
from fractions import Fraction as Q
from itertools import product
import json,random
from pathlib import Path
from mix_float_machine import Machine,Word
from float_model import add,multiply,divide,value,normalize,round_integer
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/mix-float.json'


def raw(u):return u[0],u[1]*u[2]


def run(b,entry,u,v=None,original=False):
    m=Machine(b,original)
    if v is None:
        m.load_float(u,reg='A')
    else:
        m.load_float(u,location='ACC');m.load_float(v,reg='A')
    m.execute(entry)
    return m


def want_halt(w,b):
    return 1 if w[1] and w[0]<0 else 2 if w[1] and w[0]>=b else None


def compare(m,w,context):
    expect_halt=want_halt(w,m.b)
    assert m.halt==expect_halt,(context,'halt',m.halt,w,m.trace)
    if expect_halt is None:
        assert m.output_float()[:2]==w,(context,m.output_float(),w,m.attrs,m.trace)
        assert m.memory[m.symbols['ACC']]==m.reg['A']
    for symbol in ['FU','FV']:
        assert m.memory[m.symbols[symbol]].mag % m.b==0
    assert m.memory[m.symbols['HALF']].mag==m.w//2


def timing(m,u,v):
    attrs=m.attrs;r=attrs.get('first_round',{})
    N=m.visits['A46'];X=bool(attrs.get('X',False))
    zero=m.reg['A'].mag==0
    return (73-(5-int(r.get('tail_half',False)))*(6-int(attrs.get('round_up',False)))
            +int(v[0]<u[0])+int(r.get('digit_half',False))
            -int(attrs.get('fraction_overflow',False))-10*zero
            +7*int(attrs.get('round_overflow',False))+7*N
            +(3+(16+int(m.reg['A'].val<0))*int(u[2]!=v[2]))*X)


def addition():
    rng=random.Random(4212026);cases=timed=0;max_time=0;max_case=None;visits=set();old=[]
    for b in [64,100]:
        q=b//2;lo=b**3;hi=b**4
        fs=sorted({lo,lo+1,lo+b//2,lo+b,lo+b*b,2*lo-1,hi//2-1,hi//2,hi//2+1,hi-b-1,hi-b,hi-2,hi-1})
        pairs=[((q,f,s),(q-d,g,t)) for f,g,s,t,d in product(fs,fs,[-1,1],[-1,1],range(11))]
        pairs.extend(((rng.randrange(b),rng.randrange(lo,hi),rng.choice([-1,1])),(rng.randrange(b),rng.randrange(lo,hi),rng.choice([-1,1]))) for _ in range(2000))
        for e,f,s,t in product([0,1,q,b-2,b-1],fs,[-1,1],[-1,1]):
            pairs.extend([((e,f,s),(e,f,t)),((e,f,s),(0,0,t)),((0,0,s),(e,f,t))])
        pairs.extend(((0,0,s),(0,0,t)) for s,t in product([-1,1],repeat=2))
        pairs.append(((q,lo,-1),(q-5,hi//2-1,1)))
        for u,v in pairs:
            m=run(b,'FADD',u,v);w,_=add(raw(u),raw(v),b,4,q)
            compare(m,w,(b,u,v));visits.update(m.trace);cases+=1
            if m.halt is None:
                assert m.time==timing(m,u,v),(b,u,v,m.time,timing(m,u,v),m.attrs,m.trace)
                assert m.time<=84
                timed+=1
                if m.time>max_time:max_time=m.time;max_case=dict(b=b,u=u,v=v,result=m.output_float(),attrs=m.attrs)
                if not w[1]:assert m.reg['A'].sign==u[2],(b,u,v,m.reg['A'])
        u=(q,lo,1);v=(q-5,hi//2,-1)
        m=run(b,'FADD',u,v,True);w,_=add(raw(u),raw(v),b,4,q)
        assert m.output_float()[:2]!=w
        old.append(dict(b=b,u=u,v=v,original_result=m.output_float(),correct_result=w))
    assert max_time==84
    return dict(cases=cases,timed_successes=timed,maximum_time=max_time,maximum_witness=max_case,visited_source_rows=sorted(visits),known_2002_erratum_witnesses=old,
                sign_note='Zero after hardware FADD retains original rA, which is the ACC operand u on entry to the software subroutine.')


def multiply_divide():
    rng=random.Random(4222026);cases=0;zero_divisors=0;visits=set()
    for b in [64,100]:
        q=b//2;lo=b**3;hi=b**4
        fs=sorted({lo,lo+1,lo+b,2*lo-1,hi//2-1,hi//2,hi-2,hi-1})
        pairs=[((q,f,s),(q,g,t)) for f,g,s,t in product(fs,fs,[-1,1],[-1,1])]
        pairs.extend(((rng.randrange(b),rng.randrange(lo,hi),rng.choice([-1,1])),(rng.randrange(b),rng.randrange(lo,hi),rng.choice([-1,1]))) for _ in range(5000))
        pairs.extend(((e,f,s),(ev,g,t)) for e,ev,f,g,s,t in product([0,b-1],[0,b-1],[0,lo,hi-1],[0,lo,hi-1],[-1,1],[-1,1]) if (f or e==0) and (g or ev==0))
        for u,v in pairs:
            for entry,fn in [('FMUL',multiply),('FDIV',divide)]:
                m=run(b,entry,u,v);visits.update(m.trace)
                if entry=='FDIV' and not v[1]:
                    assert m.halt==3;zero_divisors+=1;continue
                w,_=fn(raw(u),raw(v),b,4,q);compare(m,w,(entry,b,u,v));cases+=1
    return dict(operations=cases,zero_divisors=zero_divisors,visited_source_rows=sorted(visits))


def conversions():
    rng=random.Random(4232026);fixed=fractional=floating=0;errors={};visits=set()
    for b in [64,100]:
        q=b//2;hi=b**4
        fs=sorted({0,1,2,b//2,b-1,b,b+1,b*b-1,b*b,b**3-1,b**3,b**3+1,hi//2,hi-2,hi-1})
        inputs=[(e,f,s) for e,f,s in product(range(b),fs,[-1,1])]
        inputs.extend((rng.randrange(b),rng.randrange(hi),rng.choice([-1,1])) for _ in range(3000))
        for u in inputs:
            x=value(raw(u),b,4,q)
            m=run(b,'FIX',u);visits.update(m.trace);want=round_integer(x,b)
            if abs(want)>=b**5:assert m.halt==8,(b,u,want,m.halt);errors['fix_overflow']=errors.get('fix_overflow',0)+1
            else:
                assert m.halt is None and m.reg['A'].val==want,(b,u,x,m.reg['A'],want,m.trace)
                if want==0:assert m.reg['A'].sign==u[2]
            fixed+=1
            m=run(b,'FP',u);visits.update(m.trace)
            z=x-x.numerator//x.denominator;w,_=normalize(q,z,b,4)
            compare(m,w,('FP',b,u,x));fractional+=1
        ints=sorted({0,1,b-1,b,b+1,b**4-1,b**4,b**4+1,b**5-2,b**5-1,*[rng.randrange(b**5) for _ in range(1000)]})
        for n,s in product(ints,[-1,1]):
            m=Machine(b);m.reg['A']=Word(s,n);m.execute('FLOT');visits.update(m.trace)
            w,_=normalize(q+5,Q(s*n,b**5),b,4);compare(m,w,('FLOT',b,n,s));floating+=1
    return dict(fix_inputs=fixed,fractional_part_inputs=fractional,float_inputs=floating,exceptions=errors,visited_source_rows=sorted(visits))


def subtraction_and_reuse():
    """New entry, cancellation underflow, and persistent self-modified state."""
    cases=underflows=0
    for b in [64,100]:
        q=b//2;lo=b**3;hi=b**4
        for entry in ['FADD','FSUB']:
            for sign in [-1,1]:
                u=(0,lo+1,sign);v=(0,lo,-sign if entry=='FADD' else sign)
                m=run(b,entry,u,v)
                adjusted=raw(v) if entry=='FADD' else (v[0],-v[1]*v[2])
                w,_=add(raw(u),adjusted,b,4,q)
                compare(m,w,(entry,b,u,v));assert m.halt==1
                underflows+=1
        m=Machine(b)
        for i in range(48):
            u=(q,lo if i%3 else hi-1,(-1)**i)
            v=(q-i%7,hi//2-1 if i%2 else lo,(-1)**(i//2))
            entry=['FADD','FSUB','FMUL','FDIV'][i%4]
            m.j=m.ret;m.halt=None
            m.load_float(u,location='ACC');m.load_float(v,reg='A');m.execute(entry)
            if entry in ['FADD','FSUB']:
                adjusted=raw(v) if entry=='FADD' else (v[0],-v[1]*v[2])
                w,_=add(raw(u),adjusted,b,4,q)
            else:w,_=(multiply if entry=='FMUL' else divide)(raw(u),raw(v),b,4,q)
            compare(m,w,(entry,b,u,v));assert not m.ov
            cases+=1
    return dict(sequential_calls=cases,addition_subtraction_underflows=underflows)


def main():
    data=json.loads(OUT.read_text()) if OUT.exists() else {}
    for name,fn in [('addition',addition),('multiply_divide',multiply_divide),('conversions',conversions),('subtraction_and_reuse',subtraction_and_reuse)]:
        if name in data:continue
        data[name]=fn();OUT.write_text(json.dumps(data,indent=2)+'\n');print(name,'PASS',flush=True)

if __name__=='__main__':main()
