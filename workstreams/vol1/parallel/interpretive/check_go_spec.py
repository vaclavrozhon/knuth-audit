"""Actual MIX checks of the GO insertion and the new 2025 SPEC exercise."""
from pathlib import Path
import json
from programs import simulator
from check_simulator import one,COUNTS
from mix_machine import Machine,number,instruction,Word

ROOT=Path(__file__).resolve().parent
go=[]
for b in range(64,101):
    asm,lines=simulator(b);sy={k:v.value(b) for k,v in asm.symbols.items()}
    for delay in (0,17):
        h=Machine(b,card_delay=delay);asm.load(h)
        # A separate entry is equivalent to inserting the two instructions
        # between003/004, without relocating the whole printed program.
        h.program(3990,[('STZ',sy['TIME'],0,2),('IN',0,0,16),
                        ('JBUS',3992,0,16),('JSJ',sy['BEGIN']+1)])
        h.cards=[[instruction(b,'ENTA',13)]+[number(0,b)]*15]
        h.run(3990,stop=sy['CYCLE'])
        assert not h.pending and h.reg[6].value(b)==0
        h.step();h.run(h.pc,stop=sy['CYCLE'])
        assert h.mem[sy['AREG']].value(b)==13 and h.mem[sy['JREG']].value(b)==0
        go.append({'b':b,'delay':delay,'simulated_A':13,'simulated_J':0})
    for f in (0,1,2):
        for sign in (-1,1):
            rr=[number(0,b,sign)]*8
            rr[0]=Word(sign,(b-1,0,3,9,5));rr[7]=Word(-sign,(9,9,0,0,9))
            one(b,instruction(b,'NUM',f=f),rr,overflow=False,tag='SPEC')
            one(b,instruction(b,'NUM',f=f),rr,overflow=True,tag='SPEC')
    one(b,instruction(b,'NUM',f=3),expect_error='FERROR')
result={'GO_insertions':len(go),'SPEC_cases':COUNTS,'max_assembly_word':max(asm.memory),
        'notes':['Own SPEC solution uses10u for NUM/CHAR, explicitly credits1u for HLT',
                 'The simulated registers retain their separate signs throughout NUM/CHAR',
                 'GO entry verified with asynchronous card completion; JMP linkage is simulated J=0']}
(ROOT/'results/go-spec.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
