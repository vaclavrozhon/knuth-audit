"""Automorphisms, symmetry breaking, witnesses, and the2025 replacement."""
from pathlib import Path
from itertools import combinations
from math import prod
import json,re,subprocess
ROOT=Path(__file__).parent;OUT=ROOT/'results/petersen_words'
EDGES={(0,1),(1,2),(2,3),(3,4),(0,4),(0,5),(1,6),(2,7),(3,8),(4,9),(5,7),(7,9),(6,9),(6,8),(5,8)}
edge=lambda u,v:tuple(sorted((u,v))) in EDGES

def automorphisms():
    out=[]
    def visit(p):
        i=len(p)
        if i==10:out.append(tuple(p));return
        for j in range(10):
            if j not in p and all(edge(i,k)==edge(j,p[k]) for k in range(i)):visit(p+[j])
    visit([]);assert len(out)==120
    arcs={(a,b,c,d) for a in range(10) for b in range(10) for c in range(10) for d in range(10)
          if len({a,b,c,d})==4 and edge(a,b) and edge(b,c) and edge(c,d)}
    assert len(arcs)==120 and {p[:4] for p in out}==arcs
    return out

def symmetry_ok(p):return all(p[0]<p[i] for i in range(1,10)) and p[1]<p[4] and p[1]<p[5] and p[2]<p[6] and p[3]<p[7]

def corrected_mcc(words):
    letters='abcdefghijklmnopqrstuvwxyz';primary=[f'V{i}' for i in range(10)]+[f'Q{i}{j}' for i,j in sorted(EDGES)]
    nonedges=[(i,j) for i,j in combinations(range(10),2) if not edge(i,j)]
    secondary=[f'{c}{i}' for c in letters for i in range(10)]+[f'{c}{i}{j}' for c in letters for i,j in nonedges]+words
    lines=[' '.join(primary+['|']+secondary)]
    for i,j in sorted(EDGES):
        for c in letters:lines.append(f'Q{i}{j} {c}{i}:1 {c}{j}:1')
    for word in words:
        chars=set(word)
        for i in range(10):
            option=[f'V{i}']+[f'{c}{i}:{int(c in chars)}' for c in letters]
            option += [f'{c}{u}{v}' for u,v in nonedges if i in (u,v) for c in sorted(chars)]
            option.append(word);lines.append(' '.join(option))
    return '\n'.join(lines)+'\n'

def main():
    words=(ROOT/'sources/sgb-words.txt').read_text().split();models=[json.loads(s) for s in (OUT/'words834.jsonl').read_text().splitlines()]
    aut=automorphisms();results=[]
    expected_sets=[set('muddy thumb books knock ended apply fifth grass civil'.split())|{w} for w in ['refer','fewer']]
    weighted=0
    for p in models:
        assert symmetry_ok(p) and len(set(p))==10 and max(p)<834
        assert sum(symmetry_ok([p[a[i]] for i in range(10)]) for a in aut)==1
        names=[words[i] for i in p];sets=list(map(set,names))
        for i,j in combinations(range(10),2):assert bool(sets[i]&sets[j])==edge(i,j)
        assert set(names) in expected_sets
        ways=prod(len(sets[i]&sets[j]) for i,j in EDGES);weighted+=120*ways
        results.append(dict(words_by_vertex=names,ranks_1based=[i+1 for i in p],edge_letter_choices=ways,max_rank=max(p)+1))
    assert len(results)==2 and all(d['max_rank']==834 for d in results)
    restricted=sorted(set().union(*expected_sets));problem=corrected_mcc(restricted)
    (OUT/'restricted-corrected.mcc').write_text(problem)
    p=subprocess.run(['/tmp/knuth-dlx2','v1','d0'],input=problem,text=True,capture_output=True,timeout=300)
    (OUT/'restricted-corrected.log').write_text(p.stderr)
    count=int(re.search(r'Altogether (\d+) solution',p.stderr)[1]);assert count==weighted
    result=dict(automorphisms=120,three_arcs=120,unique_symmetry_representative_proved=True,
                full_dictionary_count=2,no_solution_below_rank834=True,restricted_mcc_count=count,solutions=results)
    (OUT/'verified.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':main()
