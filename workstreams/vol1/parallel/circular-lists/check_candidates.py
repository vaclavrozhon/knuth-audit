"""Small exact reproductions for two independent answer-book candidates."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import json
from check_mix import Fixture,timemult,stats,add

HERE=Path(__file__).resolve().parent


def alias_case(b):
    f=Fixture(b,pool_count=0)
    ph=f.polynomial({0:1});mh=f.polynomial({0:-1})
    node=f.read(ph)[1][1]
    t,ct,events=f.call('MULT',[(1,ph),(2,ph),(4,mh)],trace=True)
    assert f.m.halted and f.m.pc==f.s['OVERFLOW']+1
    # First deletion detaches the sole ordinary node; its LINK becomes old
    # AVAIL=0. ANEXT subsequently reads this changed LINK through I1.
    deleted=[e for e in events if e['pc']==f.s['ANEXT'] and e['avail']==node and e['regs'][1]==node]
    assert deleted
    zero=[e for e in events if e['pc']==f.s['ACOMP'] and e['regs'][1]==0]
    assert zero
    # At final halt the replacement ordinary node has coefficient zero, so
    # the representation is malformed in addition to the lost P pointer.
    head_next=f.m.mem[ph+1].magnitude(b) % (b*b)
    assert head_next==node and f.m.mem[node].value(b)==0
    return {'b':b,'p_head':ph,'m_head':mh,'ordinary_p_node':node,'time_until_overflow_halt':t,
            'first_deleted_state':deleted[0],'first_null_p_state':zero[0],
            'final_pc':f.m.pc,'overflow_pc':f.s['OVERFLOW'],
            'expected':{},'observed':'P follows freed node to address 0; routine later halts at OVERFLOW'}


def timing_case(b):
    # p=2,r=1,alpha=1/2, q0'=0. One matching noncancelling term and
    # one newly inserted term realize every assumption exactly.
    p={1:1,0:1};q={1:1};m={0:1}
    assert stats(p,q)==(0,1,1,0)
    f=Fixture(b);ph=f.polynomial(p);qh=f.polynomial(q);mh=f.polynomial(m)
    t,_,_=f.call('MULT',[(1,ph),(2,qh),(4,mh)])
    exact=timemult(p,q,m)[0]
    # Integer evaluation avoids all floating-point roundoff.
    printed=4+80+4+38+29
    corrected=4+78+5+38+29
    assert t==exact==corrected==154 and printed==155
    assert f.read(qh)[0]=={1:2,0:1}
    return {'b':b,'P':'x+1','Q':'x','M':'1','p':2,'r':1,'alpha':'1/2',
            'mprime':0,'msecond':1,'pprime':1,'qprime0':0,
            'exact_and_measured_u':t,'printed_simplified_u':printed,
            'corrected_simplified_u':corrected}


def run():
    out={'alias_pq_constant_minus_one':[alias_case(b) for b in range(64,101)],
         'multiplication_simplified_time':[timing_case(b) for b in range(64,101)]}
    (HERE/'results'/'candidates.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:{'cases':len(v),'first':v[0]} for k,v in out.items()},indent=2))


if __name__=='__main__':run()
