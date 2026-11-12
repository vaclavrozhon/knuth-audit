#!/usr/bin/env python3
"""Independent tree profiles, source comparisons, and Harris inclusion-exclusion."""
from collections import Counter
from datetime import datetime,timezone
import json
from math import prod
from dlx1_audit_tools import ROOT,sha,statistics
from check_jigsaw_small import instance,coordinate_solutions

OUT=ROOT/'results/jigsaw'


def exact_cover(rows,nitems,primary):
    item_rows=[0]*nitems
    masks=[]
    for r,row in enumerate(rows):
        masks.append(sum(1<<(i-1) for i in row))
        for i in row:item_rows[i-1]|=1<<r
    conflicts=[]
    for row in rows:
        union=0
        for i in row:union|=item_rows[i-1]
        conflicts.append(union)
    profile=Counter();models=set()
    def visit(remaining,active,selected):
        profile[len(selected)]+=1
        if not remaining:models.add(tuple(sorted(selected)));return
        best=len(rows)+1;candidates=0
        mask=remaining
        while mask:
            b=mask&-mask;mask^=b
            choices=item_rows[b.bit_length()-1]&active
            count=choices.bit_count()
            if count<best:
                best,candidates=count,choices
                if not count:return
        while candidates:
            b=candidates&-candidates;candidates^=b;r=b.bit_length()-1
            visit(remaining&~masks[r],active&~conflicts[r],selected+[r])
    visit((1<<primary)-1,(1<<len(rows))-1,[])
    return models,profile


def main():
    diagrams=json.loads((OUT/'pdf-diagrams.json').read_text())['sources']
    small=json.loads((OUT/'small.json').read_text())
    result=dict(source_sha256=sha(__file__),small_sha256=sha(OUT/'small.json'),profiles={})
    for label,key,alphabet,book in [('59a','34a','123456789',1105),('59b','34b','GRANDTIME',910),
            ('59c','34c','AFKLNTVWY',122),('60a','60qa','123456',23),
            ('60b','60qb','123456',26),('60c','60qc','123456',16)]:
        d=diagrams[key];names,rows,moves,primary=instance(d,alphabet)
        models,profile=exact_cover(rows,len(names),primary)
        filename='59b-order-GRANDTIME' if label=='59b' else label
        native=statistics((OUT/'native'/(filename+'.log')).read_text())
        assert native['profile']==[profile.get(i,0) for i in range(len(native['profile']))]
        assert len(models)==native['solutions']==1 and native['nodes']==book+1
        completed=list(d['cells'])
        for r in next(iter(models)):
            v,k=moves[r];assert completed[v]=='.';completed[v]=k
        assert ''.join(completed)==small['puzzles'][label]['solutions'][0]
        result['profiles'][label]=dict(alphabet=alphabet,primary_items=primary,total_items=len(names),
                book_nodes=book,inclusive_nodes=native['nodes'],excluding_successful_leaf=native['nodes']-1,
                profile=profile,native_log_sha256=sha(OUT/'native'/(filename+'.log')))
    # At least one full row and one full column cannot coexist as tiles.
    # For a nonempty selected set of full rows, each gap is an independent
    # n-by-gap rectangle. Inclusion-exclusion therefore removes all straight
    # rows, and twice that result removes straight rows OR columns.
    harris={3:[1,1,3,10],4:[1,1,4,23,117],5:[1,1,5,56,501,4006],
            6:[1,1,6,132,2369,33344,451206],7:[1,1,7,259,9525,270827,6633399,158753814]}
    expected={3:0,4:33,5:2082,6:320098,7:132418528}
    ie={}
    for n,counts in harris.items():
        summands=[]
        for mask in range(1,1<<n):
            rows=[i for i in range(n) if mask>>i&1]
            endpoints=[-1]+rows+[n]
            gaps=[b-a-1 for a,b in zip(endpoints,endpoints[1:])]
            term=(-1)**(len(rows)+1)*prod(counts[k] for k in gaps)
            summands.append(dict(selected_rows=rows,gaps=gaps,term=term))
        with_row=sum(t['term'] for t in summands)
        assert counts[-1]-2*with_row==expected[n]
        ie[str(n)]=dict(rectangle_counts=counts,source='Harris2010, PDF page9, tables2/3(a); T0=T1=1',
                       with_at_least_one_straight_row=with_row,nonstraight=expected[n],summands=summands)
    result['harris_inclusion_exclusion']=ie
    result['harris_source_sha256']=sha(ROOT/'sources/jigsaw/harris-tilings2010.pdf')
    # The source ABC collection has an additional3 in the final row of A.
    # It is redundant in the printed solution, not an invalid clue in TAOCP.
    d=diagrams['60qa'];board=list(d['cells']);assert board[31]=='.';board[31]='3'
    solutions,nodes=coordinate_solutions(d,'123456',board)
    assert solutions==small['puzzles']['60a']['solutions']
    result['puzzlium_source_comparison']=dict(source_sha256=sha(ROOT/'sources/jigsaw/puzzlium-abc2014.pdf'),
            visual_page=3,extra_clue_A=dict(row=5,column=1,value='3'),same_unique_solution=True,
            B_and_C='Visually matched all clues and boundaries; A differs only by the redundant3.')
    result['bibliographic_scope']={
       'Snyder':'Author reprint2025 explicitly dates the original2006/06/09; entire puzzle and disconnected New York island visually match.',
       'Harris':'Original2010 manuscript and tables obtained from author site; cites Grand Time chapter2009 pp55–57. Full2009 chapter not archived.',
       'Puzzlium':'Original2014 PDF confirms centennial collection and exact puzzle shapes. Exact announcement date21Oct and individual authorship remain separate historical checks.',
       'Behrens':'1956 original paper and precise priority claim not retrieved; PDF/PS35b error does not depend on that attribution.',
       'Thompson':'1996 magazine pages51/67 not retrieved; no independent claim of priority made.'}
    result.update(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat())
    (OUT/'supplement.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS six complete profiles, five inclusion-exclusion totals and original ABC clue variant')


if __name__=='__main__':main()
