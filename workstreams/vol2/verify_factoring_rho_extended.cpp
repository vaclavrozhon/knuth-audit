#include <algorithm>
#include <cassert>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>
#include <unistd.h>
using u64=std::uint64_t;
using u128=__uint128_t;
u64 hit(u64 p) {
    u64 x=5,anchor=2,ell=1,k=1,n=1;
    while(x!=anchor) {
        if(--k==0) {anchor=x;ell*=2;k=ell;}
        x=(x*x+1)%p;
        ++n;
    }
    return n;
}
int main(int argc,char**argv) {
    assert(argc==4);
    const int begin=std::stoi(argv[1]),end=std::stoi(argv[2]);
    assert(begin>=1000000 && begin%1000000==0 && end<=1000000000);
    std::vector<bool> small(31624,true);
    std::vector<int> base;
    small[0]=small[1]=false;
    for(int p=2;p<(int)small.size();++p) if(small[p]) {
        base.push_back(p);
        if(p*p<(int)small.size()) for(int j=p*p;j<(int)small.size();j+=p) small[j]=false;
    }
    std::ofstream out(argv[3],std::ios::app);
    out<<std::setprecision(17);
    std::cout<<"pid "<<getpid()<<" range "<<begin<<" "<<end<<std::endl;
    for(int lo=begin;lo<end;lo+=1000000) {
        auto start=std::chrono::steady_clock::now();
        int hi=std::min(lo+1000000,end);
        std::vector<bool> prime(hi-lo,true);
        for(int p:base) {
            u64 first=std::max((u64)p*p,((u64)lo+p-1)/p*p);
            for(u64 x=first;x<(u64)hi;x+=p) prime[x-lo]=false;
        }
        u64 count=0,sum=0,max_p=0,max_m=0,ratio_p=1,ratio_m=0,digest=1469598103934665603ULL;
        double roots=0;
        for(int p=lo;p<hi;++p) if(prime[p-lo]) {
            u64 m=hit(p);
            if(m*m>=256*(u64)p) {
                std::cerr<<"BOUND COUNTEREXAMPLE "<<p<<" "<<m<<std::endl;
                return 2;
            }
            ++count;sum+=m;roots+=std::sqrt((double)p);
            digest=(digest^(u64)p)*1099511628211ULL;
            digest=(digest^m)*1099511628211ULL;
            if(m>max_m) {max_m=m;max_p=p;}
            if((u128)m*m*ratio_p>(u128)ratio_m*ratio_m*p) {ratio_p=p;ratio_m=m;}
        }
        double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
        out<<lo<<","<<hi<<","<<count<<","<<sum<<","<<max_p<<","<<max_m<<","
           <<ratio_p<<","<<ratio_m<<","<<roots<<","<<digest<<","<<elapsed<<"\n";
        out.flush();
        std::cout<<"completed "<<hi<<" primes "<<count<<" maximum "<<max_m
                 <<" at "<<max_p<<" seconds "<<elapsed<<std::endl;
    }
    std::cout<<"ALL SEGMENTS COMPLETE"<<std::endl;
}
