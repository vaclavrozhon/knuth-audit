"""Accept the completed OSPD6 run and replay its stored double squares only."""
from collections import Counter
from datetime import datetime,timezone
import gzip,hashlib,json,re
from double_word_tools import ROOT,OUT,dictionary
from build_double_word_programs import sha


def main():
    label='cell-ospd6';meta=OUT/(label+'-run.json');m=json.loads(meta.read_text())
    assert m['status']=='finished' and m['returncode']==0
    result=OUT/(label+'.json');d=json.loads(result.read_text());assert sha(result)==m['result_sha256'] and d['verified']
    for name,h in m['source_sha256'].items():assert sha(ROOT/name)==h
    built=json.loads((OUT/'build.json').read_text())
    for name,h in built['sources'].items():assert sha(ROOT/name)==h
    assert sha(m['command'][2])==m['binary_sha256']==built['binaries']['cell']['sha256']
    for suffix,key in [('.words','input_sha256'),('.log','log_sha256'),('-double-models.txt.gz','models_sha256')]:
        assert sha(OUT/(label+suffix))==m[key]
    words=dictionary(6,True);rank={w:i+1 for i,w in enumerate(words)}
    assert (OUT/(label+'.words')).read_text().splitlines()==[w.lower() for w in words]
    match=re.search(r'Altogether (\d+) solutions \((\d+) mems\)',(OUT/(label+'.log')).read_text())
    assert match and int(match[1])==d['count']==m['validated_solutions']==2038753
    assert int(match[2])==d['statistics']['mems']==4597044464264
    models=set();orbits=Counter();hist=Counter();best_models={};double_xor=double_sum=0
    with gzip.open(OUT/(label+'-double-models.txt.gz'),'rt') as f:
        for line in f:
            rows=tuple(line.split());assert len(rows)==6 and all(len(w)==6 and w in rank for w in rows)
            assert rows not in models;models.add(rows)
            cols=tuple(''.join(rows[i][j] for i in range(6)) for j in range(6))
            assert all(w in rank for w in cols) and len(set(rows+cols))==12
            key=min(rows,cols);orbits[key]+=1;cost=max(rank[w] for w in rows+cols);hist[cost]+=1
            h=int.from_bytes(hashlib.sha256(''.join(key).encode()).digest(),'big');double_xor^=h;double_sum=(double_sum+h)%(1<<256)
    assert len(models)==d['double_count']==m['validated_double']==389514
    assert len(orbits)==d['double_orbits']==194757 and set(orbits.values())=={2}
    assert {str(k):v for k,v in sorted(hist.items())}==d['rank_histogram']
    assert sorted(hist)[:2]==d['best_two_distinct_ranks']==[5772,5906]
    assert f'{double_xor:064x}'==d['double_canonical_sha256_xor'] and f'{double_sum:064x}'==d['double_canonical_sha256_sum']
    orbit_xor=orbit_sum=0
    for key in orbits:
        h=int.from_bytes(hashlib.sha256(''.join(key).encode()).digest(),'big');orbit_xor^=h;orbit_sum=(orbit_sum+h)%(1<<256)
        cost=max(rank[w] for w in key+tuple(''.join(key[i][j] for i in range(6)) for j in range(6)))
        if cost in [5772,5906]:best_models.setdefault(cost,[]).append(key)
    assert f'{orbit_xor:064x}'==d['orbit_sha256_xor'] and f'{orbit_sum:064x}'==d['orbit_sha256_sum']
    assert d['count']-d['double_count']==d['repeated']==1649239
    assert d['symmetric']==1117161 and round(d['statistics']['mems']/1e12,1)==4.6
    checked=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),script_sha256=sha(__file__),
        source_metadata_sha256=sha(meta),source_result_sha256=sha(result),input_sha256=m['input_sha256'],
        complete_squares=2038753,stored_double_models=389514,transpose_orbits=194757,
        model_membership_uniqueness_and_transposes_replayed=True,rank_histogram_sha256=hashlib.sha256(json.dumps(d['rank_histogram'],sort_keys=True).encode()).hexdigest(),
        minimum_max_word_rank=5772,second_distinct_max_word_rank=5906,
        optimal_orbits=best_models,mems=4597044464264,rounded_teramems=4.6,
        scope='Terminal complete cell enumeration validates all2038753 squares while streaming; all389514 stored double squares replayed independently here. Full repeat-containing stdout was hashed during the run but is not archived. No search restarted;7x7 remains separate and live.')
    (OUT/'ospd6-terminal-checked.json').write_text(json.dumps(checked,indent=2)+'\n')
    print('PASS OSPD6:2038753 total;389514 double;194757 transpose classes;minimum5772;4.597044464264T rounds to4.6T.')


if __name__=='__main__':main()
