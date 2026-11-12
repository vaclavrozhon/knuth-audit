"""One bounded census of the explicitly corrected inventory; no literal search."""
from collections import Counter
from datetime import datetime,timezone
import json,os
import chain150 as h
import graph_native as native


def main():
    out=h.OUT/'corrected-census';out.mkdir(exist_ok=True)
    assert not (out/'started.json').exists(),'Inspect old results; never automatically repeat a search.'
    assert os.getpriority(os.PRIO_PROCESS,0)>=15
    figs=json.loads((h.OUT/'figures-checked.json').read_text())
    assert figs['geometry_sha256']==h.sha(h.__file__)
    assert figs['literal_inventory_rejected_by_all_four_figures']
    enc,text,options=h.problem(corrected=True)
    h.save(out/'started.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),pid=os.getpid(),nice=os.getpriority(os.PRIO_PROCESS,0),
        checker_sha256=h.sha(__file__),geometry_sha256=h.sha(h.__file__),figures_sha256=h.sha(h.OUT/'figures-checked.json'),
        inventory='Explicit correction:two L-dominoes and one S-domino; original printed inventory has zero solutions by parity.',
        timeout_seconds=60,literal_census_started=False))
    build=json.loads((h.ROOT/'results/puzzles101_107/word-variants-build.json').read_text());binary=build['binaries']['dlx3']
    assert h.sha(binary['path'])==binary['sha256'];native.OUT=out
    source=h.ROOT/'sources/puzzles101_107/dlx3.w'
    first=figs['figures']['original0']['normalized_model'];lines=text.splitlines()
    tiny='\n'.join([lines[0]]+[lines[1+i] for i in first])+'\n'
    smoke=native.run('fixed-printed-witness',tiny,binary=binary['path'],source=source,limit=10)
    assert smoke['status']=='completed' and smoke['solutions']==1
    result=native.run('corrected-all',text,binary=binary['path'],source=source,limit=60)
    if result['status']!='completed':
        h.save(out/'incomplete.json',dict(reason='Bounded census did not finish; do not extend/restart. Parity finding and direct witnesses remain valid.',terminal_sha256=h.sha(out/'corrected-all.json')))
        print('INCOMPLETE corrected census; literal zero remains proved. No restart.');return
    models=list(native.models('corrected-all',enc));assert len(models)==len(set(models))==result['solutions']
    hist=Counter();pathkeys={};components=Counter()
    for model in models:
        graph,cc=h.validate([options[i] for i in model],corrected=True);components[tuple(cc)]+=1
        k=h.path_key(graph);hist[k]+=1;pathkeys[model]=k
    assert components=={(34,):result['solutions']}
    occurrences=[]
    for i in range(4):
        figure=figs['figures']['original'+str(i)];model=tuple(figure['normalized_model']);assert model in models
        occurrences.append(hist[pathkeys[model]])
    h.save(out/'checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=h.sha(__file__),geometry_sha256=h.sha(h.__file__),
        corrected_inventory=True,literal_inventory_count=0,literal_count_method='General parity proof, no search',
        count=len(models),matches_book_count=(len(models)==43),path_classes=len(hist),matches_book_path_classes=(len(hist)==8),
        figure_occurrences=occurrences,matches_book_occurrences=(occurrences==[1,15,9,3]),all_models_valid=True,
        all_models_single_loop=True,loop_length=34,models=[list(m) for m in models],histogram=[dict(path=k,count=v) for k,v in sorted(hist.items())],
        native_elapsed_seconds=result['elapsed_seconds'],native_net_search_mems=result['net_search_mems'],
        terminal_sha256=h.sha(out/'corrected-all.json'),figures_sha256=h.sha(h.OUT/'figures-checked.json'),
        source_sha256=h.sha(source),binary_sha256=binary['sha256'],complete_second_census=False))
    print('ACCEPTED corrected inventory:',len(models),'solutions;',len(hist),'paths;figures',occurrences,
        'seconds',result['elapsed_seconds'],'mems',result['net_search_mems'])


if __name__=='__main__':main()
