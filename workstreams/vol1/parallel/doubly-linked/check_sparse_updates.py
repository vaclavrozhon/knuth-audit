"""Exercise11: two arrays plus a linked list of this step's writes."""
import sys
sys.dont_write_bytecode=True
import itertools,json
from pathlib import Path


class Sparse:
    def __init__(self,values):
        self.v=[None]+list(values);self.new=[None]*len(self.v)
        self.link=[0]*len(self.v);self.head=-1
    def assign(self,k,value):
        if self.link[k]:raise ValueError('second assignment in one step')
        self.link[k]=self.head;self.head=k;self.new[k]=value
    def commit(self):
        k=self.head;self.head=-1;cost=0
        while k>=0:
            self.v[k]=self.new[k];nxt=self.link[k];self.link[k]=0;k=nxt;cost+=1
        return cost
    def invariant(self,changed):
        seen=set();k=self.head
        while k>=0:
            assert 1<=k<len(self.v) and k not in seen
            seen.add(k);k=self.link[k]
        assert k==-1 and seen==set(changed)
        assert {k for k in range(1,len(self.v)) if self.link[k]}==seen


def main():
    cases=0
    for n in range(1,5):
        values=list(range(10,10+n));ops=list(itertools.product(range(1,n+1),repeat=2))
        # RHS reads from the old state. This includes swaps and longer cycles.
        for length in range(5):
            for seq in itertools.product(ops,repeat=length):
                s=Sparse(values);changed={};error=False
                for dest,src in seq:
                    try:s.assign(dest,s.v[src])
                    except ValueError:
                        assert dest in changed;error=True;break
                    assert dest not in changed;changed[dest]=values[src-1]
                    assert s.v[1:]==values;s.invariant(changed)
                if not error:
                    expected=values[:]
                    for k,v in changed.items():expected[k-1]=v
                    assert s.commit()==len(changed) and s.v[1:]==expected
                    s.invariant({})
                    # Membership marks must be reusable in the next step.
                    for k in changed:s.assign(k,0)
                    s.commit();s.invariant({})
                cases+=1
    result={'assignment_sequences':cases,'max_variables':4,'max_assignments':4,
            'duplicate_policy':'all second assignments rejected, as printed; distinct-value conflicts included'}
    (Path(__file__).resolve().parent/'results'/'sparse-checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':main()
