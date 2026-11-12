#!/usr/bin/env python3
"""Complete nonidentity D4 fixed sets, each with two independent solvers."""
from collections import Counter
from datetime import datetime,timezone
import gzip
import json
import check_jigsaw_symmetry as sym
from dlx1_audit_tools import ROOT,sha

OUT=ROOT/'results/convex68'
EXPECTED={'n2':{4:1},'n3':{1:1,4:1},'n4':{1:10,2:7,4:4,8:1},
          'n5':{1:355,2:15,4:4},'n6':{1:20154,2:342,4:8},
          'n7':{1:2272821,2:1181,4:5},'n9':{1:1014148,2:119,4:24,8:1},
          'n9-no-square':{1:675797}}


def main():
    sym.OUT=OUT
    options=json.loads((OUT/'options.json').read_text())
    counts=json.loads((OUT/'counts.json').read_text())
    result=dict(status='running',source_sha256=sha(__file__),
      orbit_helper_sha256=sha(ROOT/'check_jigsaw_symmetry.py'),
      independent_solver_sha256=sha(ROOT/'check_sudoku_trios57.py'),cases={})
    for label,expected in EXPECTED.items():
        n=options['cases'][label]['n']
        full=counts['cases'][label]['methods']['cell-mask']
        assert full['status']=='finished'
        total=full['output']['solutions']
        path=OUT/(label+'.json.gz')
        assert sha(path)==options['cases'][label]['json_sha256']
        tiles=set(map(tuple,json.loads(gzip.decompress(path.read_bytes()))))
        maps=sym.maps(n);nontrivial=set();groups={}
        for i in range(1,8):
            group={maps[0],maps[i]}
            while True:
                closed=group|{tuple(a[b[v]] for v in range(n*n)) for a in group for b in group}
                if closed==group:break
                group=closed
            models,stats=sym.solve_group(n,tiles,sorted(group),f'{label}-g{i}')
            nontrivial.update(models);groups[str(i)]=stats
            print(label,'symmetry',i,'fixed',len(models),flush=True)
        reps={min(sym.moved(t,g) for g in maps) for t in nontrivial}
        census=Counter(sum(sym.moved(t,g)==t for g in maps) for t in reps)
        assert (total-len(nontrivial))%8==0
        asymmetric=(total-len(nontrivial))//8
        if asymmetric:census[1]=asymmetric
        assert dict(census)==expected,(label,census,expected)
        assert sum(8//k*v for k,v in census.items())==total
        modelsfile=OUT/(label+'-symmetric-models.json.gz')
        with gzip.open(modelsfile,'wt') as f:json.dump(sorted(nontrivial),f)
        result['cases'][label]=dict(groups=groups,total=total,symmetric_tilings=len(nontrivial),
              class_census=dict(census),models_sha256=sha(modelsfile),
              independent_total_stdout_sha256=full['stdout_sha256'])
        (OUT/'symmetry.json').write_text(json.dumps(result,indent=2)+'\n')
    result.update(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat())
    (OUT/'symmetry.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: all exercise68 symmetry classifications')


if __name__=='__main__':main()
