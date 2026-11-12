"""New targeted checks: conversions, timing exceptions, and persistent calls.

Already completed bulk cases are not repeated. JSON is checkpointed per block.
"""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import json,random
from verify_double_precision import Harness,equivalent
from mix_float_machine import Word
from double_precision_model import model
from float_model import normalize
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/double-precision-edges.json'


def conversions(b):
    h=Harness(b,'original');Q=b*b//2;q=b//2;rng=random.Random(4236+b);count=Counter();observed=Counter()
    fs=sorted({0,b**3,b**3+1,b**4//2,b**4-1})
    for e in range(b):
        for F in fs:
            if not F and e:continue
            for sign in [-1,1]:
                h.reset();m=h.m;m.reg['A']=Word(sign,e*b**4+F);m.reg['X']=Word(-sign,rng.randrange(b**5));m.execute('DOUBLE')
                a,x=m.reg['A'],m.reg['X'];E,f=divmod(a.mag,b**3);got=(E,f*b**5+x.mag,a.sign)
                want=(e+Q-q,F*b**4,sign) if F else (0,0,sign)
                assert m.halt is None and equivalent(got,want),(b,e,F,sign,got,want)
                assert m.memory[m.symbols['ACC']]==a and m.memory[m.symbols['ACCX']]==x
                count['single_to_double']+=1
    fs=sorted({0,b**7,b**7+1,b**8-1,b**8-b**4//2,b**8-b**4//2-1,b**8//2,b**8//2+b**4//2,b**8//2+3*b**4//2})
    exps=sorted({0,1,b*b-1,*range(Q-q-2,Q-q+b+2)})
    for e in exps:
        for F in fs:
            if not F and e:continue
            for sign in [-1,1]:
                h.reset();m=h.m;m.reg['A']=Word(sign,e*b**3+F//b**5);m.reg['X']=Word(-sign,F%b**5);m.execute('SINGLE')
                want,tr=normalize(e-Q+q,Fraction(sign*F,b**8),b,4)
                halt=1 if want[1] and want[0]<0 else 2 if want[1] and want[0]>=b else None
                assert m.halt==halt,(b,e,F,sign,m.halt,halt)
                if halt is None:
                    got=m.output_float();assert got[:2]==want,(b,e,F,sign,got,want)
                    assert m.memory[m.symbols['ACC']]==m.reg['A']
                observed[str(halt)]+=1;count['double_to_single']+=1
    return {'id':f'conversions-{b}','checks':dict(count),'single_range_outcomes':dict(observed)}


def timing(b):
    Q=b*b//2;tests=[('zero',(Q,b**7,1),(Q,b**7,-1),'DFADD'),('nonzero_cancellation',(Q,b**7,1),(Q-1,b**8-1,-1),'DFADD'),('register_boundary',(Q,b**7+b**3,1),(Q,b**7,-1),'DFADD')]
    if b==100:tests.append(('multiply_threshold',(Q,909090909090910,1),(Q,1099999999999999,1),'DFMUL'))
    out=[]
    for name,u,v,op in tests:
        r={'name':name,'inputs':[u,v],'operation':op}
        for mode in ['original','improved']:
            h=Harness(b,mode);states=[]
            def observer(m,src):
                if src in ['A41','M03','M33']:
                    states.append({'source':src,'A':[m.reg['A'].sign,m.reg['A'].mag],'X':[m.reg['X'].sign,m.reg['X'].mag],'I2':m.reg['2'].val,'EXPO':m.memory[m.symbols['EXPO']].val,'time_before':m.time})
            h.m.observer=observer
            ans,halt,t=h.run(u,v,op);want,wh=model(b,u,v,op,mode=='improved');assert halt is None and wh is None and equivalent(ans,want)
            # Independent timing tally from counts, with explicit MIX costs.
            instruction={src:(op,arg) for src,lab,op,arg in h.m.rows}
            counts=Counter(instruction[src][0] for src in h.m.trace)
            one={'ENT1','ENT2','ENTX','INCA','INC1','INC2','INCX','DECA','DEC2','JG','JL','JLE','JMP','JNOV','JOV','JANZ','JXNZ','JE','JAN'}
            two={'STA','STJ','STX','LDA','LDX','LD1N','LD2','CMPA','CMPX','ADD','SUB','SLAX','SRAX','SRA','SRC','SLC'}
            assert set(counts)<=one|two|{'MOVE','MUL'}
            tally=sum(n*(1 if op in one else 2 if op in two else 5 if op=='MOVE' else 10) for op,n in counts.items())
            assert tally==t
            r[mode]={'answer':ans,'time':t,'shifts':h.m.visits['A45'],'test_X':h.m.visits['A42'],'fraction_overflow':bool(h.m.visits['A40c']),'operation_counts':dict(counts),'states':states,'trace':h.m.trace}
        r['difference']=r['improved']['time']-r['original']['time'];out.append(r)
    assert [x['difference'] for x in out[:3]]==[3,3,-4]
    if b==100:assert out[-1]['difference']==-4
    return {'id':f'timing-{b}','witnesses':out}


def persistent(b):
    h=Harness(b,'original');m=h.m;Q=b*b//2;checks=0
    for i in range(96):
        u=(Q,b**7+1 if i%2 else b**8-1,(-1)**i)
        v=(Q-i%9,b**7 if i%3 else b**8//2,(-1)**(i//2))
        for a,reg in [(u,False),(v,True)]:
            e,F,s=a;hi=Word(s,e*b**3+F//b**5);lo=Word(-s,F%b**5)
            if reg:m.reg['A']=hi;m.reg['X']=lo
            else:m.memory[m.symbols['ACC']]=hi;m.memory[m.symbols['ACCX']]=lo
        m.j=m.ret;m.halt=None;op=['DFADD','DFSUB','DFMUL','DFDIV'][i%4];m.execute(op)
        a,x=m.reg['A'],m.reg['X'];e,f=divmod(a.mag,b**3);got=(e,f*b**5+x.mag,a.sign);want,wh=model(b,u,v,op)
        assert m.halt==wh and equivalent(got,want) and not m.ov,(b,i,op,got,want,m.halt,wh)
        checks+=1
    return {'id':f'persistent-{b}','calls':checks}


def main():
    data=json.loads(OUT.read_text()) if OUT.exists() else [];done={d['id'] for d in data}
    for b in [64,100]:
        for name,fn in [('conversions',conversions),('timing',timing),('persistent',persistent)]:
            if f'{name}-{b}' in done:continue
            r=fn(b);data.append(r);OUT.write_text(json.dumps(data,indent=2)+'\n');print(r['id'],'PASS',flush=True)

if __name__=='__main__':main()
