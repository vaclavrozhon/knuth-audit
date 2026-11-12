"""Actual complete MIX simulator with own ex6/7 handlers vs event oracle."""
from pathlib import Path
import json
from io_program import assembly
from check_extensions import Devices
from mix_io import IOMachine
from mix_machine import Machine,number,instruction,Word,Undefined

ROOT=Path(__file__).resolve().parent


class Oracle(Machine):
    def __init__(self,b,delayed):
        super().__init__(b);self.dev=Devices(delayed);self.dev.mem=self.mem

    def _finish_input(self):
        self.dev.advance(self.time)

    def step(self):
        self._finish_input();w=self.read(self.pc)
        a,z,i,u,c=w.digits
        if c==5 and u==2:
            self.dev.finish();self.time=self.dev.t
        if not 34<=c<=38:return super().step()
        if u not in (16,18):raise Undefined('device')
        m=w.sign*(a*self.b+z)+(self.reg[i].value(self.b) if i else 0)
        self.pc+=1
        if c in (34,38):
            take=self.dev.busy(u) if c==34 else not self.dev.busy(u)
            if take:
                if c==34 and m==self.pc-1:
                    self.j=self.pc;self.dev.advance(self.dev.requests[u].ready)
                    self.time=self.dev.t
                else:self.jump(m)
            self.time+=1
        else:
            self.dev.issue(u,{35:'IOC',36:'IN',37:'OUT'}[c],m)
            self.time=self.dev.t
        self.steps+=1


def run_case(b,delayed,physical_delay,rows,name):
    asm,lines=assembly(b,delayed);sy={k:v.value(b) for k,v in asm.symbols.items()}
    h=IOMachine(b,delay=physical_delay);asm.load(h)
    d=Oracle(b,delayed)
    h.program(0,rows);d.program(0,rows)
    for machine in (h,d):
        machine.mem[2000:2024]=[number(k+100,b) for k in range(24)]
        machine.mem[900]=number(b**5-1,b)
        machine.mem[901]=number(1,b)
    cards=[tuple(number(k+v,b) for k in range(16)) for v in (0,16,32)]
    h.inputs[16].extend(cards);d.dev.cards.extend(cards)
    d.run(0,limit=100000)
    h.run(sy['BEGIN'],limit=300000)
    actual=[number(h.mem[sy['SIGNA']+r].value(b)*h.mem[sy['AREG']+r].magnitude(b),b,
                   h.mem[sy['SIGNA']+r].value(b)) for r in range(8)]
    assert actual==d.reg,(name,'regs',b,delayed)
    assert h.mem[:3500]==d.mem[:3500],(name,'memory',b,delayed)
    assert h.mem[sy['JREG']].value(b)==d.j,(name,'J',b,delayed)
    assert h.reg[6].value(b)==d.pc,(name,'pc',b,delayed)
    assert h.mem[sy['CLOCK']].value(b)==d.time,(name,'clock',b,delayed,h.mem[sy['CLOCK']].value(b),d.time)
    assert bool(h.mem[sy['OVTOG']].value(b))==d.overflow,(name,'overflow')
    assert h.mem[sy['COMPI']].value(b)==d.comparison,(name,'comparison')
    actual_output=list(h.outputs[18])
    expected_output=[v for v in d.dev.output if v!='PAGE']
    assert actual_output==expected_output,(name,'output')
    assert len(h.controls)==d.dev.output.count('PAGE'),(name,'page')
    assert not h.devices,(name,'undrained I/O')
    return {'name':name,'b':b,'delayed':delayed,'physical_delay':physical_delay,
            'simulated_u':d.time,'host_u':h.time,'host_steps':h.steps}


def main():
    templates={
        'overlap_and_fast_wait':[('IN',1000,0,16),('OUT',2000,0,18),('JBUS',2,0,16),('HLT',0)],
        'implicit_same_unit_wait':[('IN',1000,0,16),('IN',1100,0,16),('OUT',2000,0,18),('OUT',2000,0,18),('HLT',0)],
        'immediate_halt':[('IN',1000,0,16),('OUT',2000,0,18),('HLT',0)],
        'printer_control':[('OUT',2000,0,18),('IOC',0,0,18),('OUT',2000,0,18),('HLT',0)],
        'ready_branch':[('JRED',2,0,16),('HLT',0),('IN',1000,0,16),('JRED',7,0,16),('JBUS',6,0,16),('HLT',0),('JBUS',6,0,16),('HLT',0)],
        'indexed_buffer':[('ENT1',3),('IN',997,1,16),('OUT',1997,1,18),('JBUS',3,0,18),('HLT',0)],
        'flags_preserved':[('LDA',900),('ADD',901),('CMPA',901),('IN',1000,0,16),('OUT',2000,0,18),('JBUS',5,0,16),('HLT',0)],
        'boundary_buffers':[('IN',3484,0,16),('OUT',2000,0,18),('JBUS',2,0,16),('OUT',3476,0,18),('HLT',0)]
    }
    cases=[]
    for b in range(64,101):
        for delayed in (False,True):
            for physical_delay in (0,17):
                for name,rows in templates.items():
                    cases.append(run_case(b,delayed,physical_delay,rows,name))
    # Exact due-time boundaries in actual MIX TICK; no long artificial delay loop.
    boundary=[]
    for b in (64,100):
        for unit,op,due,addr in ((16,'IN',5000,1000),(18,'OUT',3750,2000)):
            for t in (due-1,due,due+1):
                asm,_=assembly(b,True);sy={k:v.value(b) for k,v in asm.symbols.items()}
                h=IOMachine(b,delay=17);asm.load(h);idx=0 if unit==16 else 1
                h.mem[sy['CLOCK']]=number(t,b);h.mem[sy['DUE']+idx]=number(due,b)
                h.mem[sy['COMMAND']+idx]=instruction(b,op,addr,f=unit)
                h.reg[1]=number(-17,b);h.j=3000
                h.inputs[16].append(tuple(number(k+1,b) for k in range(16)))
                h.mem[2000:2024]=[number(k+1,b) for k in range(24)]
                h.run(sy['TICK'],stop=3000)
                assert h.reg[1].value(b)==-17
                assert (h.mem[1000].value(b)==1 if unit==16 else bool(h.outputs[18]))==(t>=due)
                boundary.append({'b':b,'unit':unit,'clock':t,'transfer':t>=due})
    diagnostics=[]
    for op,m,u,error in [('IN',1000,18,'FERROR'),('OUT',2000,16,'FERROR'),('IOC',0,16,'FERROR'),
                          ('IOC',1,18,'ADDRERROR'),('JBUS',0,17,'FERROR'),('IN',3485,16,'MEMERROR'),
                          ('OUT',3477,18,'MEMERROR'),('IN',-1,16,'MEMERROR')]:
        asm,_=assembly();sy={k:v.value(64) for k,v in asm.symbols.items()};h=IOMachine();asm.load(h)
        h.mem[0]=instruction(64,op,m,f=u);h.run(sy['BEGIN'],stop=sy[error]);diagnostics.append([op,m,u,error])
    result={'cases':len(cases),'radices':37,'physical_delays':[0,17],
            'max_assembly_word':3965,'due_boundaries':boundary,'diagnostics':diagnostics,
            'representative_cases':cases[:16],
            'limits':['Integer MIX and units16/18 only','CLOCK and ready times must remain representable',
                      'Undefined early buffer access not assigned a universal hardware meaning',
                      'Physical host I/O waited synchronously at simulated transfer time; logical device remains busy until ready']}
    (ROOT/'results/io.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'cases':len(cases),'boundaries':len(boundary),'diagnostics':len(diagnostics),'last_word':3965}))


if __name__=='__main__':main()
