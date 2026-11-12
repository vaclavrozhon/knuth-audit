#!/usr/bin/env python3
"""Exact rational bounds for the two printed decimals in MPR121(a).

This does not repeat the old entropy/MI enumeration.  For r>0, use
ln r = 2 sum_{k>=0} s^(2k+1)/(2k+1), s=(r-1)/(r+1).
The omitted tail after N terms has absolute value at most
2|s|^(2N+1)/((2N+1)(1-s^2)).
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import time


def log_bounds(r, terms=12):
    s = (r - 1) / (r + 1)
    value = 2 * sum((s ** (2*k+1) / (2*k+1) for k in range(terms)), Q(0))
    tail = 2 * abs(s) ** (2*terms+1) / ((2*terms+1) * (1-s*s))
    return value-tail, value+tail


def main():
    start = time.perf_counter()
    l2 = log_bounds(Q(2))
    a, b, c = (log_bounds(r) for r in [Q(6,5), Q(4,5), Q(25,24)])
    numer = (3*a[0]+2*b[0], 3*a[1]+2*b[1])
    forward = (numer[0]/(15*l2[1]), numer[1]/(15*l2[0]))
    reverse = (c[0]/(6*l2[1]), c[1]/(6*l2[0]))
    assert Q(965,100000) < forward[0] < forward[1] < Q(975,100000)
    assert Q(975,100000) < reverse[0] < reverse[1] < Q(985,100000)
    result = {
        'purpose': 'Only the two printed four-decimal approximations in MPR121(a)',
        'method': 'Exact Fraction arithmetic and 12-term atanh-series tail bounds',
        'forward_interval': [str(x) for x in forward],
        'reverse_interval': [str(x) for x in reverse],
        'forward_display': [float(x) for x in forward],
        'reverse_display': [float(x) for x in reverse],
        'certified_rounded_values': ['0.0097','0.0098'],
        'elapsed_seconds': time.perf_counter()-start,
        'old_runs_repeated': 0,
    }
    out = Path(__file__).resolve().parents[1] / 'results/sequential/mpr-121-log-rounding.json'
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['certified_rounded_values','elapsed_seconds','old_runs_repeated']}))


if __name__ == '__main__':
    main()
