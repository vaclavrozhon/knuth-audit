"""SAT 212: literal versus exact margins, and the corrected list-color gadget."""
from itertools import product,permutations
from collections import Counter,defaultdict
from pathlib import Path
import random,json


def matrix_bits(n):
    return [frozenset((i,j) for i in range(n) for j in range(n) if mask>>(n*i+j)&1)
            for mask in range(1<<(n*n))]


def balanced(n,R,C,P):
    return (all(sum((i,k) in R for i in range(n))==sum((j,k) in C for j in range(n)) for k in range(n))
            and all(sum((j,k) in C for k in range(n))==sum((i,j) in P for i in range(n)) for j in range(n))
            and all(sum((i,k) in R for k in range(n))==sum((i,j) in P for j in range(n)) for i in range(n)))


def all_small_boards(n):
    out=[]
    for values in product(range(-1,n),repeat=n*n):
        entries=[(i,j,values[n*i+j]) for i in range(n) for j in range(n) if values[n*i+j]>=0]
        R=frozenset((i,k) for i,j,k in entries);C=frozenset((j,k) for i,j,k in entries)
        if len(R)!=len(entries) or len(C)!=len(entries):continue
        P=frozenset((i,j) for i,j,k in entries)
        out.append((R,C,P))
    return out


def exact_cover_count(n,R,C,P):
    items=[('R',*x) for x in sorted(R)]+[('C',*x) for x in sorted(C)]+[('P',*x) for x in sorted(P)]
    index={x:i for i,x in enumerate(items)};options=[];col=[0]*len(items)
    for i,j in sorted(P):
        for k in range(n):
            if (i,k) in R and (j,k) in C:
                ids=[index[('R',i,k)],index[('C',j,k)],index[('P',i,j)]]
                option=len(options);options.append(sum(1<<a for a in ids))
                for a in ids:col[a]|=1<<option
    conflicts=[]
    for row in options:
        mask=0
        while row:
            bit=row&-row;row-=bit;mask|=col[bit.bit_length()-1]
        conflicts.append(mask)
    def visit(active,available):
        if not active:return 1
        best=None;scan=active
        while scan:
            bit=scan&-scan;scan-=bit;choices=col[bit.bit_length()-1]&available
            if not choices:return 0
            if best is None or choices.bit_count()<best.bit_count():
                best=choices
                if choices.bit_count()==1:break
        total=0
        while best:
            bit=best&-best;best-=bit;row=bit.bit_length()-1
            total+=visit(active&~options[row],available&~conflicts[row])
        return total
    return visit((1<<len(items))-1,(1<<len(options))-1)


def grid_solutions(lists,N):
    out=[];rows=[]
    def visit(i):
        if i==N:out.append(tuple(rows));return
        for row in permutations(range(N)):
            if any(row[j] not in lists[i,j] for j in range(N)):continue
            if any(row[j]==old[j] for old in rows for j in range(N)):continue
            rows.append(row);visit(i+1);rows.pop()
    visit(0);return out


def gadget(lists,N,corrected):
    assert all(lists[i,j] for i in range(N) for j in range(N))
    keys=list(range(N))+[(i,j,k) for i in range(N) for j in range(N) for k in sorted(lists[i,j])]
    index={x:i for i,x in enumerate(keys)};R={(i,k) for i in range(N) for k in range(N)};P=set()
    for i in range(N):
        for j in range(N):
            colors=sorted(lists[i,j]);h=index[i,j,colors[0]]
            P.update([(i,h),(h,j)])
            for t,k in enumerate(colors):
                v=index[i,j,k]
                if t:P.update([(v,v),(v,h),(h,v)])
                allowed=colors if not t else colors[t-1:t+1]
                R.update((v,a if corrected else index[i,j,a]) for a in allowed)
    return len(keys),frozenset(R),frozenset(R),frozenset(P)


def main():
    counts=Counter();witnesses=[]
    for n in (1,2):
        boards=all_small_boards(n);exact=Counter(boards);by_p=defaultdict(list)
        for R,C,P in boards:by_p[P].append((R,C))
        # A second, independent enumeration starts from arbitrary binary tensors.
        tensors=Counter()
        for bits in product((0,1),repeat=n**3):
            entries=[(i,j,k) for i in range(n) for j in range(n) for k in range(n) if bits[n*n*i+n*j+k]]
            R=frozenset((i,k) for i,j,k in entries);C=frozenset((j,k) for i,j,k in entries);P=frozenset((i,j) for i,j,k in entries)
            if len(R)==len(C)==len(P)==len(entries):tensors[R,C,P]+=1
            counts['binary_tensors']+=1
        assert tensors==exact
        matrices=matrix_bits(n)
        for R,C,P in product(matrices,repeat=3):
            loose=sum(r<=R and c<=C for r,c in by_p[P]);strict=exact[R,C,P]
            assert strict==exact_cover_count(n,R,C,P)
            if balanced(n,R,C,P):assert loose==strict;counts['balanced_inputs']+=1
            if loose!=strict:
                counts['definition_mismatches']+=1
                if len(witnesses)<4:witnesses.append({'n':n,'R':sorted(R),'C':sorted(C),'P':sorted(P),'loose_count':loose,'exact_count':strict})
            counts['margin_inputs']+=1
    R=frozenset((i,k) for i,row in enumerate(['1100','0110','0011','1001']) for k,x in enumerate(row) if x=='1')
    P=frozenset((i,j) for i,row in enumerate(['1010','1100','0101','0011']) for j,x in enumerate(row) if x=='1')
    assert balanced(4,R,R,P) and exact_cover_count(4,R,R,P)==0
    assert (0,2) in P and not ({k for i,k in R if i==0}&{k for j,k in R if j==2})

    def audit(lists,N):
        expected=len(grid_solutions(lists,N))
        corrected=gadget(lists,N,True);printed=gadget(lists,N,False)
        assert balanced(*corrected)
        assert exact_cover_count(*corrected)==expected
        assert exact_cover_count(*printed)==0
        counts['gadget_inputs']+=1;counts['grid_solutions']+=expected
        if expected:counts['printed_gadget_false_negatives']+=1
    audit({(0,0):{0}},1)
    choices=[{0},{1},{0,1}]
    for row in product(choices,repeat=4):audit(dict(zip(product(range(2),repeat=2),row)),2)
    rng=random.Random(2122026)
    for N,samples in [(3,500),(4,30)]:
        choices=[{k for k in range(N) if mask>>k&1} for mask in range(1,1<<N)]
        for _ in range(samples):audit({(i,j):rng.choice(choices) for i in range(N) for j in range(N)},N)
        audit({(i,j):set(range(N)) for i in range(N) for j in range(N)},N)
    out={'counts':dict(counts),'definition_witnesses':witnesses,
         'minimal_gadget_input':{'N':1,'list_11':[1]},
         'printed_output':{'R':[[1,0],[0,1]],'C':[[1,0],[0,1]],'P':[[0,1],[1,0]],'solutions':0},
         'corrected_output':{'R':[[1,0],[1,0]],'C':[[1,0],[1,0]],'P':[[0,1],[1,0]],'solutions':1},
         'correction':'In answer212(d), replace k=(I,J,Kprime) with k=Kprime.',
         'status':'all assertions passed'}
    (Path(__file__).parent/'results/latin_reduction.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
