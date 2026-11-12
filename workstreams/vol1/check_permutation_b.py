"""Independent composition, output cycles and exact Program B timing."""
from collections import Counter
from itertools import permutations,product
from pathlib import Path
import json,random,time
from mixal import Assembly,CHARACTERS
from mix_io import IOMachine
from mixal_permutation_a import cycle_tokens,cards_from_tokens
from mixal_permutation_b import program,LINES
ROOT=Path(__file__).resolve().parent
LP,RP,BLANK='    (',')    ','     '
checks=0;started=time.monotonic();runs=[]
def check(value,context=None):
    global checks
    assert value,context
    checks+=1

def decode(w):return ''.join(CHARACTERS[x] for x in w.digits)

def reference(cycles):
    mapping={x:x for c in cycles for x in c}
    for c in cycles:
        factor=dict(zip(c,c[1:]+c[:1]));mapping={x:factor.get(y,y) for x,y in mapping.items()}
    todo=set(mapping);orbits=[]
    while todo:
        x=min(todo);c=[]
        while x not in c:c.append(x);todo.remove(x);x=mapping[x]
        check(x==c[0]);orbits.append(c)
    return mapping,orbits

def run(cycles,tokens=None,b=64,delay=0,max_words=1200,expanded=False):
    if tokens is None:tokens=cycle_tokens(cycles)
    cards=cards_from_tokens(tokens);flat=[decode(w) for c in cards for w in c][:-1]
    X=len(cards);Y=sum(x!=BLANK for x in flat);M=len(cycles)
    mapping,orbits=reference(cycles);N=len(mapping);U=len(orbits);V=sum(len(c)==1 for c in orbits)
    seen=[];search=0
    for x in reversed(flat):
        if x in (LP,RP,BLANK):continue
        if x in seen:search+=len(seen)-seen.index(x)
        else:search+=len(seen)+1;seen.append(x)
    a=Assembly(program(True,max_words,expanded),b);m=IOMachine(b,delay);a.load(m)
    # The optional MAXANS EQU has no location. Match instruction PCs through
    # independently assembled original-line triples instead of location offsets.
    locations=[a.locations[0],*a.locations[2:]] if expanded else a.locations
    line_at={loc:k for k,loc in zip(sorted(LINES),locations)}
    m.inputs[16].extend(cards);m.pc=a.start;freq=Counter();core=0;table_checked=False;answer=None
    while not m.halted:
        line=line_at[m.pc];freq[line]+=1
        if line==54:
            check(m.reg[3].value(b)==N)
            names={i:decode(m.mem[i]) for i in range(1,N+1)}
            actual={names[i]:names[m.mem[max_words+i].value(b)] for i in names}
            check(actual==mapping);check([names[i] for i in range(1,N+1)]==seen);table_checked=True
        if line==70:
            ans=a.symbols['ANS'].value(b);answer=[decode(w) for w in m.mem[ans:m.reg[1].value(b)]]
        old=m.time;m.step()
        if 25<=line<=68:core+=m.time-old
        assert m.steps<4000000
    cpu=m.time;m.finish_io();check(table_checked and answer is not None)
    parsed=[];i=0
    while i<len(answer):
        check(answer[i]==LP);i+=1;c=[]
        while answer[i]!=RP:c.append(answer[i]);i+=1
        i+=1;check(len(c)>=2);parsed.append(c)
    printed=[x for c in parsed for x in c];check(len(printed)==len(set(printed)))
    check(set(printed)=={x for x,y in mapping.items() if x!=y})
    actual_map={x:x for x in mapping}
    for c in parsed:actual_map.update(zip(c,c[1:]+c[:1]))
    check(actual_map==mapping);check(len(answer)==N+2*U-3*V)
    output=[''.join(decode(w) for w in row) for row in m.outputs[18]]
    expected=''.join(answer or [LP,RP]);expected+=' '*((-len(expected))%120)
    check(output[:X]==[''.join(decode(w) for w in c)+' '*40 for c in cards]);check(''.join(output[X:])==expected)
    check(not m.overflow and not m.inputs[16] and not m.devices)
    F={name:freq[line] for name,line in dict(A=27,B=28,C=31,D=33,E=35,F=37,G=40,H=41,J=45,K=49,L=51,P=52,Q=56,R=58,S=60,T=61,W=66,Z=67).items()}
    check(F['A']==M+1);check(F['B']==16*X-1);check(F['C']==Y);check(F['D']==Y-M)
    check(F['E']==F['G']==F['J']==Y-2*M);check(F['F']==search);check(F['H']==N)
    check(F['K']==F['L']==M);check(F['P']==16*X-1-Y+M)
    check(F['Q']==F['Z']==N);check(F['R']==U);check(F['S']==F['W']==U-V);check(F['T']==N-V)
    weights=dict(A=1,B=4,C=3,D=3,E=3,F=4,G=1,H=6,J=7,K=2,L=2,P=1,Q=3,R=3,S=3,T=10,W=3,Z=2)
    check(core==4+sum(weights[k]*v for k,v in F.items()))
    check(core==4*search+16*Y+80*X+21*N-19*M+9*U-16*V,(cycles,F,core))
    runs.append(dict(radix=b,cards=X,nonblank=Y,input_cycles=M,names=N,cycles=U,singletons=V,
                     comparisons=search,core_time=core,cpu_time=cpu,instructions=m.steps,output=''.join(answer or [LP,RP]),
                     max_words=max_words,expanded_answer=expanded))
    return runs[-1]

small=['A0001','B0001','C0001']
all_cycles=[list(c) for k in range(1,4) for c in permutations(small,k)]
for c in all_cycles:run([c])
for c,d in product(all_cycles,repeat=2):run([c,d])
example=[[x.ljust(5) for x in c] for c in ['ACFG','BCD','AED','FADE','BGFAE']]
for b in range(64,101):
    r=run(example,b=b,delay=1000);check(r['core_time']==983 and r['comparisons']==74)
raw=cycle_tokens([small,small[::-1]])
for i in range(len(raw)+1):run([small,small[::-1]],raw[:i]+[BLANK]*3+raw[i:])
rng=random.Random(13302)
for _ in range(60):
    pool=[f'N{k:04d}' for k in range(rng.randrange(1,13))]
    cycles=[rng.sample(pool,rng.randrange(1,len(pool)+1)) for _ in range(rng.randrange(1,9))]
    tokens=[]
    for w in cycle_tokens(cycles):tokens.extend([BLANK]*rng.randrange(4));tokens.append(w)
    run(cycles,tokens,b=rng.choice([64,65,100]),delay=rng.choice([0,17,1000]))
run([['00000','  =  ',' 0) ('],['  =  ','00000']],b=100,delay=1000)
run([small[:2]],cycle_tokens([small[:2]])+[BLANK]*(1199-4),delay=1000)
run([[small[0]]],[LP]+[BLANK]*1196+[small[0],RP],b=100,delay=1000)
run([])
# A documented capacity repair for B reduces the limit to60 cards and expands
# the reused PERM/ANS area. Its general memory bound is proved in the note.
for b in range(64,101):
    a=Assembly(program(True,960,True),b);check(max(a.memory)<4000)
t=318;aa=[f'A{k:04d}' for k in range(1,t+1)];bb=[f'B{k:04d}' for k in range(1,t+1)]
second=[aa[0]]
for k in range(t-1,-1,-1):
    second.append(bb[k])
    if k:second.append(aa[k])
for b in (64,100):
    r=run([aa,second],b=b,delay=1000,max_words=960,expanded=True)
    check(r['cards']==60 and len(r['output'])//5==4*t)
result=dict(checks=checks,runs=len(runs),elapsed_seconds=time.monotonic()-started,details=runs)
(ROOT/'results/permutation-b.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='details'}))
