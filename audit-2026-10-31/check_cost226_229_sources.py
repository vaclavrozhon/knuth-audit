"""Check printed Langford examples and the small remaining-prefix claim once."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import json,re,time,hashlib,os
import verify_f077

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/cost226_229'
def read(p):return json.loads((ROOT/p).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def seq(s):return tuple(map(int,s.split()))
def valid(a):
    n=len(a)//2
    assert sorted(a)==sorted(list(range(1,n+1))*2)
    for i in range(1,n+1):
        p=[j for j,v in enumerate(a) if v==i];assert p[1]-p[0]==i+1
def costs(a):return tuple(sum((j+1)*v for j,v in enumerate(a)) if z==0 else sum((j+1)**2*v for j,v in enumerate(a)) if z==1 else sum((j+1)*v*v for j,v in enumerate(a)) for z in range(3))


def main():
    start=time.monotonic();assert not (OUT/'source-checked.json').exists()
    a106=seq('2 3 4 2 1 3 1 4 16 13 15 5 14 7 9 6 11 5 12 10 8 7 6 13 9 16 15 14 11 8 10 12')
    a107=seq('12 10 8 11 14 15 16 9 13 6 7 8 10 12 5 11 6 9 7 14 5 15 13 16 4 1 3 1 2 4 3 2')
    a108=verify_f077.PRINTED
    p8=seq('2 8 6 2 3 5 7 4 3 6 8 5 4 1 7 1')
    q8=seq('3 5 7 4 3 8 6 5 4 1 7 1 2 6 8 2')
    p11=seq('1 5 1 7 4 8 9 5 11 4 10 7 6 3 8 2 9 3 2 6 11 10')
    q11=seq('1 4 1 6 7 10 4 5 9 11 6 8 7 5 2 3 10 2 9 3 8 11')
    minimum=seq('1 2 1 3 2 4 8 3 12 13 4 10 14 15 16 8 9 6 11 5 7 12 10 13 6 5 9 14 7 15 11 16')
    examples={'106':a106,'107':a107,'108':a108,'228_n8_a':p8,'228_n8_b':q8,'228_n11_a':p11,'228_n11_b':q11,'229_minimum':minimum}
    source_groups=[(['106','107'],'sources/preprocess218_224/original-131.txt','sources/preprocess218_224/draft-53.txt'),
        (['108'],'sources/cost226_229/original-132.txt','sources/cost226_229/draft-54.txt'),
        (['228_n8_a','228_n8_b','228_n11_a','228_n11_b'],'sources/preprocess218_224/original-495.txt','sources/preprocess218_224/draft-185.txt'),
        (['229_minimum'],'sources/cost226_229/original-496.txt','sources/cost226_229/draft-186.txt')]
    source_hashes={}
    for names,*paths in source_groups:
        for path in paths:
            text=(ROOT/path).read_text();source_hashes[path]=sha(ROOT/path)
            for name in names:assert re.search(r'\b'+r'\s+'.join(map(str,examples[name]))+r'\b',text),(name,path)
    for a in examples.values():valid(a)
    assert a106[::-1]==a107 and costs(a107)[:2]==(3708,68880)
    assert costs(a108)==(3708,68880,37552)
    assert costs(p8)[0]==costs(q8)[0] and costs(p8)[1]!=costs(q8)[1]
    assert costs(p11)[1]==costs(q11)[1] and costs(p11)[0]!=costs(q11)[0]
    assert costs(minimum)==(5240,119192,60324)
    basics=read('results/langford_costs/basics.json');accepted=read('results/langford_costs/verified.json');sat=read('results/langford_costs/sat-lex.json')
    assert minimum==tuple(basics['lexmin'])==tuple(sat['extrema'][0]['sequence'])
    assert verify_f077.LARGER==tuple(basics['lexmax'])==tuple(sat['extrema'][1]['sequence'])
    assert accepted['first_two_optimal_sets_identical'] and [q['optimum'] for q in accepted['results']]==[3708,68880,37552]
    # These models have already been validated. Only count their price labels for a new K claim.
    raw=(ROOT/'results/langford_costs/sum1.out').read_text()
    prices=Counter(map(int,re.findall(r'^\d+: \(total cost \$(\d+)\)',raw,re.M)))
    assert sum(prices.values())==81206 and prices[3708]==12016 and prices[3720]>=484
    assert 12500-12016==484
    # A genuinely new short enumeration: only the suffix after the first eight fixed options.
    filled=[0]*32;used=set();fixed=[]
    for pos,v in enumerate(minimum):
        if filled[pos]:continue
        assert v not in used and not filled[pos+v+1]
        filled[pos]=filled[pos+v+1]=v;used.add(v);fixed.append((v,pos+1,pos+v+2))
        if len(fixed)==8:break
    nodes=0;models=[]
    def dfs():
        nonlocal nodes
        nodes+=1;assert time.monotonic()-start<10
        if 0 not in filled:models.append(tuple(filled));return
        j=filled.index(0)
        for i in range(1,17):
            k=j+i+1
            if i in used or k>=32 or filled[k]:continue
            used.add(i);filled[j]=filled[k]=i;dfs();filled[j]=filled[k]=0;used.remove(i)
    dfs();assert len(models)==len(set(models))==12 and min(models)==minimum
    for a in models:valid(a)
    witness=verify_f077.verify()
    (OUT/'f077-witness.json').write_text(json.dumps(witness,indent=2)+'\n')
    dependencies=['verify_f077.py','check_langford_costs.py','verify_langford_costs.py','verify_langford_lex.py']
    data=['results/langford_costs/basics.json','results/langford_costs/verified.json','results/langford_costs/sat-lex.json','results/langford_costs/sum1.out']
    (OUT/'source-checked.json').write_text(json.dumps(dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),nice=os.nice(0),wall_seconds=time.monotonic()-start,
        source_hashes=source_hashes,dependencies={p:sha(ROOT/p) for p in dependencies},accepted_data_hashes={p:sha(ROOT/p) for p in data},
        printed_values_per_version=sum(map(len,examples.values())),printed_examples={k:dict(sequence=v,costs=costs(v)) for k,v in examples.items()},
        known_validated_price3720_witnesses=prices[3720],new_prefix_check=dict(fixed_options=fixed,search_nodes=nodes,models=models,count=12),
        old_censuses_repeated=0,old_model_validation_repeated=False,old_optimum_searches_repeated=0,new_full_n16_searches=0,
        remaining_expensive_scope=['Full653443600 census','Global upper bound120360 and exact reversedSigma2 maximizing set; the20s new feasibility attempt timed out, not a proof.','Historical algorithm cost benchmarks']),indent=2)+'\n')
    print('PASS:204 printed values/version, four exception examples, old optima reused,6525 known next-price witnesses,12 suffix completions;',nodes,'new small nodes')


if __name__=='__main__':main()
