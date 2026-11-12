"""Targeted exact power certificates for the seven polynomials in MMIX answer37.
No polynomial search, trajectory census, or repeat of the general theorem.
"""
from pathlib import Path
import json

def mul_mod(a,b,f):
    degree=f.bit_length()-1
    out=0
    while b:
        if b&1: out^=a
        b>>=1
        a<<=1
        if a&(1<<degree): a^=f
    return out

def power_mod(exponent,f):
    result=1
    base=2
    while exponent:
        if exponent&1: result=mul_mod(result,base,f)
        exponent>>=1
        if exponent: base=mul_mod(base,base,f)
    return result

cases=[(2,0x7,[3]),(3,0xd,[7]),(4,0x19,[3,5]),(5,0x29,[31]),(6,0x61,[3,7]),(7,0xc1,[127]),(8,0x171,[3,5,17])]
certificates=[]
for k,f,prime_factors in cases:
    order=(1<<k)-1
    exponents=[order]+[order//q for q in prime_factors]
    residues={str(e):hex(power_mod(e,f)) for e in exponents}
    valid=residues[str(order)]=='0x1' and all(residues[str(order//q)] not in ['0x0','0x1'] for q in prime_factors)
    certificates.append({'degree':k,'polynomial_mask':hex(f),'order':order,'distinct_prime_factors':prime_factors,'power_residues':residues,'criterion_satisfied':valid})
result={'purpose':'Named companion polynomials in answer1.3.1′–37 only. General proof inherited from workstreams/vol2/notes/primitive-polynomials.md.','method':'Exact GF(2) shift/XOR multiplication and repeated squaring, no enumeration.','certificates':certificates}
Path(__file__).with_name('results').joinpath('field37-power-certificates.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
