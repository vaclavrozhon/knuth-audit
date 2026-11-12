// Exact profiles for ordinary queens and the one-diagonal honeycomb relaxation.
#include <cstdint>
#include <iostream>
#include <array>
using namespace std;
array<uint64_t, 18> profile;
unsigned full;
int n;
bool bee;
void visit(int depth, unsigned a, unsigned b, unsigned c) {
  ++profile[depth];
  if (depth == n) return;
  unsigned choices=full & ~(a|b|c);
  while(choices) {
    unsigned bit=choices & -choices;
    choices-=bit;
    visit(depth+1,a|bit,bee?0:(b|bit)>>1,((c|bit)<<1)&full);
  }
}
int main() {
  cout << "[";
  bool first=true;
  for(int kind=0;kind<2;kind++) for(n=0;n<=(kind?14:16);n++) {
    bee=kind;full=(1u<<n)-1;profile.fill(0);visit(0,0,0,0);
    if(!first)cout << ",\n"; first=false;
    cout << "{\"kind\":\"" << (bee?"bee":"queens") << "\",\"n\":" << n << ",\"profile\":[";
    for(int i=0;i<=n;i++){if(i)cout<<",";cout<<profile[i];}
    cout<<"]}";
  }
  cout<<"]\n";
}
