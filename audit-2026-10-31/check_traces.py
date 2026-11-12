"""Independent adjacent-swap oracle for SAT trace arithmetic, 323-339."""
from itertools import combinations,product,permutations
from collections import defaultdict,Counter
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json


def graphs(m):
    pairs=list(combinations(range(m),2))
    for mask in range(1<<len(pairs)):
        clash=[1<<i for i in range(m)]
        for k,(i,j) in enumerate(pairs):
            if mask>>k&1:clash[i]|=1<<j;clash[j]|=1<<i
        yield clash


def classes(m,n,clash):
    """Union-find under all legal adjacent commutations. No heap code used."""
    words=list(product(range(m),repeat=n));index={w:i for i,w in enumerate(words)}
    parent=list(range(len(words)))
    def root(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    for i,w in enumerate(words):
        for k in range(n-1):
            if w[k]<=w[k+1] or clash[w[k]]>>w[k+1]&1:continue
            other=w[:k]+(w[k+1],w[k])+w[k+2:];a,b=root(i),root(index[other])
            if a!=b:parent[max(a,b)]=min(a,b)
    oracle={w:words[root(i)] for i,w in enumerate(words)}
    return oracle,sorted(set(oracle.values()))


def territories(clash):
    m=len(clash);out=[1<<i for i in range(m)];nextbit=m
    for i,j in combinations(range(m),2):
        if clash[i]>>j&1:out[i]|=1<<nextbit;out[j]|=1<<nextbit;nextbit+=1
    return out


def heap_from_word(word,clash):
    heights=[];levels=[]
    for i,a in enumerate(word):
        h=1+max((heights[j] for j,b in enumerate(word[:i]) if clash[a]>>b&1),default=-1)
        heights.append(h)
        if len(levels)<=h:levels.append(set())
        levels[h].add(a)
    return tuple(tuple(sorted(level)) for level in levels)


def heap_copy(h,T):return [set(level) for level in h],[sum(T[a] for a in level) for level in h]

def frozen(L):return tuple(tuple(sorted(level)) for level in L)

def multiply(alpha,beta,T):
    L,U=heap_copy(alpha,T)
    for level in beta:
        for b in level:
            j=len(L)
            while j>0 and not T[b]&U[j-1]:j-=1
            if j==len(L):L.append(set());U.append(0)
            L[j].add(b);U[j]+=T[b]
    return frozen(L)


def right_divide(alpha,beta,T):
    L,U=heap_copy(alpha,T)
    for level in reversed(beta):
        for b in level:
            if not L:return None
            j=len(L)-1
            while j>0 and not T[b]&U[j]:j-=1
            if b not in L[j]:return None
            L[j].remove(b);U[j]-=T[b]
            if not U[j]:
                assert j==len(L)-1
                L.pop();U.pop()
    return frozen(L)


def left_divide(alpha,beta,T):
    L,U=heap_copy(beta,T)
    for level in alpha:
        for a in level:
            if not L or a not in L[0]:return None
            L[0].remove(a);U[0]-=T[a]
            j=c=1
            while U[j-1]!=0 and c!=0:
                if j==len(L):break
                c=0;j+=1
                for b in sorted(L[j-1]):
                    if not T[b]&U[j-2]:
                        L[j-1].remove(b);L[j-2].add(b)
                        U[j-2]+=T[b];U[j-1]-=T[b];c=1
            if U[j-1]==0:L.pop(j-1);U.pop(j-1)
    return frozen(L)


def generate_T(m,n,clash):
    x=[-1]+[0]*n;out=[]
    while True:
        out.append(tuple(x[1:]));k=n
        while x[k]==m-1:k-=1
        if k==0:return out
        while True:
            x[k]+=1;j=k-1
            while j>0 and x[j]<x[k] and not clash[x[j]]>>x[k]&1:j-=1
            if not (x[j]>x[k] and not clash[x[j]]>>x[k]&1):break
        while k<n:
            k+=1;x[k]=0
            while x[k-1]>x[k] and not clash[x[k-1]]>>x[k]&1:x[k]+=1


def predecessor_masks(word,clash):
    out=[]
    for i,a in enumerate(word):
        mask=1<<i
        for j,b in enumerate(word[:i]):
            if clash[a]>>b&1:mask|=out[j]
        out.append(mask)
    return out


def sinks(word,clash):
    return [i for i,a in enumerate(word) if not any(clash[a]>>b&1 for b in word[i+1:])]


def independent_coeffs(clash,weights):
    coeffs=[0]*(len(clash)+1)
    for mask in range(1<<len(clash)):
        if any(mask>>i&1 and (clash[i]^(1<<i))&mask for i in range(len(clash))):continue
        value=(-1)**mask.bit_count()
        for i in range(len(clash)):
            if mask>>i&1:value*=weights[i]
        coeffs[mask.bit_count()]+=value
    return coeffs


def convolution(a,b,n):return [sum((a[k]*b[j-k] for k in range(j+1)),Q(0)) for j in range(n+1)]


def determinant_integer(A):
    """Bareiss exact elimination, including singular principal minors."""
    A=[row[:] for row in A];n=len(A);sign=1;oldpivot=1
    if not n:return 1
    for k in range(n-1):
        if not A[k][k]:
            row=next((j for j in range(k+1,n) if A[j][k]),None)
            if row is None:return 0
            A[k],A[row]=A[row],A[k];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value=A[i][j]*pivot-A[i][k]*A[k][j]
                assert value%oldpivot==0
                A[i][j]=value//oldpivot
            A[i][k]=0
        oldpivot=pivot
    return sign*A[-1][-1]


def main():
    word_checks=class_checks=generator_checks=product_checks=division_checks=weighted_gf_checks=0
    labelled_traces=labelled_distribution_checks=principal_minors=ordered_graphs=0
    all_oracles={}
    for m in range(1,5):
        for gi,clash in enumerate(graphs(m)):
            T=territories(clash);oracles=[];reps=[];heaps={}
            for n in range(6):
                oracle,representatives=classes(m,n,clash);oracles.append(oracle);reps.append(representatives)
                heap_ids={}
                for w,canonical in oracle.items():
                    h=heap_from_word(w,clash)
                    if h in heap_ids:assert heap_ids[h]==canonical
                    else:heap_ids[h]=canonical
                    heaps[w]=h;word_checks+=1
                assert len(heap_ids)==len(representatives);class_checks+=len(representatives)
                assert generate_T(m,n,clash)==representatives;generator_checks+=1
            maxlen=4 if m<=3 else 3
            traces=[w for row in reps[:maxlen+1] for w in row]
            right={};left={}
            for alpha in traces:
                for beta in traces:
                    if len(alpha)+len(beta)>maxlen:continue
                    w=oracles[len(alpha)+len(beta)][alpha+beta]
                    assert multiply(heaps[alpha],heaps[beta],T)==heaps[w]
                    right[w,beta]=alpha;left[alpha,w]=beta;product_checks+=1
            for alpha in traces:
                for beta in traces:
                    expect=right.get((alpha,beta))
                    assert right_divide(heaps[alpha],heaps[beta],T)==(heaps[expect] if expect is not None else None)
                    expect=left.get((alpha,beta))
                    assert left_divide(heaps[alpha],heaps[beta],T)==(heaps[expect] if expect is not None else None)
                    division_checks+=2
            for weights in ([1]*m,list(range(2,m+2))):
                coeffs=independent_coeffs(clash,weights);ts=[];ps=[]
                for n in range(6):
                    counts=[];pyramid=0
                    for w in reps[n]:
                        weight=1
                        for a in w:weight*=weights[a]
                        counts.append(weight)
                        if len(sinks(w,clash))==1:pyramid+=weight
                    ts.append(sum(counts));ps.append(pyramid)
                    if n:
                        assert ts[n]==-sum(coeffs[k]*ts[n-k] for k in range(1,min(m,n)+1))
                        assert ps[n]==-sum(k*coeffs[k]*ts[n-k] for k in range(1,min(m,n)+1))
                        weighted_gf_checks+=2
                if weights==[1]*m and m<=3:
                    for n in range(1,6):
                        observed=Counter()
                        for w in reps[n]:
                            pred=predecessor_masks(w,clash)
                            for labels in permutations(range(n)):
                                todo=(1<<n)-1;count=0
                                for pos in sorted(range(n),key=labels.__getitem__):
                                    if todo>>pos&1:todo&=~pred[pos];count+=1
                                assert not todo;observed[count]+=1;labelled_traces+=1
                        P=[Q(0)]+[Q(ps[k],k) for k in range(1,n+1)];power=[Q(1)]+[Q(0)]*n
                        for l in range(1,n+1):
                            power=convolution(power,P,n)
                            predicted=factorial(n)*power[n]/factorial(l)
                            assert observed[l]==predicted;labelled_distribution_checks+=1
    for m in range(1,6):
        for clash in graphs(m):
            if any(not (clash[a]>>b&1) and not (clash[b]>>c&1) and clash[a]>>c&1 for a,b,c in combinations(range(m),3)):continue
            ordered_graphs+=1
            for mask in range(1<<m):
                S=[i for i in range(m) if mask>>i&1]
                B=[[int(i>=j or clash[i]>>j&1) for j in S] for i in S]
                independent=not any(clash[i]>>j&1 for i,j in combinations(S,2))
                assert determinant_integer(B)==int(independent);principal_minors+=1
    report={'adjacent_swap_word_checks':word_checks,'trace_classes':class_checks,
            'Algorithm_T_full_output_checks':generator_checks,
            'multiplication_checks':product_checks,'left_and_right_division_checks':division_checks,
            'weighted_trace_and_pyramid_GF_checks':weighted_gf_checks,
            'labelled_traces_factorized':labelled_traces,'labelled_factor_count_coefficients':labelled_distribution_checks,
            'cocomparability_ordered_graphs':ordered_graphs,'determinant_principal_minors':principal_minors,
            'scope':'All graphs on <=4 letters, all words of length <=5; arithmetic pairs through total length 4 on <=3 letters or 3 on four letters. All labelled traces on <=3 letters through length 5. Determinant minors for every suitable ordered graph on <=5 vertices. See TRACE_NOTES.md for general arguments.'}
    (Path(__file__).parent/'results/traces.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
