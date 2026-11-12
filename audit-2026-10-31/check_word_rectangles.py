#!/usr/bin/env python3
"""Small independent exact models, printed witnesses and trie data, 7.2.2--23--33."""
from collections import defaultdict, Counter
from itertools import product
from pathlib import Path
import json
import random

ROOT=Path(__file__).resolve().parent
DATA=ROOT/'sources/wordlists'
OUT=ROOT/'results/word_rectangles'


def dictionary(n, ospd=False):
    return (DATA/f'words{n}-from-{"sgb" if n==5 and not ospd else "OSPD4"}').read_text().splitlines()


def transpose(rows):
    return [''.join(c) for c in zip(*rows)]


def trie(words):
    nodes=[{}];prefix={'':0};n=len(words[0])
    for rank,w in enumerate(words,1):
        p=0
        for j,c in enumerate(w):
            if j==n-1:
                nodes[p][c]=rank
            else:
                if c not in nodes[p]:
                    nodes[p][c]=len(nodes);prefix[w[:j+1]]=len(nodes);nodes.append({})
                p=nodes[p][c]
    return nodes,prefix


def small_models(mw,nw):
    m,n=len(mw[0]),len(nw[0]);N=set(nw)
    prefixes=[{w[:i] for w in nw} for i in range(n+1)]
    expected={tuple(cols) for cols in product(mw,repeat=n) if all(w in N for w in transpose(cols))}
    results=[];profiles=[]
    for restricted in [False,True]:
        found=set();profile=[0]*(n+1)
        def go(cols,rows):
            l=len(cols);profile[l]+=1
            if l==n:found.add(tuple(cols));return
            candidates=mw
            if restricted:
                admissible=[{w[l] for w in nw if w.startswith(rows[i])} for i in range(m)]
                k=min(range(m),key=lambda i:sum(w[i] in admissible[i] for w in mw))
                candidates=[w for w in mw if w[k] in admissible[k]]
            for w in candidates:
                nextrows=[rows[i]+w[i] for i in range(m)]
                if all(s in prefixes[l+1] for s in nextrows):go(cols+[w],nextrows)
        go([],['']*m);results.append(found);profiles.append(profile)
    mp=[{w[:i] for w in mw} for i in range(m+1)]
    found=set();profile=[0]*(n+1);grid=[['']*n for _ in range(m)]
    letters=sorted(set(''.join(mw+nw)))
    def cell(l):
        i,j=l%m,l//m
        if i==0:profile[j]+=1
        if l==m*n:found.add(tuple(transpose([''.join(r) for r in grid])));return
        for c in letters:
            grid[i][j]=c
            row=''.join(grid[i][:j+1]);col=''.join(grid[k][j] for k in range(i+1))
            if row in prefixes[j+1] and col in mp[i+1]:cell(l+1)
        grid[i][j]=''
    cell(0);results.append(found);profiles.append(profile)
    assert all(s==expected for s in results)
    assert profiles[0]==profiles[1]==profiles[2]
    return len(expected)


def main():
    OUT.mkdir(exist_ok=True)
    rng=random.Random(722233);random_counts=[]
    for _ in range(100):
        m,n=rng.randrange(2,5),rng.randrange(2,5)
        u=[''.join(x) for x in product('ab',repeat=m)]
        v=[''.join(x) for x in product('ab',repeat=n)]
        mw=rng.sample(u,rng.randrange(1,min(9,len(u))+1));nw=rng.sample(v,rng.randrange(1,min(9,len(v))+1))
        random_counts.append(small_models(mw,nw))
    words5=dictionary(5);words6=dictionary(6);sets={n:set(dictionary(n)) for n in range(2,13)}
    ranks={n:{w:i+1 for i,w in enumerate(dictionary(n))} for n in range(2,13)}
    expected=[101,1004,4002,8887,15727,23958,29718,29130,22314,16161,11412]
    assert [len(dictionary(n,True)) for n in range(2,13)]==expected
    assert len(words5)==5757 and len(set(words5))==5757
    assert 5757**6==36406369848837732146649 and 5757**3==190804533093
    base='status lowest utopia making sledge'.split()
    def rectangle(rows):
        m,n=len(rows),len(rows[0]);assert all(len(w)==n for w in rows)
        assert set(rows)<=sets[n] and set(transpose(rows))<=sets[m],rows
        return {'rows':rows,'columns':transpose(rows)}
    assert [ranks[5][w] for w in transpose(base)]==[1446,185,1021,2537,66,255]
    witnesses=[rectangle(base)]
    for replacement in ['sluff','slump','slurs','slurp','sluts']:
        columns=transpose(base);columns[0]=replacement;witnesses.append(rectangle(transpose(columns)))
    columns=transpose(base);columns[:2]=['slams','tonal'];witnesses.append(rectangle(transpose(columns)))
    for s in ['smashes partial immense emerged sadness',
              'grandest renounce episodes basement eyesores',
              'pastelist accidence mortgagor proreform andesytes',
              'varistors agentival coelomate undeleted oysterers',
              'access moolah immune needed otters',
              'assert jailer uglify geodes assert',
              'begged realer artery wienie lesser',
              'magmas online dioxin assess lessee',
              'trades revise otiose trades honest',
              'blast lunch anger scene three','weeks event eerie knife steel',
              'trade ruled along dense edges','safer agile fixes elect rests',
              'admit drone moves inept tests','yards apart radii drill still',
              'class light agree sheep steps','glass light agree sheep steps',
              'grass right agree sheep steps','grass light agree sheep steps',
              'scabs canal angle baled sleds']:
        witnesses.append(rectangle(s.split()))
    nodes,prefix=trie(words6)
    assert len(nodes)==23667
    st=[nodes[prefix['st']].get(c,0) for c in 'abcdefghijklmnopqrstuvwxyz']
    corne=[nodes[prefix['corne']].get(c,0) for c in 'abcdefghijklmnopqrstuvwxyz']
    # Numeric node labels depend on insertion order. The current author archive
    # also differs from the book's five CORNE word ranks; retain the discrepancy
    # explicitly instead of treating the archived order as the book's order.
    published_st=[484,0,0,0,1589,0,0,0,2609,0,0,0,0,0,1280,0,0,251,0,0,563,0,0,0,1621,0]
    corne_labels=dict(zip('adlrt',[3879,3878,9602,171,5013]))
    published_corne=[corne_labels.get(c,0) for c in 'abcdefghijklmnopqrstuvwxyz']
    assert [bool(v) for v in st]==[bool(v) for v in published_st]
    assert [bool(v) for v in corne]==[bool(v) for v in published_corne]
    signature=sum(1<<(ord(c)-97) for c in nodes[prefix['st']]);assert signature==int('1124111',16)
    row_prefixes=['st','lo','ut','ma','sl']
    allowed=[set(nodes[prefix[p]]) for p in row_prefixes]
    expected_allowed=[set('aeioruy'),set('abcdefghijklmnopqrstuvwxyz')-set('ehjkyz'),set('emot'),set('abcdefghijklmnopqrstuvwxyz')-set('abo'),set('aeiouy')]
    assert allowed==expected_allowed
    legal=[w for w in words5 if all(c in s for c,s in zip(w,allowed))]
    # F084: the printed 221 should be 62. Three separate formulations agree.
    assert len(legal)==62
    pattern_sets=[{w for w in words5 if w[i] in allowed[i]} for i in range(5)]
    assert set.intersection(*pattern_sets)==set(legal)
    prefixes3={w[:3] for w in words6}
    semantic=[w for w in words5 if all(p+c in prefixes3 for p,c in zip(row_prefixes,w))]
    assert semantic==legal
    sizes=[sum(w[i] in allowed[i] for w in words5) for i in range(5)]
    assert sizes==[997,4722,1370,5057,1646]
    split=Counter(w[0] for w in words5)
    assert [split[c] for c in 'aeioruy']==[296,129,74,108,268,75,47]
    trie_sizes=[]
    for n in [5,6]:
        for reverse in [False,True]:
            w=[s[::-1] if reverse else s for s in dictionary(n)]
            t,_=trie(w);entries=sum(len(s)+1 for s in t)
            assert entries==2*len(t)-1+len(w)
            trie_sizes.append({'word_length':n,'reversed':reverse,'uncompressed_nodes':len(t),'compressed_entries':entries})
    assert [(x['uncompressed_nodes'],x['compressed_entries']) for x in trie_sizes]==[(6347,18450),(5188,16132),(23667,63060),(20169,56064)]
    palindromes=[w for w in words5 if w==w[::-1]];assert len(palindromes)==18
    squares=[json.loads(x) for x in (OUT/'squares.jsonl').read_text().splitlines()]
    for result in squares:
        vocab=Path(result['file']).read_text().splitlines();vset=set(vocab);rank={w:i+1 for i,w in enumerate(vocab)}
        for key in ['best_square','diagonal_best_square']:
            rows=result[key]
            if rows:
                assert rows==transpose(rows) and set(rows)<=vset
        for rows in result['small_squares']+result['diagonal_squares']:
            assert rows==transpose(rows) and set(rows)<=vset
        if result['best_square']:assert max(rank[w] for w in result['best_square'])==result['minimax_rank']
    # A second row-prefix implementation for all symmetric SGB squares uses
    # only required row prefixes, with no future-column pruning as in C++.
    prefixes=defaultdict(list)
    for w in words5:
        for i in range(5):prefixes[w[:i]].append(w)
    python_count=0
    def square(rows):
        nonlocal python_count
        k=len(rows)
        if k==5:python_count+=1;return
        p=''.join(w[k] for w in rows)
        for w in prefixes[p]:square(rows+[w])
    square([]);assert python_count==541968
    result={'verified':True,'random_models':100,'random_solution_counts':random_counts,
            'printed_witnesses':witnesses,'trie_ST':st,'trie_CORNE':corne,
            'ordering_discrepancy':{'published_ST_node':260,'archive_ST_node':prefix['st'],
                'published_CORNE_node':580,'archive_CORNE_node':prefix['corne'],
                'published_CORNE_entries':published_corne,'archive_CORNE_entries':corne},
            'allowed_after_slums_total':[''.join(sorted(s)) for s in allowed],
            'matching_words':len(legal),'matching_word_list':legal,'candidate_sublist_sizes':sizes,
            'trie_sizes':trie_sizes,'palindromes':palindromes,
            'independent_python_symmetric_SGB_count':python_count}
    (OUT/'basic-verified.json').write_text(json.dumps(result,indent=2)+'\n')
    print('100 random models, all witnesses, trie figures and independent SGB square count verified.')


if __name__=='__main__':main()
