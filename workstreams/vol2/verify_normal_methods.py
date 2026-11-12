"""Independent interval reconstruction of TAOCP2 3.4.1 normal generators.

Intervals enclose Taylor integrals, alias construction and all printed
table constants; root locations are certified by monotone bisection.
"""
from fractions import Fraction as Q
from math import factorial, comb
from pathlib import Path
import json
import sys
import mpmath as mp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/normal-methods.json'
mp.mp.dps = 90
mp.iv.dps = 90
I = mp.iv


def bounds(v):
    def convert(t):
        sign, mantissa, exponent, _ = t
        return (-1)**sign * Q(mantissa) * Q(2)**exponent
    return tuple(convert(t) for t in v._mpi_)


def iq(q):
    q = Q(q)
    return I.mpf(q.numerator)/q.denominator


def between(lo, hi):
    return iq(lo) + I.mpf([0, 1])*iq(hi-lo)


def approx(v):
    a, b = bounds(v)
    return mp.mpf(a.numerator)/a.denominator/2+mp.mpf(b.numerator)/b.denominator/2


def serialize(v):
    return dict(enclosure=[str(t) for t in bounds(v)], decimal=mp.nstr(approx(v), 35))


def round_check(v, printed, label):
    digits = len(printed.split('.')[1]) if '.' in printed else 0
    center, radius = Q(printed), Q(1, 2*10**digits)
    a, b = bounds(v)
    return dict(label=label, printed=printed, matches=center-radius < a <= b < center+radius,
                **serialize(v))


def normal_cdf(x):
    """Half-normal CDF for rational 0<=x<=3, alternating integrated series."""
    x = Q(x)
    assert 0 <= x <= 3
    n = 160
    total = sum((-1)**j*x**(2*j+1)/Q(2**j*factorial(j)*(2*j+1)) for j in range(n+1))
    next_term = x**(2*n+3)/Q(2**(n+1)*factorial(n+1)*(2*n+3))
    # For j>=160, successive absolute terms have ratio < (9/2)/(j+1)<1.
    return I.sqrt(2/I.pi)*(iq(total)+I.mpf([-1, 1])*iq(next_term))


def density(x):
    return I.sqrt(2/I.pi)*I.exp(-x*x/2)


def parameters():
    h = iq(Q(1, 5))
    s = {j: iq(Q(j-1, 5)) for j in range(1, 17)}
    cdf = {j: normal_cdf(Q(j-1, 5)) for j in range(1, 17)}
    p = {j: h*density(s[j+1]) for j in range(1, 16)}
    p.update({j+15: cdf[j+1]-cdf[j]-p[j] for j in range(1, 16)})
    p[31], p[32] = 1-cdf[16], I.mpf(0)
    for j in range(1, 32):
        assert bounds(p[j])[0] > 0
    lo, hi = bounds(sum(p.values()))
    assert lo <= 1 <= hi
    # Independent analytic moments check the integrated Taylor CDF against erf.
    for j in range(1, 17):
        value = mp.erf(mp.mpf(j-1)/5/mp.sqrt(2))
        assert abs(approx(cdf[j])-value) < mp.mpf('1e-85')
    remaining = [(v, j) for j, v in p.items()]
    P, alias, trace = {}, {}, []
    while len(remaining) > 1:
        remaining.sort(key=lambda t: approx(t[0]))
        for (v, _), (w, _) in zip(remaining, remaining[1:]):
            assert bounds(v)[1] < bounds(w)[0]
        q1, j = remaining.pop(0)
        qn, k = remaining.pop()
        assert bounds(q1)[1] < Q(1, 32) < bounds(qn)[0]
        P[j], alias[j] = 32*q1, k
        assert 1 <= k <= 15
        remaining.append((qn-(iq(Q(1, 32))-q1), k))
        trace.append(dict(column=j, donor=k))
    qlast, j = remaining[0]
    lo, hi = bounds(qlast)
    assert lo <= Q(1, 32) <= hi
    P[j], alias[j] = I.mpf(1), None
    P[0], alias[0] = P.pop(32), alias.pop(32)
    Y, Z = {}, {}
    for j in range(32):
        if alias[j] is None:
            Y[j] = Z[j] = None
        else:
            Z[j] = 1/(5*(1-P[j]))
            Y[j] = iq(Q(alias[j], 5))-Z[j]
    # Independent branch-mass validator, without the alias construction invariant.
    actual = {j: I.mpf(0) for j in range(1, 33)}
    for j in range(32):
        actual[j or 32] += P[j]/32
        if alias[j] is not None:
            actual[alias[j]] += (1-P[j])/32
    for j in range(1, 33):
        a, b = bounds(actual[j]-p[j])
        assert a <= 0 <= b and b-a < Q(1, 10**80)
    D, E, roots, av, bv = {}, {}, {}, {}, {}
    for j in range(1, 16):
        w = p[j+15]
        def g(x):
            return (density(x)-density(s[j+1]))/w
        if j <= 5:
            a = g(s[j])
            b = h*s[j+1]*density(s[j+1])/w
            E[j+15] = iq(Q(25, j))
        else:
            b = g(s[j])
            lo, hi = Q(j-1, 5), Q(j, 5)
            # On x>1, x*exp(-x*x/2) strictly decreases.
            for _ in range(230):
                mid = (lo+hi)/2
                value = iq(mid)*density(iq(mid))-w*b/h
                vl, vh = bounds(value)
                if vl > 0:
                    lo = mid
                elif vh < 0:
                    hi = mid
                else:
                    raise AssertionError(('insufficient root precision', j))
            x = between(lo, hi)
            a = g(x)+(x-s[j])*b/h
            roots[j] = x
            E[j+15] = 1/(I.exp(iq(Q(2*j-1, 50)))-1)
        av[j], bv[j], D[j+15] = a, b, a/b
        assert 0 < bounds(D[j+15])[0] < bounds(D[j+15])[1] < 1
        # The expensive acceptance expression equals g/b throughout the interval.
        for numerator in range(1, 10):
            x = s[j]+h*iq(Q(numerator, 10))
            delta = E[j+15]*(I.exp((s[j+1]**2-x*x)/2)-1)-g(x)/b
            dl, dh = bounds(delta)
            assert dl <= 0 <= dh and dh-dl < Q(1, 10**80)
    return dict(s=s, p=p, P=P, Y=Y, Z=Z, D=D, E=E, roots=roots,
                a=av, b=bv, alias=alias, trace=trace,
                Q={j: 1/(5*P[j]) for j in range(1, 16)})


def mixture_table():
    z = parameters()
    columns = {
        'P': '.000 .849 .970 .855 .994 .995 .933 .923 .727 1.000 .691 .454 .287 .174 .101 .057 .067 .161 .236 .285 .308 .304 .280 .241 .197 .152 .112 .079 .052 .033 .020 .086'.split(),
        'Q': '.236 .206 .234 .201 .201 .214 .217 .275 .200 .289 .440 .698 1.150 1.974 3.526'.split(),
        'Y': '0.00 -.92 -5.86 -.58 -33.16 -39.51 -2.57 -1.61 .67 * .35 -.17 .92 .36 -.02 .19 .59 .96 -.06 .12 1.31 .31 1.12 .54 .75 .56 .17 .38 -.01 .39 .20 .78'.split(),
        'Z': '.20 1.32 6.66 1.38 34.96 41.31 2.97 2.61 .73 * .65 .37 .28 .24 .22 .21 .21 .24 .26 .28 .29 .29 .28 .26 .25 .24 .23 .22 .21 .21 .20 .22'.split(),
        'D': '.505 .773 .876 .939 .986 .995 .987 .979 .972 .966 .960 .954 .948 .942 .936'.split(),
        'E': '25.00 12.50 8.33 6.25 5.00 4.06 3.37 2.86 2.47 2.16 1.92 1.71 1.54 1.40 1.27'.split(),
        's': '0.0 .2 .4 .6 .8 1.0 1.2 1.4 1.6 1.8 2.0 2.2 2.4 2.6 2.8 3.0'.split(),
    }
    starts = dict(P=0, Q=1, Y=0, Z=0, D=16, E=16, s=1)
    checks = []
    for col, values in columns.items():
        for j, printed in enumerate(values, starts[col]):
            value = z[col][j]
            if printed == '*':
                assert value is None
                continue
            checks.append(round_check(value, printed, f'{col}{j}'))
    for col, printed_values, start in [
        ('p', '.156 .147 .133 .116 .097 .078 .060 .044 .032 .022 .014 .009 .005 .003 .002 .002 .005 .007 .009 .010 .009 .009 .008 .006 .005 .004 .002 .002 .001 .001 .003', 1),
        ('roots', '1.115 1.304 1.502 1.700 1.899 2.099 2.298 2.497 2.697 2.896', 6),
        ('a', '7.5 9.1 9.5 9.8 9.9 10.0 10.0 10.1 10.1 10.1 10.1 10.2 10.2 10.2 10.2', 1),
        ('b', '14.9 11.7 10.9 10.4 10.1 10.1 10.2 10.3 10.4 10.5 10.6 10.7 10.7 10.8 10.9', 1)]:
        for j, printed in enumerate(printed_values.split(), start):
            checks.append(round_check(z[col][j], printed, f'answer10:{col}{j}'))
    rectangles = sum(z['p'][j] for j in range(1, 16))
    tail_accept = 3*I.exp(I.mpf(9)/2)*(1-normal_cdf(3))/I.sqrt(2/I.pi)
    return dict(checks=checks, total_printed_numbers=len(checks),
                mismatches=[c for c in checks if not c['matches']],
                alias_trace=z['trace'], alias_donors=z['alias'],
                rectangle_probability=serialize(rectangles),
                tail_probability=serialize(z['p'][31]),
                tail_rejection_probability=serialize(1-tail_accept),
                known_corrections='2000-07-28: Y4,Y5,Z4,Z5 corrected; Y9,Z9 unused. 2024-06-30: root wording.',
                precision='90 decimal outward intervals; exact rational alternating integral remainder; 230 monotone root bisections.')


def cdf_series(q):
    """Interval half-normal CDF on [0,8], using 241 integrated terms."""
    q = Q(q)
    assert 0 <= q <= 8
    x = iq(q)
    term = total = x
    for j in range(240):
        term = -term*x*x*(2*j+1)/(2*(j+1)*(2*j+3))
        total += term
    nxt = -term*x*x*481/(482*483)
    error = max(abs(t) for t in bounds(nxt))
    return I.sqrt(2/I.pi)*(total+between(-error, error))


def odd_even():
    a = I.mpf(0)
    ordinary = I.mpf(0)
    recycled = I.mpf(0)
    rows = []
    bits, count, terms = 160, 40, 30
    independent = mp.mpf(0)
    previous_point = mp.mpf(0)
    for j in range(1, count+1):
        point = mp.sqrt(2)*mp.erfinv(1-mp.mpf(2)**(-j))
        base = int(mp.floor(point*2**bits))
        lo, hi = Q(base-1, 2**bits), Q(base+2, 2**bits)
        target = 1-Q(1, 2**j)
        assert bounds(cdf_series(lo))[1] < target < bounds(cdf_series(hi))[0]
        b = between(lo, hi)
        d = b-a
        u, v = a*d, d*d/2
        assert bounds(u+v)[1] < bounds(I.log(2))[0]
        # Integral of exp(u*t+v*t^2), 0<=t<=1, via positive moments.
        av = I.mpf(0)
        for n in range(terms+1):
            moment = sum(comb(n, ell)*u**(n-ell)*v**ell/(n+ell+1) for ell in range(n+1))
            av += moment/factorial(n)
        av += between(Q(0), Q(2, factorial(terms+1)))
        accept = I.sqrt(I.pi/2)*I.exp(a*a/2)*iq(Q(1, 2**j))/d
        ordinary += iq(Q(1, 2**j))*(av+1)/accept
        recycled += iq(Q(1, 2**j))*av/accept
        # Different numerical representation: erfi antiderivative of exp(x^2/2).
        length = point-previous_point
        acc0 = mp.sqrt(mp.pi/2)*mp.mpf(2)**(-j)*mp.exp(previous_point**2/2)/length
        av0 = (mp.exp(-previous_point**2/2)*mp.sqrt(mp.pi/2)
               *(mp.erfi(point/mp.sqrt(2))-mp.erfi(previous_point/mp.sqrt(2)))/length)
        independent += mp.mpf(2)**(-j)*av0/acc0
        rows.append(dict(j=j, quantile=serialize(b), acceptance=serialize(accept),
                         average_comparisons=serialize(av)))
        a, previous_point = b, point
    il, ih = bounds(recycled)
    assert mp.mpf(il.numerator)/il.denominator < independent < mp.mpf(ih.numerator)/ih.denominator
    # h<ln2 implies acceptance>1/2 and average comparisons<2.
    ordinary += between(Q(0), Q(6, 2**count))
    recycled += between(Q(0), Q(4, 2**count))
    f_round = round_check(ordinary, '2.53947', 'ordinary-F')
    corrected = round_check(recycled, '1.37746', 'Brent-corrected')
    printed = round_check(recycled, '1.37446', 'Brent-printed')
    assert f_round['matches'] and corrected['matches'] and not printed['matches']
    return dict(quantiles=rows, ordinary=f_round, recycled_corrected=corrected,
                recycled_printed=printed, independent_erfi_partial_sum=mp.nstr(independent, 65),
                ordinary_tail_bound=str(Q(6, 2**count)), recycled_tail_bound=str(Q(4, 2**count)),
                proof='40 quantile brackets independently certified by alternating CDF integrals; 30-term positive moment expansion; geometric upper bounds for the infinite remainder.')


def ratio_areas():
    import sympy as s
    u, a, b = s.symbols('u a b', positive=True)
    primitive0 = (a-b*u)**s.Rational(3, 2)*(s.Rational(2, 5)*(a-b*u)-s.Rational(2, 3)*a)/b**2
    primitive_minus = (b*b*a**(-s.Rational(3, 2))*s.asin(2*u*a/b-1)/8
                       +b/a*s.sqrt(b*u-a*u*u)*(2*u*a/b-1)/4)
    primitive_plus = (-b*b*a**(-s.Rational(3, 2))*s.log(s.sqrt(b*u+a*u*u)+u*s.sqrt(a)+b/(2*s.sqrt(a)))/8
                      +b/a*s.sqrt(b*u+a*u*u)*(2*u*a/b+1)/4)
    # Verify the nontrivial logarithmic primitive; the minus case is checked
    # after substituting u=b*(1+sin(theta))/(2*a), avoiding branch ambiguity.
    assert s.simplify(s.diff(primitive0, u)-u*s.sqrt(a-b*u)) == 0
    assert s.simplify(s.diff(primitive_plus, u)-s.sqrt(b*u+a*u*u)) == 0
    theta = s.symbols('theta', real=True)
    # The corresponding primitive expressed on -pi/2<theta<pi/2 is exact.
    trig_primitive = b*b/(8*a**s.Rational(3, 2))*(theta+s.sin(theta)*s.cos(theta))
    assert s.trigsimp(s.diff(trig_primitive, theta)-b*b/(4*a**s.Rational(3, 2))*s.cos(theta)**2) == 0
    R, A = I.sqrt(8/I.e), I.sqrt(I.pi/2)
    interior = iq(Q(5, 6))*I.sqrt(5/I.e)
    h = I.sqrt(2/I.e)
    aa, bb = iq(Q(7, 5)), 4*I.exp(-iq(Q(27, 20)))
    r = 2*h*h/(bb+I.sqrt(bb*bb+4*aa*h*h))
    def plus_at(t):
        w = I.sqrt(bb*t+aa*t*t)
        return (-bb*bb/(8*aa*I.sqrt(aa))*I.log(w+t*I.sqrt(aa)+bb/(2*I.sqrt(aa)))
                +bb/(4*aa)*w*(2*t*aa/bb+1))
    exterior = 2*(h*r-plus_at(r)+plus_at(I.mpf(0)))
    numeric = 2*mp.quad(lambda t:mp.sqrt(2/mp.e)-mp.sqrt(4*mp.exp(-mp.mpf(27)/20)*t+mp.mpf(7)/5*t*t), [0, approx(r)])
    assert abs(approx(exterior)-numeric) < mp.mpf('1e-80')
    counts = [[R/A]*4, [I.mpf(0), R/A, I.mpf(0), R/A],
              [I.mpf(0), I.mpf(0), R/A, (R-interior)/A],
              [R/A, (R-interior)/A, (R-exterior)/A, (R-interior-exterior)/A]]
    printed = [['1.369']*4, ['0','1.369','0','1.369'],
               ['0','0','1.369','.467'], ['1.369','.467','1.134','.232']]
    checks = [round_check(value, printed[i][j], f'R{i+1}-variant{j+1}')
              for i, row in enumerate(counts) for j, value in enumerate(row)]
    checks.extend([round_check(R, '1.71553', 'R'), round_check(A, '1.25331', 'A'),
                   round_check(interior, '1.13020', 'I'), round_check(exterior, '.29410', 'E')])
    assert all(v['matches'] for v in checks)
    # New issue: x=1 makes the R3 boundary v^2=4*u*(1-u), symmetric in u.
    r1 = (1-I.sqrt(1-2/I.e))/2
    t = 2*r1-1
    angle = I.atan2(t, I.sqrt(1-t*t))
    integral = angle/4+I.sqrt(r1*(1-r1))*t/2+I.pi/8
    printed_area = 2*(h*r1-integral)
    true_area = 2*printed_area
    assert bounds(printed_area)[0] > Q(12, 100)
    return dict(checks=checks, areas=dict(R=serialize(R), A=serialize(A),
                I=serialize(interior), E=serialize(exterior)),
                symbolic_primitives='All three verified, including 2005 factor-a correction; tangent-area maximization proved in notes.',
                x1_counterexample=dict(left_root=serialize(r1), after_2005_formula=serialize(printed_area),
                    actual_both_horizontal_sides=serialize(true_area),
                    proof='Reflection u->1-u gives a second congruent positive rejection region omitted by the stated integral.'),
                scope='20 interval rounding checks; independent quadrature of E at the actual algorithm parameter x=-0.35. No global optimization claim inferred from a grid.')


def main():
    out = json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
    for name, fn in [('mixture_table', mixture_table), ('odd_even', odd_even), ('ratio_areas', ratio_areas)]:
        if name in out:
            continue
        print('START', name, flush=True)
        out[name] = fn()
        OUT.write_text(json.dumps(out, indent=2)+'\n')
        print('PASS', name, 'mismatches:', len(out[name].get('mismatches', [])), flush=True)


if __name__ == '__main__':
    main()
