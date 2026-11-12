#!/usr/bin/env python3
"""Accept terminal word jobs, replay stored double models, retain live gaps.

This does not repeat any enumeration. Minimax incumbent histograms are never
interpreted as the complete set of solutions at the second-best word rank.
"""
from collections import Counter
from datetime import datetime, timezone
import gzip, hashlib, json
from double_word_tools import ROOT, OUT, dictionary, validate, orbit
from build_double_word_programs import sha


def main():
    build=json.loads((OUT/'build.json').read_text())
    for rel,digest in build['sources'].items():assert sha(ROOT/rel)==digest
    for row in build['binaries'].values():assert sha(row['path'])==row['sha256']
    for name in ['small-check.json','csp-small-check.json','runner-validation.json']:
        data=json.loads((OUT/name).read_text())
        for rel,digest in data.get('source_sha256',{}).items():assert sha(ROOT/rel)==digest,(name,rel)
    completed={};pending=[]
    for meta in sorted(OUT.glob('*-run.json')):
        state=json.loads(meta.read_text());config=state['config'];label=config['label']
        if state['status']!='finished':
            pending.append(dict(label=label,status=state['status'],wrapper_pid=state['wrapper_pid'],child_timeout_pid=state['pid']))
            continue
        assert state['returncode']==0
        for rel,digest in state['source_sha256'].items():assert sha(ROOT/rel)==digest
        result_path=OUT/(label+'.json');result=json.loads(result_path.read_text())
        assert result['verified'] and sha(result_path)==state['result_sha256']
        for suffix,key in [('.log','log_sha256'),('-double-models.txt.gz','models_sha256')]:assert sha(OUT/(label+suffix))==state[key]
        inp=OUT/(label+('.words' if config['method']=='cell' else '.dlx'))
        assert sha(inp)==state['input_sha256']
        words=dictionary(config['n'],config.get('ospd',False));words=words[:config.get('limit',len(words))]
        kind=config.get('kind','square');models=set();orbits=set();hist=Counter()
        with gzip.open(OUT/(label+'-double-models.txt.gz'),'rt') as f:
            for line in f:
                rows=tuple(line.split());assert rows not in models;models.add(rows)
                hist[validate(list(rows),words,kind)]+=1
                orbits.add(min(orbit(rows,kind)))
        assert len(models)==result['double_count'] and len(orbits)==result['double_orbits']
        assert dict(sorted(hist.items()))=={int(k):v for k,v in result['rank_histogram'].items()}
        if config['method']!='cell':assert result['count']==len(models)
        best=min(hist) if hist else None
        completed[label]=dict(result_sha256=sha(result_path),metadata_sha256=sha(meta),
            models=len(models),orbits=len(orbits),best_word_rank=best,
            optimal_orbits=[list(x) for x in sorted(orbits) if validate(list(x),words,kind)==best],
            statistics=result['statistics'],config=config)
    prefix=completed['cell-sgb5-prefix1800']
    raw=json.loads((OUT/'cell-sgb5-prefix1800.json').read_text())
    assert raw['count']==2482 and raw['double_count']==8 and raw['double_orbits']==4
    assert raw['rank_histogram']=={'1720':2,'1800':6}
    assert completed['dlx-minimax-sgb5']['best_word_rank']==1720
    assert set(map(tuple,completed['dlx-minimax-sgb5']['optimal_orbits']))==set(map(tuple,prefix['optimal_orbits']))
    for n,rank in [(2,16),(3,64),(4,401),(5,1310)]:
        name=f'dlx-minimax-ospd{n}';assert completed[name]['best_word_rank']==rank
        other=completed.get(f'cell-ospd{n}-prefix{rank}')
        if other:
            assert other['best_word_rank']==rank
            assert set(map(tuple,completed[name]['optimal_orbits']))<=set(map(tuple,other['optimal_orbits']))
    csp=[]
    for path in sorted(OUT.glob('csp-*-below*.json')):
        d=json.loads(path.read_text())
        for rel,digest in d['source_sha256'].items():assert sha(ROOT/rel)==digest
        assert validate(d['printed_witness'],dictionary(5),d['kind'])==d['printed_maximum_rank']
        assert d['excluded_rank_limit']==d['printed_maximum_rank']-1
        if d['status']=='unsat':assert d['printed_optimum_verified']
        else:assert not d['printed_optimum_verified']
        native=completed.get(f"dlx-minimax-{d['kind']}{d['period']}")
        if native and d['status']=='unsat':assert native['best_word_rank']==d['printed_maximum_rank']
        csp.append(dict(file=path.name,sha256=sha(path),kind=d['kind'],period=d['period'],status=d['status'],rank=d['printed_maximum_rank'],nodes=d['nodes']))
    queue=json.loads((OUT/'csp-queue.json').read_text())
    if queue['status']=='finished':
        expected={('left',p) for p in range(2,11)}|{('right',p) for p in range(1,11)}
        assert {(x['kind'],x['period']) for x in csp}==expected and len(csp)==19
        assert len(queue['completed'])==19
        for x in queue['completed']:assert sha(OUT/x['file'])==x['sha256']
    all_stairs=queue['status']=='finished' and all(x['status']=='unsat' for x in csp)
    data=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),source_sha256=sha(__file__),
        completed=completed,pending=pending,csp_thresholds=csp,
        all_19_stair_optima_proved=all_stairs,csp_total_nodes=sum(x['nodes'] for x in csp),
        csp_queue_sha256=sha(OUT/'csp-queue.json'),
        complete_88_rank_histogram=raw['rank_histogram'],
        limitations=[
            'Minimax uses a total order on options, refining ties within word ranks. It proves the best maximum word rank but need not return every square tied at that word rank.',
            'Only the complete cell prefix1800 enumeration proves the next-best rank1800 and its three transpose classes.',
            'Historical DLX mem totals depend on input ordering, preparation and implementation. Current measured costs are retained, not automatically called book errors.',
            'Live long jobs are excluded from completed results and from committed outputs.'])
    (OUT/'checkpoint.json').write_text(json.dumps(data,indent=2)+'\n')
    print('PASS:',len(completed),'terminal jobs;',len(csp),'independent threshold results;',len(pending),'live/pending jobs retained')


if __name__=='__main__':main()
