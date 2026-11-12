"""Literal answer430(d) encoding, run with the author's unmodified DLX2."""
from collections import defaultdict
from itertools import combinations
from pathlib import Path
import json,re,subprocess
ROOT=Path(__file__).parent;OUT=ROOT/'results/kakuro'


def encode(rows,cols,positions):
    n=len(rows);length_r=[sum(r==i for r,c in positions) for i in range(n)]
    length_c=[sum(c==j for r,c in positions) for j in range(n)]
    def choices(k,s):
        return sorted([x for x in combinations(range(1,10),k) if sum(x)==s],key=lambda x:sum(1<<v for v in x))
    hs=[choices(length_r[r],rows[r]) for r in range(n)]
    vs=[choices(length_c[c],cols[c]) for c in range(n)]
    prim=[f'{r}{c}' for r,c in positions]
    for direction,blocks in [('H',hs),('V',vs)]:
        for b,cs in enumerate(blocks):
            for p,cs_ in enumerate(cs):
                prim.extend(f'{direction}{b}{p:x}{x}' for x in cs_)
    second=[f'H{r}' for r in range(n)]+[f'V{c}' for c in range(n)]
    lines=[' '.join(prim)+' | '+' '.join(second)]
    for r,c in positions:
        for p,rs in enumerate(hs[r]):
            for q,cs in enumerate(vs[c]):
                for x in sorted(set(rs)&set(cs)):
                    lines.append(f'{r}{c} H{r}{p:x}{x} H{r}:{chr(97+p)} V{c}{q:x}{x} V{c}:{chr(97+q)}')
    for direction,blocks in [('H',hs),('V',vs)]:
        for b,cs in enumerate(blocks):
            for p,cs_ in enumerate(cs):
                for other in range(len(cs)):
                    if p==other:continue
                    lines.append(' '.join(f'{direction}{b}{p:x}{x}' for x in cs_)+f' {direction}{b}:{chr(97+other)}')
    return '\n'.join(lines)+'\n'


def run(label,rows,cols,positions):
    text=encode(rows,cols,positions);path=OUT/(label+'.dlx');path.write_text(text)
    p=subprocess.run(['/tmp/knuth-dlx2','v1','d0','m1'],input=text,text=True,capture_output=True,timeout=30)
    (OUT/(label+'.stdout')).write_text(p.stdout);(OUT/(label+'.stderr')).write_text(p.stderr)
    match=re.search(r'Altogether (\d+) solution.*? (\d+) nodes',p.stderr)
    assert match,p.stderr
    result=dict(label=label,rows=rows,columns=cols,solutions=int(match.group(1)),nodes=int(match.group(2)),
                returncode=p.returncode)
    print(json.dumps(result),flush=True);return result


def main():
    small=[(r,c) for r in range(3) for c in range(3) if (r,c) not in [(0,2),(2,0)]]
    cases=[('hard-printed',[6,19,6],[8,11,10]),('hard-repaired',[6,19,6],[8,13,10]),
           ('hard-other-repair',[6,19,4],[8,11,10]),('easy1',[4,15,12],[12,15,4]),
           ('easy2',[4,15,16],[12,15,8]),('example430',[5,19,6],[6,10,14])]
    results=[run(label,r,c,small) for label,r,c in cases]
    results.append(run('square4-example',[11,15,23,29],[12,15,23,28],[(r,c) for r in range(4) for c in range(4)]))
    (OUT/'author-dlx2-results.json').write_text(json.dumps(results,indent=2)+'\n')

if __name__=='__main__':main()
