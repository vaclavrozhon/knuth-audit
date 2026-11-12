// Independent odd-only, unsegmented Eratosthenes sieve for the new census.
// Does not compute or repeat Pollard iterates.
#include <cassert>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>
int main(int argc,char**argv) {
    assert(argc==2);
    auto start=std::chrono::steady_clock::now();
    constexpr std::uint64_t end=1000000000;
    std::vector<bool> composite(end/2,false);
    composite[0]=true; // odd index i represents 2*i+1
    for(std::uint64_t p=3;p*p<end;p+=2) {
        if(composite[p/2])continue;
        for(std::uint64_t j=p*p/2;j<composite.size();j+=p)composite[j]=true;
    }
    std::ofstream out(argv[1]);out<<std::setprecision(21);
    std::uint64_t total=0;
    for(std::uint64_t lo=1000000;lo<end;lo+=1000000) {
        std::uint64_t count=0;
        long double roots=0;
        for(std::uint64_t p=lo+1;p<lo+1000000;p+=2)
            if(!composite[p/2]) {++count;roots+=sqrtl((long double)p);}
        total+=count;
        out<<lo<<","<<lo+1000000<<","<<count<<","<<roots<<"\n";
    }
    assert(total==50769036);
    std::cout<<"PASS "<<total<<" primes in999newsegments; "
             <<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()
             <<" seconds\n";
}
