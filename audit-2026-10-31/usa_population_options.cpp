// Enumerate each connected vertex set once by frontier include/exclude decisions.
// Output only the interval-qualified sets whose residual components pass242.
#include <cstdint>
#include <iostream>
#include <vector>
using U = std::uint64_t;
int n;
long long low, high;
U all;
std::vector<U> adj;
std::vector<long long> weight;
U nodes=0, interval_count=0, reduced_count=0;
long long population(U s) {
  long long result=0;
  while(s) { int v=__builtin_ctzll(s); s&=s-1; result+=weight[v]; }
  return result;
}
bool residual_ok(U remaining) {
  while(remaining) {
    U frontier=remaining&-remaining, component=0;
    long long total=0;
    while(frontier) {
      int v=__builtin_ctzll(frontier); U b=U(1)<<v;
      frontier^=b;
      if(component&b) continue;
      component|=b; total+=weight[v];
      frontier|=adj[v]&remaining&~component;
    }
    remaining^=component;
    if(total<low*((total+high-2)/(high-1))) return false;
  }
  return true;
}
void visit(U chosen, U frontier, U forbidden, long long sum) {
  ++nodes;
  if(sum>=low) {
    ++interval_count;
    if(residual_ok(all^chosen)) { ++reduced_count; std::cout<<chosen<<'\n'; }
  }
  while(frontier) {
    U b=frontier&-frontier;frontier^=b;
    int v=__builtin_ctzll(b);
    if(sum+weight[v]<high)
      visit(chosen|b,(frontier|adj[v])&~(chosen|b|forbidden),forbidden,sum+weight[v]);
    forbidden|=b;
  }
}
int main() {
  if(!(std::cin>>n>>low>>high) || n<1 || n>63 || low<1 || high<=low) return 2;
  all=(U(1)<<n)-1;
  adj.resize(n);weight.resize(n);
  for(int i=0;i<n;++i) {
    std::cin>>weight[i]>>adj[i];
    if(weight[i]<=0 || (adj[i]&~all) || (adj[i]&(U(1)<<i))) return 3;
  }
  for(int i=0;i<n;++i) for(int j=0;j<n;++j)
    if(bool(adj[i]&(U(1)<<j))!=bool(adj[j]&(U(1)<<i))) return 4;
  for(int root=0;root<n;++root) {
    U b=U(1)<<root,forbidden=b-1;
    if(weight[root]<high) visit(b,adj[root]&~forbidden,forbidden,weight[root]);
  }
  std::cerr<<"{\"complete\":true,\"nodes\":"<<nodes
           <<",\"interval_count\":"<<interval_count<<",\"reduced_count\":"<<reduced_count<<"}\n";
}
