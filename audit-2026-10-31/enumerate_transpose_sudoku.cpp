// Independent upper-triangle Sudoku search, with the lower half forced by pi.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <utility>
#include <vector>

int base, n, full, perm[9], board[81], rm[9], cm[9], bm[9], fixed;
std::vector<std::pair<int,int>> cells;
std::uint64_t solutions=0, nodes=0;
unsigned permutations=0, feasible_permutations=0;
std::vector<std::vector<int>> witnesses;

int box(int i,int j) { return base*(i/base)+j/base; }
bool insert(int i,int j,int k) {
    int b=box(i,j), bit=1<<k;
    if ((rm[i]|cm[j]|bm[b])&bit) return false;
    board[i*n+j]=k;rm[i]|=bit;cm[j]|=bit;bm[b]|=bit;
    return true;
}
void remove(int i,int j,int k) {
    int b=box(i,j), bit=1<<k;
    board[i*n+j]=-1;rm[i]^=bit;cm[j]^=bit;bm[b]^=bit;
}
int domain(int i,int j) {
    int d=full&~(rm[i]|cm[j]|bm[box(i,j)]);
    if (i==j) return d&fixed;
    int lower=full&~(rm[j]|cm[i]|bm[box(j,i)]), result=0;
    if (box(i,j)==box(j,i)) d&=~fixed;
    while(d) {
        int k=__builtin_ctz(static_cast<unsigned>(d));d&=d-1;
        if (lower&(1<<perm[k])) result|=1<<k;
    }
    return result;
}
void search(unsigned depth) {
    ++nodes;
    if (depth==cells.size()) {
        ++solutions;
        if (n==4 || witnesses.size()<8) witnesses.emplace_back(board,board+n*n);
        return;
    }
    unsigned best=depth;
    int choices=0, size=100;
    for(unsigned q=depth;q<cells.size();++q) {
        auto [i,j]=cells[q];int d=domain(i,j), count=__builtin_popcount(static_cast<unsigned>(d));
        if(count<size) {best=q;size=count;choices=d;if(size<=1) break;}
    }
    if(!choices) return;
    std::swap(cells[depth],cells[best]);auto [i,j]=cells[depth];
    while(choices) {
        int k=__builtin_ctz(static_cast<unsigned>(choices));choices&=choices-1;
        bool ok=insert(i,j,k);assert(ok);
        if(i!=j) {ok=insert(j,i,perm[k]);assert(ok);}
        search(depth+1);
        if(i!=j) remove(j,i,perm[k]);
        remove(i,j,k);
    }
    std::swap(cells[depth],cells[best]);
}
void run_permutation() {
    fixed=0;for(int k=0;k<n;++k) if(perm[k]==k) fixed|=1<<k;
    // Every diagonal box has exactly base fixed cells, and all n symbols.
    if(__builtin_popcount(static_cast<unsigned>(fixed))!=base) return;
    ++permutations;
    std::fill(rm,rm+n,0);std::fill(cm,cm+n,0);std::fill(bm,bm+n,0);
    std::fill(board,board+n*n,-1);
    for(int j=0;j<n;++j) if(!insert(0,j,j)) return;
    for(int i=1;i<n;++i) if(!insert(i,0,perm[i])) return;
    ++feasible_permutations;
    auto old=solutions;auto oldnodes=nodes;search(0);
    std::cerr << "pi";for(int k=0;k<n;++k) std::cerr << ' ' << perm[k];
    std::cerr << " solutions " << solutions-old << " nodes " << nodes-oldnodes << '\n';
}
void involutions(int start) {
    while(start<n && perm[start]>=0) ++start;
    if(start==n) {run_permutation();return;}
    perm[start]=start;involutions(start+1);perm[start]=-1;
    for(int k=start+1;k<n;++k) if(perm[k]<0) {
        perm[start]=k;perm[k]=start;involutions(start+1);perm[k]=-1;perm[start]=-1;
    }
}
int main(int argc,char** argv) {
    assert(argc==2);base=std::atoi(argv[1]);assert(base==2 || base==3);
    n=base*base;full=(1<<n)-1;
    for(int i=1;i<n;++i) for(int j=i;j<n;++j) cells.emplace_back(i,j);
    std::fill(perm,perm+n,-1);perm[0]=0;involutions(1);
    std::cout << "{\"base\":" << base << ",\"solutions\":" << solutions
              << ",\"nodes\":" << nodes << ",\"involutions_with_required_fixed_points\":" << permutations
              << ",\"compatible_first_row_column\":" << feasible_permutations << ",\"witnesses\":[";
    bool first=true;for(auto& b:witnesses) {
        if(!first) std::cout << ',';first=false;std::cout << '[';
        for(unsigned k=0;k<b.size();++k) {if(k) std::cout << ',';std::cout << b[k];}
        std::cout << ']';
    }
    std::cout << "]}\n";
}
