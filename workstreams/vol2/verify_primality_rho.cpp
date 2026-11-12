// Exact dyadic detector and independent Floyd tail/cycle model for the p393 example.
#include <cassert>
#include <cstdint>
#include <iostream>
using U=uint64_t;
U step(U x,U p) { return (__uint128_t(x)*x+1)%p; }
U dyadic(U p) {
    U x=5, anchor=2, ell=1,k=1,m=1;
    while(x!=anchor) {
        if(--k==0) {anchor=x;ell*=2;k=ell;}
        x=step(x,p); ++m;
    }
    return m;
}
int main() {
    for(U p:{8174912477117ULL,23528569104401ULL}) {
        U a=step(2,p),b=step(step(2,p),p);
        while(a!=b) {a=step(a,p);b=step(step(b,p),p);}
        U mu=0; a=2;
        while(a!=b) {a=step(a,p);b=step(b,p);++mu;}
        U lambda=1; b=step(a,p);
        while(a!=b) {b=step(b,p);++lambda;}
        U block=1;
        while(block<mu+1 || block<lambda) block*=2;
        U m=dyadic(p);
        assert(m==block-1+lambda);
        std::cout << p << ',' << mu << ',' << lambda << ',' << m << std::endl;
    }
}
