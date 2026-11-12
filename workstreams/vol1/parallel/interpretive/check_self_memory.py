"""Native MIX lookup/update invariants and the full2000-word heap boundary."""
from pathlib import Path
import json
from selftrace_program import assembly
from mix_io import IOMachine
from mix_machine import number,instruction

ROOT=Path(__file__).resolve().parent
results=[]
for b in range(64,101):
    a=assembly(b);s={k:v.value(b) for k,v in a.symbols.items()}
    m=IOMachine(b);a.load(m)
    addresses=[0,1,1998,1999,2000,2999,3000,s['READRET'],s['WRITERET'],3999]
    reads=0
    def read(addr):
        global reads
        m.reg[1]=number(0,b,-1);m.reg[2]=number(-73,b)
        m.reg[7]=number(-19,b);m.reg[5]=number(addr,b);m.j=3998
        m.run(s['VREAD'],stop=3998)
        assert m.reg[1]==number(0,b,-1) and m.reg[2].value(b)==-73 and m.reg[7].value(b)==-19
        reads+=1
        return m.reg[0]
    for addr in addresses:
        expected=number(0,b) if addr<2000 else a.memory[addr if addr<3000 else addr-1000]
        assert read(addr)==expected
    for index,addr in enumerate(addresses):
        value=number(-(index+1),b)
        m.reg[1]=number(-17,b);m.reg[5]=number(addr,b);m.reg[7]=value;m.j=3998
        m.run(s['VWRITE'],stop=3998)
        assert m.reg[1].value(b)==-17 and m.reg[7]==value
        assert read(addr)==value
    used=m.mem[s['USED']].value(b)
    m.reg[5]=number(0,b,-1);m.reg[7]=number(0,b,-1);m.j=3998
    m.run(s['VWRITE'],stop=3998)
    assert m.mem[s['USED']].value(b)==used and read(0)==number(0,b,-1)
    assert all(m.mem[k]==a.memory[k] for k in range(2000,3000))
    # Start from a valid999-entry map and execute the last allocation and overflow.
    for k in range(999):
        m.mem[2*k]=number(k,b);m.mem[2*k+1]=number(k+1,b)
    m.mem[s['USED']]=number(1998,b)
    m.reg[5]=number(3999,b);m.reg[7]=number(-0,b,-1);m.j=3998
    m.run(s['VWRITE'],stop=3998)
    assert m.mem[s['USED']].value(b)==2000 and read(3999)==number(0,b,-1)
    m.reg[5]=number(3998,b);m.reg[7]=number(7,b);m.j=3998
    m.run(s['VWRITE'],stop=s['MEMFULL'])
    assert m.mem[s['USED']].value(b)==2000
    assert all(m.mem[k]==a.memory[k] for k in range(2000,3000))
    results.append({'b':b,'lookup_checks':reads,'negative_zero_preserved':True,
                    'last_allocation':2000,'next_allocation':'MEMFULL','ROM_unchanged':True})
(ROOT/'results/selftrace-memory.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({'radices':37,'lookups':sum(r['lookup_checks'] for r in results),
                  'full_capacity_transitions':37}))
