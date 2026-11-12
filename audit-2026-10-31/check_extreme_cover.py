"""Exact checks for exact-cover exercises 180,182,184-188 and (82)-(85)."""
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from math import comb, factorial
from pathlib import Path
import json
import sympy as s
from algorithm_x import DLX


def partitions(n):
    if not n:
        yield ()
        return
    for prefix in partitions(n-1):
        for label in range(max(prefix, default=-1)+2):
            yield prefix+(label,)


def coefficient_matrix(limit):
    a=[]
    for n in range(limit+1):
        row=[0]*(limit+1);row[n]=1
        if n:
            for j in range(n):
                c=comb(n-1,j)
                for k in range(j+1):
                    row[k]+=c*a[j][k]
        a.append(row)
    return a


def count_matrix(items, rows):
    @lru_cache(None)
    def visit(left, available):
        if not left:
            return 1
        b=min((1<<j for j in range(items) if left & (1<<j)),
              key=lambda b:sum(bool(r&b) for r in available))
        return sum(visit(left^r,tuple(x for x in available if not x&r))
                   for r in available if r&b)
    return visit((1<<items)-1,tuple(sorted(rows)))


def prescribed(n,t,bell):
    rows=list(range(1,1<<(n-1)))
    remainder=t;digits=[0]*n
    for j in range(n-1,-1,-1):
        digit=min(comb(n-1,j),remainder//bell[j])
        digits[j]=digit;remainder-=digit*bell[j]
        options=combinations(range(n-1),n-j-1)
        for _,subset in zip(range(digit),options):
            rows.append((1<<(n-1))+sum(1<<k for k in subset))
    assert remainder==0
    signatures=[tuple(bool(r&(1<<j)) for r in rows) for j in range(n)]
    assert len(rows)==len(set(rows)) and len(signatures)==len(set(signatures))
    return rows,digits


def main():
    a=coefficient_matrix(80)
    bell=[r[0] for r in a];gould=[r[1] for r in a]
    enumerated=0
    for n in range(9):
        tails=Counter()
        for p in partitions(n):
            enumerated+=1
            if n:
                tails[p.count(max(p))]+=1
        assert sum(tails.values())==bell[n] if n else bell[n]==1
        for k in range(1,n+1):
            assert tails[k]==a[n][k]
    tri=[[0],[0,0],[0,1,1]]
    for n in range(3,81):
        row=[0]*(n+1);row[n]=tri[n-1][1]
        for k in range(n-1,0,-1):
            row[k]=tri[n-1][k]+row[k+1]
        tri.append(row)
    # The triangle deliberately has a special first row 0. Its partition
    # interpretation in answer 188 expressly assumes n>1.
    assert tri[1][1]==0
    assert all(tri[n][1]==gould[n] for n in range(2,81))
    # Root-update polynomial and total-update recurrence, all exact.
    v=[((9*n-27)*4**n-(8*n-32)*3**n+(36*n-36)*2**n+72-41*(n==0))//72
       for n in range(81)]
    x=[]
    for n in range(81):
        value=v[n]+sum(comb(n-1,j)*x[j] for j in range(n)) if n else v[0]
        closed=22*bell[n]+12*gould[n]-Q((2*n-3)*3**n,3)-Q(5*n*2**n,2)-12*n-5-12*(n==1)-18*(n==0)
        assert value==closed
        x.append(value)
    measured=[]
    for n in range(9):
        rows=[tuple(j for j in range(n) if mask&(1<<j)) for mask in range(1,1<<n)]
        run=DLX(list(range(n)),rows).solve(collect=False)
        assert run.solution_count==bell[n]
        assert sum(run.updates_by_depth.values())==x[n]
        assert run.updates_by_depth[0]==v[n]
        measured.append({'n':n,'solutions':bell[n],'root_updates':v[n],'total_updates':x[n]})
    prescribed_count=0
    for n in range(1,8):
        for target in range(bell[n]+1):
            rows,digits=prescribed(n,target,bell)
            assert count_matrix(n,rows)==target
            prescribed_count+=1
    rows,digits=prescribed(9,10000,bell)
    assert count_matrix(9,rows)==10000
    cycle_tests=[]
    for copies in range(6):
        rows=[]
        for i in range(copies):
            rows.extend([(4*i+j,) for j in range(4)])
            rows.extend([(4*i+j,4*i+(j+1)%4) for j in range(4)])
        run=DLX(list(range(4*copies)),rows).solve(collect=False)
        nodes=sum(run.nodes_by_depth.values())
        assert run.solution_count==7**copies and nodes==(5*7**copies-3)//2
        cycle_tests.append({'copies':copies,'solutions':run.solution_count,'nodes':nodes})
    # All primary-containing options, with secondary items optional.
    secondary_checks=0
    for primary in range(6):
        for secondary in range(5):
            p_mask=(1<<primary)-1;total=primary+secondary
            rows=tuple(r for r in range(1,1<<total) if r&p_mask)
            @lru_cache(None)
            def mixed(left,available):
                if not left:
                    return 1
                b=left&-left
                return sum(mixed(left&~r,tuple(x for x in available if not x&r))
                           for r in available if r&b)
            stirling=Counter(max(p,default=-1)+1 for p in partitions(primary))
            expected=sum(v*(k+1)**secondary for k,v in stirling.items())
            assert mixed(p_mask,rows)==expected
            secondary_checks+=1
    # Differential identities: use T_00'=exp(z)*T_00+1 and B'=exp(z)*B.
    z=s.symbols('z');B=s.Function('B')(z);T=s.Function('T')(z)
    def operator(expr):
        return s.simplify((s.diff(expr,z)-s.exp(z)*expr).subs(
            {s.diff(B,z):s.exp(z)*B,s.diff(T,z):s.exp(z)*T+1}).expand())
    t13=4*B+2*T-z*s.exp(2*z)-(2*z+1)*s.exp(z)-2*z-3
    assert s.simplify(operator(t13)-z*s.exp(3*z))==0
    xx=22*B+12*T-(2*z-1)*s.exp(3*z)-5*z*s.exp(2*z)-(12*z+5)*s.exp(z)-12*z-18
    vv=((36*z-27)*s.exp(4*z)-(24*z-32)*s.exp(3*z)+(72*z-36)*s.exp(2*z)+72*s.exp(z)-41)/72
    assert s.simplify(operator(xx)-s.diff(vv,z))==0
    assert xx.subs({z:0,B:1,T:0})==0
    # F018: exact strict t=u=4 staircase contradicts i2 in o6.
    staircase=(1,3,7,15,14,12,8)
    assert [sum(bool(r&(1<<j)) for r in staircase) for j in range(4)]==[4]*4
    assert [sum(bool(r&other) for other in staircase) for r in staircase[:4]]==[4,5,6,7]
    assert not staircase[5]&2
    report={'partition_enumeration_count':enumerated,'coefficient_identity_through_n':80,
            'update_identity_through_n':80,'measured_DLX':measured,
            'all_prescribed_counts_through_n7':prescribed_count,
            'n9_10000_Bell_digits':digits,'cycle_lower_bound':cycle_tests,
            'mixed_primary_secondary_checks':secondary_checks,
            'symbolic_checks':'187(a,d), answer 187(d); exact differential equations and initial values.',
            'F018':{'rows_binary':[format(r,'04b')[::-1] for r in staircase],
                    'issue':'Answer 180 includes i2 in o6, but i2 already occurs in exactly o2,o3,o4,o5.'},
            'F019':'Answer 187(b) prints T_rs derivative as exp(z)*T_rs+z^r; the general formula needs z^r*exp(s*z), or all subscripts must use s=0.',
            'limitation':'Full saddle-point argument in exercise 189 is not covered here; 187(c) integration-by-parts formula is checked separately in the notes.'}
    (Path(__file__).parent/'results/extreme_cover.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
