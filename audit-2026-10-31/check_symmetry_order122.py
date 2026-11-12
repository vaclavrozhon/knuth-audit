"""Candidate C031: distinguish unordered input symmetry from node-order symmetry."""
from collections import Counter
from itertools import permutations,product
from datetime import datetime,timezone
from colored_dlx import brute
from color_symmetry122 import SymmetryDLX,canonical_model
from native_symmetry122 import OUT,encode,run,save,sha
from check_color_symmetry122 import native_models


def main():
    rows=[((1,0),(2,1),(3,2)),((1,0),(2,2),(3,1))]
    histogram=Counter();cases=[]
    for first,second in product(permutations(rows[0]),permutations(rows[1])):
        instance=[first,second]
        expected=brute(1,instance)
        assert expected=={(0,),(1,)}
        assert len({canonical_model(m,instance) for m in expected})==1
        actual=SymmetryDLX(3,1,instance).solve(check_each_node=True)
        fixed=SymmetryDLX(3,1,[tuple(sorted(row)) for row in instance]).solve(check_each_node=True)
        assert fixed.count==1
        histogram[actual.count]+=1
        cases.append(dict(rows=instance,representatives=sorted(actual.solutions),sorted_representatives=sorted(fixed.solutions)))
    assert histogram=={0:9,1:18,2:9}
    witnesses={
        'ordered':rows,
        'both_kept':[((1,0),(2,1),(3,2)),((1,0),(3,1),(2,2))],
        'both_lost':[((1,0),(3,2),(2,1)),((1,0),(2,2),(3,1))],
    }
    records=[]
    for label,instance in witnesses.items():
        s=SymmetryDLX(3,1,instance,trace=True).solve(check_each_node=True)
        native=[]
        for variant in ['original','symmetry122']:
            data=encode(3,1,instance)
            r=run('order122-'+label+'-'+variant,variant,data)
            model_set=native_models('order122-'+label+'-'+variant,data)
            assert model_set==(brute(1,instance) if variant=='original' else s.solutions)
            native.append(r)
        records.append(dict(label=label,rows=instance,trace=s.events,representatives=sorted(s.solutions),native=native))
    save(OUT/'order122-verified.json',dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
         validator_sha256=sha(__file__),interpreter_sha256=sha('color_symmetry122.py'),
         unordered_options_are_color_symmetric=True,every_solution_uses_both_colors=True,
         permutation_cases=cases,count_histogram=dict(histogram),witnesses=records,
         status='candidate',interpretation='The mathematical input options are sets (p66), but total symmetry in122 might implicitly require ordered representations to be equivariant. Fixed item ordering is a sufficient explicit precondition. The existing122 algorithm is correct under that stronger interpretation.'))
    print('PASS:36 row-order variants; output histogram0:9,1:18,2:9; three native witnesses accepted without rerunning.')


if __name__=='__main__':main()
