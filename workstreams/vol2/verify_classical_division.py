#!/usr/bin/env python3
"""MIX D, rare branches, exact timing and aliasing; no repeat of old D census."""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import argparse,json,random,time
from mix_float_machine import Machine, Word, word
from verify_classical_basic import digits,value,ClassicalMachine
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/classical-division.json'

class DivisionMachine(Machine):
    def __init__(self,beta,m,n,U,V,alias=False):
        super().__init__(beta,source=ROOT/'sources/classical-division.mix')
        self.symbols.update(M=m,N=n,U=1000,V=1500,Q=1000+n if alias else 2000)
        self.max_steps=20000;self.external=set();self.rare=Counter();self.initial=(U,V)
        self.m,self.n,self.alias=m,n,alias;self.windows=[];self.step_state=None
        for name,ds in [('U',digits(U,self.w,m+n)+[17]),('V',digits(V,self.w,n)+[17])]:
            a=self.symbols[name]
            for i,x in enumerate(ds):self.memory[a+i]=word(x);self.external.add(a+i)
        if not alias:
            for i in range(m+1):self.memory[2000+i]=word(17);self.external.add(2000+i)
        else:
            row=next(r for r in self.rows if r[0]=='D094');row[2]='J1N'
        self.ret=self.symbols['D_END'];self.observer=self.observe
    def store(self,addr,field,w):
        if addr>=len(self.rows):
            assert addr in self.external and field==(0,5),(addr,field)
            self.memory[addr]=w
        else:super().store(addr,field,w)
    def block(self,name,start,length):
        a=self.symbols[name]+start
        return [self.memory[a+i].val for i in range(length)]
    def observe(self,mm,src):
        if src=='N006' and self.ov:self.rare['normalizer_overflow']+=1
        if src=='D052' and self.ov:self.rare['rhat_overflow']+=1
        if src=='D060' and self.cmp<=0:self.rare['equal_high_final']+=1
        if src=='D023':assert self.reg['X'].mag==0
        if src=='D3':raise AssertionError('source IDs, not labels')
        if src=='D037':
            j=self.reg['2'].val
            u=self.block('U',j,self.n+1);v=self.block('V',0,self.n)
            assert all(0<=x<self.w for x in u+v)
            a,b=value(u,self.w),value(v,self.w)
            assert 0<=a<self.w*b
            self.step_state=(j,a,b)
        if src=='D061':
            j,u,v=self.step_state;h=self.memory[self.symbols['QHAT']].val
            assert u//v<=h<=u//v+1 and 0<=h<self.w
        if src=='D095':
            j,u,v=self.step_state;q=self.block('Q',j,1)[0]
            r=value(self.block('U',j,self.n),self.w)
            assert (q,r)==divmod(u,v)
            if not self.alias:assert self.block('U',j+self.n,1)[0]==0
            self.windows.append({'j':j,'q':q,'r':r})
    def check(self):
        self.execute('D1');assert self.halt is None
        q=self.block('Q',0,self.m+1);r=self.block('U',0,self.n)
        assert all(0<=x<self.w for x in q+r)
        assert (value(q,self.w),value(r,self.w))==divmod(*self.initial)
        d=self.memory[self.symbols['D']].val
        assert d==self.w//(digits(self.initial[1],self.w,self.n)[-1]+1)
        assert value(self.block('V',0,self.n),self.w)==d*self.initial[1]
        # Manual frequency sum, with corrections for all ignored rare branches.
        m,n=self.m,self.n;E=self.visits['D047'];K=self.visits['D070'];Kp=self.visits['D074']
        exact=29*(n+1)*(m+1)+45*(m+1)+28*E+36+K+Kp
        if d>1:exact+=66*n+23*m+self.visits['D019']+self.visits['D030']+4
        exact-=14*self.rare['normalizer_overflow']
        exact+=9*self.visits['D044']-17*self.rare['rhat_overflow']
        exact+=3*self.visits['D059']+self.rare['equal_high_final']
        exact+=6*self.visits['D082']+10*self.visits['D087']+self.visits['D093']
        assert self.time==exact,(self.time,exact,dict(self.visits),dict(self.rare))
        return {'cycles':self.time,'d':d,'m':m,'n':n,'U':str(self.initial[0]),'V':str(self.initial[1]),'alias':self.alias,'visits':dict(self.visits),'rare':dict(self.rare)}


def ordinary():
    rng=random.Random(4312526);count=0;branches=Counter();normalizers=Counter()
    for beta in [64,100,256]:
        B=beta**5
        for m in range(5):
            for n in range(2,7):
                for k in range(12):
                    a=[1,2,B//2-1,B//2,B-2,B-1][k%6]
                    V=a*B**(n-1)+rng.randrange(B**(n-1))
                    U=rng.randrange(B**(m+n))
                    if k==0:U=0
                    if k==1:U=V-1
                    if k==2:U=V
                    if k==3:U=B**(m+n)-1
                    mm=DivisionMachine(beta,m,n,U,V)
                    result=mm.check();branches.update(mm.visits);normalizers[str(result['d']>1)]+=1;count+=1
    return {'cases':count,'normalization_needed':dict(normalizers),'instruction_visits':dict(branches)}


def targeted():
    cases=[];coverage=Counter();rng=random.Random(43122)
    for beta in [64,100,256]:
        B=beta**5
        # qhat=1 but exact quotient0; first two leading words are identical.
        # qhat=B from two leading words, and then rhat overflow/no-overflow.
        pairs=[(B**2//2+1,B**2//2+2,2),
               ((B//2)*B**2+(B//2-1)*B,B//2*B+B-1,2),
               ((B//2)*B**2+(B-2)*B+(B-1),B//2*B+B-1,2),
               (B**3//2,B**3//2+1,3)]
        # Generalized published base-2^16 witness (base must be a MIX word here).
        V=(B//2)*B**2+(B//2+2)*B+5
        U=(B//2-1)*B**3+(B//2+1)*B**2
        pairs.append((U,V,3))
        # Force qhat downward twice using leading words; parameterized from a
        # small-radix extremum, independently accepted only by the actual run.
        V=(B//2)*B**2+(B-1)*B+(B-1)
        U=(B-2)*V+(V-1)
        pairs.append((U,V,3))
        for U,V,n in pairs:
            # Exact length, avoiding any logarithm or binary-base assumption.
            length=1;t=U
            while t>=B:length+=1;t//=B
            m=max(0,length-n)
            for alias in [False,True]:
                mm=DivisionMachine(beta,m,n,U,V,alias);res=mm.check()
                coverage.update(mm.visits)
                res['beta']=beta;cases.append(res)
    assert coverage['D044']>0 and coverage['D047']>0 and coverage['D059']>0 and coverage['D082']>0
    assert any(c['rare'].get('rhat_overflow',0) for c in cases)
    return {'cases':cases,'instruction_visits':dict(coverage)}


def aliasing():
    rng=random.Random(43130);count=0;witness=None
    for beta in [64,100,256]:
        B=beta**5
        for m in range(1,6):
            for n in range(1,6):
                for k in range(5):
                    u=[rng.randrange(B) for _ in range(m)]
                    v=[rng.randrange(B) for _ in range(n)]
                    mm=ClassicalMachine(beta,n,m);mm.symbols['V']=mm.symbols['W']+m
                    mm.put('W',[17]*(m+n));mm.put('U',u);mm.put('V',v)
                    mm.ret=mm.symbols['PM_END'];mm.execute('PM')
                    out=[mm.memory[mm.symbols['W']+j].val for j in range(m+n)]
                    assert value(out,B)==value(u,B)*value(v,B);count+=1
        mm=ClassicalMachine(beta,1,2);mm.symbols['V']=mm.symbols['W']+1
        mm.put('W',[17]*3);mm.put('U',[0,1]);mm.put('V',[1])
        mm.ret=mm.symbols['PM_END'];mm.execute('PM')
        out=[mm.memory[mm.symbols['W']+j].val for j in range(3)]
        assert out==[0,0,0]
        if beta==64:witness={'beta':beta,'b':B,'m':2,'n':1,'U_words':[0,1],'V_words':[1],'printed_V_offset':1,'actual_output':out,'expected_output':[0,1,0]}
    return {'corrected_alias_cases':count,'printed_M_alias_counterexample':witness,'scope':'M v_j=w_(j+m); D q_j=u_(j+n) tested separately with D094 J1N'}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--resume',action='store_true');args=ap.parse_args()
    if OUT.exists() and not args.resume:raise SystemExit('Use --resume')
    data=json.loads(OUT.read_text()) if OUT.exists() else {'scope':'MIX D plus exercises25,26,30','blocks':{}}
    for name,fn in [('ordinary',ordinary),('targeted',targeted),('aliasing',aliasing)]:
        if name in data['blocks']:continue
        start=time.monotonic();res=fn();res['elapsed_seconds']=time.monotonic()-start
        data['blocks'][name]=res;OUT.write_text(json.dumps(data,indent=2)+'\n');print(name,'PASS',flush=True)
    print('ALL CHECKPOINTS COMPLETE',flush=True)
if __name__=='__main__':main()
