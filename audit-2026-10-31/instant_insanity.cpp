// Uniform independent face colors; enumerate all 2-regular factors exactly.
#include <array>
#include <vector>
#include <random>
#include <iostream>
#include <iomanip>
#include <cassert>
using Cube = std::array<std::array<int,2>,3>;
struct Factor {std::array<int,5> choices; bool cycle;};
std::vector<Factor> factors(const std::vector<Cube>&cubes){
 int n=cubes.size(), limit=1;for(int i=0;i<n;i++)limit*=3;
 std::vector<Factor> out;
 for(int code=0;code<limit;code++){
  int x=code;std::array<int,5> deg{},parent{0,1,2,3,4};Factor f;
  auto root=[&](int a){while(parent[a]!=a)a=parent[a];return a;};bool ok=true;
  for(int i=0;i<n;i++){
   int k=x%3;x/=3;f.choices[i]=k;int a=cubes[i][k][0],b=cubes[i][k][1];
   deg[a]++;deg[b]++;if(deg[a]>2||deg[b]>2){ok=false;break;}parent[root(a)]=root(b);
  }
  if(!ok)continue;for(int a=0;a<n;a++)assert(deg[a]==2);
  f.cycle=true;for(int a=1;a<n;a++)if(root(a)!=root(0))f.cycle=false;
  out.push_back(f);
 }
 return out;
}
struct Result{int factor_count,pair_count;bool strong;};
Result solve(const std::vector<Cube>&cubes){
 auto f=factors(cubes);int n=cubes.size(),pairs=0;bool strong=false;
 for(size_t i=0;i<f.size();i++)for(size_t j=0;j<i;j++){
  bool disjoint=true;for(int k=0;k<n;k++)if(f[i].choices[k]==f[j].choices[k]){disjoint=false;break;}
  if(disjoint){pairs++;strong=f[i].cycle&&f[j].cycle;}
 }
 return {(int)f.size(),pairs,pairs==1&&strong};
}
struct Stats {
 long long count=0,factors=0,strong=0;std::array<long long,11> hist{};
 void add(Result r){count++;factors+=r.factor_count;strong+=r.strong;hist[std::min(r.pair_count,10)]++;}
 void print(int n,bool restricted){
  std::cout<<"{\"n\":"<<n<<",\"restricted_min5\":"<<(restricted?"true":"false")<<",\"samples\":"<<count<<",\"factors_sum\":"<<factors
   <<",\"mean_factors\":"<<(double)factors/count<<",\"strong_unique\":"<<strong<<",\"pair_histogram\":[";
  for(int k=0;k<=10;k++){if(k)std::cout<<",";std::cout<<hist[k];}std::cout<<"]}"<<std::endl;
 }
};
int main(){
 std::cout<<std::setprecision(15);
 std::vector<Cube> example={Cube{{{1,2},{1,3},{3,4}}},Cube{{{0,2},{0,3},{1,4}}},Cube{{{0,1},{1,4},{2,4}}},Cube{{{0,4},{1,3},{2,3}}},Cube{{{0,1},{1,2},{3,4}}}};
 auto ex=solve(example);assert(ex.pair_count==1&&ex.strong);
 std::cout<<"{\"example63_factors\":"<<ex.factor_count<<",\"example63_pairs\":"<<ex.pair_count<<",\"example63_strong\":true}"<<std::endl;
 for(int n:{4,5}){
  uint64_t seed=20261101062ULL+n;std::mt19937_64 rng(seed);std::uniform_int_distribution<int> color(0,n-1);
  Stats all,restricted;std::vector<Cube> cubes(n);const long long trials=5000000;
  for(long long trial=0;trial<trials;trial++){
   std::array<int,5> counts{};
   for(auto &c:cubes)for(auto &pair:c)for(int &a:pair){a=color(rng);counts[a]++;}
   auto result=solve(cubes);all.add(result);bool ok=true;
   for(int a=0;a<n;a++)if(counts[a]<5)ok=false;
   if(ok)restricted.add(result);
  }
  std::cout<<"{\"seed\":"<<seed<<",\"generator\":\"mt19937_64\",\"trials\":"<<trials<<"}"<<std::endl;
  all.print(n,false);restricted.print(n,true);
 }
 return 0;
}
