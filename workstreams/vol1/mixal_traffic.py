"""Traffic controller, §1.3.2-20, with the published 2008 LDA * correction.

DelayMachine collapses only the separately proved DELAY body. External events
are handled by simulate, with JOV/JNOV sampled at instruction start and light
changes at instruction completion. That convention is explicit, not a claim
that the book defines the within-instruction sampling instant.
"""
from math import ceil
from mix_machine import Machine, number
from mixal import Assembly, put


def delay_rows():
    return [('DELAY','STJ','1F'),('','DECA','6'),('','DECA','2'),
            ('','JAP','*-1'),('','JAN','*+2'),('','NOP',''),('1H','JMP','*')]


def program():
    return [('BSIZE','EQU','1(4:4)'),('2BSIZE','EQU','2(4:4)'),
            ('','ORIG','100')] + delay_rows() + [
        ('FLASH','STJ','2F'),('','ENT2','8'),('1H','LDA','=49991='),
        ('','JMP','DELAY'),('','DECX','0,1'),('','LDA','=49996='),
        ('','JMP','DELAY'),('','INCX','0,1'),('','DEC2','1'),('','J2Z','1F'),
        ('','LDA','*'),('','JMP','1B'),('1H','LDA','=399992='),
        ('','JMP','DELAY'),('2H','JMP','*'),('WAIT','JNOV','*'),
        ('TRIP','INCX','BSIZE'),('','ENT1','2BSIZE'),('','JMP','FLASH'),
        ('','LDX','BAMBER'),('','LDA','=799995='),('','JMP','DELAY'),
        ('','LDX','AGREEN'),('','LDA','=799996='),('','JMP','DELAY'),
        ('','INCX','1'),('','ENT1','2'),('','JMP','FLASH'),('','LDX','AAMBER'),
        ('','JOV','*+1'),('','LDA','=499994='),('','JMP','DELAY'),
        ('BEGIN','LDX','BGREEN'),('','LDA','=1799994='),('','JMP','DELAY'),
        ('','JMP','WAIT'),('AGREEN','ALF',' CABA'),('AAMBER','ALF',' CBBB'),
        ('BGREEN','ALF',' ACAB'),('BAMBER','ALF',' BCBB'),('','END','BEGIN')]


class DelayMachine(Machine):
    def __init__(self,b,delay):
        super().__init__(b)
        self.delay=delay
        self.summarized_calls=0

    def step(self):
        if self.pc != self.delay:
            return super().step()
        n=self.reg[0].value(self.b)
        assert 0 <= n < self.B
        return_to=self.j
        # STJ modifies exactly the address field of the final JMP.
        location=self.delay+6
        self.write(location,put(self.read(location),number(return_to,self.b),2))
        k=max(1,(n-5)//2)
        self.reg[0]=number(n-6-2*k,self.b)
        self.pc=return_to
        self.j=self.delay+7
        duration=max(n,7)
        self.time+=duration
        self.steps+=duration-1  # STJ costs 2u; every other instruction costs1u.
        self.summarized_calls+=1


def simulate(events=(),horizon=13_000_000,b=64):
    """Return every changed light state and overflow read, in MIX units.

    Each input event sets the overflow toggle. An event exactly at an
    instruction boundary is available to the following instruction. Events
    inside a DELAY are safely aggregated because DELAY never reads the toggle.
    The idle JNOV loop is similarly skipped only until the next event.
    """
    rows=program();a=Assembly(rows,b);sym=lambda s:a.symbols[s].value(b)
    m=DelayMachine(b,sym('DELAY'));a.load(m);m.pc=a.start
    event_list=sorted(events);i=0;trace=[];reads=[]
    while m.time < horizon:
        while i<len(event_list) and event_list[i]<=m.time:
            m.overflow=True;i+=1
        if m.pc==sym('WAIT') and not m.overflow:
            next_time=min(horizon,ceil(event_list[i]) if i<len(event_list) else horizon)
            if next_time>m.time:
                m.steps+=next_time-m.time;m.time=next_time;m.j=m.pc+1
                continue
        old=m.reg[7];pc=m.pc;t=m.time;w=m.read(pc)
        if w.digits[-1]==39 and w.digits[-2] in (2,3):
            reads.append({'time':t,'overflow':m.overflow,'op':'JOV' if w.digits[-2]==2 else 'JNOV'})
        m.step()
        if m.reg[7]!=old:
            trace.append({'time':m.time,'lights':list(m.reg[7].digits[1:]),'pc':pc})
        assert not m.halted
        assert len(trace)<10000
    return {'trace':trace,'toggle_reads':reads,'final_time':m.time,
            'instructions':m.steps,'summarized_delay_calls':m.summarized_calls,
            'final_overflow':m.overflow}
