// Independent value-permutation backtracking for TAOCP 4B DLX103.
// No exact-cover data structures, and no symmetry pruning of the search.
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>

int n, x[32];
uint32_t all_values;
uint64_t nodes=0, solutions=0, reverse_fixed=0, negative_q_fixed=0, qr_fixed=0;
std::ofstream rows;

int mod(int a) { a%=n; return a<0?a+n:a; }

void accept() {
    assert(x[n-1]==n/2);
    ++solutions;
    if(rows.is_open()) {
        for(int i=0;i<n;++i) rows.put(static_cast<char>(x[i]));
    }
    int cut=-1;
    for(int i=1;i<n;++i) if(mod(x[i]-x[i-1])==n/2) cut=i;
    assert(cut>0);
    bool r=true,q=true,qr=(n%8==4);
    for(int i=0;i<n;++i) {
        r &= x[i]==mod(x[n-1-i]-x[n-1]);
        q &= x[i]==mod(x[cut]-x[(cut+i)%n]);
        qr &= x[i]==mod((n/2+1)*(x[(cut+n-1-i)%n]-x[cut-1]));
    }
    reverse_fixed+=r; negative_q_fixed+=q; qr_fixed+=qr;
    if(n>4) assert(static_cast<int>(r)+static_cast<int>(q)+static_cast<int>(qr)<=1);
}

void dfs(int pos,uint32_t used,uint32_t differences) {
    ++nodes;
    if(pos==n) { accept(); return; }
    uint32_t available=all_values & ~used;
    if(pos<n-1) available &= ~(1u<<(n/2));
    else available &= 1u<<(n/2);
    while(available) {
        unsigned v=__builtin_ctz(available); available&=available-1;
        int d=mod(static_cast<int>(v)-x[pos-1]);
        if(differences&(1u<<d)) continue;
        x[pos]=v;
        dfs(pos+1,used|(1u<<v),differences|(1u<<d));
    }
}

int main(int argc,char**argv) {
    assert(argc==2 || argc==3);
    n=std::atoi(argv[1]); assert(n>=2 && n<=24);
    if(argc==3) { rows.open(argv[2],std::ios::binary); assert(rows); }
    all_values=(1u<<n)-1; x[0]=0;
    if(n%2==0) dfs(1,1,1);
    std::cout<<"{\"n\":"<<n<<",\"solutions\":"<<solutions<<",\"nodes\":"<<nodes
             <<",\"reverse_fixed\":"<<reverse_fixed<<",\"negative_q_fixed\":"<<negative_q_fixed
             <<",\"qr_fixed\":"<<qr_fixed<<"}\n";
}
