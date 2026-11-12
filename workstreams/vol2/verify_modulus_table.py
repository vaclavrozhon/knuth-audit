"""Table 3.2.1.1-1, transcribed from p.14; exact products and prime certificates."""
from math import gcd, prod
from pathlib import Path
import json
import sympy

ROOT = Path(__file__).resolve().parent
# Exponent | factorization of 2^e-1 | factorization of 2^e+1.
BINARY = '''
15|7 31 151|3^2 11 331
16|3 5 17 257|65537
17|131071|3 43691
18|3^3 7 19 73|5 13 37 109
19|524287|3 174763
20|3 5^2 11 31 41|17 61681
21|7^2 127 337|3^2 43 5419
22|3 23 89 683|5 397 2113
23|47 178481|3 2796203
24|3^2 5 7 13 17 241|97 257 673
25|31 601 1801|3 11 251 4051
26|3 2731 8191|5 53 157 1613
27|7 73 262657|3^4 19 87211
28|3 5 29 43 113 127|17 15790321
29|233 1103 2089|3 59 3033169
30|3^2 7 11 31 151 331|5^2 13 41 61 1321
31|2147483647|3 715827883
32|3 5 17 257 65537|641 6700417
33|7 23 89 599479|3^2 67 683 20857
34|3 43691 131071|5 137 953 26317
35|31 71 127 122921|3 11 43 281 86171
36|3^3 5 7 13 19 37 73 109|17 241 433 38737
37|223 616318177|3 1777 25781083
38|3 174763 524287|5 229 457 525313
39|7 79 8191 121369|3^2 2731 22366891
40|3 5^2 11 17 31 41 61681|257 4278255361
41|13367 164511353|3 83 8831418697
42|3^2 7^2 43 127 337 5419|5 13 29 113 1429 14449
43|431 9719 2099863|3 2932031007403
44|3 5 23 89 397 683 2113|17 353 2931542417
45|7 31 73 151 631 23311|3^3 11 19 331 18837001
46|3 47 178481 2796203|5 277 1013 1657 30269
47|2351 4513 13264529|3 283 165768537521
48|3^2 5 7 13 17 97 241 257 673|193 65537 22253377
59|179951 3203431780337|3 2833 37171 1824726041
60|3^2 5^2 7 11 13 31 41 61 151 331 1321|17 241 61681 4562284561
63|7^2 73 127 337 92737 649657|3^3 19 43 5419 77158673929
64|3 5 17 257 641 65537 6700417|274177 67280421310721
'''
DECIMAL = '''
6|3^3 7 11 13 37|101 9901
7|3^2 239 4649|11 909091
8|3^2 11 73 101 137|17 5882353
9|3^4 37 333667|7 11 13 19 52579
10|3^2 11 41 271 9091|101 3541 27961
11|3^2 21649 513239|11^2 23 4093 8779
12|3^3 7 11 13 37 101 9901|73 137 99990001
16|3^2 11 17 73 101 137 5882353|353 449 641 1409 69857
'''


def factors(text):
    return [tuple(map(int,t.split('^'))) if '^' in t else (int(t),1)
            for t in text.split()]


def main():
    certificates = {2: {'prime': 2}}
    def build(n):
        if n in certificates:
            return
        fs = [(int(q),int(e)) for q,e in sympy.factorint(n-1).items()]
        assert prod(q**e for q,e in fs) == n-1
        for q,_ in fs:
            build(q)
        for a in range(2,10000):
            if pow(a,n-1,n)==1 and all(gcd(pow(a,(n-1)//q,n)-1,n)==1 for q,_ in fs):
                certificates[n] = dict(prime=n,witness=a,factors_of_previous=fs)
                return
        raise AssertionError(('No certificate found',n))
    rows=[]
    for b,table in [(2,BINARY),(10,DECIMAL)]:
        for row in table.strip().splitlines():
            e,minus,plus=row.split('|')
            for sign,txt in [(-1,minus),(1,plus)]:
                fs=factors(txt); value=b**int(e)+sign
                assert prod(p**k for p,k in fs)==value,(b,e,sign)
                for p,_ in fs:
                    build(p)
                rows.append(dict(base=b,exponent=int(e),sign=sign,value=value,factors=fs))
    # Validation uses only exact integer arithmetic, no primality library.
    validated={2}
    for n in sorted(certificates):
        if n==2:
            continue
        c=certificates[n]; fs=c['factors_of_previous']; a=c['witness']
        assert all(q in validated and e>=1 for q,e in fs)
        assert prod(q**e for q,e in fs)==n-1
        assert pow(a,n-1,n)==1
        assert all(gcd(pow(a,(n-1)//q,n)-1,n)==1 for q,_ in fs)
        validated.add(n)
    assert len(rows)==92
    result=dict(status='all exact products and recursive Lucas certificates passed',
                table_entries=len(rows),certified_primes=len(certificates),
                table_rows=rows,prime_certificates=[certificates[n] for n in sorted(certificates)])
    (ROOT/'results/modulus-table.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['table_rows','prime_certificates']},indent=2))


if __name__=='__main__':
    main()
