"""Exact reconstruction of both decks in §3.4.2-14.

Transcribed from the scanned suits, not OCR. A separate direct two-packet
predicate validates witnesses. Small complete permutation products validate
the cyclic-descent composition criterion independently.
"""
from pathlib import Path
from itertools import permutations
import json
ROOT=Path(__file__).resolve().parent
ranks=list(map(str,range(2,11)))+['J','Q','K','A']
original=[r+s for s in 'cdhs' for r in ranks]
A='9c 10c Kh Jc Qc Ah Kc Ac 2d Qh 3d 2s 3s 4s 5s 6s 7s 4d 8s 9s 5d 10s 6d Js 7d Qs 8d Ks 9d 10d Jd Qd As Kd 2c 3c Ad 4c 2h 3h 4h 5c 6c 5h 6h 7h 8h 7c 9h 10h Jh 8c'.split()
B='10d Jc Qc 3s 4h 5h 6d Js Jd Qs 4s 6h Kc As 2c 3c Kh 4c 7h 5s 6s Qd Ac 7d 5c Ah 8h 7s 6c Kd Ks 9h Ad 7c 8c 9c 10h 8s 10c 8d 2h 5d Jh 2d 3d Qh 4d 9s 3h 2s 9d 10s'.split()

def breaks(deck,orig):
    p={x:i for i,x in enumerate(deck)};N=len(orig)
    return [i for i in range(N) if p[orig[(i-1)%N]]>p[orig[i]]]

def candidates(deck,limit):
    return [dict(position=i+1,card=x,cyclic_descents=len(breaks([x]+deck[:i]+deck[i+1:],original)))
            for i,x in enumerate(deck) if len(breaks([x]+deck[:i]+deck[i+1:],original))<=limit]

def direct_riffle(before,after,x,y):
    N=len(before);length=(y-x)%N
    first=[before[(x+i)%N] for i in range(length)]
    second=[before[(y+i)%N] for i in range(N-length)]
    aset=set(first);assert [v for v in after if v in aset]==first
    assert [v for v in after if v not in aset]==second
    assert len(set(after))==N and set(after)==set(before)

def witness(deck,rounds):
    starts=breaks(deck,original);start=starts[0]
    rotated=original[start:]+original[:start]
    starts_set={original[i] for i in starts};label={};v=-1
    for card in rotated:
        if card in starts_set:v+=1
        label[card]=v
    assert v+1<=2**rounds
    current=deck[:];reverse=[]
    for bit in range(rounds):
        low=[x for x in current if not ((label[x]>>bit)&1)]
        high=[x for x in current if (label[x]>>bit)&1]
        before=low+high;assert 0<len(low)<len(before)
        direct_riffle(before,current,0,len(low))
        reverse.append(dict(before=before,after=current[:],cut=len(low)))
        current=before
    assert current==rotated
    ans=[];current=original[:]
    for step,record in enumerate(reversed(reverse)):
        x=start if step==0 else 0;y=(x+record['cut'])%len(original)
        direct_riffle(current,record['after'],x,y)
        ans.append(dict(cut_x=x,cut_y=y,output=record['after']));current=record['after']
    assert current==deck
    return ans

rows=[]
for deck,limit,card,rounds in [(A,2,'Qh',1),(B,8,'5d',3)]:
    assert len(deck)==len(set(deck))==52 and set(deck)==set(original)
    cs=candidates(deck,limit);assert len(cs)==1 and cs[0]['card']==card
    i=deck.index(card);undone=[card]+deck[:i]+deck[i+1:]
    row=dict(observed=deck,observed_descents=len(breaks(deck,original)),candidates=cs,
             undone=undone,shuffle_witness=witness(undone,rounds))
    if deck==A:
        exceptions=[]
        for j in range(52):
            moved=undone[1:j+1]+[card]+undone[j+1:]
            cc=candidates(moved,2)
            if [x['card'] for x in cc]!=[card]:exceptions.append(dict(position=j+1,candidates=cc))
        assert [x['position'] for x in exceptions]==[1,2,3,51,52]
        row['exceptional_insertions']=exceptions
    rows.append(row)

complete=[];pairs=0
for N in range(2,8):
    orig=list(range(N));perms=list(permutations(orig))
    # Independent direct packet test for every permutation and every two cuts.
    one=set()
    for p in perms:
      direct=False
      for x in range(N):
        for length in range(1,N):
          y=(x+length)%N;first=[orig[(x+i)%N] for i in range(length)];aset=set(first)
          second=[orig[(y+i)%N] for i in range(N-length)]
          if [v for v in p if v in aset]==first and [v for v in p if v not in aset]==second:direct=True;break
        if direct:break
      assert direct==(len(breaks(p,orig))<=2)
      if direct:one.add(p)
    two=set()
    for p in one:
      for q in one:
        out=tuple(p[i] for i in q);assert len(breaks(out,orig))<=4;two.add(out);pairs+=1
    assert two=={p for p in perms if len(breaks(p,orig))<=4}
    complete.append(dict(N=N,permutations=len(perms),one_riffle=len(one),two_riffles=len(two)))
result=dict(suit_encoding='c=clubs,d=diamonds,h=hearts,s=spades; original rank order2..10,J,Q,K,A',
            examples=rows,complete_small_models=complete,ordered_pair_products=pairs)
(ROOT/'results/card-riffles.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS decks, all104 undo candidates, all52 insertion positions, four direct shuffle witnesses')
print('PASS small models',complete,'products',pairs)
