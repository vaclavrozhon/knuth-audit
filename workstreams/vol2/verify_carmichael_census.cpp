// Complete Korselt census by increasing prime prefixes and final-prime progressions.
// Proof of completeness: notes/primality-basic.md. No probabilistic primality test.
#include <algorithm>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
using U = uint64_t;
using W = __uint128_t;
U bound, root, prefixes=0, candidates=0, found=0;
std::vector<bool> prime;
std::vector<U> primes, factors;
std::ofstream out;

U inverse(U a, U m) {
    int64_t x=0, y=1, b=m, c=a%m;
    while(c) {
        int64_t q=b/c, r=b-q*c, z=x-q*y;
        b=c; c=r; x=y; y=z;
    }
    assert(b==1);
    x%=int64_t(m); if(x<0) x+=m;
    assert(W(a)*U(x)%m==1);
    return x;
}

void finish(U m, U lambda) {
    U lo=factors.back()+1, hi=std::min({m,(bound-1)/m,root});
    if(lo>hi) return;
    U r=inverse(m,lambda);
    if(r<lo) r+=((lo-r+lambda-1)/lambda)*lambda;
    for(;r<=hi;r+=lambda) {
        ++candidates;
        if((m-1)%(r-1) || !prime[r]) continue;
        U n=m*r;
        assert(n<bound && (n-1)%lambda==0 && (n-1)%(r-1)==0);
        out << n;
        for(U p:factors) out << ',' << p;
        out << ',' << r << '\n';
        ++found;
    }
}

void search(U m, U lambda, size_t next) {
    ++prefixes;
    if(factors.size()>=2) finish(m,lambda);
    for(size_t j=next;j<primes.size();++j) {
        U p=primes[j];
        if(W(m)*p*p>=bound) break; // Still need a strictly larger last prime.
        if(factors.empty() && W(p)*p*p>=bound) break;
        U new_m=m*p, new_lambda=lambda/std::gcd(lambda,p-1)*(p-1);
        assert(new_lambda<=new_m);
        if(std::gcd(new_m,new_lambda)!=1) continue;
        factors.push_back(p);
        search(new_m,new_lambda,j+1);
        factors.pop_back();
        if(factors.empty()) {
            out.flush();
            std::cerr << "first=" << p << " prefixes=" << prefixes
                      << " progressions=" << candidates << " found=" << found << '\n';
        }
    }
}

int main(int argc,char**argv) {
    assert(argc==3);
    bound=std::stoull(argv[1]); assert(bound<=1000000000000ULL);
    root=1; while((root+1)*(root+1)<bound) ++root;
    prime.assign(root+1,true); prime[0]=prime[1]=false;
    for(U p=2;p*p<=root;++p) if(prime[p])
        for(U k=p*p;k<=root;k+=p) prime[k]=false;
    for(U p=3;p<=root;++p) if(prime[p]) primes.push_back(p);
    out.open(argv[2]); assert(out);
    auto t=std::chrono::steady_clock::now();
    search(1,1,0); out.close();
    std::cerr << "COMPLETE bound=" << bound << " found=" << found
              << " prefixes=" << prefixes << " candidates=" << candidates
              << " seconds=" << std::chrono::duration<double>(std::chrono::steady_clock::now()-t).count() << '\n';
}
