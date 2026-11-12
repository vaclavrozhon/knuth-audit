"""Constructive event model for exercises6/7 and separate scope counterexample.

No printed MIX I/O solution is supplied. This model supplies an independent
algorithmic existence check, not an unprinted MIX transcription.
"""
from dataclasses import dataclass
from pathlib import Path
import json
from programs import tracer
from mix_machine import Machine,number,instruction

ROOT=Path(__file__).resolve().parent


@dataclass
class Request:
    unit:int
    op:str
    addr:int
    transfer:int
    ready:int
    payload:tuple=()
    done:bool=False


class Devices:
    """t denotes simulated instruction-start time; durations start at issue."""
    def __init__(self,delayed):
        self.delayed=delayed;self.t=0;self.j=0
        self.mem=[0]*3500;self.requests={};self.output=[];self.cards=[];self.transfers=[]

    def advance(self,t):
        assert t>=self.t
        for r in sorted(self.requests.values(),key=lambda r:(r.transfer,r.unit)):
            if not r.done and r.transfer<=t:
                if r.op=='IN':self.mem[r.addr:r.addr+16]=r.payload
                if r.op=='OUT':self.output.append(tuple(self.mem[r.addr:r.addr+24]))
                if r.op=='IOC':self.output.append('PAGE')
                self.transfers.append((r.unit,r.op,r.transfer));r.done=True
        self.t=t

    def busy(self,u):
        return u in self.requests and self.t<self.requests[u].ready

    def issue(self,u,op,addr=0):
        if (u,op) not in ((16,'IN'),(18,'OUT'),(18,'IOC')):raise ValueError('unsupported device/operator')
        n=16 if op=='IN' else 24 if op=='OUT' else 0
        if op=='IOC' and addr!=0 or n and not 0<=addr<=3500-n:raise ValueError('buffer address')
        if self.busy(u):self.advance(self.requests[u].ready)
        T=7500 if op=='OUT' else 10000
        payload=tuple(self.cards.pop(0)) if op=='IN' else ()
        if op=='IN':assert len(payload)==16
        self.requests[u]=Request(u,op,addr,self.t+(T//2 if self.delayed else 0),self.t+T,payload)
        self.advance(self.t+1)

    def wait_loop(self,u,p,fast):
        while self.busy(u):
            self.j=p+1
            self.advance(self.requests[u].ready if fast else self.t+1)
        self.advance(self.t+1) # final, non-taken JBUS

    def finish(self):
        self.advance(max([self.t]+[r.ready for r in self.requests.values()]))


def main():
    waits=0
    for delayed in (False,True):
        for u,op in ((16,'IN'),(18,'OUT'),(18,'IOC')):
            T=7500 if op=='OUT' else 10000
            for start in (1,T//2-1,T//2,T//2+1,T-1,T,T+1):
                states=[]
                for fast in (False,True):
                    d=Devices(delayed);d.cards=[tuple(range(16))];d.mem[100:124]=range(24)
                    d.issue(u,op,0 if op=='IOC' else 100);d.advance(start)
                    d.wait_loop(u,700,fast)
                    states.append((d.t,d.j,d.mem,d.output,d.transfers))
                assert states[0]==states[1]
                waits+=1
    d=Devices(True);d.cards=[tuple(range(16))];d.issue(16,'IN',100)
    assert d.mem[101]==0
    d.advance(4999);assert d.mem[101]==0
    d.advance(5000);assert d.mem[101]==1 and d.busy(16)
    d.advance(10000);assert not d.busy(16)
    d=Devices(True);d.mem[100:124]=range(24);d.issue(18,'OUT',100)
    d.advance(3749);d.mem[100]=99
    d.advance(3750);assert d.output[0][0]==99 and d.busy(18)
    d=Devices(True);d.cards=[tuple(range(16)),tuple(range(16,32))]
    d.issue(16,'IN',100);d.issue(18,'OUT',200);d.issue(16,'IN',300)
    assert d.t==10001 and d.mem[101]==1 and len(d.output)==1
    d.finish();assert d.t==20000 and d.mem[301]==17
    # The literal restriction6(a) prohibits stores, but this program only reads.
    scope=[]
    for b in range(64,101):
        asm=tracer(b);sy={k:v.value(b) for k,v in asm.symbols.items()}
        vals=[]
        for traced in (False,True):
            m=Machine(b);asm.load(m);m.mem[100]=instruction(b,'LDA',sy['AREG'])
            m.reg[0]=number(1,b);m.reg[7]=number(101,b);m.j=100
            if traced:m.run(sy['ENTER'],stop=101)
            else:m.pc=100;m.step()
            vals.append(m.reg[0].value(b))
        assert vals==[0,1]
        scope.append({'b':b,'AREG':sy['AREG'],'direct_A':vals[0],'traced_A':vals[1]})
    result={'busy_loop_equivalences':waits,'delayed_transfer_boundaries':'passed',
            'implicit_wait_and_halt_drain':'passed','trace_private_read':scope,
            'limits':['I/O is a constructive event model, not assembled MIX source',
                      'T measured from instruction issue; arbitrary absolute epoch is irrelevant',
                      'Finite tests support event invariants stated in NOTES.md']}
    (ROOT/'results/extensions.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='trace_private_read'},indent=2))


if __name__=='__main__':main()
