"""Independent pi king path and summary of the reproducible Monte Carlo runs."""
from pathlib import Path
from collections import Counter
import json, math, statistics
import mpmath as mp

R = Path(__file__).resolve().parent / 'results/estimation'


def pi_path():
    mp.mp.dps = 300
    fraction = mp.pi - 3
    bits = []
    for _ in range(900):
        fraction *= 2
        b = int(fraction); bits.append(b); fraction -= b
    adj = [[b for b in range(64) if b != a and
            max(abs(a//8-b//8), abs(a%8-b%8)) == 1] for a in range(64)]
    path = [0]; used = set(); degrees = []; product = 1; consumed = 0
    while path[-1] != 63:
        u = path[-1]; used.add(u)
        reachable = {63}; queue = [63]
        for v in queue:
            for w in adj[v]:
                if w not in used and w not in reachable:
                    reachable.add(w); queue.append(w)
        choices = [w for w in adj[u] if w in reachable]
        d = len(choices); degrees.append(d); product *= d
        width = (d-1).bit_length()
        while True:
            candidate = 0
            for _ in range(width):
                candidate = 2*candidate+bits[consumed]; consumed += 1
            if candidate < d: break
        path.append(choices[candidate])
    assert path == [0,1,9,10,2,11,20,19,18,17,24,16,25,32,40,48,56,49,57,
                    50,41,42,34,27,35,28,36,44,37,45,38,47,39,46,54,62,63]
    assert product == 866843099136000000000 and consumed == 95
    assert Counter(degrees) == {1:2,2:4,3:4,4:10,5:9,6:6,7:1}
    return {'path_row_major':path, 'degrees':degrees, 'estimate':product,
            'bits_used':consumed, 'length':len(path)-1,
            'degree_histogram':dict(sorted(Counter(degrees).items()))}


def summarize():
    exact = int(json.loads((R/'king-8-stats.json').read_text())['stats']['count'])
    data = [json.loads(s) for s in (R/'king-monte-carlo.jsonl').read_text().splitlines()]
    result = {}
    for mode in ['uniform','biased']:
        rows = [r for r in data if r['mode'] == mode]
        assert len(rows) == 20 and all(r['trials'] == 10000 for r in rows)
        means = [r['mean'] for r in rows]; mean = statistics.mean(means)
        result[mode] = {
            'batches':len(rows), 'trials_per_batch':10000,
            'mean_of_batch_means':mean,
            'relative_error':mean/exact-1,
            'batch_means_standard_error':statistics.stdev(means)/math.sqrt(len(rows)),
            'relative_rmse_of_batch_means':math.sqrt(statistics.mean([(v/exact-1)**2 for v in means])),
            'median_reported_standard_error':statistics.median(r['standard_error'] for r in rows),
            'median_chi':statistics.median(r['chi'] for r in rows),
            'largest_chi':max(r['chi'] for r in rows),
            'range_of_batch_means':[min(means),max(means)],
            'scope':'These fixed seeds test the proposed strategy; they do not recreate the unknown seeds of the printed figure.'
        }
    return {'exact_path_count':exact, 'methods':result}


def summarize_extra():
    rows = [json.loads(s) for s in (R/'extra-monte-carlo.jsonl').read_text().splitlines()]
    out = {}
    for kind in ['queens64','knight8']:
        data = [v for v in rows if v['problem'] == kind]
        assert len(data) == 20
        means = [v['mean'] for v in data]
        out[kind] = {'batches':len(data), 'trials_per_batch':data[0]['trials'],
                     'pooled_mean':statistics.mean(means),
                     'between_batches_standard_error':statistics.stdev(means)/math.sqrt(len(means)),
                     'batch_means_range':[min(means),max(means)],
                     'max_chi':max(v['chi'] for v in data)}
    return out


if __name__ == '__main__':
    out = {'status':'pass', 'pi_king_path':pi_path(), 'monte_carlo':summarize(),
           'ten_printed_16_queen_estimates_mean_billions':sum([632,866,237,1027,4006,982,143,140,3402,510])/10000}
    (R/'examples-verified.json').write_text(json.dumps(out,indent=2)+'\n')
    (R/'extra-summary.json').write_text(json.dumps(summarize_extra(),indent=2)+'\n')
    print(json.dumps(out['monte_carlo'],indent=2))
