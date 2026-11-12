"""Exact independent check of section4.2.3 MIX programs and exercise variants.

Incremental JSON checkpoints; --resume preserves passed blocks.
"""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import json,random,sys,time
from mix_float_machine import Machine,Word
from double_precision_model import model,value,normalize,power
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'sources/double-precision.mix'
OUT=ROOT/'results/double-precision.json'


def variants():
    rows=[line.split() for line in BASE.read_text().splitlines() if line and not line.startswith('#')]
    extra=[]
    for line in (ROOT/'sources/single-precision.mix').read_text().splitlines():
        if line and not line.startswith('#'):
            a=line.split()
            if a[0].startswith('A') and 43<=int(a[0][1:])<=69:
                a[0]='F'+a[0];extra.append(a)
    conversions='''C01 DOUBLE STJ EXITDF
C02 - ENTX 0
C03 - STA TEMP
C04 - LD2 TEMP(EXP)
C05 - INC2 QQ-Q
C06 - STZ EXPO
C07 - SLAX 1
C08 - JMP DNORM
C09 SINGLE STJ EXITF
C10 - JOV OFLO
C11 - STA TEMP
C12 - LD2 TEMP(EXPD)
C13 - DEC2 QQ-Q
C14 - SLAX 2
C15 - JMP NORM'''
    extra.extend(s.split() for s in conversions.splitlines())
    for mode in ['original','improved','clear_x','swap_adds']:
        new=[]
        for src,label,op,arg in rows:
            if mode=='improved':
                if src=='A23':arg='0,1'
                if src=='A31':arg='5'
                if src=='A39':arg='ACC'
                if src=='M21':continue
                if src=='M22':arg='TEMP(ABS)'
                if src in ['M28','M29','M30','M31']:
                    if src=='M28':new.extend([s.split() for s in ['M28a - SLAX 5','M28b - ADD TEMP','M28c - JNOV *+2','M28d - INC1 1','M28e - ENTX 0,1','M28f - SRC 5']])
                    continue
            if mode=='swap_adds':
                if src=='A39':arg='ARG'
                if src=='A40':arg='ACC(0:4)'
            new.append([src,label,op,arg])
            if mode=='improved':
                if src in ['A06','M03']:new.append([src+'a','-','JOV','OFLO'])
                if src=='M03':new.append(['M03b','-','ENT1','0'])
                if src=='M22':new.extend([['M22a','-','JNOV','*+2'],['M22b','-','INC1','1']])
                if src=='A40':new.extend([s.split() for s in ['A40a - DEC2 1','A40b - JNOV DNORM','A40c - INC2 1','A40d - INCX 1','A40e - SRC 1']])
            if mode=='clear_x' and src=='M30':new.append(['M30a','-','ENTX','0'])
        path=ROOT/f'sources/double-precision-{mode}.mix'
        path.write_text('# Generated from inspected sources; see verify_double_precision.py.\n'+'\n'.join(' '.join(a) for a in new+extra)+'\n')


class Harness:
    def __init__(self,b,mode):
        self.m=Machine(b,source=ROOT/f'sources/double-precision-{mode}.mix');self.mem=self.m.memory.copy();self.b=b
    def reset(self):
        m=self.m;m.memory=self.mem.copy();m.reg={k:Word() for k in m.reg};m.code_sign={};m.code_addr={};m.j=m.ret;m.ov=False;m.cmp=0;m.time=0;m.visits=Counter();m.trace=[];m.halt=None;m.attrs={}
    def run(self,u,v,op,low_signs=(1,1)):
        self.reset();m=self.m;b=self.b
        for a,reg,sgn in [(u,False,low_signs[0]),(v,True,low_signs[1])]:
            e,F,s=a;hi=Word(s,e*b**3+F//b**5);lo=Word(sgn,F%b**5)
            if reg:m.reg['A']=hi;m.reg['X']=lo
            else:m.memory[m.symbols['ACC']]=hi;m.memory[m.symbols['ACCX']]=lo
        m.execute(op);hi=m.reg['A'];lo=m.reg['X'];e,f=divmod(hi.mag,b**3)
        answer=(e,f*b**5+lo.mag,hi.sign)
        if m.halt is None:
            assert m.memory[m.symbols['ACC']]==hi and m.memory[m.symbols['ACCX']]==lo
        return answer,m.halt,m.time


def equivalent(a,c):return a[:2]==c[:2] and (not a[1] or a[2]==c[2])

def main():
    variants();blocks=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else []
    done={v['id'] for v in blocks}
    def save(r):
        blocks.append(r);OUT.write_text(json.dumps(blocks,indent=2)+'\n');print(json.dumps(r),flush=True)
    for b in [64,100]:
        if f'routines-{b}' in done:continue
        t=time.monotonic();rng=random.Random(42300+b);Q=b*b//2;lo=b**7;hi=b**8-1
        harness={k:Harness(b,k) for k in ['original','improved','clear_x','swap_adds']}
        counts=Counter();times={};worst={};branch=Counter();swapped=None
        fs=sorted({lo,lo+1,lo+b-1,lo+b,lo+b**3-1,b**8//2,hi-1,hi,2*lo-1,2*lo,b**8//2+1})
        cases=[]
        for U in fs:
            for V in fs:
                for d in [0,1,2,8,9,20]:
                    for s in [1,-1]:cases.append(((Q,U,1),(Q-d,V,s)))
        for i in range(3000):
            eu=Q+rng.randrange(-15,16);ev=Q+rng.randrange(-15,16)
            U=rng.randrange(lo,hi+1);V=rng.randrange(lo,hi+1)
            if i%5==0:ev=eu;V=max(lo,min(hi,U+rng.randrange(-2*b,2*b)))
            cases.append(((eu,U,rng.choice([-1,1])),(ev,V,rng.choice([-1,1]))))
        for e in [0,1,Q,b*b-2,b*b-1]:
            for f in [lo,hi]:
                for s in [-1,1]:
                    cases.extend([((0,0,s),(e,f,1)),((e,f,s),(0,0,1)),((e,f,s),(e,f,-s))])
        cases.extend([((0,0,1),(0,0,-1))])
        # Input exponents near both limits, exercising checked overflow/underflow.
        for eu in [0,1,b*b-2,b*b-1]:
            for ev in [0,1,b*b-2,b*b-1]:cases.append(((eu,lo,1),(ev,hi,-1)))
        for ix,(u,v) in enumerate(cases):
            signs=((-1)**ix,(-1)**(ix//2))
            for op in ['DFADD','DFSUB','DFMUL','DFDIV']:
                for mode in ['original','improved']:
                    h=harness[mode];ans,halt,tm=h.run(u,v,op,signs)
                    target,expected_halt=model(b,u,v,op,mode=='improved')
                    assert halt==expected_halt,(b,ix,u,v,op,mode,ans,target,halt,expected_halt,h.m.trace)
                    if halt is None:
                        assert equivalent(ans,target),(b,ix,u,v,op,mode,ans,target,h.m.trace)
                        assert (ans[1]==0)==(target[1]==0)
                        if max(abs(u[0]-Q),abs(v[0]-Q))<100:
                            a=value(b,u);c=value(b,v);true=a+c if op=='DFADD' else a-c if op=='DFSUB' else a*c if op=='DFMUL' else a/c
                            if true:
                                error=abs((value(b,ans)-true)/true)
                                bound=Fraction(1,b**7) if mode=='improved' and op in ['DFADD','DFSUB'] else Fraction(b-1) if op in ['DFADD','DFSUB'] else Fraction(b+2,b**8) if mode=='improved' or op=='DFDIV' else Fraction(3,b**7)
                                assert error<=bound,(b,ix,op,mode,error,bound,u,v,ans)
                                key=mode+'-'+op
                                if key not in worst or error>Fraction(worst[key]['relative_error']):worst[key]={'relative_error':str(error),'inputs':[u,v],'output':ans,'bound':str(bound)}
                    key=mode+'-'+op;counts[key]+=1;times.setdefault(key,Counter())[tm]+=1
                    branch.update(h.m.trace)
                    if op=='DFMUL' and mode=='original':
                        clear,hc,tc=harness['clear_x'].run(u,v,op,signs)
                        assert hc==halt and (halt or equivalent(ans,clear)),('clear_x',u,v,ans,clear)
                        counts['clear_x']+=1
                    if op=='DFADD' and mode=='original' and swapped is None and halt is None:
                        wrong,hw,tw=harness['swap_adds'].run(u,v,op,signs)
                        if hw is None and not equivalent(ans,wrong):swapped={'inputs':[u,v],'correct':ans,'swapped':wrong}
        assert swapped is not None
        save({'id':f'routines-{b}','cases':len(cases),'checks':dict(counts),'timing_range':{k:[min(v),max(v)] for k,v in times.items()},'worst':worst,'swap_counterexample':swapped,'visited':dict(branch),'seconds':round(time.monotonic()-t,2)})
    print('COMPLETED',len(blocks),flush=True)

if __name__=='__main__':main()
