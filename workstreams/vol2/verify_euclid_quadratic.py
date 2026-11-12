#!/usr/bin/env python3
"""Independent exact quadratic-field validation for TAOCP 4.5.3-11/12."""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from math import isqrt
from pathlib import Path
import json, os, random, sys, time

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/euclid-quadratic.json'


@dataclass(frozen=True)
class Q:
    """a + b*sqrt(D), evaluated by field operations and rational enclosures."""
    a: F
    b: F
    D: int

    def __post_init__(self):
        object.__setattr__(self,'a',F(self.a))
        object.__setattr__(self,'b',F(self.b))

    def __add__(self, other):
        if not isinstance(other,Q):
            other = Q(other,0,self.D)
        assert self.D == other.D
        return Q(self.a+other.a,self.b+other.b,self.D)

    def __neg__(self):
        return Q(-self.a,-self.b,self.D)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if not isinstance(other,Q):
            other = Q(other,0,self.D)
        assert self.D == other.D
        return Q(self.a*other.a+self.D*self.b*other.b,
                 self.a*other.b+self.b*other.a,self.D)

    def inv(self):
        norm = self.a*self.a-self.D*self.b*self.b
        assert norm
        return Q(self.a/norm,-self.b/norm,self.D)

    def floor(self):
        if not self.b:
            return self.a.__floor__()
        bits = 16
        while True:
            scale = 1 << bits
            s = isqrt(self.D*scale*scale)
            ends = [self.a+self.b*F(s,scale),self.a+self.b*F(s+1,scale)]
            lo,hi = sorted(ends)
            if lo.__floor__() == hi.__floor__():
                return lo.__floor__()
            bits *= 2
            assert bits < 8192


def integer_floor_root(D,U,V):
    """Floor of (sqrt(D)+U)/V; the printed integer-only rule."""
    return (isqrt(D)+(V<0)+U)//V


def reduced(D,U,V):
    if not (U>0 and U*U<D and V>0):
        return False
    # V < sqrt(D)+U; all comparisons are exact integer comparisons.
    return V-U <= 0 or (V-U)**2 < D


def check_quadratic(D,U,V):
    source_D,source_U,source_V = D,U,V
    original = Q(F(-U,V),F(1,V),D)
    multiplier = 1
    if (D-U*U)%V:
        multiplier = abs(V)
        D,U,V = D*V*V,U*abs(V),V*abs(V)
    assert (D-U*U)%V == 0
    initial_U,initial_V = U,V
    a0 = integer_floor_root(D,-U,V)
    assert a0 == original.floor()
    U += a0*V
    tail = original-a0
    p,q,previous_p,previous_q = a0,1,1,0
    seen,states,quotients = {},[],[]
    previous_state = None
    previous_a = None
    n = 0
    while (U,V) not in seen:
        assert n < 2000
        seen[U,V] = n
        states.append((U,V))
        assert tail == Q(F(-U,V),F(multiplier,V),source_D)
        assert tail.floor() == 0 and tail.a*tail.a-source_D*tail.b*tail.b != 0
        assert (D-U*U)%V == 0
        new_V = (D-U*U)//V
        a = integer_floor_root(D,U,new_V)
        assert a >= 1 and a == tail.inv().floor()
        new_U = a*new_V-U
        norm = initial_V*p*p+2*initial_U*p*q+F(initial_U**2-D,initial_V)*q*q
        cross = initial_V*p*previous_p+initial_U*(p*previous_q+previous_p*q) + \
            F(initial_U**2-D,initial_V)*q*previous_q
        assert norm == (-1)**(n+1)*new_V
        assert cross == (-1)**n*U
        if previous_state is not None:
            old_U,old_V = previous_state
            assert new_V == previous_a*(old_U-U)+old_V
        if reduced(D,U,V):
            assert reduced(D,new_U,new_V)
            inverse_a = integer_floor_root(D,new_U,new_V)
            inverse_U = inverse_a*new_V-new_U
            inverse_V = (D-inverse_U*inverse_U)//new_V
            assert inverse_a == a and (inverse_U,inverse_V) == (U,V)
        previous_state,previous_a = (U,V),a
        U,V = new_U,new_V
        p,previous_p = a*p+previous_p,p
        q,previous_q = a*q+previous_q,q
        tail = tail.inv()-a
        quotients.append(a)
        n += 1
    start = seen[U,V]
    assert all(reduced(D,u,v) == (i>=start) for i,(u,v) in enumerate(states))
    assert all(u>0 and u*u<D and v>0 and v*v<4*D for u,v in states[start:])
    return dict(input=[source_D,source_U,source_V], normalized_D=D,
                a0=a0, prefix=quotients[:start], period=quotients[start:],
                steps=n, preperiod=start)


def quadratic():
    cases = [(D,U,V) for D in range(2,61) if isqrt(D)**2 != D
             for U in range(-6,7) for V in range(-10,11)
             if V and (D-U*U)%V == 0]
    rng = random.Random(45312)
    for _ in range(80):
        D = rng.randrange(2,10000)
        if isqrt(D)**2 == D:
            D += 1
        cases.append((D,rng.randrange(-100,101),rng.choice([-1,1])*rng.randrange(1,41)))
    steps=0
    longest=None
    negative=normalizations=0
    for D,U,V in cases:
        r = check_quadratic(D,U,V)
        steps += r['steps']
        negative += V<0
        normalizations += r['normalized_D'] != D
        if longest is None or r['steps'] > longest['steps']:
            longest = r
    example = check_quadratic(232,0,29)
    # The first displayed partial quotients of sqrt(8/29), p.358.
    digits = example['prefix']+example['period']*4
    expected = [1]+[1,9,2,2,3,2,2,9,1,2]*3
    assert example['a0'] == 0 and digits[:31] == expected
    return dict(inputs=len(cases), steps=steps, negative_denominators=negative,
                rescaled_inputs=normalizations, longest=longest, sqrt_8_over_29=example)


def tail_orbit(x):
    a0 = x.floor()
    x = x-a0
    seen,states = {},[]
    while x not in seen:
        assert len(states)<2000
        seen[x] = len(states)
        states.append(x)
        z = x.inv()
        x = z-z.floor()
    start = seen[x]
    # Two copies permit both possible parity matches for an odd period.
    return states+states[start:]+states[start:]


def serret():
    rng = random.Random(45311)
    count=0
    for D in [2,3,5,7,13,19,23,61]:
        y = Q(F(-2,3),F(1,3),D)
        yo = tail_orbit(y)
        for _ in range(20):
            a,b,c,d = 1,0,0,1
            x = y
            for _ in range(rng.randrange(1,13)):
                op = rng.randrange(3)
                if op == 0:
                    t = rng.randrange(-5,6)
                    a,b,c,d = a+t*c,b+t*d,c,d
                    x = x+t
                elif op == 1:
                    a,b,c,d = c,d,a,b
                    x = x.inv()
                else:
                    a,b = -a,-b
                    x = -x
            det = a*d-b*c
            assert abs(det) == 1
            assert x == (y*a+b)*(y*c+d).inv()
            xo = tail_orbit(x)
            matches = [(i,j) for i,u in enumerate(xo) for j,v in enumerate(yo)
                       if u == v and (-1)**(i-j) == det]
            assert matches,(D,a,b,c,d)
            count += 1
    return dict(unimodular_transforms=count, exact_tail_and_parity_matches=True)


def main():
    print('PID',os.getpid(),flush=True)
    data = json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
    for fn in [quadratic,serret]:
        if data.get(fn.__name__,{}).get('status') == 'passed':
            continue
        start = time.monotonic()
        result = fn()
        data[fn.__name__] = dict(status='passed',seconds=time.monotonic()-start,result=result)
        OUT.write_text(json.dumps(data,indent=2)+'\n')
        print(fn.__name__,data[fn.__name__]['seconds'],flush=True)


if __name__ == '__main__':
    main()
