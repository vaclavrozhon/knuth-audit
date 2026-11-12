"""Executable answers 17 (canonical arithmetic) and 19 (free lattices).

Arithmetic normalization is an exact, terminating rewrite system, not a
decision procedure for all elementary-function identities. Equalities hold
where the original expression is defined; original domain conditions must be
retained by a caller that also wants domain equivalence. Positive variables
are explicitly assumed only by the guarded logarithm-of-power rewrite.
"""
import sys
sys.dont_write_bytecode=True
from functools import lru_cache
from fractions import Fraction
from pathlib import Path
import math,json,random
from check_mix import C,V,derivative
HERE=Path(__file__).resolve().parent

def constant(t):return t[0]=='c'
def coeff(t):
    if constant(t):return Fraction(t[1]),C(1)
    if t[0]=='*' and constant(t[1]):
        rest=t[2:];return Fraction(t[1][1]),rest[0] if len(rest)==1 else ('*',*rest)
    return Fraction(1),t
def add(ts):
    flat=[]
    for t in ts:flat.extend(t[1:] if t[0]=='+' else [t])
    by={}
    for t in flat:
        c,a=coeff(t);by[a]=by.get(a,0)+c
    terms=[mul([C(c),a]) for a,c in sorted(by.items(),key=lambda kv:repr(kv[0])) if c]
    return C(0) if not terms else terms[0] if len(terms)==1 else ('+',*terms)
def mul(ts):
    flat=[]
    for t in ts:flat.extend(t[1:] if t[0]=='*' else [t])
    c=Fraction(1);powers={}
    for t in flat:
        if constant(t):c*=t[1];continue
        a,k=(t[1],int(t[2][1])) if t[0]=='^' and constant(t[2]) and Fraction(t[2][1]).denominator==1 else (t,1)
        powers[a]=powers.get(a,0)+k
    if not c:return C(0)
    factors=[a if k==1 else ('^',a,C(k)) for a,k in sorted(powers.items(),key=lambda kv:repr(kv[0])) if k]
    if c!=1 or not factors:factors.insert(0,C(c))
    return factors[0] if len(factors)==1 else ('*',*factors)
def power(u,v):
    if constant(v) and Fraction(v[1]).denominator==1:
        k=int(v[1])
        if constant(u):
            if u[1]==0 and k<=0:raise ValueError('undefined constant power')
            return C(Fraction(u[1])**k)
        if k==0:return C(1)
        if k==1:return u
        if u[0]=='*':return mul(power(t,v) for t in u[1:])
        if u[0]=='^' and constant(u[2]) and Fraction(u[2][1]).denominator==1:return power(u[1],C(u[2][1]*k))
    return ('^',u,v)
def positive(t,positive_variables):
    if constant(t):return t[1]>0
    if t[0]=='v':return t[1] in positive_variables
    if t[0] in ('+','*'):return all(positive(c,positive_variables) for c in t[1:])
    if t[0]=='^':return positive(t[1],positive_variables)
    return False
def simplify(t,positive_variables=frozenset()):
    op=t[0]
    if op in ('c','v'):return C(Fraction(t[1])) if op=='c' else t
    cs=[simplify(c,positive_variables) for c in t[1:]]
    if op=='+':return add(cs)
    if op=='-':return add([cs[0],mul([C(-1),cs[1]])])
    if op=='neg':return mul([C(-1),cs[0]])
    if op=='*':return mul(cs)
    if op=='/':return mul([cs[0],power(cs[1],C(-1))])
    if op=='^':return power(*cs)
    assert op=='ln'
    u=cs[0]
    if u==C(1):return C(0)
    if u[0]=='^' and positive(u[1],positive_variables):return mul([u[2],simplify(('ln',u[1]),positive_variables)])
    return ('ln',u)

def value(t,env):
    op=t[0]
    if op=='c':return float(t[1])
    if op=='v':return env[t[1]]
    vs=[value(c,env) for c in t[1:]]
    if op=='ln':return math.log(vs[0])
    if op=='neg':return -vs[0]
    if op=='+':return sum(vs)
    if op=='-':return vs[0]-vs[1]
    if op=='*':return math.prod(vs)
    if op=='/':return vs[0]/vs[1]
    if op=='^':return math.pow(vs[0],vs[1])
    raise ValueError(op)

def dual(t,env):
    """Forward-mode value/derivative, independent of the tree-building oracle."""
    op=t[0]
    if op=='c':return float(t[1]),0.
    if op=='v':return env[t[1]],float(t[1]=='X')
    u,du=dual(t[1],env)
    if op=='ln':return math.log(u),du/u
    if op=='neg':return -u,-du
    v,dv=dual(t[2],env)
    if op=='+':return u+v,du+dv
    if op=='-':return u-v,du-dv
    if op=='*':return u*v,du*v+u*dv
    if op=='/':return u/v,(du*v-u*dv)/(v*v)
    if op=='^':
        w=math.pow(u,v)
        return w,(v*math.pow(u,v-1)*du if dv==0 else w*(dv*math.log(u)+v*du/u))

def blind(t):
    op=t[0]
    if op=='c':return C(0)
    if op=='v':return C(int(t[1]=='X'))
    u=t[1];du=blind(u)
    if op=='ln':return ('/',du,u)
    if op=='neg':return ('neg',du)
    v=t[2];dv=blind(v)
    if op in ('+','-'):return (op,du,dv)
    if op=='*':return ('+',('*',du,v),('*',u,dv))
    if op=='/':return ('-',('/',du,v),('/',('*',u,dv),('^',v,C(2))))
    first=('*',du,('*',v,('^',u,('-',v,C(1)))))
    second=('*',('*',('ln',u),dv),('^',u,v))
    return ('+',first,second)

def lattice_ge(x,y):
    """x,y are variable strings or ('join'/'meet',child,child)."""
    @lru_cache(None)
    def go(x,y):
        if isinstance(x,tuple) and x[0]=='meet':return go(x[1],y) and go(x[2],y)
        if isinstance(y,tuple) and y[0]=='join':return go(x,y[1]) and go(x,y[2])
        if isinstance(x,tuple) and isinstance(y,tuple):return go(x,y[1]) or go(x,y[2]) or go(x[1],y) or go(x[2],y)
        if isinstance(x,str) and isinstance(y,tuple):return go(x,y[1]) or go(x,y[2])
        if isinstance(x,tuple) and isinstance(y,str):return go(x[1],y) or go(x[2],y)
        return x==y
    answer=go(x,y)
    return answer,go.cache_info().currsize

def lattice_closure(x,y):
    """Independent finite partial-lattice closure, using <= internally."""
    terms=[]
    def visit(t):
        if t not in terms:
            if isinstance(t,tuple):visit(t[1]);visit(t[2])
            terms.append(t)
    visit(x);visit(y);ids={t:i for i,t in enumerate(terms)};n=len(terms)
    rel=[[i==j for j in range(n)] for i in range(n)]
    ops=[]
    for t in terms:
        if isinstance(t,tuple):
            z,a,b=ids[t],ids[t[1]],ids[t[2]];ops.append((t[0],z,a,b))
            if t[0]=='meet':rel[z][a]=rel[z][b]=True
            else:rel[a][z]=rel[b][z]=True
    change=True
    while change:
        old=sum(map(sum,rel))
        for k in range(n):
            for i in range(n):
                if rel[i][k]:
                    for j in range(n):rel[i][j]|=rel[k][j]
        for op,z,a,b in ops:
            for i in range(n):
                if op=='meet':rel[i][z]|=rel[i][a] and rel[i][b]
                else:rel[z][i]|=rel[a][i] and rel[b][i]
        change=sum(map(sum,rel))!=old
    return rel[ids[y]][ids[x]]

def validate():
    x=V();a=V('A');y=('-',('*',C(3),('ln',('+',x,C(1)))),('/',a,('^',x,C(2))))
    target=simplify(('+',('*',C(3),('^',('+',x,C(1)),C(-1))),('*',C(2),a,('^',x,C(-3)))))
    assert simplify(blind(y))==target and simplify(derivative(y))==target
    assert simplify(('ln',('^',x,a)),frozenset(['X']))==simplify(('*',a,('ln',x)))
    assert simplify(('ln',('^',x,a)))==('ln',('^',x,a))
    from validate_mix import random_tree
    rng=random.Random(23217);valid=0;skipped=0
    for _ in range(700):
        t=random_tree(rng,rng.randrange(1,16))
        try:
            s=simplify(t);assert simplify(s)==s,(t,s,simplify(s))
            for env in [{'X':1.25,'A':.75},{'X':2.1,'A':1.3}]:
                v,d=dual(t,env);w=value(s,env);dd=value(derivative(t),env)
                if not all(map(math.isfinite,[v,d,w,dd])):raise ValueError('nonfinite')
                assert math.isclose(v,w,rel_tol=1e-9,abs_tol=1e-9),(t,s,v,w)
                assert math.isclose(d,dd,rel_tol=1e-8,abs_tol=1e-8),(t,d,dd)
            valid+=1
        except (ValueError,ZeroDivisionError,OverflowError):skipped+=1
    terms=['a','b','c']+[(op,a,b) for op in ['meet','join'] for a in ['a','b','c'] for b in ['a','b','c']]
    pairs=[(a,b) for a in terms for b in terms]
    def randterm(d):return rng.choice(['a','b','c']) if not d or rng.randrange(3)==0 else (rng.choice(['meet','join']),randterm(d-1),randterm(d-1))
    pairs += [(randterm(4),randterm(4)) for _ in range(350)]
    for a,b in pairs:
        answer,m=lattice_ge(a,b);assert answer==lattice_closure(a,b),(a,b,answer)
        def sub(t):return {t} if isinstance(t,str) else {t}|sub(t[1])|sub(t[2])
        assert m<=len(sub(a))*len(sub(b))
    lhs=('meet','a',('join','b','c'));rhs=('join',('meet','a','b'),('meet','a','c'))
    assert lattice_ge(lhs,rhs)[0] and not lattice_ge(rhs,lhs)[0]
    return {'simplification_eq20_eq21_eq22':repr(target),'arithmetic_random_valid':valid,'arithmetic_random_domain_or_range_skipped':skipped,'lattice_pairs':len(pairs),'lattice_independent_oracle':'finite partial-lattice closure','seed':23217}

if __name__=='__main__':
    data=validate();(HERE/'results/algebra.json').write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2))
