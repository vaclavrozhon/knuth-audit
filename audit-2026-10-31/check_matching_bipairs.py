"""Exercise 215: direct set search versus original DLX2 profiles."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json, subprocess, random, re

ROOT=Path(__file__).parent
OUT=ROOT/'results/matching_bipairs'
OUT.mkdir(exist_ok=True)

def instance(q,mode,seed=0):
    edges=list(combinations(range(2*q+1),2))
    if mode in ('clever','clever_small'):
        first=[(i,2*q+1-i) for i in range(1,q+1)]
        edges=first+[e for e in edges if e not in first]
    if mode=='prefix':
        first=[(1,2),(1,3),(2,3)]
        edges=first+[e for e in edges if e not in first]
    if mode=='random':random.Random(seed).shuffle(edges)
    rank={e:i for i,e in enumerate(edges)}
    forbidden=set()
    for a,b,c,d in combinations(range(2*q+1),4):
        matchings=[((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c))]
        favorite=min(range(3),key=lambda j:min(rank[e] for e in matchings[j]))
        for j,m in enumerate(matchings):
            if j==favorite:continue
            if mode=='lex_small' and not (a%2==0 and b==a+1):continue
            if mode=='clever_small':
                if a!=0:continue
                k=m[0][1]
                if 2*q+1-k not in m[1]:continue
            forbidden.add(tuple(sorted(rank[e] for e in m)))
    return edges,forbidden

def direct(q,edges,forbidden):
    bad=[set([j]) for j in range(len(edges))]
    masks=[(1<<a)|(1<<b) for a,b in edges]
    for a,b in forbidden:bad[a].add(b);bad[b].add(a)
    profile=Counter()
    def visit(items,available,level):
        profile[level]+=1
        if not items:raise AssertionError('Odd graph cannot have a perfect matching')
        rows=[tuple(j for j in available if masks[j]>>i&1) for i in range(2*q+1) if items>>i&1]
        column=min(rows,key=len)
        for j in column:
            visit(items^masks[j],tuple(k for k in available if not masks[k]&masks[j] and k not in bad[j]),level+1)
    visit((1<<(2*q+1))-1,tuple(range(len(edges))),0)
    return [profile[i] for i in range(max(profile)+1)]

def original(q,edges,forbidden,name):
    secondary=[[] for _ in edges]
    for k,(a,b) in enumerate(sorted(forbidden)):
        secondary[a].append('b'+str(k));secondary[b].append('b'+str(k))
    data=' '.join(map(str,range(2*q+1)))+' | '+' '.join('b'+str(k) for k in range(len(forbidden)))+'\n'
    data+='\n'.join(' '.join([str(a),str(b)]+secondary[j]) for j,(a,b) in enumerate(edges))+'\n'
    (OUT/(name+'.xcc')).write_text(data)
    p=subprocess.run(['/tmp/knuth-dlx2','v129','d0'],input=data,text=True,capture_output=True,timeout=60)
    (OUT/(name+'.log')).write_text(p.stdout+p.stderr)
    assert 'Altogether 0 solution' in p.stderr
    part=p.stderr.split('Profile:')[-1]
    profile=[int(n) for n in re.findall(r'^\s*\d+:\s*(\d+)\s*$',part,re.M)]
    return profile

def main():
    cases=[]
    for q in range(1,11):
        expected=[1]+list(range(2*q,0,-2))
        for mode in ['lex','lex_small','clever','clever_small']:
            edges,forbidden=instance(q,mode)
            p=direct(q,edges,forbidden)
            n=original(q,edges,forbidden,f'q{q}-{mode}')
            assert p==n,(q,mode,p,n)
            assert p==(expected if mode.startswith('lex') else [1,2*q])
            if mode=='lex_small':assert len(forbidden)==q*(q-1)*(4*q+1)//3
            if mode=='clever_small':assert len(forbidden)==2*q*(2*q-2)
            cases.append(dict(q=q,mode=mode,excluded=len(forbidden),profile=p,nodes=sum(p)))
    (OUT/'native.json').write_text(json.dumps(cases,indent=2)+'\n')
    samples=[]
    for q in range(2,7):
        worst=[1]+list(range(2*q,0,-2))
        for seed in range(100):
            edges,forbidden=instance(q,'random',seed)
            p=direct(q,edges,forbidden)
            exceeds=any(n>worst[i] for i,n in enumerate(p))
            samples.append(dict(q=q,seed=seed,profile=p,exceeds_levelwise=exceeds,exceeds_total=sum(p)>sum(worst)))
    e,f=instance(3,'prefix')
    assert direct(3,e,f)==original(3,e,f,'counter-prefix')==[1,6,2,4]
    result=dict(native_cases=cases,random_samples=samples)
    (OUT/'verified.json').write_text(json.dumps(result,indent=2)+'\n')
    print('40 native profiles agree; random levelwise counterexamples:',sum(x['exceeds_levelwise'] for x in samples),'; total counterexamples:',sum(x['exceeds_total'] for x in samples))

if __name__=='__main__':main()
