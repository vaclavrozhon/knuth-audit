// Independent occupancy-bitset count. No linked lists, stored predecessor
// array, goto state machine, or printed forcing modification is used.
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <array>
using namespace std;
using U = uint64_t;
int n, special, half;
bool symmetry;
array<U, 18> profile;
U count_solutions(U empty, unsigned remaining, int depth) {
  ++profile[depth];
  if (!remaining) return 1;
  const int pos = __builtin_ctzll(empty); // zero-based first empty cell
  const int largest = 31 - __builtin_clz(remaining);
  const int last_start = 2*n-1-(3*largest)/2;
  if (pos > last_start) return 0;
  unsigned choices = pos == last_start ? (1u << largest) : remaining;
  U total = 0;
  while (choices) {
    unsigned bit = choices & -choices;
    choices -= bit;
    const int k = __builtin_ctz(bit);
    if (symmetry && k == special && pos+1 > half) continue;
    int mate = pos+(3*k)/2;
    if (mate >= 2*n) continue;
    U cells = (U(1) << pos) | (U(1) << mate);
    if ((empty & cells) == cells)
      total += count_solutions(empty ^ cells, remaining ^ bit, depth+1);
  }
  return total;
}
int main(int argc, char **argv) {
  int maximum = argc > 1 ? atoi(argv[1]) : 16;
  cout << "[\n";
  for (n=1;n<=maximum;n++) {
    profile.fill(0);
    const int subtract[] = {0,1,2,0}, add[] = {0,1,2,1};
    special = n-subtract[n%4]; half = n/4+add[n%4]; symmetry = n>=4;
    // The elementary parity proof gives zero without an exponential search.
    U count = n%4 == 3 ? 0 : count_solutions((U(1)<<(2*n))-1, (1u<<(n+1))-2, 0);
    U nodes=0; for(U value:profile) nodes+=value;
    if(n>1)cout<<",\n";
    cout << "{\"n\":" << n << ",\"solutions\":" << count*(symmetry?2:1)
         << ",\"representatives\":" << count << ",\"nodes\":" << nodes
         << ",\"parity_only\":" << (n%4==3?"true":"false") << "}" << flush;
    cerr << "n=" << n << ": " << count*(symmetry?2:1) << " solutions; " << nodes << " nodes\n";
  }
  cout << "\n]\n";
}
