"""Exact survey-propagation fields and fixed points, SAT 357--361."""
from fractions import Fraction as Q
from itertools import product
from math import prod
from collections import Counter
from pathlib import Path
import json

R=[(1,2,-3),(-1,-2,3),(2,3,-4),(-2,-3,4),(1,3,4),(-1,-3,-4),(-1,2,4)]


def update(n,clauses,reinforcement,eta):
    literals=[l for i in range(1,n+1) for l in (i,-i)]
    pi={l:(1-reinforcement[l])*prod(1-eta[c,l] for c,C in enumerate(clauses) if l in C) for l in literals}
    if any(pi[v]==pi[-v]==0 for v in range(1,n+1)):return None,pi,None
    gamma={}
    for c,C in enumerate(clauses):
        for l in C:
            excluded=(1-reinforcement[l])*prod(1-eta[d,l] for d,D in enumerate(clauses) if d!=c and l in D)
            numerator=(1-pi[-l])*excluded
            gamma[c,l]=numerator/(pi[-l]+numerator)
    new={(c,l):prod(gamma[c,k] for k in C if k!=l) for c,C in enumerate(clauses) for l in C}
    return new,pi,gamma


def reduced_state(a,b,c,d,x,y,z):
    reinforcement={l:Q(0) for i in range(1,5) for l in (i,-i)}
    reinforcement.update({-1:a,2:b,4:c,-3:d})
    eta={(k,l):Q(0) for k,C in enumerate(R) for l in C}
    eta.update({(1,-1):x,(2,2):y,(4,4):z})
    return reinforcement,eta


def stable_and_constrained(assignment,clauses):
    constrained=set()
    for C in clauses:
        true=[l for l in C if assignment[abs(l)-1] is not None and assignment[abs(l)-1]==(l>0)]
        wild=[l for l in C if assignment[abs(l)-1] is None]
        if not true and len(wild)<2:return False,set()
        if len(true)==1 and not wild:constrained.add(abs(true[0]))
    return True,constrained


def binary_fixed_points():
    n=2;literals=[1,-1,2,-2]
    allclauses=[tuple((i+1)*v for i,v in enumerate(a) if v) for a in product([-1,0,1],repeat=n) if any(a)]
    states=fixed=formulas=0;assignment_totals=0
    for mask in range(1<<len(allclauses)):
        clauses=[C for i,C in enumerate(allclauses) if mask>>i&1]
        messages=[(c,l) for c,C in enumerate(clauses) for l in C]
        incoming={l:[k for k,(c,v) in enumerate(messages) if v==l] for l in literals}
        found=Counter()
        for bits in product([0,1],repeat=len(messages)):
            surveys=dict(zip(messages,bits))
            for rb in product([0,1],repeat=4):
                states+=1;r=dict(zip(literals,rb))
                pi={l:int(not r[l] and not any(bits[k] for k in incoming[l])) for l in literals}
                if any(pi[v]==pi[-v]==0 for v in (1,2)):continue
                gamma={}
                for c,l in messages:
                    excluded=int(not r[l] and not any(bits[k] for k in incoming[l] if messages[k][0]!=c))
                    numerator=(1-pi[-l])*excluded;den=pi[-l]+numerator
                    assert den==1
                    gamma[c,l]=numerator
                new={(c,l):prod(gamma[c,k] for k in C if k!=l) for c,C in enumerate(clauses) for l in C}
                if new!=surveys:continue
                fixed+=1
                assignment=tuple(None if pi[v]==pi[-v]==1 else pi[v]==0 for v in (1,2))
                valid,constrained=stable_and_constrained(assignment,clauses);assert valid
                for l in literals:
                    if pi[l]==1:assert r[l]==0
                    elif not any(bits[k] for k in incoming[l]):assert r[l]==1
                found[assignment]+=1
        expected={}
        for assignment in product([False,True,None],repeat=n):
            valid,constrained=stable_and_constrained(assignment,clauses)
            if valid:expected[assignment]=2**len(constrained)
        assert dict(found)==expected
        formulas+=1;assignment_totals+=len(expected)
    return dict(formulas=formulas,states=states,fixed_points=fixed,stable_assignment_pairs=assignment_totals)


def main():
    fields=0
    for X,Y in product(range(17),repeat=2):
        if not(X or Y):continue
        x,y=Q(X,16),Q(Y,16);den=x+y-x*y
        p,q,r=x*(1-y)/den,y*(1-x)/den,x*y/den
        assert p+q+r==1
        assert (r>=p and r>=q)==(x>=Q(1,2) and y>=Q(1,2))
        if r:assert r/(1-p)==x and r/(1-q)==y
        elif p==1:assert x>0 and y==0
        else:assert q==1 and x==0 and y>0
        fields+=1
    # A printed y=1 would instead give field (0,1/2,1/2).
    assert (Q(1,2)*(1-1),1*(1-Q(1,2)),Q(1,2)*1)==(0,Q(1,2),Q(1,2))
    generic=continuum=0
    for a,b,c,d in product([Q(i,4) for i in range(5)],repeat=4):
        den=1-d**3*(1-a)*(1-b)*(1-c)
        if den==0:
            assert (a,b,c,d)==(0,0,0,1);continue
        x=d*(b+c*d*(1-b)+a*d*d*(1-b)*(1-c))/den
        y=d*(c+a*d*(1-c)+b*d*d*(1-c)*(1-a))/den
        z=d*(a+b*d*(1-a)+c*d*d*(1-a)*(1-b))/den
        assert x==d*(b+(1-b)*y) and y==d*(c+(1-c)*z) and z==d*(a+(1-a)*x)
        rein,eta=reduced_state(a,b,c,d,x,y,z)
        new,pi,gamma=update(4,R,rein,eta)
        assert new==eta and pi[1]==pi[-2]==pi[-4]==1;generic+=1
    for k in range(17):
        t=Q(k,16);rein,eta=reduced_state(0,0,0,1,t,t,t)
        new,pi,gamma=update(4,R,rein,eta)
        assert new==eta and pi[1]==pi[-2]==pi[-4]==1
        continuum+=1
    rein,eta=reduced_state(Q(1,2),Q(1,2),Q(1,2),Q(1,3),Q(1,5),Q(1,5),Q(1,5))
    new,pi,gamma=update(4,R,rein,eta)
    assert new==eta and [pi[i] for i in [-1,2,4]]==[Q(2,5)]*3 and pi[-3]==Q(2,3)
    # Verify (159)'s full gamma table, in clause order.
    table=[(Q(3,5),0,0),(0,Q(3,5),Q(1,3)),(0,Q(1,3),Q(3,5)),
           (Q(3,5),0,0),(Q(3,5),Q(1,3),0),(0,0,Q(3,5)),(0,0,0)]
    assert [tuple(gamma[c,l] for l in C) for c,C in enumerate(R)]==table
    zero_products=0
    for size in range(8):
        for factors in product([Q(0),Q(1,3),Q(1)],repeat=size):
            nonzero=prod(v for v in factors if v);zeros=factors.count(0)
            assert (nonzero if not zeros else 0)==prod(factors)
            for k,value in enumerate(factors):
                answer=(nonzero if zeros==1 else 0) if value==0 else (nonzero/value if zeros==0 else 0)
                assert answer==prod(factors[:k]+factors[k+1:]);zero_products+=1
    result=dict(field_vectors=fields,generic_fixed_points=generic,boundary_family_samples=continuum,
                example_159='All pi, eta and gamma entries verified exactly',zero_factor_exclusions=zero_products,
                binary=binary_fixed_points(),F044='Answer357: y=0, not1, when(p,q)=(1,0).',
                F045='Answer360: when(a,b,c,d)=(0,0,0,1), every x=y=z=t in[0,1] is a fixed point.')
    Path('results/surveys.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
