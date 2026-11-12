// Explicit IEEE round-to-nearest operations, no FMA or reassociation.
// g++ -O2 -std=c++17 -fno-fast-math -ffp-contract=off experiment_logistic.cpp -o ...
#include <algorithm>
#include <array>
#include <cassert>
#include <cfenv>
#include <cmath>
#include <cstdint>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <limits>
#include <vector>

template<class T> uint64_t bits(T x) {
    if constexpr(sizeof(T)==4) {uint32_t b;std::memcpy(&b,&x,4);return b;}
    else {uint64_t b;std::memcpy(&b,&x,8);return b;}
}
template<class T> T step(T x,int expression) {
    if(expression==0) {
        volatile T a=T(4)*x;
        volatile T b=T(1)-x;
        volatile T y=a*b;
        return y;
    }
    volatile T a=x*x;
    volatile T b=x-a;
    volatile T y=T(4)*b;
    return y;
}
template<class T> void trial(double original,int expression) {
    constexpr uint64_t limit=50000000;
    constexpr int samples=65536;
    T seed=T(original),x=seed;
    std::vector<double> sample;
    std::vector<std::array<uint64_t,2>> edges;
    long double s1=0,s2=0;
    for(int j=0;j<samples;j++) {
        sample.push_back(x);s1+=x;s2+=static_cast<long double>(x)*x;
        T y=step(x,expression);
        if(j<128 || j%1024==0)edges.push_back({bits(x),bits(y)});
        x=y;
    }
    std::sort(sample.begin(),sample.end());
    double distance=0;
    for(int j=0;j<samples;j++) {
        double cdf=2/std::acos(-1.0)*std::asin(std::sqrt(sample[j]));
        distance=std::max({distance,(j+1.0)/samples-cdf,cdf-double(j)/samples});
    }
    uint64_t power=1,period=1,evaluations=1;
    T tortoise=seed,hare=step(seed,expression);
    while(tortoise!=hare && evaluations<limit) {
        if(power==period) {tortoise=hare;power*=2;period=0;}
        hare=step(hare,expression);period++;evaluations++;
    }
    bool found=(tortoise==hare);
    uint64_t transient=0,hash=14695981039346656037ull;
    T entry=seed;
    if(found) {
        tortoise=hare=seed;
        for(uint64_t j=0;j<period;j++)hare=step(hare,expression);
        while(tortoise!=hare) {
            tortoise=step(tortoise,expression);hare=step(hare,expression);transient++;
        }
        entry=tortoise;x=entry;
        uint64_t divisor=period;
        std::vector<uint64_t> check_at;
        for(uint64_t p=2;p<=divisor/p;p++)if(divisor%p==0) {
            check_at.push_back(period/p);while(divisor%p==0)divisor/=p;
        }
        if(divisor>1)check_at.push_back(period/divisor);
        // Closure plus nonclosure at period/p for each prime p proves minimality.
        for(uint64_t j=0;j<period;j++) {
            if(std::find(check_at.begin(),check_at.end(),j)!=check_at.end())assert(x!=entry);
            hash^=bits(x);hash*=1099511628211ull;
            T y=step(x,expression);
            if(j<128 || j%std::max(uint64_t(1),period/64)==0)edges.push_back({bits(x),bits(y)});
            x=y;
        }
        assert(x==entry);
    }
    std::cout<<"{\"format\":\"binary"<<8*sizeof(T)<<"\",\"expression\":"<<expression
       <<",\"seed_bits\":"<<bits(seed)<<",\"sample_size\":"<<samples
       <<",\"sample_mean\":"<<double(s1/samples)<<",\"sample_second_moment\":"<<double(s2/samples)
       <<",\"sample_cdf_distance\":"<<distance<<",\"brent_evaluation_limit\":"<<limit
       <<",\"brent_evaluations\":"<<evaluations<<",\"cycle_found\":"<<(found?"true":"false");
    if(found)std::cout<<",\"period\":"<<period<<",\"transient\":"<<transient
       <<",\"entry_bits\":"<<bits(entry)<<",\"cycle_hash_fnv64\":"<<hash;
    std::cout<<",\"edge_probes\":[";
    for(size_t j=0;j<edges.size();j++) {
        if(j)std::cout<<',';
        std::cout<<'['<<edges[j][0]<<','<<edges[j][1]<<']';
    }
    std::cout<<"]}"<<std::endl;
}
int main() {
    static_assert(std::numeric_limits<float>::is_iec559 && std::numeric_limits<float>::digits==24);
    static_assert(std::numeric_limits<double>::is_iec559 && std::numeric_limits<double>::digits==53);
    assert(std::fegetround()==FE_TONEAREST);
    std::cout<<std::setprecision(17);
    for(int expression=0;expression<2;expression++)
        for(double seed:{0.0,0.25,0.5,0.75,1.0,0.1,0.123456789,1.0/7,0.3141592653589793,0.625}) {
            trial<float>(seed,expression);trial<double>(seed,expression);
        }
}
