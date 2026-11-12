"""Direct character histogram versus the asynchronous MIX counter."""
from collections import Counter
from pathlib import Path
import json,random
from mixal_crypt import program
from mixal import Assembly,CHAR_CODE,CHARACTERS
from mix_io import IOMachine
from mix_machine import Word,number

ROOT=Path(__file__).resolve().parent
checks=0

def check(ok,label):
    global checks
    if not ok:raise AssertionError(label)
    checks+=1


def run(s,b,delay,seeds=None):
    a=Assembly(program(),b);m=IOMachine(b,delay);a.load(m)
    if seeds:
        for c,value in seeds.items():m.mem[1000+CHAR_CODE[c]]=number(value,b)
    end=s.index('*');blocks=(end//70)+2
    s=s.ljust(blocks*70,'X')[:blocks*70]
    for k in range(blocks):
        chars=s[k*70:(k+1)*70]
        m.inputs[20].append([Word(1,tuple(CHAR_CODE[c] for c in chars[i:i+5])) for i in range(0,70,5)])
    m.run(a.start,limit=200000);m.finish_io()
    counts=Counter(seeds or {});counts.update(c for c in s[:end] if c!=' ')
    check(all(m.mem[1000+CHAR_CODE[c]].value(b)==v for c,v in counts.items()),('histogram',b,delay,s))
    check(m.mem[1000].value(b)==m.mem[1046].value(b)==-1,('special sentinels',b))
    actual=[''.join(CHARACTERS[d] for word in block for d in word.digits) for block in m.outputs[19]]
    expected=[(' '*10+c+'  '+f'{counts[c]:07}').ljust(70) for c in sorted(counts,key=CHAR_CODE.get) if counts[c]>0]
    check(actual==expected,('printed counts',b,delay,actual,expected))
    # Exactly one extra block is requested beyond the terminator-containing block.
    check(not m.inputs[20],('input buffering',b,delay,end))
    return len(expected)

rng=random.Random(13213);runs=0;lines=0
cases=['*',' '*300+'*','ABCDE'*47+'*IGNORE','AAAAA     '*20+'*',
       ''.join(c for c in CHARACTERS if c not in ' *')+'*']
cases += [('A '*(i//2)+'A'*(i%2))+'*Z' for i in range(70)]
cases += [''.join(rng.choice(CHARACTERS.replace('*','')) for _ in range(k))+'*AFTER' for k in (69,70,71,139,140,141,509)]
for b in (64,100):
    for delay in (0,43,1200):
        for s in cases:lines+=run(s,b,delay);runs+=1
        lines+=run('*',b,delay,{'A':1,'B':9999999,'Z':10257});runs+=1
result={'checks':checks,'runs':runs,'output_lines':lines,'radices':[64,100],
        'io_delays':[0,43,1200],'terminator_offsets_in_block':list(range(70)),
        'scope':'Valid MIX character input, nonnegative counts fitting the requested seven decimal columns; extra block after terminator.'}
(ROOT/'results/mixal-crypt.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
