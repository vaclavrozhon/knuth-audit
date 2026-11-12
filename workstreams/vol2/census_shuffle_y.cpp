// Full census of the particular Y generator in 3.2.2-(13), omitting zero.
// Compile: g++ -O3 -std=c++17 census_shuffle_y.cpp -o <private-temp>/census-y
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
using U = std::uint64_t;
struct Row { U count=0, first=0, last=0, last_raw=0, gap=0, from=0, to=0; };
int main(int argc, char** argv) {
    if (argc != 2) return 2;
    const U m=U(1)<<35, a=2718281829, c=3141592653, seed=1781072418;
    std::array<Row,64> rows{};
    U y=seed, n=0, zeros=0;
    auto start=std::chrono::steady_clock::now();
    for (U raw=0; raw<m; ++raw) {
        if (y) {
            Row &r=rows[y>>29];
            if (!r.count) r.first=n;
            else if (n-r.last > r.gap) {r.gap=n-r.last;r.from=r.last_raw;r.to=raw;}
            ++r.count; r.last=n; r.last_raw=raw; ++n;
        } else ++zeros;
        y=(a*y+c)&(m-1); // uint64 wrap is harmless before reduction modulo 2^35.
    }
    if(y!=seed || zeros!=1 || n!=m-1) return 3;
    for (U j=0;j<64;++j) {
        Row &r=rows[j];
        if(r.count!=(U(1)<<29)-(j==0)) return 4;
        U gap=n-r.last+r.first;
        if(gap>r.gap) {
            r.gap=gap;r.from=r.last_raw;
            // Raw position of the first visit, recovered in a small prefix.
            U z=seed,raw=0;
            while(!z || (z>>29)!=j) {z=(a*z+c)&(m-1);++raw;}
            r.to=raw+m;
        }
    }
    double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
    std::ofstream out(argv[1]);
    out << "{\"status\":\"complete\",\"modulus\":"<<m<<",\"a\":"<<a<<",\"c\":"<<c
        <<",\"seed\":"<<seed<<",\"raw_steps\":"<<m<<",\"filtered_period\":"<<n
        <<",\"zeros\":"<<zeros<<",\"elapsed_seconds\":"<<elapsed<<",\"rows\":[\n";
    for(U j=0;j<64;++j) {
        const Row &r=rows[j];
        out << (j?",\n":"") << "{\"bucket\":"<<j<<",\"count\":"<<r.count
            <<",\"first\":"<<r.first<<",\"last\":"<<r.last<<",\"max_gap\":"<<r.gap
            <<",\"from_raw\":"<<r.from<<",\"to_raw\":"<<r.to<<"}";
    }
    out << "\n]}\n";
    std::cout << "Completed "<<m<<" states in "<<elapsed<<" seconds.\n";
}
