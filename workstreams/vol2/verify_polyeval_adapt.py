#!/usr/bin/env python3
"""Exact coefficient checks for TAOCP 4.6.4 (9)--(23), exercises 18--24.

The oracle is expansion in the independent indeterminate x. Cubic constraints
are checked by polynomial remainder, never by approximate root computation.
The general root-location proof is in notes/polyeval-adapt.md.
"""
import argparse
from datetime import datetime, timezone
from pathlib import Path
import json
import os
import time
import sympy as S

ROOT = Path(__file__).resolve().parent
RESULT = ROOT / 'results/polyeval-adapt.json'
x, t, W = S.symbols('x t W')


def zero(v):
    assert S.cancel(S.expand(v)) == 0, S.factor(v)


def direct(u):
    return sum(c*x**i for i, c in enumerate(u))


class Ops:
    def __init__(self):
        self.m = self.a = 0

    def add(self, u, v):
        self.a += 1
        return u + v

    def sub(self, u, v):
        self.a += 1
        return u - v

    def mul(self, u, v):
        self.m += 1
        return u*v

    def counts(self):
        return [self.m, self.a]


def quartic(u, sign):
    v = [c/u[4] for c in u]
    a0 = (v[3]-sign)/2
    b = v[2]-a0*(a0+sign)
    a1 = sign*(v[1]-a0*b)
    a2 = b-2*a1
    a3 = v[0]-a1*(a1+a2)
    return [a0, a1, a2, a3, u[4]]


def eval4(a, sign, c):
    y = c.add(c.mul(c.add(x, a[0]), x), a[1])
    v = c.add(y, x) if sign == 1 else c.sub(y, x)
    return c.mul(c.add(c.mul(c.add(v, a[2]), y), a[3]), a[4])


def quintic(u, z):
    a3 = u[4]-4*z
    a1 = u[3]-4*z*a3-6*z*z
    a2 = u[1]-z*(z*a1+4*z*z*a3+2*a1*a3+z**3)
    a4 = u[0]-a3*(z**4+a1*z*z+a2)
    cubic = 40*z**3-24*u[4]*z*z+(4*u[4]**2+2*u[3])*z+u[2]-u[3]*u[4]
    return [z, a1, a2, a3, a4, S.Integer(1)], cubic


def eval5(a, c):
    y0 = c.add(x, a[0])
    y = c.mul(y0, y0)
    v = c.add(c.mul(c.add(y, a[1]), y), a[2])
    return c.mul(c.add(c.mul(v, c.add(x, a[3])), a[4]), a[5])


def mix5(a):
    # Read the four printed columns top to bottom, from left to right.
    mem = {'X': x, 'A3': a[3], 'A03': a[0]-a[3],
           'A1': a[1], 'A2': a[2], 'A4': a[4], 'A5': a[5]}
    program = [('LDA','X'), ('FADD','A3'), ('STA','TEMP1'),
               ('FADD','A03'), ('STA','TEMP2'), ('FMUL','TEMP2'),
               ('STA','TEMP2'), ('FADD','A1'), ('FMUL','TEMP2'),
               ('FADD','A2'), ('FMUL','TEMP1'), ('FADD','A4'), ('FMUL','A5')]
    counts = {}
    acc = None
    for op, operand in program:
        counts[op] = counts.get(op, 0)+1
        if op == 'LDA': acc = mem[operand]
        elif op == 'STA': mem[operand] = acc
        elif op == 'FADD': acc += mem[operand]
        elif op == 'FMUL': acc *= mem[operand]
        else: raise AssertionError(op)
    return acc, counts


def low_degrees_block():
    u = S.symbols('u0:5', nonzero=True)
    for sign in [-1, 1]:
        c = Ops()
        zero(eval4(quartic(u, sign), sign, c)-direct(u))
        assert c.counts() == [3, 5]
    v = [*S.symbols('u0:5'), S.Integer(1)]
    a, cubic = quintic(v, t)
    c = Ops()
    residual = S.Poly(S.expand(eval5(a,c)-direct(v)), x)
    assert c.counts() == [4, 5]
    # Independent algebraic division in Q(u0,...,u4)[t].
    for coefficient in residual.all_coeffs():
        zero(S.rem(coefficient, cubic, t))
    generic = S.symbols('a0:6')
    program, counts = mix5(generic)
    zero(program-eval5(generic, Ops()))
    assert counts == {'LDA':1, 'FADD':5, 'STA':3, 'FMUL':4}
    given = [60,13,-50,-10,5,S.Integer(1)]
    expected = [[0,-10,13,5,-5,1],[1,-20,68,1,11,1],[2,-10,13,-3,27,1]]
    for root, ex in zip(map(S.Integer, range(3)), expected):
        a, eq = quintic(given, root)
        assert a == ex and eq == 0
        zero(eval5(a, Ops())-direct(given))
    return {'quartic_symbolic_identities':2, 'quintic_generic_cubic_reduction':True,
            'quintic_examples':3, 'mix_instructions':counts,
            'quintic_residual':str(S.factor(residual.as_expr())),
            'scope':'Exact algebra and instruction/data-flow counts; no universal floating-point stability or instruction-minimality claim.'}


def knuth6(u, b6):
    b1 = (u[5]-1)/2
    b2 = u[4]-b1*(b1+1)
    b3 = u[3]-b1*b2
    b4 = b1-b2
    b5 = u[2]-b1*b3
    eq = 2*b6**3+(2*b4-b2+1)*b6**2+(2*b5-b2*b4-b3)*b6+u[1]-b2*b5
    b7 = b6*b6+b4*b6+b5
    b8 = b3-b6-b7
    a0 = b2-2*b6
    a2 = b1-a0
    a1 = b6-a0*a2
    a3 = b7-a1*a2
    return [a0,a1,a2,a3,b8-b7-a1,u[0]-b7*b8,S.Integer(1)], eq


def eval6(a, c, repeated=False, monic=False):
    b = c.add(x,a[0])
    z = c.add(c.mul(b,x),a[1])
    if not repeated: b = c.add(x,a[2])
    else: assert a[0] == a[2]
    w = c.add(c.mul(b,z),a[3])
    v = c.add(c.mul(c.add(c.add(w,z),a[4]),w),a[5])
    return v if monic else c.mul(v,a[6])


def pan6(u, a1=None):
    a0 = u[5]/3
    N = u[1]-a0*u[2]+a0*a0*u[3]-a0**3*u[4]+2*a0**5
    D = u[3]-2*a0*u[4]+5*a0**3
    if a1 is None: a1 = N/D
    b1 = 2*a0
    b2 = u[4]-a0*b1-a1
    b3 = u[3]-a0*b2-a1*b1
    b4 = u[2]-a0*b3-a1*b2
    a3 = (b3-(a0-1)*b2+(a0-1)*(a0*a0-1))/2-a1
    a2 = b2-(a0*a0-1)-a3-2*a1
    a4 = b4-(a2+a1)*(a3+a1)
    a5 = u[0]-a1*b4
    return [a0,a1,a2,a3,a4,a5,S.Integer(1)], D, N


def eval_pan(a,c):
    z = c.add(c.mul(c.add(x,a[0]),x),a[1])
    w = c.add(c.add(z,x),a[2])
    v = c.add(c.mul(c.add(c.sub(z,x),a[3]),w),a[4])
    return c.mul(c.add(c.mul(v,z),a[5]),a[6])


def sextics_block():
    u = [*S.symbols('u0:6'), S.Integer(1)]
    a, cubic = knuth6(u,t)
    c = Ops()
    residual = S.Poly(S.expand(eval6(a,c)-direct(u)),x)
    assert c.counts() == [4,7]
    for coefficient in residual.all_coeffs(): zero(S.rem(coefficient,cubic,t))
    given = list(map(S.Integer,[3,-37,-61,33,49,13,1]))
    expected = {2:[3,-7,3,16,6,-27,1],3:[1,-2,5,9,-8,-8,1],-1:[9,26,-3,73,-24,-12,1]}
    for root,ex in expected.items():
        a,eq = knuth6(given,S.Integer(root))
        assert a == ex and eq == 0
        c = Ops()
        zero(eval6(a,c,repeated=(root==2),monic=True)-direct(given))
        assert c.counts() == ([3,6] if root==2 else [3,7])
    # Leave alpha1 independent: exactly one scalar equation remains.
    a,D,N = pan6(u,t)
    c = Ops()
    residual_pan = S.factor(eval_pan(a,c)-direct(u))
    zero(residual_pan-(D*t-N)*x)
    assert c.counts() == [4,8]
    given = list(map(S.Integer,[-1,-3,1,-2,1,-3,1]))
    a,D,N = pan6(given)
    assert a == [-1,1,0,-4,4,-2,1]
    zero(eval_pan(a,Ops())-direct(given))
    w = x*x+1
    z = w-x
    zero(((z-x-4)*w+4)*z-2-direct(given))
    ev = [S.Symbol('v0'),S.Integer(0),S.Symbol('v2'),S.Integer(0),S.Symbol('v4'),S.Integer(0),S.Integer(1)]
    a,D,N = pan6(ev,S.Integer(0))
    assert D == N == 0
    zero(eval_pan(a,Ops())-direct(ev))
    zero(((x*x-x)*(x*x+x))*x*x-(x**6-x**4))
    bad = list(map(S.Integer,[0,1,0,0,0,0,1]))
    _,D,N = pan6(bad,t)
    assert D == 0 and N == 1
    return {'knuth_generic_cubic_reduction':True,'knuth_examples':3,
            'pan_residual_identity':str(residual_pan),
            'pan_example_and_optimization':True,'pan_even_family_D_N_zero':True,
            'pan_impossible_D_zero_N_nonzero':'x^6+x',
            'scope':'All identities are symbolic; general sextic leading coefficient is restored by one final multiplication.'}


def eve_eval(n,c,leading,a0,b0,alpha,beta,counter):
    y = counter.add(x,c)
    w = counter.mul(y,y)
    z = counter.mul(leading,y)
    if n % 2 == 0: z = counter.mul(counter.add(z,a0),y)
    z = counter.add(z,b0)
    for j,(a,b) in enumerate(zip(alpha,beta)):
        z = counter.mul(z,counter.sub(w,a))
        if j < len(beta)-1 or b != 0: z = counter.add(z,b)
    return z


def eve_block():
    given = (x+7)*(x*x+6*x+10)*(x*x+4*x+5)*(x+1)
    examples = [dict(c=2,a0=6,b0=S.Rational(16,3),alpha=[S.Rational(1,3),-1],beta=[-S.Rational(74,9),0]),
                dict(c=4,a0=-6,b0=12,alpha=[-3,9],beta=[-26,0])]
    for a in examples:
        c = Ops()
        zero(eve_eval(6,leading=1,counter=c,**a)-given)
        assert c.counts() == [5,6]
    pc3 = S.Poly(S.expand(given.subs(x,x-3)),x)
    assert pc3.nth(5) == 0 and pc3.nth(3) != 0
    # A symbolic division certificate for the odd-coefficient criterion.
    a = S.symbols('a0:10')
    divisions = 0
    for n in range(3,10):
        p = sum(a[j]*x**j for j in range(n+1))
        q = sum(a[j]*W**((j-1)//2) for j in range(1,n+1,2))
        rem = S.rem(p,x*x-t,x)
        zero(S.Poly(rem,x).nth(1)-q.subs(W,t))
        divisions += 1
        m = (n+1)//2-1
        c = Ops()
        eve_eval(n,S.Symbol('c'),a[n],a[0],a[1],
                 S.symbols('b:'+str(m)),[1]*(m-1)+[0],c)
        assert c.counts() == [n//2+2,n]
    # The two printed directions fail already for this right-half-plane polynomial.
    tr = S.Symbol('tr',real=True)
    fr = (S.I*tr-1)**4
    zero(S.im(S.diff(fr,tr)/fr)+4/(1+tr*tr))
    # Odd n: a_(n-1)=0 need not imply q=0. The scheme still succeeds.
    c = Ops()
    zero(eve_eval(3,0,1,0,0,[-1],[0],c)-(x**3+x))
    return {'exercise24_solutions':2,'c3_q':str(sum(pc3.nth(j)*W**((j-1)//2) for j in [1,3,5])),
            'constant_remainder_symbolic_checks':divisions,
            'operation_counts_n3_through9':True,
            'clockwise_witness':'f(z)=(z-1)^4; d arg f(it)/dt=-4/(1+t^2)',
            'odd_degree_boundary':'x^3+x: c=0, a2=0, q(W)=W+1',
            'scope':'Finite symbolic checks supplement, but do not replace, the general proof of Eve\'s root-location lemma.'}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('block',choices=['low_degrees','sextics','eve'])
    a = p.parse_args()
    d = json.loads(RESULT.read_text()) if RESULT.exists() else {}
    assert a.block not in d, 'Do not repeat a passed block'
    start = time.perf_counter()
    r = globals()[a.block+'_block']()
    r.update(status='passed',pid=os.getpid(),seconds=time.perf_counter()-start,
             completed_at_utc=datetime.now(timezone.utc).isoformat())
    d[a.block] = r
    RESULT.write_text(json.dumps(d,indent=2)+'\n')
    print(json.dumps({a.block:r}),flush=True)


if __name__ == '__main__':
    main()
