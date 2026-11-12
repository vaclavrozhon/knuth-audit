// X262(b): exact signature recursion on the corrected triangular region.
#include <gmpxx.h>
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <map>
#include <tuple>
#include <unordered_map>
#include <vector>

struct Hexagon {
  using Cell=std::tuple<int,int,int>;
  std::vector<Cell> cells;
  std::vector<std::vector<int>> next;
  std::unordered_map<uint64_t,mpz_class> memo;
  int span=0;uint64_t nodes=0,successful=0,calls=0;
  Hexagon(int m,int n,bool prime_first) {
    for(int x=0;x<n+m;x++) for(int y=0;y<2*m;y++) for(int k=0;k<2;k++) {
      int prime=prime_first?1-k:k;
      if(!prime && m<=x+y && x+y<n+2*m) cells.emplace_back(x,y,prime);
      if(prime && m-1<=x+y && x+y<n+2*m-1) cells.emplace_back(x,y,prime);
    }
    std::map<Cell,int> indices;
    for(int i=0;i<int(cells.size());i++)indices[cells[i]]=i;
    next.resize(cells.size());
    for(int i=0;i<int(cells.size());i++) {
      auto[x,y,p]=cells[i];if(p)continue;
      for(auto[dx,dy]:std::vector<std::pair<int,int>>{{0,0},{0,1},{1,0}}) {
        auto other=indices.find({x-dx,y-dy,1});
        if(other==indices.end())continue;
        int j=other->second;int a=std::min(i,j),b=std::max(i,j);
        next[a].push_back(b);span=std::max(span,b-a);
      }
    }
    if(span>48 || cells.size()>65535)throw std::runtime_error("signature too wide");
  }
  mpz_class solve(int pos,uint64_t mask) {
    calls++;
    while(pos<int(cells.size()) && (mask&1)) {mask>>=1;pos++;}
    if(pos==int(cells.size())) {if(mask)throw std::runtime_error("frontier");return 1;}
    uint64_t key=(uint64_t(pos)<<span)|mask;
    auto old=memo.find(key);if(old!=memo.end())return old->second;
    mpz_class total=0;
    for(int other:next[pos]) {
      uint64_t flag=uint64_t(1)<<(other-pos);
      if(mask&flag)continue;
      mpz_class child=solve(pos+1,(mask|flag)>>1);
      if(child!=0)nodes++;
      total+=child;
    }
    if(total!=0)successful++;
    memo.emplace(key,total);return total;
  }
};

int main(int argc,char**argv) {
  if(argc!=4){std::cerr<<"usage: hexagon_zdd m n prime_first\n";return 2;}
  int m=std::stoi(argv[1]),n=std::stoi(argv[2]);bool first=std::stoi(argv[3]);
  auto start=std::chrono::steady_clock::now();Hexagon h(m,n,first);mpz_class count=h.solve(0,0);
  std::cout<<"{\"m\":"<<m<<",\"n\":"<<n<<",\"prime_first\":"<<(first?"true":"false")
           <<",\"items\":"<<h.cells.size()<<",\"frontier_span\":"<<h.span
           <<",\"solutions\":\""<<count<<"\",\"zdd_nodes\":"<<(h.nodes?h.nodes+2:1)
           <<",\"cached_nonempty_states\":"<<h.memo.size()<<",\"successful_nonempty_states\":"<<h.successful
           <<",\"calls\":"<<h.calls<<",\"seconds\":"
           <<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"}\n";
}
