"""Supplementary independent checks of the named examples and cancellation."""
from itertools import product,combinations
from pathlib import Path
import json
from check_traces import graphs,classes,predecessor_masks


def variants(word,clash):
    seen={word};queue=[word]
    for w in queue:
        for k in range(len(w)-1):
            if clash[w[k]]>>w[k+1]&1:continue
            new=w[:k]+(w[k+1],w[k])+w[k+2:]
            if new not in seen:seen.add(new);queue.append(new)
    return seen


def main():
    word=tuple(ord(c)-97 for c in 'bcebafdc');clash=[sum(1<<j for j in range(6) if abs(i-j)<=1) for i in range(6)]
    equivalent=variants(word,clash);assert len(equivalent)==105
    preds=predecessor_masks(word,clash)
    pyramids=[''.join(chr(a+97) for i,a in enumerate(word) if mask>>i&1) for mask in preds]
    assert pyramids==['b','bc','e','bcb','bcba','ef','bced','bcebdc']
    labels=[6,2,4,7,8,5,1,3];todo=(1<<8)-1;factors=[]
    for pos in sorted(range(8),key=labels.__getitem__):
        if todo>>pos&1:
            mask=todo&preds[pos];todo&=~mask
            factors.append(''.join(chr(a+97)+str(labels[i]) for i,a in enumerate(word) if mask>>i&1))
    assert factors==['b6c2e4d1','b7c3','f5','a8']
    words_checked=0;valid_cuts=0
    for m in range(1,4):
        for edges in range(1<<(m*m)):
            for n in range(1,6):
                for w in product(range(m),repeat=n):
                    inside=[bool(edges>>(m*a+b)&1) for a,b in zip(w,w[1:])]
                    cuts=[k for k in range(n+1) if all(inside[:max(0,k-1)]) and not any(inside[k:])]
                    assert len(cuts) in (0,2)
                    if cuts:assert cuts[1]==cuts[0]+1
                    assert sum((-1)**(n-k) for k in cuts)==0
                    words_checked+=1;valid_cuts+=len(cuts)
    orientations=0;graph_checks=0
    for m in range(1,5):
        for clash in graphs(m):
            oracle,reps=classes(m,m,clash)
            permutation_traces={oracle[w] for w in oracle if len(set(w))==m}
            edges=[(i,j) for i,j in combinations(range(m),2) if clash[i]>>j&1]
            acyclic=0
            for bits in range(1<<len(edges)):
                outgoing=[[] for _ in range(m)];indegree=[0]*m
                for k,(i,j) in enumerate(edges):
                    if bits>>k&1:i,j=j,i
                    outgoing[i].append(j);indegree[j]+=1
                queue=[i for i in range(m) if indegree[i]==0]
                for i in queue:
                    for j in outgoing[i]:
                        indegree[j]-=1
                        if not indegree[j]:queue.append(j)
                acyclic+=len(queue)==m;orientations+=1
            assert len(permutation_traces)==acyclic;graph_checks+=1
    report={'example_324_equivalent_strings':len(equivalent),'example_339_pyramids':pyramids,
            'example_339_labelled_factors':factors,
            'F036':'The printed middle factor b7 a8 c3 has two sinks, a8 and c3. The corrected factorization has four pyramids with top labels 1,3,5,8.',
            'noncommutative_identity_words':words_checked,
            'noncommutative_identity_valid_cuts':valid_cuts,'acyclic_orientation_graph_checks':graph_checks,
            'acyclic_orientations_and_cyclic_orientations_tested':orientations,
            'scope':'Examples 324 and 339, all directed graphs with loops on <=3 letters and words through length 5 for identity 333, all orientations of all graphs on <=4 vertices for 325.'}
    (Path(__file__).parent/'results/trace_examples.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
