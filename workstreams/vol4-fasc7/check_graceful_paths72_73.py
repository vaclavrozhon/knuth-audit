#!/usr/bin/env python3
"""Literal P1--P5 and corrected73, only n<=10 (tiny exact trees).

Every successful join and every undo is checked against an independently
reconstructed path forest. No large permutation count or benchmark.
"""
from collections import Counter
from functools import lru_cache
from itertools import permutations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def forest_certificate(n,level,lo,mate):
    edges=[(lo[n-j],lo[n-j]+n-j) for j in range(1,level)]
    adj=[[] for _ in range(n)]
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    assert all(len(a)<=2 for a in adj)
    seen=set();fragments=[]
    for v in range(n):
        if not adj[v]:assert mate[v]==v;seen.add(v)
    for v in range(n):
        if v in seen or len(adj[v])!=1:continue
        path=[v];prev=-1;current=v
        while True:
            seen.add(current)
            nxt=[x for x in adj[current] if x!=prev]
            if not nxt:break
            assert len(nxt)==1 and nxt[0] not in seen
            prev,current=current,nxt[0];path.append(current)
        assert mate[path[0]]==path[-1] and mate[path[-1]]==path[0]
        assert all(mate[x]<0 for x in path[1:-1])
        if n>=3 and 0 in path and len(adj[0])==2:
            k=path.index(0)
            if path[k-1:k+2]!=[n-2,0,n-1]:path.reverse()
            k=path.index(0);assert path[k-1:k+2]==[n-2,0,n-1]
        elif tuple(reversed(path))<tuple(path):path.reverse()
        fragments.append(path)
    assert len(seen)==n and len(edges)==level-1
    fragments.sort(key=lambda p:(0 not in p,p))
    return ','.join(''.join(map(str,p)) for p in fragments) if fragments else ('0' if n==1 else '')


def run(n,memo=False):
    assert 1<=n<=10
    mate=list(range(n));lo=[None]*n;level=1;v=0;step='P2'
    before={};nodes=[];prefix_id={};solutions=[];attempts=0;restorations=0
    seen={tuple(mate):0};states=[{'blur':list(mate),'level':1,'first':0,'loc':0}]
    alpha={1:0};branches=[None,{'v':None,'target':0,'other':0,'difference':None}]
    def record():
        prefix=tuple(lo[n-j] for j in range(1,level))
        fragment=forest_certificate(n,level,lo,mate)
        row={'level':level,'prefix':list(prefix),'mate':mate.copy(),'fragment':fragment,
             'parent':None if not prefix else prefix_id[prefix[:-1]]}
        index=len(nodes);nodes.append(row);prefix_id[prefix]=index
    record()
    operations=0
    while True:
        operations+=1;assert operations<100000
        if step=='P2':
            if level==n:
                solutions.append(tuple(lo[n-j] for j in range(1,n)))
                if memo:states[alpha[level]]['loc']=1
                step='P5'
            else:v=0;step='P3'
        elif step=='P3':
            attempts+=1;w=v+n-level;vp=mate[v];wp=mate[w]
            if vp<0 or wp<0 or vp==w:step='P4';continue
            before[level]=tuple(mate);lo[n-level]=v
            mate[v]=~vp;mate[w]=~wp;mate[vp]=wp;mate[wp]=vp
            level+=1;record()
            if memo:
                blur=tuple(None if x<0 else x for x in mate)
                old=blur in seen
                if not old:
                    seen[blur]=len(states)
                    states.append({'blur':list(blur),'level':level,'first':0,'loc':0})
                child=seen[blur];assert states[child]['level']==level
                alpha[level]=child;parent=alpha[level-1]
                branches.append({'v':v,'target':child,'other':states[parent]['first'],
                                 'difference':n-level+1})
                states[parent]['first']=len(branches)-1
                step='P5' if old else 'P2'
            else:step='P2'
        elif step=='P4':
            v+=1;step='P3' if v<level and level>2 else 'P5'
        elif step=='P5':
            level-=1
            if level==0:break
            v=lo[n-level];w=v+n-level;vp=mate[v];wp=mate[w]
            if vp>=0:mate[v]=v
            else:mate[v]=~vp;mate[~vp]=v
            if wp>=0:mate[w]=w
            else:mate[w]=~wp;mate[~wp]=w
            assert tuple(mate)==before[level]
            forest_certificate(n,level,lo,mate);restorations+=1;step='P4'
    assert mate==list(range(n))
    return {'n':n,'nodes':nodes,'solutions':solutions,'attempts':attempts,
            'restorations':restorations,'states':states,'branches':branches}


def convert(r):
    # Literal corrected conversion. Root-terminal n=1 is treated separately
    # and not represented as a success of the printed initialization.
    if r['n']==1:return {'terminal_root':True,'printed_initialization_needs_exception':True,'count':1}
    states=[dict(s) for s in r['states']];branches=[None]+[dict(b) for b in r['branches'][1:]]
    stack=1;branches[1]['target']=0;branches[1]['other']=0;states[0]['loc']=2;z=3
    output={};pushes=0;processed=[]
    while stack:
        state=branches[stack]['target'];p=states[state]['loc'];q=states[state]['first'];stack=branches[stack]['other']
        assert state not in processed;processed.append(state)
        while q:
            qp=branches[q]['other'];child=branches[q]['target']
            if states[child]['loc']==0 and states[child]['first']!=0:
                branches[q]['other']=stack;stack=q;states[child]['loc']=z;z+=1;pushes+=1
            assert p not in output
            reject=z if qp else 0
            output[p]={'difference':branches[q]['difference'],'lower':branches[q]['v'],
                       'reject':reject,'choose':states[child]['loc']}
            if qp:p=z;z+=1
            q=qp
    assert set(output)==set(range(2,z))
    visiting=set()
    @lru_cache(None)
    def paths(p):
        if p==0:return ()
        if p==1:return ((),)
        assert p not in visiting;visiting.add(p);node=output[p]
        out=paths(node['reject'])+tuple(((node['difference'],node['lower']),)+q for q in paths(node['choose']))
        visiting.remove(p);return out
    expanded=paths(2)
    assert all([d for d,v in path]==list(range(r['n']-1,0,-1)) for path in expanded)
    lo_set={tuple(v for d,v in path) for path in expanded}
    assert len(lo_set)==len(expanded)
    count_certificate=count_like_4a208(output)
    assert count_certificate['count']==len(expanded)
    return {'nodes':output,'count':len(expanded),'prefixes':sorted(lo_set),
            '4a208':count_certificate,
            'nonroot_state_pushes':pushes,'processed_states':processed,
            'every_record_output_once':len(output)==len(r['branches'])-2}


def count_like_4a208(nodes):
    # Algorithm C explicitly requires both children before their parent.
    nodes={int(k):v for k,v in nodes.items()};seen={0,1};order=[]
    def visit(p):
        if p in seen:return
        seen.add(p);visit(nodes[p]['reject']);visit(nodes[p]['choose']);order.append(p)
    visit(2);mapping={0:0,1:1,**{p:k+2 for k,p in enumerate(order)}}
    counts=[0,1]
    for p in order:
        lo=mapping[nodes[p]['reject']];hi=mapping[nodes[p]['choose']]
        assert lo<len(counts) and hi<len(counts)
        counts.append(counts[lo]+counts[hi])
    assert order[-1]==2
    return {'old_node_postorder':order,'counts_in_new_order':counts,'count':counts[-1]}


def canonical_lo(p):
    n=len(p);lo=[None]*n
    for u,v in zip(p,p[1:]):lo[abs(v-u)]=min(u,v)
    if n>2 and lo[n-2]==1:
        return canonical_lo(tuple(n-1-x for x in p))
    return tuple(lo[d] for d in range(n-1,0,-1))


def main():
    summaries=[];saved={}
    for n in range(1,11):
        plain=run(n);merged=run(n,True);dag=convert(merged)
        assert dag['count']==len(plain['solutions'])
        if n>1:assert set(map(tuple,dag['prefixes']))==set(plain['solutions'])
        brute=[]
        if n<=6:
            brute=[p for p in permutations(range(n)) if sorted(abs(a-b) for a,b in zip(p,p[1:]))==list(range(1,n))]
            assert {canonical_lo(p) for p in brute}==set(plain['solutions'])
        summaries.append({'n':n,'full_nodes':len(plain['nodes']),
                          'nodes_after_two_initial_edges':sum(q['level']>=3 for q in plain['nodes']),
                          'canonical_solutions':len(plain['solutions']),'pair_attempts':plain['attempts'],
                          'exact_restorations':plain['restorations'],'blurred_states':len(merged['states']),
                          'merged_branches':len(merged['branches'])-2,'output_nodes':len(dag.get('nodes',{})),
                          'brute_permutations':brute if n<=3 else len(brute) if n<=6 else None})
        if n in (1,2,4,5,6,10):saved[str(n)]={'plain':plain,'merged':merged,'converted':dag}
    n6=saved['6']['plain']['nodes'];by_fragment={q['fragment']:q for q in n6}
    assert by_fragment['405']['mate']==[~5,1,2,3,5,4]
    assert by_fragment['4052,13']['mate']==[~5,3,4,1,2,~4]
    expected={
      '405':{'1405','4052'},'1405':{'31405','14053'},'4052':{'4052,13'},
      '31405':{'231405'},'14053':{'140532','214053'},
      '4052,13':{'134052','405213','405231'}}
    for parent,children in expected.items():
        pi=next(i for i,q in enumerate(n6) if q['fragment']==parent)
        assert {q['fragment'] for q in n6 if q['parent']==pi}==children
    nodes10=saved['10']['plain']['nodes']
    equal=[]
    for name in ('1738092','1809372'):
        q=next(q for q in nodes10 if q['fragment']==name)
        blur=[None if v<0 else v for v in q['mate']]
        assert blur==[None,2,1,None,4,5,6,None,None,None]
        equal.append({'fragment':name,'level':q['level'],'blur':blur})
    assert sum(q['level']>=3 for q in nodes10)==206
    result={'known_corrections':['2026-09-13: p starts at1','2026-09-13: repeated state jumps to P5','2026-09-13: LOC(root)=2 and next free z=3'],
            'summaries':summaries,'detailed_small_runs':saved,'P6_printed_tree':{k:sorted(v) for k,v in expected.items()},
            'P10_equal_blurred_states':equal,'scope':'Only n<=10; all large census and historical mem counts excluded.'}
    (ROOT/'results/graceful-paths72-73.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(summaries))


if __name__=='__main__':main()
