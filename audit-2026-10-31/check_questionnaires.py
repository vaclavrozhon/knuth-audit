"""Independent finite-domain model and literal grading of Table 666.

Question 20's global claims are explicit parameters, not circular solver
assertions. The caller states each hypothesis and checks its consequences.
Run using the isolated audit venv containing z3-solver.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import json
import time

import z3 as z

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/questionnaires'


def model(modified, maximum, indeterminate=False, only_wrong=False):
    a = [z.Int(f'a{i+1}') for i in range(20)]
    x = [z.Bool(f'x{i+1}') for i in range(20)]
    solver = z.Solver()
    solver.set(timeout=1800000)
    solver.add(*[z.And(v >= 0,v < 5) for v in a])
    c = [z.Sum([z.If(v==s,1,0) for v in a]) for s in range(5)]
    unique = [z.And([c[s]!=c[t] for t in range(5) if t!=s]) for s in range(5)]
    prime_vowels = z.Sum([z.If(z.Or(a[j-1]==0,a[j-1]==4),1,0)
                          for j in [2,3,5,7,11,13,17,19]])
    f = []
    f.append([z.And(a[s]==0,*[a[j]!=0 for j in range(s)]) for s in range(5)])
    f.append([z.And(a[t-1]==s,*[a[j]!=s for j in range(2,t-1)])
              for s,t in enumerate([4,6,8,10,12])])
    f.append([z.And([a[j]==a[j+1] if j==14+s else a[j]!=a[j+1]
                     for j in range(19)]) for s in range(5)])
    f.append([z.And(a[j-1]==s,a[k-1]==s)
              for s,(j,k) in enumerate([(10,13),(14,16),(7,20),(1,15),(8,12)])])
    f.append([a[13]==v for v in [1,4,2,0,3]])
    f.append([z.BoolVal(True)]*5)
    f.append([z.And([c[s]>=c[t] for t in range(5)]) for s in range(5)])
    f.append([z.And(unique[s],*[z.Implies(unique[t],c[s]<=c[t])
                               for t in range(5)]) for s in range(5)])
    ranges = [(59,62),(52,55),(44,49),(59,67),(39,43) if modified else (44,53)]
    sums = [z.Sum([z.If(z.And(a[j]==s,x[j]),j+1,0) for j in range(20)])
            for s in range(5)]
    f.append([z.And(lo<=v,v<=hi) for v,(lo,hi) in zip(sums,ranges)])
    f.append([a[16]==v for v in [3,1,0,4]]+[z.Not(x[16])])
    f.append([c[3]==s+2 for s in range(5)])
    f.append([c[s]-1==c[s+1] for s in range(4)]
              +[z.And([c[4]-1!=c[t] for t in range(1,5)])])
    f.append([c[4]==5-s for s in range(5)])
    f.append([z.And([v!=s+2 for v in c]) for s in range(4)]
              +[z.And([z.Or([v==j for v in c]) for j in range(2,6)])])
    odd_sets = [z.And([a[j-1]==0 if j==t else a[j-1]!=0
                       for j in range(1,21,2)]) for t in [7,9,11,13,15]]
    if not modified:
        odd_sets[2] = z.Not(odd_sets[2])
    f.append(odd_sets)
    f.append([a[7]==a[j-1] for j in [3,2,13,18,20]])
    f.append([a[9]==v for v in [2,3,1,0]]+[x[9]])
    f.append([z.Or([prime_vowels==v for v in [2,3,5,7]]),
              z.Or([prime_vowels==v for v in [0,1,4]]),
              prime_vowels%2==1,prime_vowels%2==0,prime_vowels==0])
    f.append([z.And(a[t-1]==1,*[a[j]!=1 for j in range(t,20)])
              for t in range(14,19)])
    f.append([z.BoolVal(maximum==v) for v in [18,19,20]]
              +[z.BoolVal(indeterminate),z.BoolVal(only_wrong)])
    for j in range(20):
        for s in range(5):
            solver.add(z.Implies(a[j]==s,x[j]==f[j][s]))
    return solver,a,x


def literal_grade(answers, grades, modified, maximum,
                  indeterminate=False, only_wrong=False):
    """No symbolic constraints: evaluate the chosen sentences directly."""
    a = ' '+answers.upper()
    x = [False]+list(grades)
    count = Counter(a[1:])
    dist = {v:count[v] for v in 'ABCDE'}
    ans = []
    first = next((j for j in range(1,21) if a[j]=='A'),None)
    ans.append(first == 'ABCDE'.index(a[1])+1)
    nxt = next((j for j in range(3,21) if a[j]==a[2]),None)
    ans.append(nxt == 4+2*'ABCDE'.index(a[2]))
    pairs = [j for j in range(1,20) if a[j]==a[j+1]]
    ans.append(pairs == [15+'ABCDE'.index(a[3])])
    jj,kk = [(10,13),(14,16),(7,20),(1,15),(8,12)]['ABCDE'.index(a[4])]
    ans.append(a[jj]==a[4] and a[kk]==a[4])
    ans.append(a[14]=='BECAD'['ABCDE'.index(a[5])])
    ans.append(True)
    ans.append(dist[a[7]]==max(dist.values()))
    single = [v for v in 'ABCDE' if list(dist.values()).count(dist[v])==1]
    ans.append(bool(single) and a[8]==min(single,key=lambda v:dist[v]))
    total = sum(j for j in range(1,21) if x[j] and a[j]==a[9])
    lo,hi = [(59,62),(52,55),(44,49),(59,67),
             (39,43) if modified else (44,53)]['ABCDE'.index(a[9])]
    ans.append(lo<=total<=hi)
    ans.append(not x[17] if a[10]=='E' else a[17]=='DBAE'['ABCD'.index(a[10])])
    ans.append(dist['D']==2+'ABCDE'.index(a[11]))
    others = dist[a[12]]-1
    ans.append(all(others!=dist[v] for v in 'BCDE') if a[12]=='E'
               else others==dist['BCDE'['ABCD'.index(a[12])]])
    ans.append(dist['E']==5-'ABCDE'.index(a[13]))
    ans.append(all(v in dist.values() for v in [2,3,4,5]) if a[14]=='E'
               else 2+'ABCD'.index(a[14]) not in dist.values())
    odds = {j for j in range(1,21,2) if a[j]=='A'}
    desired = {7+2*'ABCDE'.index(a[15])}
    ans.append(odds!=desired if a[15]=='C' and not modified else odds==desired)
    ans.append(a[8]==a[[3,2,13,18,20]['ABCDE'.index(a[16])]])
    ans.append(x[10] if a[17]=='E' else a[10]=='CBDA'['ABCD'.index(a[17])])
    nv = sum(a[j] in 'AE' for j in [2,3,5,7,11,13,17,19])
    ans.append([nv in (2,3,5,7),nv in (0,1,4),nv%2==1,nv%2==0,nv==0]
               ['ABCDE'.index(a[18])])
    last = next((j for j in range(20,0,-1) if a[j]=='B'),None)
    ans.append(last==14+'ABCDE'.index(a[19]))
    ans.append([maximum==18,maximum==19,maximum==20,indeterminate,only_wrong]
               ['ABCDE'.index(a[20])])
    return ans


def enumerate_case(name, modified, score, indeterminate=False,
                   only_wrong=False, last_answer=None):
    start = time.monotonic()
    solver,a,x = model(modified,score,indeterminate,only_wrong)
    solver.add(z.Sum([z.If(v,1,0) for v in x])==score)
    if last_answer is not None:
        solver.add(a[-1]=='ABCDE'.index(last_answer))
    found = []
    while True:
        status = solver.check()
        if status == z.unsat:
            break
        assert status == z.sat, (name,status,solver.reason_unknown())
        sol = solver.model()
        aa = [sol.eval(v).as_long() for v in a]
        xx = [z.is_true(sol.eval(v)) for v in x]
        answer = ''.join('ABCDE'[v] for v in aa)
        assert literal_grade(answer,xx,modified,score,indeterminate,only_wrong)==xx
        annotated = ''.join(ch if ok else ch.lower() for ch,ok in zip(answer,xx))
        found.append(annotated)
        solver.add(z.Or(*[v!=value for v,value in zip(a,aa)],
                        *[v!=value for v,value in zip(x,xx)]))
        if len(found)%50==0:
            print(name,len(found),flush=True)
    result = dict(name=name,modified=modified,score=score,
                  indeterminate=indeterminate,only_wrong=only_wrong,
                  last_answer=last_answer,count=len(found),solutions=sorted(found),
                  elapsed_seconds=time.monotonic()-start,status='complete',
                  solver=z.get_version_string())
    (OUT/(name+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(name,len(found),'seconds',result['elapsed_seconds'],flush=True)
    return result


def small_examples():
    warmup = {}
    for a in product('AB',repeat=2):
        good = []
        for x in product([False,True],repeat=2):
            f1 = a[1]=='B' if a[0]=='A' else a[0]=='A'
            f2 = x[0] if a[1]=='A' else (not x[1]) != (a[0]=='A')
            if tuple([f1,f2])==x:
                good.append(''.join(str(int(v)) for v in x))
        warmup[''.join(a)] = good
    assert warmup=={'AA':['00'],'AB':['10','11'],'BA':['00'],'BB':[]}
    # All four hypotheses for the two global claims in the recursive example.
    fixed = []
    for ungradable,no_perfect in product([False,True],repeat=2):
        valid = {''.join(a):[] for a in product('AB',repeat=2)}
        for a in product('AB',repeat=2):
            for x in product([False,True],repeat=2):
                f1 = not x[0] if a[0]=='A' else not x[1]
                f2 = ungradable if a[1]=='A' else no_perfect
                if (f1,f2)==x: valid[''.join(a)].append(x)
        actual_ungradable = any(not v for v in valid.values())
        actual_no_perfect = not any((True,True) in v for v in valid.values())
        if (actual_ungradable,actual_no_perfect)==(ungradable,no_perfect):
            fixed.append(dict(ungradable=ungradable,no_perfect=no_perfect,valid=valid))
    assert len(fixed)==1 and fixed[0]['ungradable'] and fixed[0]['no_perfect']
    assert fixed[0]['valid']=={'AA':[],'AB':[],'BA':[(False,True)],'BB':[(False,True)]}
    (OUT/'small-examples.json').write_text(json.dumps(dict(warmup=warmup,recursive=fixed),indent=2)+'\n')


def main():
    OUT.mkdir(exist_ok=True)
    small_examples()
    for name,modified,score,indeterminate,last in [
        ('base-20',False,20,False,None),('base-19',False,19,False,None),
        ('modified-20',True,20,False,None),('modified-19',True,19,False,None),
        ('modified-18-C',True,18,False,'C'),('modified-18-A',True,18,False,'A'),
        ('indeterminate-19',True,19,True,None)]:
        enumerate_case(name,modified,score,indeterminate,last_answer=last)


if __name__ == '__main__':
    main()
