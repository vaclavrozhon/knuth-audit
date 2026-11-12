"""Accept new figures and bounded counts; reuse all old USA/C$ evidence."""
from pathlib import Path
from datetime import datetime, timezone
import json
import os
import re
import time
from puzzle_xcc import save, sha

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/usa239_246'
SRC=ROOT/'sources/usa239_246'


def read(p):return json.loads((ROOT/p).read_text())


def connected(group,edges):
    seen={group[0]}
    while True:
        new=seen|{b for a,b in edges if a in seen and b in group}|{a for a,b in edges if b in seen and a in group}
        if new==seen:return len(seen)==len(group)
        seen=new


def main():
    start=time.monotonic()
    assert os.nice(0)>=15 and not (OUT/'source-checked.json').exists()
    figures=read('results/usa239_246/figures.json');data=figures['data'];g=figures['versions']['original'];pop=data['population']
    for p,h in figures['trace_hashes'].items():assert sha(ROOT/p)==h
    assert sha(ROOT/'extract_usa239_246.py')==figures['extractor_sha256']
    runs=read('results/usa239_246/population-runs.json');assert runs['status']=='finished' and len(runs['small_cases'])==30
    assert runs['source_sha256']==sha(ROOT/'usa_population_options.cpp') and runs['runner_sha256']==sha(ROOT/'run_usa_population_bounded.py')
    expected=[(291282,31685),(1926811,355754),(1587884,36190),(1176310,59551)]
    for q,counts in zip(runs['cases'],expected):
        assert q['status']=='complete' and q['returncode']==0 and q['nice']>=15
        assert (q['terminal']['interval_count'],q['terminal']['reduced_count'])==counts
        for suffix,key in [('input','input_sha256'),('out','output_sha256'),('log','log_sha256')]:assert sha(OUT/(q['name']+'.'+suffix))==q[key]
    ny=read('results/usa239_246/ny-exception-run.json')
    assert ny['status']=='complete' and ny['terminal']['reduced_count']==33716
    assert ny['checker_sha256']==sha(ROOT/'check_usa_population_exceptions.py')
    assert ny['output_sha256']==sha(OUT/'pop38-with-ny.out')
    proof=read('results/usa239_246/f148-f149-witness.json');assert proof['checker_sha256']==sha(ROOT/'verify_f148_f149.py')
    p48=sum(v for k,v in pop.items() if k!='DC');p49=sum(pop.values())
    assert p48==306084180 and p49==306685947
    assert (p48//9+1,(p48+6)//7)==(34009354,43726312)
    england=set('CT MA ME NH RI VT'.split());ny_plus=england|{'NY'}
    ny_pop=sum(pop[s] for s in ny_plus);ne_pop=sum(pop[s] for s in england)
    assert ny_pop==33823525 and ne_pop==14445438
    # NY separates the six New England states from all other states.
    assert {b if a in england else a for a,b in data['edges'] if (a in england)!=(b in england)}=={'NY'}
    assert {b if a=='NY' else a for a,b in data['edges'] if 'NY' in [a,b]}-england=={'NJ','PA'}
    assert ny_pop<37000000 and ny_pop+min(pop['NJ'],pop['PA'])>39000000
    for exception in ny['exceptions']:
        x=exception['population'];assert x+6*39000000<p48<x+8*37000000
    assert 5*51500000<p48<7*50500000 and 6*45000000<p49<8*43000000
    for title,q in g.items():
        assert all(connected(c,data['edges']) for c in q['sets'])
        assert sum(q['sizes'])==48+int(title.startswith('245'))
        assert max([abs(v) for v in (q['relative_area_errors'] or {}).values()] or [0])<.0005
    assert min(g['116-right']['populations'])>=50650000 and max(g['116-right']['populations'])<=51150000
    assert min(g['245b']['populations'])>=43510000 and max(g['245b']['populations'])<=44240000
    assert [g[q]['exterior'] for q in ['246-ext-left','246-ext-right']]==[90,74]
    assert [g[q]['interior'] for q in ['246-int-left','246-int-right']]==[176,230]
    assert g['246-ext-left']['interior']>176 and g['246-int-left']['exterior']>90
    assert g['246-ext-right']['interior']>230 and g['246-int-right']['exterior']>74
    masks=set(map(int,(OUT/'pop38-with-ny.out').read_text().split()))
    names=runs['cases'][0]['states'];index={s:i for i,s in enumerate(names)}
    printed_option_membership=[]
    for title in ['116-left','246-ext-left','246-int-left']:
        for group in g[title]['sets']:
            mask=sum(1<<index[s] for s in group)
            assert mask in masks or set(group) in [set(q['states']) for q in ny['exceptions']]
            printed_option_membership.append(dict(figure=title,states=group,mask=mask))
    for title,case in [('116-right','pop51'),('246-ext-right','pop51'),('246-int-right','pop51'),('245b','pop44-dc')]:
        q=next(q for q in runs['cases'] if q['name']==case);idx={s:i for i,s in enumerate(q['states'])}
        choices=set(map(int,(OUT/(case+'.out')).read_text().split()))
        assert all(sum(1<<idx[s] for s in group) in choices for group in g[title]['sets'])
    old=read('results/usa_partitions/verified.json');swaps=[]
    for title,case,k,cycle in [('115-left','n48-k6',6,['VA','WV']),('115-right','n48-k8',8,['MI','NE','LA','VA']),('245a','n49-k7',7,[])]:
        accepted=next(q for q in old['cases'] if q['case']==case)
        assert g[title]['exterior']==accepted['minimum_cost']
        if cycle:
            variants=[]
            for direction in [-1,1]:
                mapping={s:cycle[(i+direction)%len(cycle)] for i,s in enumerate(cycle)}
                groups=sorted(sorted(mapping.get(s,s) for s in group) for group in g[title]['sets'])
                membership={s:i for i,group in enumerate(groups) for s in group}
                cost=2*sum(membership[a]!=membership[b] for a,b in data['edges'] if a!='DC' and b!='DC')
                if all(connected(q,data['edges']) and len(q)==k for q in groups) and cost==accepted['minimum_cost']:
                    variants.append(groups)
            unique={tuple(map(tuple,q)) for q in variants};assert len(unique)==1
            assert accepted['optimal_count']==2 and tuple(map(tuple,g[title]['sets'])) not in unique
            swaps.append(dict(figure=title,other_optimum=list(next(iter(unique)))))
        else:
            rows=read('results/usa_partitions/n49-k7.json')['rows']
            expected=sorted(sorted(rows[i]['states']) for i in accepted['witness_rows'])
            assert expected==g[title]['sets'] and accepted['optimal_count']==1
    chain=set('ND SD NE KS OK TX'.split());edges=[(a,b) for a,b in data['edges'] if 'DC' not in [a,b]]
    assert sum((a in chain)!=(b in chain) for a,b in edges)==19
    assert len(chain)*(len(chain)-1)-2*sum(a in chain and b in chain for a,b in edges)==20
    pre=[set(line.split()) for line in (ROOT/'results/usa_partitions/n48-k6-pre.xcc').read_text().splitlines()[1:]]
    assert chain in pre and set('LA AR TN VA MD PA'.split()) not in pre
    assert old['interval_checks']==36000 and old['exercise240_six_options_correct']
    # Primary census and revised baseline attribution, without changing the frozen inputs.
    census=(SRC/'apport2010-table4.txt').read_text();baseline=(SRC/'census-2015-pepannres.txt').read_text()
    originals={};bases={}
    for s,name in data['fullnames'].items():
        a=re.search(r'^\s*'+re.escape(name)+r'\s+([\d,]+)',census,re.M)
        b=re.search(r'^\s*'+re.escape(name)+r'\s+[\d,]+\s+([\d,]+)',baseline,re.M)
        assert a and b
        originals[s]=int(a.group(1).replace(',',''));bases[s]=int(b.group(1).replace(',',''))
    different={s:dict(sgb=pop[s],base2015=bases[s],delta=pop[s]-bases[s]) for s in pop if pop[s]!=bases[s]}
    assert different=={'CA':dict(sgb=37252895,base2015=37254503,delta=-1608)}
    assert sum(v for s,v in originals.items() if s!='DC')==306073283
    provenance=dict(sgb48=p48,census2010_48=306073283,base2015_48=sum(v for s,v in bases.items() if s!='DC'),
                    differences_from_base2015=different,original_census=originals,base2015=bases,classification='candidate_source_attribution',frozen_sgb_not_modified=True)
    save(OUT/'population-provenance.json',provenance)
    accepted_paths=['results/usa_partitions/verified.json','results/usa_partitions/graph.json','results/cost_reductions/verified.json',
                    'prepare_usa_partitions.py','verify_usa_partitions.py','check_cost_reductions.py']
    current=['extract_usa239_246.py','usa_population_options.cpp','run_usa_population_bounded.py','check_usa_population_exceptions.py','verify_f148_f149.py',
             'results/usa239_246/figures.json','results/usa239_246/population-runs.json','results/usa239_246/ny-exception-run.json','results/usa239_246/f148-f149-witness.json','results/usa239_246/population-provenance.json']
    save(OUT/'source-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),nice=os.nice(0),wall_seconds=time.monotonic()-start,
        accepted_hashes={p:sha(ROOT/p) for p in accepted_paths},current_hashes={p:sha(ROOT/p) for p in current},
        figures_per_version=11,vertices_per_version=530,edges_per_version=1159,alternative_optima=swaps,printed_population_options=printed_option_membership,
        verified_option_counts=dict(broad8=[1926811,355754],dc7=[1176310,59551]),
        unresolved34111=dict(printed=34111,raw=291282,literal242=31685,restrict_broad_preprocessed=61526,allow_ny_exceptions=33716),
        old_censuses_repeated=0,old_native_models_revalidated=0,population_global_optimality_independently_verified=False,
        all_population_witness_costs_valid=True,all_figurative_population_ranges_valid=False,F148=True,F149=True,source239_original_exercise1035_obtained=False))
    print('PASS USA source check:22 graphs; accepted old optima; new population witnesses/counts.34111 and source attribution remain open.')


if __name__=='__main__':main()
