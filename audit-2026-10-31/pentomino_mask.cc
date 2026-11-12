// Independent occupied-cell/used-piece DFS; no dancing-links data structure.
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using U = std::uint64_t;
struct Move { U cells; unsigned piece; };
std::vector<Move> moves;
std::array<std::vector<int>,72> lists;
std::array<U,13> profile{};
std::string primary;
bool nomrv;
U solutions=0;
constexpr U board=(U(1)<<60)-1;

void visit(U occupied,unsigned used,int depth) {
  ++profile[depth];
  if (depth==12) { assert(occupied==board && used==4095); ++solutions; return; }
  std::array<int,1236> best{},candidate{};
  unsigned bestsize=1237;
  // Cell indices0..59 come before piece indices60..71 in the all-primary case.
  const int begin=primary=="pieces"?60:0;
  const int end=primary=="cells"?60:72;
  for (int item=begin;item<end;++item) {
    if (item<60 ? bool(occupied&(U(1)<<item)) : bool(used&(1u<<(item-60)))) continue;
    unsigned size=0;
    for (int i:lists[item]) {
      const auto &m=moves[i];
      if (!(m.cells&occupied) && !(used&m.piece)) candidate[size++]=i;
    }
    if (size<bestsize) {
      bestsize=size;
      if (!size) return;
      for (unsigned j=0;j<size;++j) best[j]=candidate[j];
    }
    if (nomrv) break;
  }
  assert(bestsize<=1236);
  for (unsigned j=0;j<bestsize;++j) {
    const auto &m=moves[best[j]];
    visit(occupied|m.cells,used|m.piece,depth+1);
  }
}

int main(int argc,char**argv) {
  assert(argc==2);
  std::ifstream f(argv[1]);int n,mode;
  f>>primary>>mode>>n;nomrv=mode;
  assert(f && n<=1236 && (primary=="all" || primary=="cells" || primary=="pieces"));
  for (int i=0;i<n;++i) {
    int p;U cells;f>>std::dec>>p>>std::hex>>cells;
    assert(f && p>=0 && p<12 && __builtin_popcountll(cells)==5 && !(cells&~board));
    moves.push_back({cells,1u<<p});lists[60+p].push_back(i);
    for (int j=0;j<60;++j) if (cells&(U(1)<<j)) lists[j].push_back(i);
  }
  visit(0,0,0);U nodes=0;for (auto v:profile)nodes+=v;
  std::cout<<"{\"solutions\":"<<solutions<<",\"nodes\":"<<nodes<<",\"profile\":[";
  for (int i=0;i<13;++i)std::cout<<(i?",":"")<<profile[i];
  std::cout<<"]}\n";
}
