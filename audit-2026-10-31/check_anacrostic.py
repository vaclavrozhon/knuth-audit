#!/usr/bin/env python3
"""Anacrostic 73--74: exact bitset table CSP and independent SAT encoding.

The quotation dictionaries are prefixes of Knuth's frequency-ordered OSPD4
files, with the lengths stated in the book. This checks the CSP counts; it
does NOT independently establish the BNC frequency cutoff or its counts.
"""
from collections import Counter, defaultdict, deque
import hashlib
import json
from pathlib import Path
import time

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/anacrostic'
SIZES=[85,562,1863,3199,4650,5631,5417,4724,3657,2448]
KEYWORDS=('spark often lucky other month ought names water games offer lying '
          'opens magic brick lamps empty organ noise after raise drink draft '
          'backs among under match earth roofs topic').split()
QUOTE=('the success or failure of backtrack often depends on the skill and '
       'ingenuity of the programmer backtrack programming as many other types '
       'of programming is somewhat of an art').split()


def load():
    groups=json.loads((OUT/'extracted.json').read_text())['groups']
    assert sorted(sum(groups,[])) == list(range(1,146))
    wfile=ROOT/'sources/wordlists/words5-from-sgb'
    words=wfile.read_text().split()[:1000]
    dictionaries={n:(ROOT/f'sources/wordlists/words{n}-from-OSPD4').read_text().split()[:size]
                  for n,size in enumerate(SIZES,2)}
    domains=[words for _ in range(29)]+[dictionaries[len(g)] for g in groups]
    positions=[list(range(5*i+1,5*i+6)) for i in range(29)]+groups
    return groups,domains,positions


def constraints(domains,positions):
    links=defaultdict(list)
    location={label:(i,p) for i,g in enumerate(positions[:29]) for p,label in enumerate(g)}
    for j in range(29,58):
        for q,label in enumerate(positions[j]):
            i,p=location[label]
            links[i,j].append((p,q))
    edges=[[] for _ in domains]
    for (i,j),pairs in links.items():
        maps=[]
        for var,side in [(i,0),(j,1)]:
            table=defaultdict(int)
            for w,word in enumerate(domains[var]):
                key=''.join(word[pair[side]] for pair in pairs)
                table[key] |= 1<<w
            maps.append(table)
        keys=maps[0].keys() & maps[1].keys()
        a=tuple(maps[0][k] for k in sorted(keys))
        b=tuple(maps[1][k] for k in sorted(keys))
        edges[i].append((j,a,b))
        edges[j].append((i,b,a))
    return edges


def propagate(state,edges,changed):
    todo=deque(changed)
    queued=set(changed)
    while todo:
        i=todo.popleft();queued.remove(i)
        for j,a,b in edges[i]:
            support=0
            for mask,target in zip(a,b):
                if state[i]&mask:support |= target
            reduced=state[j]&support
            if not reduced:return False
            if reduced!=state[j]:
                state[j]=reduced
                if j not in queued:
                    queued.add(j);todo.append(j)
    return True


def bitset_solve(domains,edges):
    start=[(1<<len(d))-1 for d in domains]
    assert propagate(start,edges,range(len(start)))
    sols=[];nodes=0
    def search(state):
        nonlocal nodes
        nodes+=1
        choices=[(x.bit_count(),i) for i,x in enumerate(state) if x.bit_count()>1]
        if not choices:
            sols.append(tuple(x.bit_length()-1 for x in state));return
        _,i=min(choices)
        bits=state[i]
        while bits:
            bit=bits&-bits;bits-=bit
            nxt=state.copy();nxt[i]=bit
            if propagate(nxt,edges,[i]):search(nxt)
    search(start)
    return sols,start,nodes


def sat_solve(domains,positions,reduced=None,support_encoding=False):
    from pysat.formula import CNF,IDPool
    from pysat.card import CardEnc,EncType
    from pysat.solvers import Solver
    pool=IDPool();cnf=CNF();choices=[]
    for i,d in enumerate(domains):
        row={k:pool.id(('word',i,k)) for k in range(len(d)) if reduced is None or reduced[i]>>k&1}
        choices.append(row)
        cnf.extend(CardEnc.equals(list(row.values()),bound=1,vpool=pool,
                                 encoding=EncType.seqcounter).clauses)
        for k,v in row.items():
            for label,ch in zip(positions[i],d[k]):
                cnf.append([-v,pool.id(('letter',label,ch))])
        if support_encoding:
            for p,label in enumerate(positions[i]):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    cnf.append([-pool.id(('letter',label,ch))]+[v for k,v in row.items() if d[k][p]==ch])
    for label in range(1,146):
        lits=[pool.id(('letter',label,c)) for c in 'abcdefghijklmnopqrstuvwxyz']
        cnf.extend(CardEnc.equals(lits,bound=1,vpool=pool,
                                 encoding=EncType.seqcounter).clauses)
    sols=[]
    with Solver(name='cadical195',bootstrap_with=cnf.clauses) as solver:
        while solver.solve():
            model=set(v for v in solver.get_model() if v>0)
            assignment=tuple(next(k for k,v in row.items() if v in model) for row in choices)
            sols.append(assignment)
            if len(sols)%100==0:print('SAT models',len(sols),flush=True)
            solver.add_clause([-choices[i][k] for i,k in enumerate(assignment)])
        stats=solver.accum_stats()
    return sols,{'variables':pool.top,'clauses':len(cnf.clauses),'stats':stats,
                 'initial_pruning':('none; all original dictionary alternatives encoded' if reduced is None else
                                    'arc consistency; every removed choice lacks support in a necessary equality'),
                 'support_encoding':support_encoding}


def validate(words,positions):
    labels={}
    for word,row in zip(words,positions):
        assert len(word)==len(row)
        for label,ch in zip(row,word):
            if label in labels:assert labels[label]==ch
            labels[label]=ch
    assert len(labels)==145


def main():
    started=time.time()
    groups,domains,positions=load()
    validate(KEYWORDS+QUOTE,positions)
    assert ''.join(w[0] for w in KEYWORDS)=='solomonwgolombleonarddbaumert'
    for i,word in enumerate(KEYWORDS+QUOTE):assert word in domains[i]
    pairs=sorted({w[1:3] for w in domains[26] if w[3:]+w[0] in domains[43]})
    assert len(pairs)==43 and pairs[:2]==['ab','ag'] and pairs[-1]=='ve'
    edges=constraints(domains,positions)
    solutions,reduced,nodes=bitset_solve(domains,edges)
    print('bitset',len(solutions),'nodes',nodes,'remaining',sum(x.bit_count() for x in reduced),flush=True)
    assert len(solutions)==720
    sat,stats=sat_solve(domains,positions,reduced)
    assert set(solutions)==set(sat) and len(sat)==720
    decoded=[[domains[i][k] for i,k in enumerate(sol)] for sol in sorted(solutions)]
    for words in decoded:
        validate(words,positions)
        assert all(word==QUOTE[i] for i,word in enumerate(words[29:]) if len(word)>5)
        assert words[26][1:3]=='ar'
    assert Counter(words[26] for words in decoded)=={'earth':240,'harsh':240,'large':240}
    first_quote=('the success or failure of backtrack often depends on roe skill '
                 'and ingenuity at the programmer backtrack programming as lacy '
                 'offal types of programming as somewhat al an art').split()
    assert any(words[29:]==first_quote for words in decoded)
    # Removing the internally constrained triple in keyword 27 leaves a
    # shared outside assignment; each of its 240 values has all 3 choices.
    external=Counter(tuple(w for i,w in enumerate(words) if i not in (26,43)) for words in decoded)
    assert len(external)==240 and set(external.values())=={3}
    variable={f'q{i+1}':sorted({w[29+i] for w in decoded}) for i in range(29)
              if len({w[29+i] for w in decoded})>1}
    result={'status':'pass','source_scope':'Author wordlist prefixes at stated sizes; BNC cutoff frequencies not independently verified',
            'domain_sizes':SIZES,'keyword_ranks':[domains[i].index(w)+1 for i,w in enumerate(KEYWORDS)],
            'count':720,'nodes':nodes,'initial_reduced_sizes':[x.bit_count() for x in reduced],
            'independent_sat':stats,'pairs':pairs,'factors':{'earth':240,'harsh':240,'large':240},
            'external_assignments':len(external),'variable_quotation_words':variable,
            'elapsed_seconds':time.time()-started}
    (OUT/'solutions.json').write_text(json.dumps(decoded,indent=2)+'\n')
    (OUT/'verified.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
