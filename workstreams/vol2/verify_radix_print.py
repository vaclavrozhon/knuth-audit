#!/usr/bin/env python3
"""Instruction simulation of 4.4-13 including the actual 24-word printer."""
from pathlib import Path
import json, random, time
from mix_float_machine import Machine,Word,word

ROOT=Path(__file__).resolve().parent
SOURCE=ROOT/'sources/radix-print.mix'


class PrintMachine(Machine):
    def __init__(self,beta,m,fixed,delay):
        super().__init__(beta,source=SOURCE)
        self.symbols.update(U=1000,BUF=2000,M=m)
        self.m=m;self.fixed=fixed;self.delay=delay
        self.outputs=[];self.pending=None;self.conflicts=[];self.blocks=[]
        self.max_steps=1000000;self.special={}
        # CHAR and OUT are intercepted as explicit suspension points; the
        # existing interpreter still executes every arithmetic instruction.
        for pc,row in enumerate(self.rows):
            if row[2] in ['CHAR','OUT']:
                self.special[pc]=row.copy();row[2]='HLT';row[3]='500'
        for a in range(2000,2052):self.memory[a]=word(0)
        self.memory[2000]=word(40*self.b**4) # MIX character 40 is a period.
        if not fixed:
            # The original ORIG puts the first instructions at BUF+40.
            # Encode those four words, including the guaranteed nonblank
            # ENT2 -40 bytes. Its sign does not affect character output.
            headers=[(2040+self.symbols['OFLO'],2,39),(40,2,50),(10,2,51),(m,2,49)]
            for j,(a,f,c) in enumerate(headers):
                self.memory[2040+j]=word((a//beta)*beta**4+(a%beta)*beta**3+f*beta+c)
        self.ret=self.symbols['R13FIX_END' if fixed else 'R13_END']

    def store(self,addr,field,v):
        if addr>=len(self.rows):
            if self.pending is not None and self.pending<=addr<self.pending+24:
                self.conflicts.append(addr)
            assert 1001<=addr<=1000+self.m or 2000<=addr<2048,(addr,field)
            old=self.memory.get(addr,word(0));l,r=field;n=r-max(l,1)+1
            mag=old.mag
            if n>0:
                factor=self.b**(5-r);mask=self.b**n
                mag+=(v.mag%mask-(mag//factor)%mask)*factor
            self.memory[addr]=Word(v.sign if l==0 else old.sign,mag)
        else:super().store(addr,field,v)

    def complete(self):
        if self.pending is not None:
            self.outputs.append([self.memory[a].mag for a in range(self.pending,self.pending+24)])
            self.pending=None

    def execute_print(self,U):
        den=self.w**self.m;assert 0<=U<den
        for j in range(1,self.m+1):self.memory[1000+j]=word(U//self.w**(self.m-j)%self.w)
        entry='R13FIX' if self.fixed else 'R13'
        for _ in range(30):
            # There are 20 CHAR events and 2 OUT events.
            self.halt=None;super().execute(entry)
            if self.pc==self.ret:break
            assert self.halt==500,(self.halt,self.trace[-8:])
            pc=self.pc-1;src,label,op,arg=self.special[pc]
            if op=='CHAR':
                a=self.reg['A'];x=self.reg['X'];assert a.mag<10**9
                self.blocks.append(a.mag);t=len(self.blocks)
                assert a.mag==(U*10**(9*t)//den)%10**9
                current=sum(self.memory[1000+j].mag*self.w**(self.m-j) for j in range(1,self.m+1))
                assert current==(U*10**(9*t))%den
                ds=[30+int(d) for d in f'{a.mag:010d}']
                self.reg['A']=Word(a.sign,sum(d*self.b**(4-j) for j,d in enumerate(ds[:5])))
                self.reg['X']=Word(x.sign,sum(d*self.b**(4-j) for j,d in enumerate(ds[5:])))
                self.time+=9 # CHAR has cost 10; the suspension cost was 1.
            else:
                # OUT must wait for the preceding device operation.
                self.complete();addr,field=self.operand(arg,pc)
                assert 8*field[0]+field[1]==18
                self.pending=addr
                if not self.delay:self.complete()
            self.symbols['CONTINUE']=self.pc;entry='CONTINUE'
        else:raise AssertionError('too many special operations')
        self.complete() # caller waits before reclaiming the buffers.
        assert len(self.blocks)==20 and len(self.outputs)==2
        assert ''.join(f'{d:09d}' for d in self.blocks)==f'{U*10**180//den:0180d}'
        return self

    def bytes(self,ws):
        return [w//self.b**j%self.b for w in ws for j in range(4,-1,-1)]

    def check_lines(self):
        for i,ws in enumerate(self.outputs):
            out=self.bytes(ws);expected=[]
            for j in range(10):
                expected += [40 if i==j==0 else 0]
                expected += [30+int(d) for d in f'{self.blocks[10*i+j]:09d}']
            assert out[:100]==expected
            if self.fixed:assert out[100:]==[0]*20
        if self.fixed:assert not self.conflicts


def main():
    start=time.monotonic();rng=random.Random(4413);cases=0;overflows=0;maximum_steps=0
    failures=[]
    for delay in [False,True]:
        q=PrintMachine(64,1,False,delay).execute_print(0);q.check_lines()
        assert any(q.bytes(q.outputs[1])[100:])
        if delay:assert set(q.conflicts)==set(range(2020,2024))
        failures.append({'delayed':delay,'input':0,'second_line_tail_codes':q.bytes(q.outputs[1])[100:],
                         'first_line_tail_codes':q.bytes(q.outputs[0])[100:],'overlapping_writes':q.conflicts})
    for beta in [64,128,256]:
        w=beta**5
        for m in [1,2,3,8,20,64]:
            den=w**m
            inputs=[0,1,den-1,den//2,den//3,den//10,den//10+1]
            inputs += [rng.randrange(den) for _ in range(8)]
            for U in inputs:
                q=PrintMachine(beta,m,True,bool(cases%2)).execute_print(U);q.check_lines()
                overflows+=q.visits['F12'];maximum_steps=max(maximum_steps,len(q.trace));cases+=1
    data={'scope':'4.4-13: exact arithmetic, 180 digits, 24-word asynchronous printer',
          'status':'passed','seconds':time.monotonic()-start,'corrected_cases':cases,
          'carry_overflow_branches':overflows,'max_instructions':maximum_steps,
          'original_buffer_counterexamples':failures}
    (ROOT/'results/radix-print.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data),flush=True)


if __name__=='__main__':main()
