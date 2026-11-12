"""Full small solution sets, printed examples, and the answer92 index defect."""
import hashlib,json,random,subprocess,time
from itertools import permutations,product
from pathlib import Path
from colored_dlx import ColoredDLX
from double_word_tools import dictionary,input_text
from three_way_stairs import *

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/three_way_stairs'


class DiscardEvents(list):
    def append(self,event):pass


def xcc(enc):
    solver=ColoredDLX(len(enc['names']),enc['primary'],enc['rows']);solver.events=DiscardEvents();solver.solve()
    p=enc['primary']//3;result=set()
    for model in solver.solutions:
        rows=[None]*p
        for ri in model:
            slot,rank=enc['info'][ri]
            if slot<p:rows[slot]=enc['words'][rank]
        result.add(tuple(rows))
    return result


def main():
    OUT.mkdir(exist_ok=True);started=time.monotonic();rng=random.Random(929326);cases=[]
    for kind in ['two-way','diagonal']:
        for n in [2,3,4]:
            universe=[''.join(w) for w in product('ABC',repeat=n)]
            for p in [1,2,3,4]:
                words=rng.sample(universe,min(len(universe),max(5,3*p)))
                cases.append((kind,p,words))
                if (kind=='diagonal' and p<3) or (kind=='two-way' and p<2):continue
                for _ in range(3000):
                    seed=rng.sample(universe,p);formed=all_words(seed,kind)
                    if len(set(formed))==3*p:
                        cases.append((kind,p,sorted(set(formed))));break
    cases += [('two-way',3,sorted(set(all_words('AA BC CB'.split(),'two-way')))),
              ('two-way',3,sorted(set(all_words('WAVES LINED LEPER'.split(),'two-way'))))]
    checks=[]
    for kind,p,words in cases:
        expected=set()
        allowed=set(words)
        for rows in permutations(words,p):
            formed=all_words(rows,kind)
            if len(set(formed))==3*p and all(w in allowed for w in formed):expected.add(rows)
        actual=xcc(encoding(words,p,kind));assert actual==expected,(kind,p,words,actual,expected)
        csp=ThreeWayCSP(words,p,kind,symmetry=False);assert set(csp.solve())==expected
        symmetric=ThreeWayCSP(words,p,kind,symmetry=True).solve()
        assert set(symmetric)=={r for r in expected if r[0]==min(r,key=words.index)}
        checks.append(dict(kind=kind,n=len(words[0]),p=p,W=len(words),models=len(actual),csp_nodes=csp.nodes))
    words=dictionary(5);examples=[]
    for kind,table in [('two-way',TWO_WAY),('diagonal',DIAGONAL)]:
        for p,text in table.items():
            rows=text.split();assert len(rows)==p;threshold=validate(rows,words,kind)
            for shift in range(p):validate(rows[shift:]+rows[:shift],words,kind)
            if kind=='diagonal':
                for shift in range(p):
                    reflected=list(reversed(rows));validate(reflected[shift:]+reflected[:shift],words,kind)
            examples.append(dict(kind=kind,p=p,rank=threshold,rows=rows,all_words=all_words(rows,kind)))
    illustrations=[]
    for kind,text in [('two-way','RAPID RATED LACES ROBES'),('diagonal','SLANT FLUNK BLINK')]:
        rows=text.split();illustrations.append(dict(kind=kind,rows=rows,rank=validate(rows,words,kind),all_words=all_words(rows,kind)))
    historical=all_words('TINE SALE MALE VINE'.split(),'diagonal');assert len(set(historical))==12
    build=json.loads((ROOT/'results/colored_basics/native/build.json').read_text());binary=build['binaries']['original']['binary']
    assert hashlib.sha256(Path(binary).read_bytes()).hexdigest()==build['binaries']['original']['sha256']
    counter=[]
    for label,text in [('tiny','AA BC CB'),('printed','WAVES LINED LEPER')]:
        across=text.split();local=sorted(all_words(across,'two-way'))
        for wrong in [False,True]:
            enc=encoding(local,3,'two-way',printed92=wrong)
            keep=[i for i,(slot,rank) in enumerate(enc['info']) if slot>=3 or local[rank]==across[slot]]
            enc['rows']=[enc['rows'][i] for i in keep];enc['info']=[enc['info'][i] for i in keep]
            expected=set() if wrong else {tuple(across)};assert xcc(enc)==expected
            prefix=OUT/(label+('-printed-formula' if wrong else '-corrected-formula'))
            inp=prefix.with_suffix('.dlx');inp.write_text(input_text(enc))
            run=subprocess.run([binary,'v129','m1'],input=inp.read_bytes(),capture_output=True,check=True,timeout=30)
            prefix.with_suffix('.out').write_bytes(run.stdout);prefix.with_suffix('.log').write_bytes(run.stderr)
            assert ('Altogether '+str(len(expected))+' solution') in run.stderr.decode()
            counter.append(dict(example=label,printed_formula=wrong,models=len(expected),input_sha256=hashlib.sha256(inp.read_bytes()).hexdigest(),native_returncode=run.returncode))
    result=dict(checks=checks,comparisons=len(checks),total_small_models=sum(c['models'] for c in checks),examples=examples,
                illustrations=illustrations,historical_example=historical,counterexamples=counter,
                native_binary_sha256=build['binaries']['original']['sha256'],
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),seconds=time.monotonic()-started)
    (OUT/'checked.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(comparisons=len(checks),models=result['total_small_models'],
         thresholds=[(r['kind'],r['p'],r['rank']) for r in examples],counterexamples=counter,seconds=result['seconds'])))


if __name__=='__main__':main()
