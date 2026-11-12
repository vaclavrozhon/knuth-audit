#!/usr/bin/env python3
"""A qualification to 'Algorithm X will discover that fact quickly', DLX4.

k separate edges, followed by a triangle, are not bipartite. With the listed
edge order, MRV explores a full binary tree with 2^(k+2)-1 nodes. 'Quickly'
is informal, so this is evidence for a candidate, not a definite erratum.
"""
from datetime import datetime,timezone
from pathlib import Path
import hashlib
import json
from algorithm_x import DLX
from spacer_algorithm_x import SpacerX


def main():
    cases=[]
    for k in range(10):
        n=k+3
        # Each of the first k connected components has two vertices and one
        # edge; the final three vertices have the three triangle incidences.
        rows=[(i,) for i in range(1,k+1) for _ in range(2)]
        rows += [(k+1,k+2),(k+2,k+3),(k+1,k+3)]
        expected={depth:2**depth for depth in range(k+2)}
        for mrv in (False,True):
            run=DLX(list(range(1,n+1)),rows).solve(mrv=mrv)
            assert not run.solutions and dict(run.nodes_by_depth)==expected
        literal=SpacerX([str(i) for i in range(1,n+1)],rows).solve()
        assert not literal.solutions and dict(literal.profile)==expected
        cases.append(dict(separate_edges=k,graph_vertices=2*k+3,graph_edges=n,
                          solutions=0,profile=list(expected.values()),nodes=sum(expected.values())))
    root=Path(__file__).resolve().parent
    out=dict(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat(),
             source_sha256={name:hashlib.sha256((root/name).read_bytes()).hexdigest()
                for name in ['check_incidence_runtime.py','algorithm_x.py','spacer_algorithm_x.py']},
             cases=cases,general_formula='nodes=2^(k+2)-1, zero solutions',
             interpretation='An exponential counterexample to a universal fast-rejection reading; the book uses only the informal word quickly.')
    (root/'results/dancing_links/incidence-runtime.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['status','general_formula','interpretation']},indent=2))


if __name__=='__main__':main()
