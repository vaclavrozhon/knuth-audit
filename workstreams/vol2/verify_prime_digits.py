"""Exact optimality certificates for TAOCP2 4.5.4-38.

All competing decimal words are enumerated in two different ways.  Each
exclusion has an integer divisor or a failed strong probable-prime test;
the ten surviving primes have independently checked ECPP certificates.
Successful per-digit checkpoints are retained on restart.
"""
from pathlib import Path
from itertools import combinations, product
from math import gcd
import json
import subprocess
import time
from verify_ecpp import Verifier

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/prime-digits.json'
GP = '/tmp/knuth-vol2-or9kgh/pari-local/usr/bin/gp'
SMALL = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
         53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def save(path, data):
    tmp = path.with_suffix('.tmp')
    tmp.write_text(json.dumps(data, indent=2)+'\n')
    tmp.replace(path)


def targets():
    r = (10**50-1)//9
    return [10**49+9, r+3*10**46, 2*r+3*10**47+7, 3*r+2*10**49,
            4*r+2*10**49-3, 5*r+3*10**49+4, 6*r+2*10**48+3,
            7*r+2*10**25, 8*r+10**38-7, 9*r-8000]


def candidates(d, p):
    """Mutate positions in the constant decimal word; no primality filtering."""
    digits = str(p).count(str(d)); base = d*((10**50-1)//9)
    powers = [10**j for j in range(50)]
    other = [j for j in range(10) if j != d]
    result = set()
    for k in range(51-digits):
        for places in combinations(range(50), k):
            for replacement in product(other, repeat=k):
                n = base+sum((x-d)*powers[j] for j, x in zip(places, replacement))
                if n < 10**49: continue
                if 50-k > digits or n > p: result.add(n)
    return result


def decimal_tree(d, p):
    """Independent lexicographic digit tree, tracking number of non-d digits."""
    word = str(p); maximum = 50-word.count(str(d)); result = set()
    def visit(prefix, depth, changed, relation):
        if changed > maximum: return
        if changed == maximum and relation < 0: return
        if depth == 50:
            if changed < maximum or relation > 0: result.add(prefix)
            return
        for x in range(1 if depth == 0 else 0, 10):
            c = changed+(x != d)
            if c > maximum: continue
            rel = relation if relation else (x > int(word[depth]))-(x < int(word[depth]))
            visit(prefix*10+x, depth+1, c, rel)
    visit(0, 0, 0, 0)
    return result


def strong_composite(n, a):
    t = n-1; s = 0
    while t % 2 == 0: t //= 2; s += 1
    x = pow(a, t, n)
    if x in (1, n-1): return False
    for _ in range(s-1):
        x = x*x % n
        if x == n-1: return False
    return True


def explicit_power(a, e, n):
    # Left-to-right binary arithmetic, independent of built-in pow.
    x = 1
    for bit in bin(e)[2:]:
        x = x*x % n
        if bit == '1': x = x*a % n
    return x


def validate_exclusion(n, witness):
    kind, a = witness
    if kind == 'divisor':
        assert 1 < a < n
        # Decimal digit recurrence independently checks the supplied divisor.
        residue = 0
        for c in str(n): residue = (10*residue+int(c)) % a
        assert residue == 0
        return
    assert kind == 'strong' and 1 < a < n
    exponents = []; e = n-1
    while e % 2 == 0: e //= 2; exponents.append(e)
    # A prime requires a^odd=1, or a^((n-1)/2^j)=-1 for some j>=1.
    assert explicit_power(a, e, n) != 1
    assert all(explicit_power(a, j, n) != n-1 for j in exponents)


def check_digit(d, p):
    assert len(str(p)) == 50
    proposed = candidates(d, p); independent = decimal_tree(d, p)
    assert proposed == independent
    witnesses = []
    for n in sorted(proposed):
        divisor = next((q for q in SMALL if n % q == 0), None)
        if divisor is not None: witness = ['divisor', divisor]
        else:
            a = next((a for a in [2, 3, 5, 7, 11, 13, 17, 19, 23]
                      if strong_composite(n, a)), None)
            assert a is not None, ('unexcluded competitor', d, n)
            witness = ['strong', a]
        validate_exclusion(n, witness)
        witnesses.append([n, *witness])
    certpath = ROOT/f'results/prime-digits-certificate-{d}.json'
    if certpath.exists(): cert = json.loads(certpath.read_text())
    else:
        proc = subprocess.Popen([GP, '-fq', '-s', '134217728'], stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print('certificate PID', proc.pid, 'digit', d, 'limit60', flush=True)
        try:
            stdout, stderr = proc.communicate(f'default(nbthreads,1);print(primecert({p}));quit;\n', timeout=60)
        except subprocess.TimeoutExpired:
            proc.kill(); proc.communicate(); raise
        assert proc.returncode == 0, stderr
        cert = json.loads(stdout.strip()); save(certpath, cert)
    v = Verifier(); v.verify(cert, p); v.validate_small_certificates()
    return dict(digit=d, prime=p, copies=str(p).count(str(d)), competitors=len(proposed),
                exclusions=witnesses, ecpp_links=v.links,
                terminal_certificates=[v.small[n] for n in sorted(v.small)])


def main():
    result = json.loads(OUT.read_text()) if OUT.exists() else dict(status='running', digits={})
    for d, p in enumerate(targets()):
        if str(d) in result['digits']: continue
        start = time.perf_counter(); row = check_digit(d, p)
        row['seconds'] = time.perf_counter()-start; result['digits'][str(d)] = row
        save(OUT, result)
        print('digit', d, 'passed', row['copies'], 'copies;', row['competitors'],
              'exclusions;', row['ecpp_links'], 'ECPP links;', row['seconds'], 's', flush=True)
    result['status'] = 'passed'; save(OUT, result)


if __name__ == '__main__': main()
