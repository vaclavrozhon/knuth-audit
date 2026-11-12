#include <algorithm>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using u64=std::uint64_t;
u64 hit(u64 p) {
    u64 x=5%p, anchor=2%p, ell=1, k=1, n=1;
    while(x!=anchor) {
        --k;
        if(k==0) {anchor=x;ell*=2;k=ell;}
        x=(x*x+1)%p;
        ++n;
    }
    return n;
}
int main(int argc,char**argv) {
    assert(argc==2);
    constexpr int M=1000000;
    std::vector<bool> prime(M,true);
    prime[0]=prime[1]=false;
    for(int p=2;p*p<M;++p) if(prime[p])
        for(int j=p*p;j<M;j+=p) prime[j]=false;
    std::vector<int> seen(M,-1), at(M,0);
    std::ofstream out(argv[1]);
    out<<"p,m,mu,lambda\n";
    u64 maximum=0, maxp=0, ratio_m=0, ratio_p=1, count=0, total=0;
    for(int p=2;p<M;++p) if(prime[p]) {
        const u64 n=hit(p);
        u64 x=2%p;
        int i=0;
        while(seen[x]!=p) {
            seen[x]=p;at[x]=i++;
            x=(x*x+1)%p;
        }
        int mu=at[x], lambda=i-mu;
        u64 ell=1;
        while(ell < (u64)std::max(mu+1,lambda)) ell*=2;
        assert(n==ell-1+lambda);
        assert(n*n < 144*(u64)p);
        out<<p<<","<<n<<","<<mu<<","<<lambda<<"\n";
        if(n>maximum) {maximum=n;maxp=p;}
        if(n*n*ratio_p>ratio_m*ratio_m*(u64)p) {ratio_m=n;ratio_p=p;}
        ++count;total+=n;
    }
    assert(count==78498 && maximum==7685 && maxp==874771);
    assert(ratio_p==290047 && ratio_m==6251);
    out.close();
    std::cout<<"count "<<count<<" maximum "<<maximum<<" at "<<maxp
             <<" ratio maximum "<<ratio_m<<" at "<<ratio_p
             <<" sum "<<total<<"\n";
    for(u64 p : {850112303ULL,695361131ULL})
        std::cout<<"errata-record "<<p<<" "<<hit(p)<<"\n";
}
