"""Reproducible illustration, not reconstruction of unspecified historical seeds."""
from collections import Counter
from hashlib import shake_256
from pathlib import Path
import json
import struct
import mpmath as mp

ROOT=Path(__file__).resolve().parent
M=2**25;N=512;TRIALS=2000


def words(tag,count):
    raw=shake_256(tag.encode('ascii')).digest(4*count)
    return [x[0]&(M-1) for x in struct.iter_unpack('<I',raw)]


def lagged(seed,stride):
    state=seed[:];i=0
    while True:
        for _ in range(stride):
            x=(state[i]+state[(i+31)%55])&(M-1)
            state[i]=x;i=(i+1)%55
        yield x


def analyze(values):
    hist=Counter()
    for _ in range(TRIALS):
        y=sorted(next(values) for j in range(N))
        gaps=[y[j+1]-y[j] for j in range(N-1)]+[y[0]+M-y[-1]]
        hist[N-len(set(gaps))]+=1
    probabilities=[mp.mpf(s) for s in ['.368801577097920890285859',
                    '.369035243450689819080441','.183471182131179017765623']]
    probabilities.append(1-sum(probabilities))
    categories=[hist[0],hist[1],hist[2],sum(v for k,v in hist.items() if k>=3)]
    chi=sum((c-TRIALS*p)**2/(TRIALS*p) for c,p in zip(categories,probabilities))
    upper=mp.gammainc(mp.mpf('1.5'),chi/2,mp.inf)/mp.gamma(mp.mpf('1.5'))
    return dict(trials=TRIALS,mean=sum(k*v for k,v in hist.items())/TRIALS,
                histogram=dict(sorted(hist.items())),categories=categories,
                chi_square=float(chi),upper_tail_pvalue=mp.nstr(upper,12))


def main():
    mp.mp.dps=50
    dest=ROOT/'results/birthday-generators.json'
    result=dict(m=M,n=N,description='Deterministic SHAKE256 initial data; exploratory empirical replication only.',rows=[])
    reference_tag='TAOCP volume2 birthday reference 2026-11-01'
    result['rows'].append(dict(generator='SHAKE256 reference',tag=reference_tag,
                              **analyze(iter(words(reference_tag,TRIALS*N)))))
    dest.write_text(json.dumps(result,indent=2)+'\n');print('REFERENCE',result['rows'][-1],flush=True)
    for k in range(3):
        tag=f'TAOCP volume2 birthday lag55 seed{k} 2026-11-01';seed=words(tag,55)
        assert any(x%2 for x in seed)
        for stride in (1,2):
            row=dict(generator='additive lag55/24',tag=tag,initial_state=seed,stride=stride,
                     **analyze(lagged(seed,stride)))
            result['rows'].append(row);dest.write_text(json.dumps(result,indent=2)+'\n')
            print('LAG',k,stride,'mean',row['mean'],'chi',row['chi_square'],'p',row['upper_tail_pvalue'],flush=True)
    print('ALL EXPERIMENTS COMPLETE',flush=True)


if __name__=='__main__':main()
