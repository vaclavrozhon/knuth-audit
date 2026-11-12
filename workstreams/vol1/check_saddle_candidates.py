"""Only new third-variant checks; earlier saddle checkers are not repeated."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product,permutations
import json,random
from mixal_saddle_candidates import program,binary_mean,distinct_mean
from mixal_saddle import saddles,scalar2
from mixal import Assembly
from mix_machine import Machine,number
from saddle_expectations import binary_solution2,distinct_intervals

ROOT=Path(__file__).resolve().parent
checks=0

def check(ok,label):
    global checks
    if not ok:raise AssertionError(label)
    checks+=1


def expected(a):
    m,n=len(a),len(a[0]);hi=[max(row[j] for row in a) for j in range(n)]
    mu=min(hi);j0=max(j for j in range(n) if hi[j]==mu)
    records=1+sum(hi[j]<min(hi[j+1:]) for j in range(n-1))
    time=scalar2(a)[2]+records+2
    for i in reversed(range(m)):
        if a[i][j0]!=mu:time+=6;continue
        failed=next((k for k,x in enumerate(reversed(a[i])) if x<mu),None)
        if failed is None:return 1000+n+i*n+j0+1,time+6*n+7
        time+=6*(failed+1)+6
    return 0,time+2


def run(a,b=64):
    m,n=len(a),len(a[0]);asm=Assembly(program(m,n),b);machine=Machine(b);asm.load(machine)
    for i,row in enumerate(a):
        for j,x in enumerate(row):machine.mem[1000+n+i*n+j+1]=number(x,b)
    machine.run(asm.start)
    answer=machine.reg[1].value(b);ss=saddles(a)
    check(answer in ss if ss else answer==0,('candidate result',m,n,a,answer))
    check((answer,machine.time)==expected(a),('candidate cost',m,n,a,answer,machine.time,expected(a)))
    return machine.time

records=[]
for kind,shapes in [('binary',[(1,1),(1,4),(4,1),(2,2),(2,3),(3,2),(3,3)]),
                    ('distinct',[(1,3),(3,1),(2,2),(2,3),(3,2)]),('ternary',[(2,2),(2,3)])]:
    for m,n in shapes:
        samples=permutations(range(m*n)) if kind=='distinct' else product(range(2 if kind=='binary' else 3),repeat=m*n)
        total=count=0
        for xs in samples:
            total+=run([list(xs[i*n:(i+1)*n]) for i in range(m)]);count+=1
        if kind!='ternary':
            mean=binary_mean(m,n) if kind=='binary' else distinct_mean(m,n)
            check(F(total,count)==mean,('candidate mean',kind,m,n,F(total,count),mean))
        records.append({'kind':kind,'m':m,'n':n,'matrices':count,'mean_time':str(F(total,count))})
rng=random.Random(132123)
for b in (64,100):
    for _ in range(40):
        a=[[rng.choice([-b**5+1,-1,0,1,b**5-1]) for j in range(8)] for i in range(9)];run(a,b)
mb,md=binary_mean(9,8),distinct_mean(9,8)
check(mb<binary_solution2(9,8),'general third faster binary')
check(md<distinct_intervals(9,8)['solution2'][0],'general third faster distinct')
result={'checks':checks,'exhaustive':records,'9x8_including_hlt':{
    'binary':str(mb),'binary_decimal':float(mb),'distinct':str(md),'distinct_decimal':float(md)},
    'scope':'General ordered-word inputs with ties; lazy candidate rows from one minmax column. Not a global optimality claim.'}
(ROOT/'results/saddle-candidates.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'checks':checks,'9x8':result['9x8_including_hlt']},indent=2))
