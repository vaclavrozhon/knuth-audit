"""Exact, bounded reproduction of the two specified MMIX Fibonacci loops.
Only binary64 positive normal arithmetic is needed; no simulator or broad search.
"""
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path
import json


def nearest_integer(x):
    a, r = divmod(x.numerator, x.denominator)
    return a + (2*r > x.denominator or (2*r == x.denominator and a & 1))


def binary64(x):
    e = x.numerator.bit_length() - x.denominator.bit_length()
    if (x < (Q(1 << e) if e >= 0 else Q(1, 1 << -e))):
        e -= 1
    sh = 52-e
    scaled = x * (1 << sh) if sh >= 0 else x / (1 << -sh)
    m = nearest_integer(scaled)
    return Q(m, 1 << sh) if sh >= 0 else Q(m * (1 << -sh))


def bits(x):
    e = x.numerator.bit_length() - x.denominator.bit_length()
    if x < (Q(1 << e) if e >= 0 else Q(1, 1 << -e)):
        e -= 1
    sig = x * (1 << (52-e)) if e <= 52 else x / (1 << (e-52))
    assert sig.denominator == 1
    return f'{((e+1023)<<52) + int(sig) - (1<<52):016x}'

# FSQRT(5): choose between adjacent exact binary64 values by squaring
# their midpoint; sqrt(5) is irrational, so equality cannot occur.
s = isqrt(5 << 102)
s += (5 << 104) > (2*s+1)**2
rt5 = Q(s, 1 << 51)
phi = binary64(Q(1)+rt5)/2
acc = binary64(phi/rt5)
assert nearest_integer(binary64(1/rt5)) == 0
assert nearest_integer(acc) == 1
old,new = 0,1
rows=[]
for n in range(2,95):
    old,new = new,old+new
    acc = binary64(acc*phi)
    got = nearest_integer(acc)
    if n >= 69:
        rows.append({'n':n,'F_n':new,'approximation_bits':bits(acc),'rounded':got,
                     'error_exact':str(acc-new)})
    if got != new:
        first_a=n; break
assert first_a == 71
B=1<<64;phii=0x9e3779b97f4a7c16
old=new=1;last=None
for n in range(3,95):
    mathematical = old+new
    new_wrapped = mathematical % B
    if new_wrapped < new:
        overflow={'n':n,'F_n':mathematical,'wrapped':new_wrapped,'previous_F':new}
        break
    old,new = new,new_wrapped
    hi,lo=divmod(old*phii,B)
    got=old+hi+(lo >= B//2)
    assert got==new, (n,got,new)
    last={'n':n,'F_n':new,'previous_F':old,'rounded_fixed_result':got}
assert overflow['n']==94
out={'method':'Exact rational binary64 rounding and integer high/low products; bounded loops only through the printed stopping indices.',
     'sqrt5_bits':bits(rt5),'phi_bits':bits(phi),'first_floating_failure':first_a,
     'floating_boundary':rows,'fixed_last_success':last,'first_unsigned_overflow':overflow,
     'fixed_rounding_convention':'lo>=2^63 rounds upward; exactly the CSN rule in the printed program.'}
p=Path(__file__).parent/'results/fibonacci27-exact.json'
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
