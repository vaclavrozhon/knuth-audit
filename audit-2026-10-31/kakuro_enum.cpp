// Exhaustive distinct-row/column fillings for X432, independent of XCC.
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

struct Enumeration {
  int q,base;bool full;std::vector<std::pair<int,int>> cells;
  std::array<int,3> rowmask{},colmask{},rowsum{},colsum{};
  std::array<uint64_t,10> rgs{};uint64_t total=0;
  std::vector<uint8_t> counts;std::vector<uint64_t> first;
  Enumeration(int alphabet,bool square):q(alphabet),base(3*alphabet+1),full(square) {
    for(int r=0;r<3;r++)for(int c=0;c<3;c++)if(full || !((r==0&&c==2)||(r==2&&c==0)))cells.emplace_back(r,c);
    size_t size=1;for(int i=0;i<5;i++)size*=base;
    counts.resize(size);first.resize(size);
  }
  void restricted(int pos,int used) {
    if(pos==int(cells.size())){rgs[used]++;return;}
    auto [r,c]=cells[pos];
    for(int digit=1;digit<=used+1;digit++) {
      int bit=1<<(digit-1);if((rowmask[r]|colmask[c])&bit)continue;
      rowmask[r]|=bit;colmask[c]|=bit;restricted(pos+1,std::max(used,digit));
      rowmask[r]^=bit;colmask[c]^=bit;
    }
  }
  void solve(int pos,uint64_t code) {
    if(pos==int(cells.size())) {
      total++;size_t key=0;
      for(int s:rowsum)key=key*base+s;
      key=(key*base+colsum[0])*base+colsum[1];
      if(!counts[key]){counts[key]=1;first[key]=code;}else counts[key]=2;
      return;
    }
    auto [r,c]=cells[pos];int available=((1<<q)-1)&~(rowmask[r]|colmask[c]);
    while(available) {
      int bit=available&-available;available^=bit;int digit=__builtin_ctz(unsigned(bit))+1;
      rowmask[r]|=bit;colmask[c]|=bit;rowsum[r]+=digit;colsum[c]+=digit;
      solve(pos+1,code|(uint64_t(digit)<<(4*pos)));
      rowmask[r]^=bit;colmask[c]^=bit;rowsum[r]-=digit;colsum[c]-=digit;
    }
  }
  void output(const std::string&path,double elapsed)const {
    std::ofstream f(path);if(!f)throw std::runtime_error("cannot open output");
    uint64_t unique=0,distinct=0;
    for(size_t key=0;key<counts.size();key++)if(counts[key]) {
      distinct++;if(counts[key]!=1)continue;unique++;
      std::array<int,6> sums{};size_t value=key;
      for(int j=4;j>=0;j--){sums[j]=value%base;value/=base;}
      sums[5]=sums[0]+sums[1]+sums[2]-sums[3]-sums[4];
      f<<"{\"sums\":[";for(int j=0;j<6;j++){if(j)f<<',';f<<sums[j];}
      f<<"],\"digits\":[";for(size_t j=0;j<cells.size();j++){if(j)f<<',';f<<((first[key]>>(4*j))&15);}
      f<<"]}\n";
    }
    std::cout<<"{\"shape\":\""<<(full?'b':'a')<<"\",\"alphabet\":"<<q<<",\"fillings\":"<<total
             <<",\"distinct_sum_sequences\":"<<distinct<<",\"unique_puzzles\":"<<unique<<",\"rgs_counts\":[";
    for(int i=0;i<10;i++){if(i)std::cout<<',';std::cout<<rgs[i];}
    std::cout<<"],\"seconds\":"<<elapsed<<"}\n";
  }
};

int main(int argc,char**argv) {
  try {
    if(argc!=4){std::cerr<<"usage: kakuro_enum a|b alphabet uniques.jsonl\n";return 2;}
    int q=std::stoi(argv[2]);if(q<1||q>9)return 2;
    bool full=std::string(argv[1])=="b";
    auto start=std::chrono::steady_clock::now();Enumeration e(q,full);
    e.restricted(0,0);e.solve(0,0);
    e.output(argv[3],std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count());
  }catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 1;}
}
