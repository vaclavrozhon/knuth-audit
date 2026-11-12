"""Check whether the answer12 end-of-input change preserves COMPUTE's CI."""
from pathlib import Path
import json
import sys

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parents[1]))
from mix_machine import Word
from mixal import Assembly
from io_model import TapeIO
from programs import comparison_example

checks=0
cases=[]
for b in [64,100]:
    for delay in [0,17,10000]:
        for ci in [-1,0,1]:
            for variant in ['none','printed','preserve_ci']:
                a=Assembly(comparison_example(variant,ci),b)
                m=TapeIO(b,delay=delay);a.load(m)
                m.inputs[16].append(tuple(Word(1,(0,0,0,0,0)) for _ in range(16)))
                m.inputs[16].append(tuple([Word(1,(0,0,0,0,0))]*15+[Word(1,(0,0,0,0,40))]))
                m.run(a.start,limit=100000);m.finish_io()
                success=m.pc==a.symbols['SUCCESS'].value(b)+1
                assert success==(ci==0 if variant=='printed' else True),(b,delay,ci,variant)
                checks+=1
                assert m.reg[0]==m.zero,'A is correctly preserved even in bad printed variant'
                checks+=1
                assert not m.inputs[16] and m.reg[6].value(b)==0
                checks+=1
                cases.append({'b':b,'delay':delay,'initial_CI':ci,'variant':variant,
                              'final_CI':m.comparison,'success_branch':success})
result={'checks':checks,'cases':cases,'scope':'Two actual input cards, second ending in period; original control, printed answer12, and local CI-preserving repair.','finding':'Printed answer12 changes the comparison indicator across an inserted JRED CONTROL poll; A is preserved.'}
(ROOT/'results/comparison.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'checks':checks,'runs':len(cases),'printed_wrong_branches':sum(not x['success_branch'] for x in cases if x['variant']=='printed')},indent=2))
