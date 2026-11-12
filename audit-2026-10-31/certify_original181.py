"""Finite all-n certificate for181's original recurrence, not a new cover census.

F017's corrected recurrence already has its own accepted certificate. This
separate certificate establishes the constants of the originally defined D.
"""
from fractions import Fraction
from pathlib import Path
from datetime import datetime, timezone
import json
from puzzle_xcc import save,sha

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/extreme180_188'


def main():
    assert not (OUT/'original181-certificate.json').exists()
    oldpath=ROOT/'results/doomsday.json'
    old=json.loads(oldpath.read_text())['original_recurrence_first_26']
    constants=[Fraction(q,96) for q in [188,248,320,425,566]]
    def f(n):
        assert n>=0
        if n<15:return old[n]
        q,r=divmod(n,5);v=4**q*constants[r]-Fraction(1,3)
        assert v.denominator==1
        return v.numerator
    def terms(n,max_t=None):
        for t in range(1,min(n,1+max_t) if max_t else n):
            if n-t-1>=0:yield (t,0),1+t*f(n-t-1)
            for u in range(1,t+1):
                a,b=n-t-u+1,n-t-u-1
                if a>=0 and (t==u or b>=0):yield (t,u),u+u*f(a)+((t-u)*f(b) if t>u else 0)
    assert [f(n) for n in range(26)]==old
    base=[]
    for n in range(2,48):
        ts=list(terms(n));m=max(v for k,v in ts);winners=[k for k,v in ts if v==m]
        assert m==f(n),(n,m,f(n))
        if n>=19:assert winners==[(4,0)]
        base.append(dict(n=n,value=m,maximizers=winners))
    assert all(f(n+1)>=f(n) for n in range(20))
    assert all(f(n+5)>=4*f(n)+1 for n in range(20))
    assert all(f(n+5)==4*f(n)+1 for n in range(14,20))
    assert all(4**(t//5)>=2*t for t in range(15,20))
    residues=[]
    for n in range(43,48):
        for (t,u),v in terms(n,14):
            gap=f(n)-v;c=4-t if u==0 else 1-t+3*u
            assert 3*gap+c>=0
            assert gap==c==0 if (t,u)==(4,0) else gap>0
            residues.append(dict(n=n,t=t,u=u,gap=gap,step_constant=c))
    assert len(residues)==595
    save(OUT/'original181-certificate.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),
        accepted_data_sha256=sha(oldpath),original_base=[1,1],constants=[str(v) for v in constants],
        finite_base=base,residue_certificates=residues,periodic_index_threshold=14,large_t_threshold=15,
        unique_maximizer_from=19,scope='Original mathematical recurrence only; its failure as a node bound remains F017.',
        old_cover_censuses_rerun=0,new_solver_calls=0))
    print('PASS181:595 residue certificates plus finite base prove original constants for every n;no cover search.')


if __name__=='__main__':main()
