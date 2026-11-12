#!/usr/bin/env python3
"""Exact completion of TAOCP2 Table 2, p408.

Reuse the completed first-column proof. SymPy only proposes factorizations;
all new prime certificates and composite witnesses are checked independently.
"""
from pathlib import Path
import hashlib
import json
import time
from math import gcd, prod
from verify_prime_chains import Certificates, exclusion, validate_exclusion, explicit_power

ROOT = Path(__file__).resolve().parent
# Visual transcription, original p408. First coordinate is the exponent.
BINARY = '''
15 19 49 51 55 61 75 81 115 121 135
16 15 17 39 57 87 89 99 113 117 123
17 1 9 13 31 49 61 63 85 91 99
18 5 11 17 23 33 35 41 65 75 93
19 1 19 27 31 45 57 67 69 85 87
20 3 5 17 27 59 69 129 143 153 185
21 9 19 21 55 61 69 105 111 121 129
22 3 17 27 33 57 87 105 113 117 123
23 15 21 27 37 61 69 135 147 157 159
24 3 17 33 63 75 77 89 95 117 167
25 39 49 61 85 91 115 141 159 165 183
26 5 27 45 87 101 107 111 117 125 135
27 39 79 111 115 135 187 199 219 231 235
28 57 89 95 119 125 143 165 183 213 273
29 3 33 43 63 73 75 93 99 121 133
30 35 41 83 101 105 107 135 153 161 173
31 1 19 61 69 85 99 105 151 159 171
32 5 17 65 99 107 135 153 185 209 267
33 9 25 49 79 105 285 301 303 321 355
34 41 77 113 131 143 165 185 207 227 281
35 31 49 61 69 79 121 141 247 309 325
36 5 17 23 65 117 137 159 173 189 233
37 25 31 45 69 123 141 199 201 351 375
38 45 87 107 131 153 185 191 227 231 257
39 7 19 67 91 135 165 219 231 241 301
40 87 167 195 203 213 285 293 299 389 437
41 21 31 55 63 73 75 91 111 133 139
42 11 17 33 53 65 143 161 165 215 227
43 57 67 117 175 255 267 291 309 319 369
44 17 117 119 129 143 149 287 327 359 377
45 55 69 81 93 121 133 139 159 193 229
46 21 57 63 77 167 197 237 287 305 311
47 115 127 147 279 297 339 435 541 619 649
48 59 65 89 93 147 165 189 233 243 257
59 55 99 225 427 517 607 649 687 861 871
60 93 107 173 179 257 279 369 395 399 453
63 25 165 259 301 375 387 391 409 457 471
64 59 83 95 179 189 257 279 323 353 363
'''
DECIMAL = '''
6 17 21 39 41 47 69 83 93 117 137
7 9 27 29 57 63 69 71 93 99 111
8 11 29 41 59 69 153 161 173 179 213
9 63 71 107 117 203 239 243 249 261 267
10 33 57 71 119 149 167 183 213 219 231
11 23 53 57 93 129 149 167 171 179 231
12 11 39 41 63 101 123 137 143 153 233
16 63 83 113 149 183 191 329 357 359 369
'''

def main():
    start = time.perf_counter()
    prior_path = ROOT / 'results/primitive-criteria.json'
    prior_bytes = prior_path.read_bytes()
    prior = json.loads(prior_bytes)
    assert prior['status'] == 'passed'
    prior_rows = {(r['base'], r['exponent']): r for r in prior['exercise19']}
    certs = Certificates()
    for row in prior['small_lucas_certificates']:
        n = row['prime']
        certs.data[n] = {'n': n, 'factors': row.get('factors', []),
                         'base': row.get('witness')}
    inherited = set(certs.data)
    output = []
    for base, source in [(2, BINARY), (10, DECIMAL)]:
        for line in source.splitlines():
            if not line.strip():
                continue
            e, *deltas = map(int, line.split())
            assert len(deltas) == 10 and deltas == sorted(set(deltas))
            assert deltas[0] == prior_rows[base,e]['delta']
            N = base**e
            for d in deltas[1:]:
                certs.add(N-d)
            excluded = []
            for d in range(deltas[0]+1, deltas[-1]):
                if d in deltas:
                    continue
                witness = exclusion(N-d)
                validate_exclusion(N-d, witness)
                excluded.append([d, *witness])
            output.append(dict(base=base, exponent=e, offsets=deltas,
                               new_composite_exclusions=excluded))
    # Validate only new certificate links; previously proved roots are reused.
    proven = set(inherited)
    new_certificates = []
    for n in sorted(set(certs.data)-inherited):
        row = certs.data[n]
        factors = row['factors']
        assert all(p in proven and e >= 1 for p,e in factors)
        assert len({p for p,e in factors}) == len(factors)
        assert prod(p**e for p,e in factors) == n-1
        a = row['base']
        assert 1 < a < n and explicit_power(a,n-1,n) == 1
        assert all(gcd(explicit_power(a,(n-1)//p,n)-1,n) == 1 for p,e in factors)
        proven.add(n)
        new_certificates.append(row)
    assert len(output) == 46
    result = dict(status='passed', rows=output, new_prime_entries=46*9,
                  new_certificate_links=len(new_certificates),
                  new_composite_exclusions=sum(len(r['new_composite_exclusions']) for r in output),
                  certificates=new_certificates,
                  inherited_certificate_file='results/primitive-criteria.json',
                  inherited_sha256=hashlib.sha256(prior_bytes).hexdigest(),
                  inherited_prime_certificates=len(inherited),
                  seconds=time.perf_counter()-start)
    (ROOT/'results/prime-table.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS', result['new_prime_entries'], 'new prime entries;',
          result['new_certificate_links'], 'new Lucas links;',
          result['new_composite_exclusions'], 'new composite witnesses;',
          result['seconds'], 'seconds',flush=True)

if __name__ == '__main__':
    main()
