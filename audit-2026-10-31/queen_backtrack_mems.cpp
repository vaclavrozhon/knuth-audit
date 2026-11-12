// Exact accounting of the search methods on 4B pp.32--33.
// Enumerate legal prefixes with bits, then count the accesses made by the
// described slower methods. Independent literal small cases check the counts.
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
using namespace std;
using U32=uint32_t;
using U64=uint64_t;
int n;
U32 mask;
array<U32,16> queens{};
array<U64,17> profile{};
U64 forward_reads=0, reverse_reads=0, array_test_reads=0;

void search(int row,U32 cols,U32 left,U32 right,U64 multiplicity) {
  profile[row]+=multiplicity;
  if (row==n) return;
  // At an ordinary B* node all n trials read a_t; n-row also read b_t,
  // and n-popcount(cols|right) also read c_t. In a mirrored prefix the
  // two diagonal masks swap, so it must not blindly double this last term.
  array_test_reads+=multiplicity*U64(2*n-row);
  if (multiplicity==2)
    array_test_reads+=U64(2*n-__builtin_popcount(cols|left)-__builtin_popcount(cols|right));
  else
    array_test_reads+=U64(n-__builtin_popcount(cols|right));
  // For a sequential comparison against earlier queens, the j-th queen is
  // fetched for exactly the trial columns not already rejected by earlier
  // comparisons. Union masks count those trial columns without trying each.
  U32 blocked=0;
  for (int j=0;j<row;++j) {
    forward_reads+=multiplicity*U64(n-__builtin_popcount(blocked));
    const U32 bit=queens[j]; const int distance=row-j;
    blocked|=(bit|(bit<<distance)|(bit>>distance))&mask;
  }
  blocked=0;
  for (int j=row-1;j>=0;--j) {
    reverse_reads+=multiplicity*U64(n-__builtin_popcount(blocked));
    const U32 bit=queens[j]; const int distance=row-j;
    blocked|=(bit|(bit<<distance)|(bit>>distance))&mask;
  }
  U32 available=mask&~(cols|left|right);
  while (available) {
    U32 bit=available&-available; available-=bit;
    U64 next_multiplicity=multiplicity;
    if (!row) {
      const int column=__builtin_ctz(bit);
      if (column>=(n+1)/2) break;
      next_multiplicity=column<n/2 ? 2 : 1;
    }
    queens[row]=bit;
    search(row+1,cols|bit,((left|bit)<<1)&mask,(right|bit)>>1,next_multiplicity);
  }
}

int main(int argc,char** argv) {
  if (argc!=2) return 2;
  n=stoi(argv[1]); if (n<1 || n>16) return 2;
  mask=(U32(1)<<n)-1;
  search(0,0,0,0,1);
  U64 nodes=0;for (int i=0;i<=n;++i) nodes+=profile[i];
  const U64 edges=nodes-1, initialization=5*n-2;
  cout<<"{\"n\":"<<n<<",\"nodes\":"<<nodes<<",\"solutions\":"<<profile[n]
      <<",\"profile\":[";
  for(int i=0;i<=n;++i){if(i)cout<<',';cout<<profile[i];}
  cout<<"],\"successful_edges\":"<<edges
      <<",\"naive_forward_comparison_reads\":"<<forward_reads
      <<",\"naive_reverse_comparison_reads\":"<<reverse_reads
      <<",\"naive_forward_total_mems\":"<<forward_reads+2*edges
      <<",\"naive_reverse_total_mems\":"<<reverse_reads+2*edges
      <<",\"array_test_reads\":"<<array_test_reads
      <<",\"array_initialization_mems\":"<<initialization
      <<",\"array_total_mems\":"<<array_test_reads+8*edges+initialization
      <<",\"register_Bstar_total_mems\":"<<2*edges
      <<",\"walker_total_mems\":"<<8*edges<<"}\n";
}
