"""Exact finite certificates for exercises3.5-35--37,39."""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations, product, combinations
from collections import Counter
import argparse,json
P=Path(__file__).resolve().parent;OUT=P/'results/selection-extensions.json'
ap=argparse.ArgumentParser();ap.add_argument('--resume',action='store_true');args=ap.parse_args()
r=json.loads(OUT.read_text()) if args.resume and OUT.exists() else {}
def save():OUT.write_text(json.dumps(r,indent=2)+'\n')
if 'loveland' not in r:
    examples=[]
    for first in [(0,1,2),(1,0,2)]:
        a=first[0];states=[a]
        for _ in range(5):a=max(first[j] if j<len(first) else j for j in range(2**a));states.append(a)
        assert len(set(states))==1
        examples.append(dict(prefix=first,printed_boundaries=states))
    histories=checks=0
    for perm in permutations(range(7)):
        def s(j):return perm[j] if j<7 else j
        a=2;chosen=set()
        for stage in range(2):
            K=2**a;target={s(j) for j in range(K)};b=max(target)
            assert b>a
            chosen|={j for j in target if a<=j<b}
            assert chosen<=target
            assert len(target-chosen)<=a+1
            assert len(chosen)>=K-a-1
            checks+=1;a=b
        histories+=1
    r['loveland']=dict(C0066=examples,permutation_histories=histories,stage_set_checks=checks)
    save();print('PASS Loveland repaired selection sets',histories,checks,flush=True)
if 'bit_lifting' not in r:
    cells=0;strict_one_cell_bound_counterexample=None
    for k in range(1,9):
        M=2**k
        for b in range(2,33):
            for a in range(b):
                left=F(a,b);right=F(a+1,b)
                low=sum(left<=F(j,M) and F(j+1,M)<=right for j in range(M))
                high=sum(F(j,M)<right and F(j+1,M)>left for j in range(M))
                assert F(low,M)<=F(1,b)<=F(high,M)
                assert F(1,b)-F(low,M)<F(2,M) and F(high,M)-F(1,b)<F(2,M)
                if (b,k,a)==(3,3,1):
                    strict_one_cell_bound_counterexample=dict(b=b,k=k,a=a,outer_mass=str(F(high,M)),true_mass=str(F(1,b)),difference=str(F(high,M)-F(1,b)))
                    assert F(high,M)-F(1,b)>F(1,M)
                cells+=1
    r['bit_lifting']=dict(interval_cells=cells,safe_error='2/2^k',fixed_precision_bracket_example=strict_one_cell_bound_counterexample,note='This tests the proof bracket only, not a counterexample to the full R6 theorem or its final exact frequencies.')
    save();print('PASS binary lifting interval bounds',cells,flush=True)
if 'coppersmith' not in r:
    cases=0;rows=[]
    for n in range(2,6):
        width=2*n-1;words=[]
        for bits in product((0,1),repeat=width-1):
            delta=sum(v==0 for v in bits)%2
            words.append(bits+(delta,))
        assert all(sum(w)%2==0 for w in words)
        for size in range(1,width):
            for chosen in combinations(range(width),size):
                c=Counter(tuple(w[j] for j in chosen) for w in words)
                assert len(c)==2**size and set(c.values())=={2**(width-1-size)}
                cases+=1
        rows.append(dict(n=n,coordinates=width,independent_up_to=width-1,even_parity_words=len(words)))
    r['coppersmith']=dict(proper_coordinate_sets=cases,rows=rows)
    save();print('PASS Coppersmith proper marginals',cases,flush=True)
if 'schmidt' not in r:
    count=0
    for a in product(range(-1,2),repeat=4):
        for b in product(range(-1,2),repeat=4):
            h=lambda x:max(x)-min(x)
            d=[y-x for x,y in zip(a,b)]
            cross=max(min(d[:2])-max(d[2:]),min(d[2:])-max(d[:2]))
            assert 2*(h(a)+h(b))>=2*cross+h(a[:2])+h(a[2:])+h(b[:2])+h(b[2:])
            count+=1
    # C0067 was dismissed on 2026-11-12: the original counts j <= n.
    # At n=0 choose u=(1+U_0)/2; the count is one, not zero.
    r['schmidt']=dict(oscillation_lemma_arrays=count,C0067=dict(status='dismissed',N=1,only_n=0,printed_count='j <= n',choose_u='(1+U_0)/2',left_side=1,right_side=0,strict_inequality=True),safe_c_standard_convention='1/200',source_c='1/100 with1<=n<=N')
    save();print('PASS Schmidt oscillation lemma',count,flush=True)
