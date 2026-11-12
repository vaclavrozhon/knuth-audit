"""Accept newly terminal paired cases; counts and full/sample scopes stay separate."""
from datetime import datetime,timezone
from pathlib import Path
import argparse,gzip,hashlib,json,re
import octagons142 as h
from octagons142_jobs import JOBS


def read(p):
    return json.loads(Path(p).read_text())


def checker(layout,periodic):
    board=sorted(layout);edges=sorted({e for cell in board for e in h.half_edges(cell)})
    edge_index={e:i for i,e in enumerate(edges)}
    entries=[[ (edge_index[e],sector) for e,sector in zip(h.half_edges(c),h.sector_indices(layout[c]))] for c in board]
    types={word:i for i,word in enumerate(h.inventory()[1])}
    piece={word:types[h.tile(word)] for word in h.inventory()[0]}
    pairs={axis:[(edge_index[a],edge_index[b]) for a,b in pp] for axis,pp in h.boundary_pairs(layout).items()}
    def validate(words):
        assert len(words)==24
        fields=[None]*len(edges);used=0
        for index,word in enumerate(words):
            assert word in piece
            bit=1<<piece[word];assert not used&bit;used|=bit
            for edge,sector in entries[index]:
                value=word[sector]
                assert fields[edge] in [None,value]
                fields[edge]=value
        assert used==(1<<24)-1 and None not in fields
        matches={axis:all(fields[a]==fields[b] for a,b in pp) for axis,pp in pairs.items()}
        assert all(matches[axis] for axis in periodic)
        return h.color_key(''.join(words)),matches
    return validate


def reflected(key,case,layout):
    board=sorted(layout);original=dict(zip(board,[key[4*i:4*i+4] for i in range(24)]))
    transformed={}
    for (x,y),word in original.items():
        mode=layout[x,y]
        if case=='i':
            cell=x,3-y;indices=[3,2,1,0] if mode=='V' else [2,1,0,3]
        elif case=='ii':
            cell=5-x,y;indices=[1,0,3,2] if mode=='V' else [0,3,2,1]
        else:
            cell=5-x,3-y;indices=[2,3,0,1]
        assert layout[cell]==mode
        transformed[cell]=''.join(word[j] for j in indices)
    return h.color_key(''.join(transformed[c] for c in board))


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--labels',nargs='*');args=parser.parse_args()
    accepted=h.OUT/'accepted';accepted.mkdir(exist_ok=True)
    jobs=[j for j in JOBS if (args.labels is None or j['label'] in args.labels)
          and all((h.OUT/method/(j['label']+'.json')).exists() for method in ['native','independent'])
          and not (accepted/(j['label']+'.json')).exists()]
    assert jobs,'No new paired terminal exists; do not rerun a search.'
    queues={method:read(h.OUT/method/'queue.json') for method in ['native','independent']}
    for queue in queues.values():
        for path,digest in queue['source_sha256'].items():
            assert h.sha(h.ROOT/path)==digest,path
    for job in jobs:
        label=job['label'];layout=h.modes(job['case']);validate=checker(layout,job['periodic'])
        enc=h.problem(layout,periodic=job['periodic']);contract=h.contracted(layout,job['periodic'])
        metadata={method:read(h.OUT/method/(label+'.json')) for method in queues}
        for method,meta in metadata.items():
            assert meta['status']=='completed' and meta['returncode']==0
            done=next(c for c in queues[method]['done'] if c['label']==label)
            assert done['terminal_sha256']==h.sha(h.OUT/method/(label+'.json'))
            assert done['solutions']==meta['solutions']
            for suffix,key in [('.out.gz','stdout_sha256'),('.log','stderr_sha256')]:
                assert h.sha(h.OUT/method/(label+suffix))==meta[key],(label,method,key)
            assert h.sha(meta['command'][2])==meta['binary_sha256']
        native=metadata['native'];independent=metadata['independent']
        assert native['solutions']==independent['solutions']
        assert native['model_output_period']==job['every']
        assert h.sha(native['source'])==native['source_sha256']
        assert h.sha(h.ROOT/'graph_native.py')==native['runner_sha256']
        assert (h.OUT/'native'/(label+'.dlx')).read_text()==h.native_text(enc)
        assert h.sha(h.OUT/'native'/(label+'.dlx'))==native['input_sha256']
        assert (h.OUT/'independent'/(label+'.case')).read_text()==h.independent_case(label,layout,every=job['every'],periodic=job['periodic'])
        assert h.sha(h.OUT/'independent'/(label+'.case'))==independent['input_sha256']
        lookup={tuple(sorted(row)):(tuple(place['cell']),place['word']) for row,place in zip(enc['rows'],enc['placements'])}
        assert len(lookup)==len(enc['rows'])
        nmodels=set();nordinals=[];choices=None;hash_native=hashlib.sha256()
        board=sorted(layout)
        def finish():
            assert set(choices)==set(layout)
            key,matches=validate([choices[c] for c in board]);assert key not in nmodels;nmodels.add(key)
        with gzip.open(h.OUT/'native'/(label+'.out.gz'),'rb') as fin:
            for raw in fin:
                hash_native.update(raw);line=raw.decode().strip()
                if re.fullmatch(r'\d+:',line):
                    if choices is not None:finish()
                    choices={};nordinals.append(int(line[:-1]))
                elif line:
                    assert choices is not None
                    tokens=re.sub(r'\s*\(\d+ of \d+\)\s*$','',line).split()
                    cell,word=lookup[tuple(sorted(tokens))];assert cell not in choices;choices[cell]=word
        if choices is not None:finish()
        assert hash_native.hexdigest()==native['raw_stdout_sha256']
        assert nordinals==list(range(job['every'],native['solutions']+1,job['every']))
        imodels=set();iordinals=[];hash_independent=hashlib.sha256();terminal=None
        with gzip.open(h.OUT/'independent'/(label+'.out.gz'),'rb') as fin:
            for raw in fin:
                hash_independent.update(raw);parts=raw.decode().split()
                if parts[0]=='M':
                    assert terminal is None and len(parts)==4 and parts[1]==label
                    word=parts[3];assert len(word)==contract['variables'] and set(word)<=set('abc') and h.color_key(word)==word
                    key,matches=validate([''.join(word[j] for j in ids) for ids in contract['sectors']])
                    assert key not in imodels;imodels.add(key);iordinals.append(int(parts[2]))
                else:
                    assert parts[:2]==['C',label] and terminal is None and len(parts)==8
                    terminal=list(map(int,parts[2:]))
        assert hash_independent.hexdigest()==independent['raw_stdout_sha256']
        assert terminal==[independent[k] for k in ['solutions','nodes','tb','lr','both','emitted']]
        expected_ordinals=list(range(job['every'],independent['solutions']+1,job['every']))
        if job['every']>1 and independent['solutions']:
            expected_ordinals=[1]+expected_ordinals
        assert iordinals==expected_ordinals and len(imodels)==independent['emitted']
        log=(h.OUT/'independent'/(label+'.log')).read_text().splitlines()
        assert log[-2:]==['COMPLETED '+label+' '+' '.join(map(str,terminal)),'ALL_COMPLETED 1']
        all_sets=job['every']==1
        case=dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=h.sha(__file__),
            geometry_sha256=h.sha(h.__file__),label=label,case=job['case'],periodic=job['periodic'],
            solutions=native['solutions'],book_expected=job['expected'],
            matches_book=(native['solutions']==job['expected']) if job['expected'] is not None else None,
            native_direct_models=len(nmodels),independent_direct_models=len(imodels),
            complete_sets_equal=all_sets,native_net_search_mems=native['net_search_mems'],
            independent_boundary_counts={k:independent[k] for k in ['tb','lr','both']},
            terminal_sha256={m:h.sha(h.OUT/m/(label+'.json')) for m in metadata})
        if all_sets:
            assert nmodels==imodels and len(nmodels)==native['solutions']
            representatives=[]
            for key in sorted(nmodels):
                mate=reflected(key,job['case'],layout)
                assert mate in nmodels and mate!=key and reflected(mate,job['case'],layout)==key
                if key<mate:representatives.append(key)
            assert 2*len(representatives)==len(nmodels)
            model_path=accepted/(label+'-models.txt.gz')
            with gzip.open(model_path,'wt') as fout:
                fout.write(''.join(key+'\n' for key in sorted(nmodels)))
            reps_path=accepted/(label+'-representatives.txt.gz')
            with gzip.open(reps_path,'wt') as fout:
                fout.write(''.join(key+'\n' for key in representatives))
            case.update(geometric_classes=len(representatives),all_geometric_orbits_size=2,
                        models_sha256=h.sha(model_path),representatives_sha256=h.sha(reps_path))
        h.save(accepted/(label+'.json'),case)
        print('ACCEPTED',label,native['solutions'],'complete sets',all_sets,'matches book',case['matches_book'],flush=True)


if __name__=='__main__':
    main()
