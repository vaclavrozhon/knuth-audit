#!/usr/bin/env python3
"""Stopped extended Euclid versus complete bounded reconstruction oracle."""
from math import gcd,isqrt
from pathlib import Path
import argparse,json,os,time
ROOT=Path(__file__).resolve().parent;DEST=ROOT/'results/euclid-reconstruction.json'

def stopped(a,m,X,Y):
    r0,r1,s0,s1,t0,t1=m,a,1,0,0,1
    previous=m
    while r1>Y:
        q=r0//r1
        r0,r1,s0,s1,t0,t1=r1,r0-q*r1,s1,s0-q*s1,t1,t0-q*t1
        assert s1*m+t1*a==r1 and abs(s0*t1-s1*t0)==1
    x=abs(t1);y=r1 if t1>0 else -r1;z=-s1 if t1>0 else s1
    assert x>0 and a*x-m*z==y and gcd(x,z)==1
    result=(x,y) if x<=X and gcd(x,y)==1 else None
    return result,(x,y,z,r0)

def oracle(a,m,X,Y):
    result=[]
    for x in range(1,X+1):
        r=(a*x)%m
        for y in (r,r-m):
            if abs(y)<=Y and gcd(x,y)==1:result.append((x,y))
    return sorted(set(result))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--resume',action='store_true');args=ap.parse_args()
    out=json.loads(DEST.read_text()) if args.resume and DEST.exists() else {};print('pid',os.getpid(),flush=True)
    def save(name,x):out[name]=x;DEST.write_text(json.dumps(out,indent=2)+'\n');print(name,json.dumps(x),flush=True)
    if 'square' not in out:
        start=time.monotonic();count=found=boundary=0
        for m in range(3,1025):
            H=isqrt(m//2)
            for a in range(2,m):
                got,cert=stopped(a,m,H,H);all_solutions=oracle(a,m,H,H)
                assert len(all_solutions)<=1
                assert ([] if got is None else [got])==all_solutions,(a,m,got,all_solutions)
                if got:
                    found+=1;boundary+=int(2*got[0]**2==m or 2*got[1]**2==m)
                count+=1
        save('square',dict(cases=count,solutions=found,boundary_solutions=boundary,max_modulus=1024,seconds=time.monotonic()-start))
    if 'rectangles' not in out:
        start=time.monotonic();count=twins=0
        for m in range(3,97):
            for X in range(1,9):
                for Y in range(1,9):
                    if 2*X*Y>m:continue
                    for a in range(2,m):
                        got,cert=stopped(a,m,X,Y);all_solutions=oracle(a,m,X,Y)
                        assert (got in all_solutions) if all_solutions else (got is None)
                        if len(all_solutions)>1:
                            assert X==1 and 2*Y==m and a==Y
                            assert all_solutions==[(1,-Y),(1,Y)];twins+=1
                        count+=1
        # Large boundary rectangles beyond the small bound grid.
        for Y in range(2,257):
            m=2*Y;a=Y;got,_=stopped(a,m,1,Y)
            assert got==(1,Y) and oracle(a,m,1,Y)==[(1,-Y),(1,Y)]
        save('rectangles',dict(cases=count,twin_cases_in_grid=twins,twin_family=255,seconds=time.monotonic()-start))
    if 'book_example' not in out:
        a,m=28481,199999;H=isqrt(m//2);got,cert=stopped(a,m,H,H)
        assert got==(316,41) and oracle(a,m,H,H)==[got]
        assert a*316-m*45==41
        assert stopped(3,18,3,3)[0]==(1,3)
        save('book_example',dict(a=a,m=m,x=316,y=41,z=45,boundary_example=[3,18,1,3]))
    out['status']='passed';out['final_pid']=os.getpid();out['scope']='Exact Euclidean recurrence and independent exhaustive denominator/residue enumeration. General proof and classification of rectangular equality are in euclid-reconstruction.md.';DEST.write_text(json.dumps(out,indent=2)+'\n');print('passed',flush=True)
if __name__=='__main__':main()
