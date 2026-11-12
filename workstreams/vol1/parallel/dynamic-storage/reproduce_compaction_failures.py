"""Small exact reproductions, independently rerunnable without the larger audit."""
from pathlib import Path
import sys,json
sys.dont_write_bytecode = True
from compaction import *


def main():
    result={}
    mem,heads,avail,use=make_pool([(1,[]),(2,[])],1)
    mem[3]=number(1,64)
    setf(mem,3,SIZE,1,64)
    ref,end,root,stats=independent(mem,heads,avail,use,64)
    literal,lend,lroot,trace=algorithm_g(mem,avail,use,64,False)
    assert (lend,lroot)==(end,root)==(3,1)
    assert get(ref,1,SIZE,64)==2 and get(literal,1,SIZE,64)==1
    result['G9_three_word_overlap']=dict(input={'heads':[1,2],'sizes':[1,2],
        'T':[0,0],'use':2,'avail':4,'payload_word3':{'SIZE':1,'LINK':1}},
        trace=trace,expected_root_size=2,actual_root_size=1)
    mem,heads,avail,use=make_pool([(2,[None])])
    original,end,root,time=mix_g(mem,avail,use)
    assert get(original,2,LINK,64)==1
    result['MIX_G8_null']=dict(input={'size':2,'T':1,'LINK2':0,'LINK0':1,
        'USE':1,'AVAIL':3},actual_LINK2=1,expected_LINK2=0,time=time)
    timing=[]
    for spec,root in [([(1,[]),(1,[])],1), ([(1,[]),(2,[3]),(1,[]),(1,[])],1)]:
        mem,heads,avail,use=make_pool(spec,root)
        ref,end,root,stats=independent(mem,heads,avail,use,64)
        actual,aend,aroot,time=mix_g(mem,avail,use)
        assert (aend,aroot,actual[1:end])==(end,root,ref[1:end])
        printed=44*stats['a']+17*stats['b']+2*stats['w']+25*stats['c']+8*stats['d']+47
        assert printed-time==stats['c']
        timing.append(dict(stats=stats,actual=time,printed=printed))
    result['MIX_timing']=timing
    # New full G1 prefix, including arbitrary scratch-link contents, all radices.
    prefix=[]
    for b in range(64,101):
        mem,heads,avail,use=make_pool([(2,[None]),(3,[3,None]),(2,[]),(2,[1])],1,b)
        for i,p in enumerate(heads):setf(mem,p,LINK,i+7,b)
        ref,end,root,stats=independent(mem,heads,avail,use,b)
        actual,aend,aroot,time=mix_g(mem,avail,use,b,True,True)
        assert (aend,aroot,actual[1:end])==(end,root,ref[1:end])
        nulls=1
        expected=44*stats['a']+18*stats['b']+2*stats['w']+24*stats['c']+8*stats['d']+47-4*nulls+8*len(heads)+2
        assert time==expected
        prefix.append(b)
    result['full_G1_prefix_radices']=prefix
    out=Path(__file__).parent/'results'/'compaction-minimal.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
