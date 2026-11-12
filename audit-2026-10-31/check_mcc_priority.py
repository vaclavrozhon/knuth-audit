"""Independent tree recurrence for the five-option counterexample to167."""
from collections import Counter
from pathlib import Path
import json,re,subprocess
ROOT=Path(__file__).parent;OUT=ROOT/'results/mcc_arithmetic'

def simulate(upper_A):
    slack={'A':upper_A-1,'B':4};profile=Counter();leaves=0;choices=[]
    def walk(state,depth=0):
        nonlocal leaves
        profile[depth]+=1
        if not state:leaves+=1;return
        p=min(state,key=lambda p:(max(0,state[p][0]+1-max(state[p][1],0)),slack[p],-state[p][0],p))
        length,lower=state[p]
        if length<lower:return
        if depth==0:choices.append(p)
        # i options are skipped, then one selected. They are all independent.
        for i in range(length-max(lower,1)+1):
            child=dict(state);child[p]=(length-i-1,lower-1);walk(child,depth+1)
        if lower<=0:
            child=dict(state);del child[p];walk(child,depth+1)
    walk({'A':(2,1),'B':(3,2)})
    return dict(upper_A=upper_A,upper_B=6,root=choices[0],solutions=leaves,nodes=sum(profile.values()),profile=dict(profile))

def main():
    result=[]
    for a in [4,5,6,7,100]:
        d=simulate(a);log=(OUT/f'upper-bound-a{a}.log').read_text()
        assert int(re.search(r'(\d+) nodes',log)[1])==d['nodes']
        assert int(re.search(r'Altogether (\d+) solution',log)[1])==d['solutions']==12
        result.append(d)
    (OUT/'upper-bound-independent.json').write_text(json.dumps(result,indent=2)+'\n');print(result)

if __name__=='__main__':main()
