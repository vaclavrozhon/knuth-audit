// DLX137: forced radial match reduces each outer nut to a directed pair.
// Complete depth-first search, capped at 3 only for histogram classification.
#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <vector>

using Nuts = std::array<int,7>;
using Word = std::array<int,6>;
std::vector<Word> types;
int left_digit[120][7], right_digit[120][7];

void initialize() {
  Word w{1,2,3,4,5,6};
  do { types.push_back(w); } while (std::next_permutation(w.begin()+1,w.end()));
  assert(types.size()==120);
  for (int t=0;t<120;++t) for (int i=0;i<6;++i) {
    left_digit[t][types[t][i]]=types[t][(i+1)%6];
    right_digit[t][types[t][i]]=types[t][(i+5)%6];
  }
}

struct Search {
  int left[6][7], right[6][7], rule, cap, count;
  bool match(int a,int b) const { return rule ? a+b==7 : a==b; }
  void dfs(int k,unsigned unused,int first_left,int previous_right) {
    if (count>=cap) return;
    if (k==6) { if (match(previous_right,first_left)) ++count; return; }
    unsigned candidates=unused;
    while (candidates && count<cap) {
      int i=__builtin_ctz(candidates); candidates&=candidates-1;
      if (k && !match(previous_right,left[k][i])) continue;
      dfs(k+1,unused^(1u<<i), k ? first_left : left[0][i],right[k][i]);
    }
  }
  int solve(const Nuts& nuts,int matching_rule,int limit) {
    rule=matching_rule; cap=limit; count=0;
    for (int c=0;c<7 && count<cap;++c) {
      for (int k=0;k<6;++k) {
        int inward=types[nuts[c]][k];
        if (rule) inward=7-inward;
        for (int i=0;i<7;++i) {
          left[k][i]=left_digit[nuts[i]][inward];
          right[k][i]=right_digit[nuts[i]][inward];
        }
      }
      dfs(0,127u^(1u<<c),0,0);
    }
    return count;
  }
};

// Uniform bounded integers under uniform 64-bit draws; no modulo bias.
uint64_t bounded(std::mt19937_64& rng,uint64_t bound) {
  uint64_t threshold=(-bound)%bound, x;
  do { x=rng(); } while (x<threshold);
  return x%bound;
}

int main(int argc,char** argv) {
  initialize(); Search search;
  if (argc==2 && std::string(argv[1])=="--cases") {
    Nuts nuts;
    while (std::cin>>nuts[0]) {
      for (int i=1;i<7;++i) { std::cin>>nuts[i]; assert(std::cin); }
      auto check=nuts; std::sort(check.begin(),check.end());
      assert(check[0]>=0 && check[6]<120 && std::adjacent_find(check.begin(),check.end())==check.end());
      std::cout<<search.solve(nuts,0,1000000)<<' '<<search.solve(nuts,1,1000000)<<'\n';
    }
    return 0;
  }
  if (argc!=4) { std::cerr<<"Usage: binary trials seed records.bin | binary --cases\n"; return 2; }
  uint64_t trials=std::stoull(argv[1]),seed=std::stoull(argv[2]);
  std::mt19937_64 rng(seed);
  std::ofstream out(argv[3],std::ios::binary); assert(out);
  uint64_t histogram[4][4]={}, totals[120]={};
  auto start=std::chrono::steady_clock::now();
  for (uint64_t t=0;t<trials;++t) {
    Nuts nuts;
    for (int i=0;i<7;++i) {
      int x;
      do { x=static_cast<int>(bounded(rng,120)); }
      while (std::find(nuts.begin(),nuts.begin()+i,x)!=nuts.begin()+i);
      nuts[i]=x;
    }
    std::sort(nuts.begin(),nuts.end());
    int eq=search.solve(nuts,0,3),sum=search.solve(nuts,1,3);
    ++histogram[eq][sum];
    unsigned char record[9];
    for (int i=0;i<7;++i) { record[i]=nuts[i]; ++totals[nuts[i]]; }
    record[7]=eq; record[8]=sum; out.write(reinterpret_cast<char*>(record),9);
    if ((t+1)%100000==0) std::cerr<<"completed "<<(t+1)<<" / "<<trials<<'\n';
  }
  out.close(); assert(out);
  std::cout<<"{\"trials\":"<<trials<<",\"seed\":"<<seed<<",\"histogram\":[";
  for (int i=0;i<4;++i) {
    if (i) std::cout<<',';
    std::cout<<'[';
    for (int j=0;j<4;++j) { if (j) std::cout<<','; std::cout<<histogram[i][j]; }
    std::cout<<']';
  }
  std::cout<<"],\"type_occurrences\":[";
  for (int i=0;i<120;++i) { if (i) std::cout<<','; std::cout<<totals[i]; }
  std::cout<<"],\"elapsed_seconds\":"<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"}\n";
}
