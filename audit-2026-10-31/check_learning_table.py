"""SAT53--57 and59: table digits, covering polynomial and circuit witnesses."""
from itertools import combinations,product
from collections import Counter
from pathlib import Path
import json,re
import numpy as np
import mpmath as mp

ROOT=Path(__file__).parent
TERMS={
    'eq27':[[-2,-3,-10],[-6,-10,-12],[8,-13,-15],[-8,10,-12]],
    'eq32':[[-2,-3,-10],[3,-6,-10,-12],[8,-13,-15],[-8,10,-12]],
    '54a':[[-1,9,11,-18],[-6,-10,-12],[-4,10,-12]],
    '54c':[[-1,-5,-12,17],[-4,8,-13,-15],[-6,-9,-12,16],[-6,-13,-16,20],[13,14,-16]],
    '55':[[-1,-7,-8],[-2,-3,-4],[-4,-13,-14],[-6,-10,-12]],
    'morgenstern':[[-4,10,-12],[-6,-10,-12],[9,-10,11]],
}


def evaluate(terms,bits):
    return int(any(all(bits[abs(l)-1]==int(l>0) for l in term) for term in terms))


def circuit(bits):
    x=lambda i:bits[i-1]
    g1=x(9)|x(10);g2=x(8)^g1;g3=x(6)|x(12)
    g4=1^(g3^x(10));g5=g2|g4;g6=g5^x(12)
    return g6


def digits(precision,rows):
    mp.mp.dps=precision
    out=[]
    for constant in (mp.pi,mp.e):
        value=constant/4;words=[]
        for _ in range(rows):
            value*=1<<20;word=int(value);value-=word
            words.append(f'{word:020b}')
        out.append(words)
    return out


def cardinality_counts(n,r):
    t={k:1 for k in range(n,2*n)}
    for k in range(n-1,0,-1):t[k]=min(r,t[2*k]+t[2*k+1])
    lengths=[]
    for k in range(2,n):
        for i in range(t[2*k]+1):
            for j in range(t[2*k+1]+1):
                if 1<=i+j<=t[k]+1:
                    lengths.append(int(i>0)+int(j>0)+int(i+j<=r))
    for i in range(t[2]+1):
        for j in range(t[3]+1):
            if i+j==r+1:lengths.append(int(i>0)+int(j>0))
    return sum(t[k] for k in range(2,n)),len(lengths),sum(lengths)


def main():
    text=(ROOT.parent/'text/vol4b.txt').read_text().split('\f')[218]
    words=re.findall(r'(?m)^[01]{20}$',text);assert len(words)==32
    generated=digits(250,40);assert generated==digits(400,40)
    assert words==generated[0][:16]+generated[1][:16]
    positives,negatives=generated
    integer=lambda word:sum(int(c)<<j for j,c in enumerate(word))
    P=[integer(w) for w in positives[:16]];Q=[integer(w) for w in negatives[:16]]
    differences=[a^b for a in P for b in Q]
    assert ''.join(str((differences[0]>>i)&1) for i in range(20))=='01100100111101111000'
    # Subset zeta closure: bad[T] iff T contains some positive/negative difference.
    bad=np.zeros(1<<20,dtype=bool);bad[differences]=True
    for j in range(20):
        step=1<<j;blocks=bad.reshape(-1,2*step);blocks[:,step:]|=blocks[:,:step]
    full=(1<<20)-1;coeff=Counter();five=[]
    for mask in range(1<<20):
        if not bad[full^mask]:
            coeff[mask.bit_count()]+=1
            if mask.bit_count()==5:five.append(tuple(i+1 for i in range(20) if mask>>i&1))
    five.sort()
    expected=[(1,4,15,17,20),(1,10,15,17,20),(1,15,17,18,20),(4,6,7,10,12),
              (4,6,9,10,12),(4,6,10,12,19),(4,10,12,15,19),(5,7,11,12,15),
              (6,7,8,10,12),(6,8,9,10,12),(7,10,12,15,20),(8,15,17,18,20)]
    assert five==expected
    assert coeff[5]==12 and coeff[6]==994 and coeff[7]==13503 and coeff[19]==20 and coeff[20]==1
    direct=[choice for choice in combinations(range(1,21),5)
            if all(any(d>>(j-1)&1 for j in choice) for d in differences)]
    assert direct==five
    assert any(d&((1<<10)-1)==0 for d in differences)
    assert all(d&((1<<11)-1) for d in differences)
    auxiliary,clauses,length=cardinality_counts(20,5)
    assert (20+auxiliary,256+clauses,sum(d.bit_count() for d in differences)+length)==(75,396,2894)

    answer=(ROOT.parent/'text/vol4b.txt').read_text().split('\f')[577]
    block=answer.split('So we have twelve diﬀerent truth tables:')[1].split('And the tenth')[0]
    chunks=re.findall('[01∗]{8}',block);assert len(chunks)==48
    rows=[''.join(chunks[4*i:4*i+4]) for i in range(12)]
    # The two printed columns are read downwards, not in extracted row order.
    printed=rows[::2]+rows[1::2];tables=[]
    for choice in five:
        table=['∗']*32
        for value,examples in [(1,positives[:16]),(0,negatives[:16])]:
            for word in examples:
                index=int(''.join(word[j-1] for j in choice),2)
                assert table[index] in ('∗',str(value));table[index]=str(value)
        tables.append(''.join(table))
    assert tables==printed
    for value,examples in [(1,positives[:16]),(0,negatives[:16])]:
        for word in examples:assert circuit(list(map(int,word)))==value
    circuit_table=''.join(str(circuit([int(f'{i:05b}'[five[9].index(j)]) if j in five[9] else 0 for j in range(1,21)])) for i in range(32))
    assert all(a=='∗' or a==b for a,b in zip(tables[9],circuit_table))
    witness_rows={}
    for name,rows in [('eq27',20),('54a',16),('54c',28),('55',16),('morgenstern',16)]:
        for value,examples in [(1,positives[:rows]),(0,negatives[:rows])]:
            for word in examples:assert evaluate(TERMS[name],list(map(int,word)))==value,(name,word,value)
        witness_rows[name]=rows
    active=(2,3,6,8,10,12,13,15);different=0
    for row in product((0,1),repeat=8):
        bits=[0]*20
        for j,value in zip(active,row):bits[j-1]=value
        delta=evaluate(TERMS['eq27'],bits)^evaluate(TERMS['eq32'],bits)
        x=lambda j:bits[j-1]
        explicit=x(2)*(1-x(3))*(1-x(6))*(1-x(10))*(1-x(12))*((1-x(8))|(x(8)*(x(13)|x(15))))
        assert delta==explicit;different+=delta
    assert different==7
    data={'positive_words_pi':positives,'negative_words_e':negatives,'dnf_witnesses':TERMS}
    (ROOT/'results/learning_table_data.json').write_text(json.dumps(data,indent=2)+'\n')
    result={'32_table_words_match_pi_e':True,'cover_counts_by_size':dict(sorted(coeff.items())),
            'five_coordinate_solutions':five,'all_12_truth_tables_match':True,'six_operation_truth_table':circuit_table,
            'dnf_witness_rows':witness_rows,'cardinality_encoding':{'variables':75,'clauses':396,'total_length':2894},
            '59_disagreement_probability':'7/256','status':'all assertions passed'}
    (ROOT/'results/learning_table.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
