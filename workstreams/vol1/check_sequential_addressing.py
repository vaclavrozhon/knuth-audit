"""Check extended MIX address semantics against the book's compressed evaluator."""
from dataclasses import dataclass
from pathlib import Path
from itertools import product
import json,random
@dataclass(frozen=True)
class Address:
    value:int
    first:int=0
    second:int=0

def expansion(word,memory,index,limit=10000):
    # Literal leftmost rewriting: pending modifiers are a real stack/list.
    value=word.value;pending=[word.first,word.second];reads=0;max_pending=2
    while pending:
        k=pending.pop(0)
        if k==7:
            reads+=1
            if reads>limit:raise TimeoutError
            w=memory[value];value=w.value;pending[0:0]=[w.first,w.second]
        elif k:value+=index[k]
        max_pending=max(max_pending,len(pending))
    return value,reads,max_pending

def compressed(word,memory,index,limit=10000):
    H=0;N=0;reads=0
    while True:
        M=word.value;a=word.first;b=word.second
        if 1<=a<=6:M+=index[a]
        if 1<=b<=6:H+=index[b]
        if a==b==7:N+=1;H=0
        if a==7 or b==7:
            word=memory[M];reads+=1
        else:
            M+=H;H=0
            if N:N-=1;word=memory[M];reads+=1
            else:return M,reads
        if reads>limit:raise TimeoutError

class Compiler:
    def __init__(self,index,rng):self.index=index;self.rng=rng;self.memory={};self.next=100
    def place(self,word):
        a=self.next;self.next+=1;self.memory[a]=word;return a
    def expression(self,depth,target):
        if depth==0:
            a,b=self.rng.randrange(7),self.rng.randrange(7)
            return Address(target-self.index[a]-self.index[b],a,b)
        j=self.rng.randrange(7)
        if self.rng.randrange(2):
            a=self.place(self.expression(depth-1,target-self.index[j]));return Address(a,7,j)
        a=self.place(self.expression(depth-1,target));return Address(a-self.index[j],j,7)

def main():
    rng=random.Random(20261101);count=0;maximum=0
    for radix in range(64,101):
        for trial in range(80):
            index=[0]+[rng.randint(-20,20) for _ in range(6)]
            c=Compiler(index,rng);target=rng.randint(-1000,1000)
            if trial%2:
                second=c.place(c.expression(rng.randrange(15),target))
                first=c.place(c.expression(rng.randrange(15),second));word=Address(first,7,7)
            else:word=c.expression(rng.randrange(20),target)
            a=expansion(word,c.memory,index);b=compressed(word,c.memory,index)
            assert a[:2]==b and a[0]==target,(radix,word,a,b)
            assert all(not (w.first==w.second==7) for w in c.memory.values())
            assert abs(a[0])<radix**2
            maximum=max(maximum,a[2]);count+=1
    index=[0,1,2,3,4,5,6]
    example={1000:Address(1000,1,7),1001:Address(1000,0,2)}
    assert expansion(Address(1000,7,2),example,index)[0]==1004
    auxiliary={100:Address(101,7,2),101:Address(102,7,3),102:Address(103,7,4),103:Address(0,5,6)}
    assert expansion(Address(100,7,1),auxiliary,index)[:2]==(21,4)
    assert compressed(Address(100,7,1),auxiliary,index)==(21,4)
    assert expansion(Address(100,7,6),{100:Address(0,6,6)},index)[0]+index[6]==4*index[6]
    printed=[(1001,7,7),(1004,7,1),(1002,2,2),(1001,1,1),(1005,1,7),(1006,1,7),(1008,7,7),(1002,7,1),(1003,7,2)]
    m={1000+i:Address(*x) for i,x in enumerate(printed)}
    full=expansion(Address(1000,7,7),m,index)
    assert full[0]==1007
    # Milder restriction: 7:7 may nest when no post-index additions surround it.
    nested={100:Address(101,7,7),101:Address(102),102:Address(103),103:Address(321)}
    assert expansion(Address(100,7),nested,index)[:2]==compressed(Address(100,7),nested,index)==(103,3)
    # Explicit forbidden pattern: resetting H loses a pending nonzero index.
    forbidden=dict(nested)
    a=expansion(Address(100,7,1),forbidden,index);b=compressed(Address(100,7,1),forbidden,index)
    assert a[0]==b[0]+1
    try:expansion(Address(100,7),{100:Address(100,7)},index,100)
    except TimeoutError:pass
    else:raise AssertionError('loop not detected by finite cap')
    result={'random_valid_cases':count,'all_radices':[64,100],'max_pending_modifiers':maximum,'printed5a_value':full[0],'printed5a_indirections':full[1],'printed5a_max_pending':full[2],'known_invalid_milder_case':{'literal':a,'compressed':b},'seed':20261101,'note':'Final numeric address checks; signed-zero ENTi behavior separately proved in note.'}
    (Path(__file__).parent/'results/sequential-addressing.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
