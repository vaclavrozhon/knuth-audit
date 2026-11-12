// Independent exhaustive dual-cube edge colorings and unordered 3-partitions.
// No XCC input or geometry table is read. Bit x,y,z identifies a cube vertex;
// the corresponding octahedron face has cyclic order reversed at odd parity.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>

struct Entry { uint64_t count=0; uint32_t witness=0; };

int main(int argc, char **argv) {
  if (argc != 3) return 2;
  int tile[64], index[64]; std::fill(index,index+64,-1);
  int n=0;
  for (int code=0;code<64;code++) {
    int r1=((code&15)<<2)|(code>>4), r2=((code&3)<<4)|(code>>2);
    int canon=std::min({code,r1,r2});
    if (index[canon]<0) index[canon]=n++;
    tile[code]=index[canon];
  }
  if (n!=24) return 3;
  std::map<uint32_t,Entry> sets;
  uint64_t accepted=0;
  for (uint32_t coloring=0;coloring<(1u<<24);coloring++) {
    uint32_t mask=0; bool ok=true;
    for (int xyz=0;xyz<8;xyz++) {
      int x=xyz>>2,y=(xyz>>1)&1,z=xyz&1;
      int a=(coloring>>(2*(2*y+z)))&3;
      int b=(coloring>>(2*(4+2*x+z)))&3;
      int c=(coloring>>(2*(8+2*x+y)))&3;
      if ((x+y+z)&1) std::swap(b,c);
      uint32_t bit=1u<<tile[16*a+4*b+c];
      if (mask&bit) { ok=false; break; }
      mask|=bit;
    }
    if (ok) {
      Entry &e=sets[mask]; if (!e.count) e.witness=coloring;
      e.count++; accepted++;
    }
  }
  std::ofstream out(argv[1]);
  std::array<std::vector<uint32_t>,24> containing;
  // Direct-address membership avoids hashing and makes the final complement test exact.
  std::vector<uint8_t> member(1u<<24,0);
  for (const auto &[mask,e]:sets) {
    out<<mask<<'\t'<<e.count<<'\t';
    for (int j=0;j<12;j++) out<<char('a'+((e.witness>>(2*j))&3));
    out<<'\n'; member[mask]=1;
    for (int j=0;j<24;j++) if ((mask>>j)&1) containing[j].push_back(mask);
  }
  out.close();
  std::ofstream samples(argv[2]);
  uint64_t partitions=0,disjoint_pairs=0;
  const uint32_t all=(1u<<24)-1;
  for (uint32_t a:containing[0]) {
    uint32_t remaining=all^a;
    int first=__builtin_ctz(remaining);
    for (uint32_t b:containing[first]) if (!(a&b)) {
      disjoint_pairs++;
      uint32_t c=remaining^b;
      if (member[c]) {
        partitions++;
        if (partitions%1000==0) samples<<a<<'\t'<<b<<'\t'<<c<<'\n';
      }
    }
  }
  samples.close();
  std::cout<<"{\"colorings_examined\":16777216,\"solutions\":"<<accepted
           <<",\"distinct_sets\":"<<sets.size()<<",\"partitions\":"<<partitions
           <<",\"disjoint_pairs\":"<<disjoint_pairs<<",\"sample_period\":1000}\n";
  return out.fail() || samples.fail();
}
