#!/usr/bin/env python3
"""Only the two new MPR122(a) decimals; no old calculation is rerun."""
from fractions import Fraction as Q
from pathlib import Path
import json
import time
from verify_mpr121_log_rounding import log_bounds


def main():
    start = time.perf_counter()
    l2 = log_bounds(Q(2))
    rows = []
    for ratio, low, high, printed in [
        (Q(27,16), Q(7545,10000), Q(7555,10000), '0.755'),
        (Q(4,3), Q(4145,10000), Q(4155,10000), '0.415'),
    ]:
        b = log_bounds(ratio)
        interval = (b[0]/l2[1], b[1]/l2[0])
        assert low < interval[0] < interval[1] < high
        rows.append({'ratio':str(ratio),'exact_interval':[str(x) for x in interval],
                     'display_interval':[float(x) for x in interval], 'printed':printed})
    result = {'purpose':'Only the two MPR122(a) approximations',
              'method':'Exact12-term atanh-series bounds; imported helper does not run121 checks',
              'rows':rows,'elapsed_seconds':time.perf_counter()-start,'old_runs_repeated':0}
    out = Path(__file__).resolve().parents[1]/'results/sequential/mpr-122-log-rounding.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'rows':[{k:r[k] for k in ['ratio','display_interval','printed']} for r in rows],
                      'elapsed_seconds':result['elapsed_seconds']}))


if __name__ == '__main__':
    main()
