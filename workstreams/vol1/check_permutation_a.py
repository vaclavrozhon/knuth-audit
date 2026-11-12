"""Check Program A against independent maps and all printed frequency identities.

Large capacity and empty-cycle witnesses have separate completed checks. This
suite checks valid nonempty cycles, positional blanks, I/O and finite bounds.
"""
from collections import Counter
from itertools import permutations,product
from pathlib import Path
import json,random,time
from mixal import Assembly,CHARACTERS
from mix_io import IOMachine
from mixal_permutation_a import program,LINES,cycle_tokens,cards_from_tokens
ROOT=Path(__file__).resolve().parent
LP,RP,BLANK='    (',')    ','     '
checks=0;started=time.monotonic();runs=[]
def check(condition,context=None):
    global checks
    assert condition,context
    checks+=1

def decode(word):return ''.join(CHARACTERS[x] for x in word.digits)

def reference(cycles):
    names=set(x for c in cycles for x in c)
    result={x:x for x in names}
    for c in cycles:
        mapping=dict(zip(c,c[1:]+c[:1]))
        result={x:mapping.get(y,y) for x,y in result.items()}
    todo=set(names);orbits=[]
    while todo:
        start=min(todo);orbit=[];x=start
        while x not in orbit:
            orbit.append(x);todo.remove(x);x=result[x]
        check(x==start)
        orbits.append(orbit)
    return result,orbits

def run(cycles,tokens=None,b=64,delay=0):
    if tokens is None:tokens=cycle_tokens(cycles)
    cards=cards_from_tokens(tokens);flat=[decode(w) for card in cards for w in card][:-1]
    mapping,orbits=reference(cycles)
    X=len(cards);Y=sum(w!=BLANK for w in flat);M=len(cycles);N=len(mapping)
    U=len(orbits);V=sum(len(c)==1 for c in orbits)
    after_left=after_name=0;previous=None;name_positions=[]
    for i,w in enumerate(flat):
        if w==BLANK:
            after_left+=previous==LP
            after_name+=previous not in (None,LP,RP)
        else:
            previous=w
            if w not in (LP,RP):name_positions.append(i)
    a=Assembly(program(),b);m=IOMachine(b,delay);a.load(m);m.inputs[16].extend(cards);m.pc=a.start
    line_at={loc:k for k,loc in zip(sorted(LINES),a.locations)}
    freq=Counter();tags=Counter();core_time=0;before_output=None;walk_source=None
    while not m.halted:
        line=line_at[m.pc];freq[line]+=1
        if line==64:walk_source=decode(m.reg[7])
        if line==67:tags[m.reg[3].value(b)]+=1
        if line==80:
            current=decode(m.reg[7]);check(current==mapping[walk_source],(cycles,walk_source,current));walk_source=current
        if line==48:
            length=m.reg[1].value(b)-1200
            before_output=[decode(w) for w in m.mem[1200:1200+length]]
        oldtime=m.time;m.step()
        if 23<=line<=46 or 64<=line<=86:core_time+=m.time-oldtime
        assert m.steps<300000
    cpu=m.time;m.finish_io()
    check(before_output is not None)
    check(tags==Counter({i:1 for i in name_positions}),(cycles,tags,name_positions))
    check(all(m.mem[i].sign==-1 for i,w in enumerate(flat) if w!=BLANK))
    # Parse the actual answer and recover its map independently of output order.
    parsed=[];cursor=0
    while cursor<len(before_output):
        check(before_output[cursor]==LP);cursor+=1;cycle=[]
        while before_output[cursor]!=RP:cycle.append(before_output[cursor]);cursor+=1
        cursor+=1;check(len(cycle)>=2);parsed.append(cycle)
    printed=[x for c in parsed for x in c]
    check(len(set(printed))==len(printed))
    check(set(printed)=={x for x,y in mapping.items() if x!=y})
    output_map={x:x for x in mapping}
    for c in parsed:output_map.update(zip(c,c[1:]+c[:1]))
    check(output_map==mapping)
    check(len(before_output)==N+2*U-3*V)
    actual=[''.join(decode(w) for w in row) for row in m.outputs[18]]
    echo=[''.join(decode(w) for w in card)+' '*40 for card in cards]
    answer=''.join(before_output or [LP,RP]);answer+=' '*((-len(answer))%120)
    check(actual[:X]==echo);check(''.join(actual[X:])==answer)
    check(not m.overflow and not m.inputs[16] and not m.devices)
    F={symbol:freq[line] for symbol,line in dict(A=26,B=29,C=33,D=35,E=41,F=42,G=44,H=64,J=67,K=75,L=77,P=80,Q=72,R=82,S=85).items()}
    check(F['A']==F['C']==16*X-1-M-after_left)
    check(F['B']==F['D']==M);check(F['E']==U+1);check(F['F']==U+F['G'])
    check(F['H']==F['R']==U);check(F['J']==Y-2*M);check(F['K']==F['L']-U)
    check(F['P']==N);check(F['Q']==N-U);check(F['S']==V)
    check(F['G']+F['J']+after_name+F['L']==(16*X-1)*(N+1))
    check(freq[30]==freq[31]==freq[32]==M+after_left)
    check(freq[68]==freq[69]==freq[70]==F['J']+after_name);check(freq[71]==after_name)
    weights=dict(A=5,B=6,C=7,D=2,E=1,F=3,G=4,H=8,J=6,K=3,L=4,P=3,Q=4,R=6,S=2)
    check(core_time==7+sum(weights[k]*v for k,v in F.items())+4*after_left+5*after_name)
    expected=112*N*X+304*X-2*M-Y+11*U+2*V-11-8*after_left-2*after_name
    check(core_time==expected,(cycles,tokens,F,core_time,expected))
    record=dict(radix=b,cards=X,nonblank=Y,input_cycles=M,names=N,cycles=U,singletons=V,
                blanks_after_left=after_left,blanks_after_name=after_name,core_time=core_time,
                cpu_time=cpu,instructions=m.steps,output=''.join(before_output or [LP,RP]))
    runs.append(record);return record

small=['A0001','B0001','C0001']
all_cycles=[list(c) for k in range(1,4) for c in permutations(small,k)]
for c in all_cycles:run([c])
for c,d in product(all_cycles,repeat=2):run([c,d])
example=[[x.ljust(5) for x in c] for c in ['ACFG','BCD','AED','FADE','BGFAE']]
for b in range(64,101):
    r=run(example,b=b,delay=1000)
    check((r['cards'],r['nonblank'],r['input_cycles'],r['names'],r['cycles'],r['singletons'],r['core_time'])==(2,29,5,7,3,1,2161))
# Every single blank position, plus consecutive interior blanks, at fixed data.
raw=cycle_tokens([small,small[::-1]])
for i in range(len(raw)+1):
    run([small,small[::-1]],raw[:i]+[BLANK]*3+raw[i:])
rng=random.Random(13301)
for _ in range(60):
    pool=[f'N{k:04d}' for k in range(rng.randrange(1,13))]
    cycles=[rng.sample(pool,rng.randrange(1,len(pool)+1)) for _ in range(rng.randrange(1,9))]
    tokens=[]
    for w in cycle_tokens(cycles):tokens.extend([BLANK]*rng.randrange(4));tokens.append(w)
    run(cycles,tokens,b=rng.choice([64,65,100]),delay=rng.choice([0,17,1000]))
# Names are complete five-character fields; punctuation and zeros are names too.
run([['00000','  =  ',' 0) ('],['  =  ','00000']],b=100,delay=1000)
# Last accepted input card and the completely blank representation of identity.
run([small[:2]],cycle_tokens([small[:2]])+[BLANK]*(1199-4),delay=1000)
run([[small[0]]],[LP]+[BLANK]*1196+[small[0],RP],b=100,delay=1000)
run([])
result=dict(checks=checks,instruction_limit_checks=sum(r['instructions'] for r in runs),runs=len(runs),elapsed_seconds=time.monotonic()-started,
            suite='All pairs of nonempty cycles on three names;37 radix sample profiles;blanks,75-card boundary,independent maps',details=runs)
(ROOT/'results/permutation-a.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='details'}))
