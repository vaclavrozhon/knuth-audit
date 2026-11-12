"""A finite exact counterexample to the assertion in 3.2.1.1-12(d)."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def main():
    m=9999998999;a=999999900
    assert 10*a%m==1
    states=[]
    for last,bn in [(1,0),(2,1)]:
        digits=[0]*9+[last]  # x_-1,...,x_-10
        X0=int(''.join(map(str,digits)))-int(''.join(map(str,digits[:3])))-bn
        assert X0==1
        raw=digits[-1]-digits[2]-bn
        x0=raw%10; b1=int(raw<0)
        following=[x0]+digits[:-1]
        states.append((following,b1))
        assert x0==1 and b1==0
    assert states[0]==states[1]
    assert all(pow(10,j,m)!=1 for j in range(1,11))
    def X(n):return pow(a,n,m)
    def periodic_digit(n):
        numerator=10*X(n+1)-X(n)
        assert numerator%m==0
        result=numerator//m
        assert 0<=result<10
        return result
    extended_x_minus10=periodic_digit(-10)
    extended_x_minus3=periodic_digit(-3)
    assert (extended_x_minus10,extended_x_minus3)==(1,0)
    claimed=(extended_x_minus10-extended_x_minus3-1)%10
    assert claimed==0 and periodic_digit(0)==1
    result=dict(status='counterexample confirmed by exact arithmetic',
                modulus=m,multiplier=a,supplied_x_minus10=2,supplied_b0=1,
                other_supplied_digits=0,encoded_X0=1,actual_x0=1,
                extended_x_minus10=extended_x_minus10,
                extended_x_minus3=extended_x_minus3,
                recurrence_rhs_after_extension=claimed,
                scope='The intermediate all-integer recurrence assertion fails; the final radix identity remains true.')
    (ROOT/'results/borrow-extension.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
