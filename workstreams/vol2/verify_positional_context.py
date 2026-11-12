#!/usr/bin/env python3
"""New exact numerical checks for the historical context of 4.1.

The earlier positional-basic tests are not repeated. Their rational Machin
bound helper is reused for the new 35-place and Madhava checks.
"""
from fractions import Fraction as F
from itertools import groupby
from pathlib import Path
import json
from verify_positional_basic import pi_bounds

ROOT=Path(__file__).resolve().parent
lo,hi=pi_bounds()
# Manually read from Gerhardt1855, printed97; last position is printed 1/0.
lines=['111100100000010011111101100110001101101101100110000100',
       '111100100101100101011011011010100011011100101010000000',
       '1111010000']
s=''.join(lines)
run_word='421612612223212121222412421211221111212121111321321111174114'
assert ''.join(str(len(list(g))) for _,g in groupby(s))==run_word
expected=314159265358979323846264338327950288
assert expected < 10**35*lo < 10**35*hi < expected+1
actual=int(s,2)
assert len(s)==118 and actual==314159265358979323846264338327929808
records=[]
for last in (0,1):
    b=actual+last;a=expected+last
    differences=[i for i in range(118) if (a^b)>>i&1]
    assert differences==[12,14] and a-b==20480
    records.append(dict(last_digit=last,printed_integer=str(b),correct_integer=str(a),
                        incorrect_bit_exponents=differences,difference=a-b))
madhava=2827433388233
err_lo=madhava-9*10**11*hi;err_hi=madhava-9*10**11*lo
assert F(2186,1000)<err_lo<err_hi<F(2187,1000)
octal=3+F(int('1463',8),8**4-1)
assert octal/64==F(5,100)
assert int('111001',2)**2==int('110010110001',2)==3249
assert int('1001111',2)**3==int('1111000010111101111',2)==493039
result=dict(status='passed',bernoulli=dict(lines=lines,run_word=run_word,cases=records),
            madhava=dict(scaled_absolute_error_interval=['2.186','2.187'],
                         pi_absolute_error_interval=[str(F(2186,1000)/(9*10**11)),str(F(2187,1000)/(9*10**11))]),
            octal_percentage=dict(period='1463',value=str(octal),per=64,result='1/20'),
            pelikan=dict(square_root=[57,3249],cube_root=[79,493039]),
            scope='Arithmetic only; original source scope and historical limits in notes/positional-context.md.')
(ROOT/'results/positional-context.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False),flush=True)
