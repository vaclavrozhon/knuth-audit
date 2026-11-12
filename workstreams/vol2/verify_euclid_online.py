#!/usr/bin/env python3
"""Exact checks of Hurwitz identities and Gosper's online homographies."""
from fractions import Fraction as F
from itertools import product, islice
from math import ceil, floor, isqrt
from pathlib import Path
import json, os, random, sys, time
from verify_euclid_quadratic import Q

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/euclid-online.json'


def cf_value(digits):
    p,q = 1,0
    for a in reversed(digits):
        p,q = a*p+q,p
    return F(p,q)


def cf_digits(x):
    result = []
    while True:
        a = floor(x)
        result.append(a)
        if x == a:
            return result
        x = 1/(x-a)


def C(*digits):
    return cf_value([0]+list(digits))


def multiply(X,Y):
    a,b,c,d = X
    e,f,g,h = Y
    return a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h


def matrix(digits):
    result = (1,0,0,1)
    for a in digits:
        result = multiply(result,(a,1,1,0))
    return result


def emit_digit(state):
    a,b,c,d = state
    if c*(c+d) <= 0:
        # A pole in the interval or at an endpoint makes the image unbounded.
        return None
    lo,hi = sorted([F(a,c),F(a+b,c+d)])
    if ceil(hi)-floor(lo) == 1:
        return floor(lo)
    return None


def consume(state,x):
    a,b,c,d = state
    return a*x+b,a,c*x+d,c


def emit(state,x):
    a,b,c,d = state
    return c,d,a-x*c,b-x*d


def finite_transform(original,digits,trace=False):
    a,b,c,d = original
    source = cf_value(digits)
    target = (a*source+b)/(c*source+d)
    state = original
    j = 0
    output = []
    events = []
    while True:
        k = emit_digit(state) if j else None
        if k is None:
            x = digits[j]
            if j == len(digits)-1:
                a,b,c,d = state
                final = F(a*x+b,c*x+d)
                tail = cf_digits(final)
                output += tail
                if trace:
                    events.append(dict(action='finish',input=x,state=state,output=tail))
                assert cf_value(output) == target
                assert output == cf_digits(target)
                return output,events
            state = consume(state,x)
            j += 1
            if trace:
                events.append(dict(action='input',digit=x,state=state))
        else:
            output.append(k)
            state = emit(state,k)
            if trace:
                events.append(dict(action='output',digit=k,state=state))


def infinite_transform(original,source):
    state = consume(original,next(source))
    consumed = 1
    steps = 0
    while True:
        steps += 1
        assert steps < 100000
        k = emit_digit(state)
        if k is None:
            state = consume(state,next(source))
            consumed += 1
        else:
            state = emit(state,k)
            yield k,consumed


def identities():
    count = 0
    for a,b,c,d in product(range(5),range(1,9),range(1,9),range(1,5)):
        tail = C(c,d)
        assert 2*C(2*a,b,c,d) == C(a,2*b+2*tail)
        assert 2*C(2*a+1,b,c,d) == C(a,1,1+2*C(b-1,c,d))
        count += 2
    D = (1,0,0,2)
    assert multiply(D,matrix([2,1])) == multiply(matrix([1,2]),D)
    for m in range(100):
        left = multiply(D,matrix([4*m+2,1,1,4*m+4,1,1]))
        right = multiply(matrix([2*m+1,3,1,2*m+1,1,3]),D)
        expected = (64*m*m+120*m+51,32*m*m+64*m+28,32*m+40,16*m+22)
        assert left == right == expected
    return dict(hurwitz_identities=count,e_half_block_checks=100)


def finite_cases():
    rng = random.Random(45315)
    cases = 0
    skipped_poles = 0
    for _ in range(12000):
        source = F(rng.randrange(-500,501),rng.randrange(1,201))
        original = tuple(rng.randrange(-100,101) for _ in range(4))
        a,b,c,d = original
        if a*d-b*c == 0:
            continue
        if c*source+d == 0:
            skipped_poles += 1
            continue
        finite_transform(original,cf_digits(source))
        cases += 1
    original = (97,39,-62,-25)
    source = [-1,5,1,1,1,2,1,2]
    digits,events = finite_transform(original,source,True)
    expected_states = [(-58,97,37,-62),(-193,-58,123,37),
                       (123,37,53,16),(53,16,17,5),(17,5,2,1),
                       (22,17,3,2),(3,2,1,3),(5,3,4,1),(4,1,1,2),
                       (5,4,3,1),(14,5,7,3),(7,3,7,2),(7,2,0,1),(9,7,1,0)]
    assert [tuple(e['state']) for e in events[:-1]] == expected_states
    assert digits == [-2,2,3,7,1,1,1,12,2]
    # Integer endpoints need the open-interval rule, not equal endpoint floors.
    assert emit_digit((14,5,7,3)) == 1
    assert emit_digit((7,3,7,2)) == 1
    assert emit_digit((7,2,0,1)) is None
    assert emit_digit((-58,97,37,-62)) is None
    return dict(random_valid_cases=cases,undefined_poles_excluded=skipped_poles,
                printed_input=source,printed_output=digits,printed_trace=events)


def quadratic_digits(x):
    while True:
        a = x.floor()
        yield a
        x = (x-a).inv()


def infinite_cases():
    rng = random.Random(453150)
    cases = quotients = 0
    maximum_consumed = 0
    for _ in range(120):
        D = rng.randrange(2,100)
        if isqrt(D)**2 == D:
            D += 1
        x = Q(F(rng.randrange(-20,21),7),F(rng.choice([-1,1]),3),D)
        original = tuple(rng.randrange(-50,51) for _ in range(4))
        a,b,c,d = original
        if a*d-b*c == 0:
            continue
        target = (x*a+b)*(x*c+d).inv()
        oracle = quadratic_digits(target)
        transducer = infinite_transform(original,quadratic_digits(x))
        for digit,consumed in islice(transducer,100):
            assert digit == next(oracle)
            maximum_consumed = max(maximum_consumed,consumed)
            quotients += 1
        cases += 1
    return dict(quadratic_inputs=cases,checked_output_quotients=quotients,
                maximum_inputs_for_100_outputs=maximum_consumed)


def e_digits():
    yield 2
    m = 1
    while True:
        yield 1
        yield 2*m
        yield 1
        m += 1


def e_half():
    # Independent rational enclosure from Taylor's series; no input CF used here.
    n = 2000
    factorial = 1
    s = F(1)
    for k in range(1,n+1):
        factorial *= k
        s += F(1,factorial)
    lower,upper = s/2,(s+F(1,n*factorial))/2
    expected = [1,2]
    for m in range(100):
        expected += [2*m+1,3,1,2*m+1,1,3]
    output = list(islice(infinite_transform((1,0,0,2),e_digits()),len(expected)))
    assert [a for a,j in output] == expected
    previous_p,p,previous_q,q = 0,1,1,0
    for a,j in output:
        previous_p,p = p,a*p+previous_p
        previous_q,q = q,a*q+previous_q
        lo,hi = sorted([F(p,q),F(p+previous_p,q+previous_q)])
        assert lo < lower < upper < hi
    return dict(output_quotients=len(output),input_quotients=output[-1][1],
                independent_taylor_terms=n+1,certified_prefixes=len(output),
                first_50=expected[:50])


def main():
    print(f'PID {os.getpid()}',flush=True)
    result = json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
    for name,job in [('identities',identities),('finite',finite_cases),
                     ('infinite',infinite_cases),('e_half',e_half)]:
        if name in result:
            continue
        start = time.monotonic()
        data = job()
        data['seconds'] = time.monotonic()-start
        result[name] = data
        OUT.write_text(json.dumps(result,indent=2)+'\n')
        print(name,'passed',round(data['seconds'],3),flush=True)


if __name__ == '__main__':
    main()
