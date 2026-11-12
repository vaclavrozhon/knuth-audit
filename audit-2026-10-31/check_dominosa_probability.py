#!/usr/bin/env python3
"""Exact witness for the DLX72 wording distinction; no new historical sample claim."""
from collections import Counter
from datetime import datetime,timezone
from fractions import Fraction
import json
import math
from dlx1_audit_tools import ROOT,sha
from check_dominosa_records import OUT,PAIRS


def main():
    previous=ROOT/'results/convex68/dominosa70.json'
    d=json.loads(previous.read_text())
    N=1292697*math.factorial(28)*2**21
    M=math.factorial(56)//math.factorial(8)**7
    witnesses={}
    for label,case in d['cases'].items():
        board=case['board'];models=case['all_models']
        assert Counter(board)=={x:8 for x in range(7)}
        assert len(models)==case['solutions']==case['native']['solutions']
        for model in models:
            assert sorted(v for edge in model for v in edge)==list(range(56))
            assert sorted(tuple(sorted((board[u],board[v]))) for u,v in model)==PAIRS
            assert all((u//8==v//8 and v==u+1) or v==u+8 for u,v in model)
        witnesses[label]=dict(board=board,solutions=len(models),
          probability_uniform_arrangement=str(Fraction(len(models),N)),
          probability_uniform_solvable_matrix='1/K, where K is the number of distinct solvable matrices')
    assert witnesses['a']['solutions']==2 and witnesses['b']['solutions']==1
    result=dict(status='verified_probability_distinction; wording_remains_candidate',
      checked_at_utc=datetime.now(timezone.utc).isoformat(),source_sha256=sha(__file__),
      previous_complete_enumeration_sha256=sha(previous),M=M,N=N,
      witnesses=witnesses,arrangement_probability_ratio='2:1',uniform_matrix_probability_ratio='1:1',
      identities={
        'sample_space':'Omega={(A,T): T is a valid complete Dominosa solution for A}',
        'number_of_geometric_tilings':1292697,
        'assignments_per_tiling':'28!*2^21',
        'number_of_arrangements':'|Omega|=N=sum_A S(A)',
        'uniform_i':'P_i(A)=1/M for every admissible multiset matrix',
        'answer_ii':'P_ii(A)=S(A)/N',
        'literal_uniform_distinct_solvable':'P_literal(A)=1/K if S(A)>0, else0; equals model(i) conditioned on solvability',
        'expected_i':'E_i S=N/M',
        'unique_ii':'P_ii(S=1)=P_i(S=1)/(N/M)',
      },
      interpretation='Question72 says each matrix ... is equally likely. Answer72 uses uniform arrangements, which are not uniform distinct matrices. If matrix is shorthand for a labelled arrangement with divisions, the intent is consistent; retain C024 as wording candidate.')
    (OUT/'model-ii-scope.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: exact2:1 versus1:1 witness; all three sample spaces distinguished.')


if __name__=='__main__':main()
