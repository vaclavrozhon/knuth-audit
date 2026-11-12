"""Compare matrix invariants, grouped costs, exact probabilities and MIX runs."""
from collections import Counter
from fractions import Fraction as F
from itertools import product, permutations
from pathlib import Path
import json, random
from mixal_saddle import execute,saddles,scalar1,scalar2,solution1,solution2
from saddle_expectations import *
from mixal import Assembly
from mix_machine import Machine,number

ROOT=Path(__file__).resolve().parent
checks=0

def check(ok,label):
    global checks
    if not ok:raise AssertionError(label)
    checks+=1


def matrix(flat,m,n):return [list(flat[i*n:(i+1)*n]) for i in range(m)]

binary=[]
for m,n in [(1,1),(1,4),(4,1),(2,2),(2,3),(3,2),(3,3)]:
    times=[0,0];found=0
    for bits in product((0,1),repeat=m*n):
        a=matrix(bits,m,n);expected=saddles(a);found+=bool(expected)
        for which,scalar in [(1,scalar1),(2,scalar2)]:
            loc,t=execute(a,which)
            check(loc in expected if expected else loc==0,('binary result',m,n,bits,which))
            check((loc,t)==scalar(a)[:2],('binary cost',m,n,bits,which,loc,t,scalar(a)))
            times[which-1]+=t
    count=2**(m*n)
    check(F(found,count)==probability_binary(m,n),('binary probability',m,n))
    exact=[binary_solution1(m,n),binary_solution2(m,n)]
    check([F(t,count) for t in times]==exact,('binary expectations',m,n,times,exact))
    binary.append({'m':m,'n':n,'matrices':count,'probability':str(F(found,count)),
                   'mean_times_including_hlt':list(map(str,exact))})

distinct=[]
for m,n in [(1,3),(3,1),(2,2),(2,3),(3,2)]:
    count=found=0;times=[0,0];qsum=rsum=0
    for xs in permutations(range(m*n)):
        a=matrix(xs,m,n);expected=saddles(a);found+=bool(expected);count+=1
        hi=[max(row[j] for row in a) for j in range(n)];mu=min(hi)
        j0=hi.index(mu);i0=next(i for i in range(m) if a[i][j0]==mu)
        lengths=[next((k+1 for k,x in enumerate(reversed(row)) if x<mu),n) for row in a]
        qsum+=sum(lengths);rsum+=lengths[i0]
        for which,scalar in [(1,scalar1),(2,scalar2)]:
            loc,t=execute(a,which)
            check(loc in expected if expected else loc==0,('distinct result',m,n,xs,which))
            check((loc,t)==scalar(a)[:2],('distinct cost',m,n,xs,which))
            times[which-1]+=t
    e=distinct_intervals(m,n)
    check(F(found,count)==probability_distinct(m,n),('distinct probability',m,n))
    check(F(qsum,count*m)==e['row_scans'],('row tail integrals',m,n))
    check(F(rsum,count)==e['selected_row_scans'],('selected row tail integrals',m,n))
    for w in (1,2):
        lo,hi=e['solution'+str(w)]
        check(lo<=F(times[w-1],count)<=hi,('distinct expectation interval',m,n,w,lo,hi,times))
    distinct.append({'m':m,'n':n,'matrices':count,'probability':str(F(found,count)),
                     'mean_times_including_hlt':[str(F(t,count)) for t in times]})

rng=random.Random(1321012)
for b in (64,100):
    cases=[[[0]*8 for _ in range(9)],[[1]*8 for _ in range(9)],
           [[i*8+j for j in range(8)] for i in range(9)],
           [[-(i*8+j) for j in range(8)] for i in range(9)]]
    for _ in range(40):
        cases.append(matrix([rng.choice([-b**5+1,-1,0,1,b**5-1]) for _ in range(72)],9,8))
        xs=list(range(72));rng.shuffle(xs);cases.append(matrix(xs,9,8))
    for a in cases:
        expected=saddles(a)
        for w,f in [(1,scalar1),(2,scalar2)]:
            loc,t=execute(a,w,b)
            check(loc in expected if expected else loc==0,('9x8 result',b,w,a))
            check((loc,t)==f(a)[:2],('9x8 cost',b,w,a))

# The old 2013 bug skips the top row; the 1999 change saves one unit per
# failed row while preserving the answer (it is not a correctness repair).
a=[[2]*8]+[[0 if j==i%8 else 1 for j in range(8)] for i in range(8)]
check(execute(a,2,fix2013=False)[0]==0 and execute(a,2)[0] in saddles(a),'2013 counterexample')
a=[[0 if i==j else 1 for j in range(8)] for i in range(9)]
a[8][0]=0
old=execute(a,2,fix1999=False);new=execute(a,2)
check(old[0]==new[0]==0 and old[1]-new[1]==8,('1999 saving',old,new))

profiles=[]
for w,rows in [(1,solution1()),(2,solution2())]:
    asm=Assembly(rows);machine=Machine();asm.load(machine);machine.pc=asm.start
    counts=Counter();costs=Counter()
    while not machine.halted:
        pc=machine.pc;t=machine.time;counts[pc]+=1;machine.step();costs[pc]+=machine.time-t
    check(machine.time==[138,524][w-1],('all-zero time',w,machine.time))
    labels={}
    for loc,row in zip(asm.locations,rows):
        if loc in counts:labels[loc]=row
    profiles.append({'solution':w,'time_including_hlt':machine.time,
                     'instructions':[{'location':loc,'row':labels.get(loc),
                                      'executions':counts[loc],'time':costs[loc]} for loc in sorted(counts)]})

e=distinct_intervals(9,8)
check(e['solution2'][1]<e['solution1'][0],'distinct second faster')
b1,b2=binary_solution1(9,8),binary_solution2(9,8)
check(b2<b1,'binary second faster')
result={'checks':checks,'binary_exhaustive':binary,'distinct_exhaustive':distinct,
        'all_zero_profiles':profiles,'9x8':{'probability_distinct':str(probability_distinct(9,8)),
        'probability_binary':str(probability_binary(9,8)),
        'binary_mean_times_including_hlt':[str(b1),str(b2)],'binary_mean_times_decimal':[float(b1),float(b2)],
        'distinct_time_intervals_including_hlt':{k:list(map(str,e[k])) for k in ('solution1','solution2')},
        'distinct_time_intervals_decimal':{k:list(map(float,e[k])) for k in ('solution1','solution2')},
        'all_rows_average_scan_length':str(e['row_scans']),
        'selected_row_average_scan_length':str(e['selected_row_scans'])}}
(ROOT/'results/mixal-saddle.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'checks':checks,'9x8':result['9x8']},indent=2))
