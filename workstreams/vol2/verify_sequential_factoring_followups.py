"""Six interval-certified table rows, with no prime enumeration.

Recorded run: nice -n 15 env
PYTHONPATH=/tmp/knuth-vol2-or9kgh/python-deps python3 ...
Uses the existing python-flint installation; printed L has lower limit 2.
"""
import json
from pathlib import Path
from flint import arb, ctx


def mobius(n):
    sign, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
        p += 1
    return -sign if n > 1 else sign


def main():
    ctx.dps = 90
    printed_l = ['176.6', '78626.5', '50849233.9', '37607950279.8',
                 '29844571475286.5', '24739954309690414.0']
    printed_r = ['168.3', '78527.4', '50847455.4', '37607910542.2',
                 '29844570495886.9', '24739954284239494.4']
    rows = []
    for exponent, lp, rp in zip(range(3, 19, 3), printed_l, printed_r):
        x = 10 ** exponent
        log_x = arb(x).log()
        last_k = x.bit_length() - 1
        lv = arb(x).li() - arb(2).li()
        rv = sum((mobius(k) * ((log_x / k).ei() - arb(2).li()) / k
                  for k in range(1, last_k + 1)), arb(0))
        l_ok = bool(abs(lv - arb(lp)) < arb('0.05'))
        r_ok = bool(abs(rv - arb(rp)) < arb('0.05'))
        assert l_ok and r_ok, (exponent, lv, rv)
        rows.append(dict(exponent=exponent, last_k=last_k, L=str(lv),
                         R_truncated=str(rv), printed_L=lp, printed_R=rp,
                         L_rounding_certified=l_ok, R_rounding_certified=r_ok))
    result = dict(status='completed', precision_bits=ctx.prec, nice=15,
                  scope='Only six table rows at printed382; no prime census.',
                  table382=rows)
    path = Path(__file__).resolve().parent / 'results/sequential-factoring-followups.json'
    path.write_text(json.dumps(result, indent=2) + '\n')
    print('Certified all 12 decimal cells in six table rows.')


if __name__ == '__main__':
    main()
