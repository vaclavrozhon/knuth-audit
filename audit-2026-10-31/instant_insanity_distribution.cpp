// Exact distribution for four cubes: quotient only by irrelevant face-pair
// order/orientation and cube order; preserve each orbit's integer weight.
#define main monte_carlo_main
#include "instant_insanity.cpp"
#undef main
#include <algorithm>
struct Type {Cube cube;uint64_t weight;std::array<int,4> colors{};};
struct ExactStats {
 uint64_t cases=0,factor_sum=0,pair_sum=0,strong=0;std::array<uint64_t,11> hist{};
 void add(Result r,uint64_t w){cases+=w;factor_sum+=w*r.factor_count;pair_sum+=w*r.pair_count;strong+=w*r.strong;hist[std::min(r.pair_count,10)]+=w;}
 void print(bool restricted){
  std::cout<<"{\"restricted_min5\":"<<(restricted?"true":"false")<<",\"face_colorings\":"<<cases<<",\"factor_sum\":"<<factor_sum<<",\"pair_sum\":"<<pair_sum<<",\"strong_unique\":"<<strong<<",\"pair_histogram\":[";
  for(int i=0;i<11;i++){if(i)std::cout<<",";std::cout<<hist[i];}std::cout<<"]}"<<std::endl;
 }
};
int main(){
 std::vector<std::array<int,2>> edges;for(int a=0;a<4;a++)for(int b=a;b<4;b++)edges.push_back({a,b});
 std::vector<Type> types;uint64_t total_weight=0;
 for(int i=0;i<10;i++)for(int j=i;j<10;j++)for(int k=j;k<10;k++){
  Type t;t.cube={edges[i],edges[j],edges[k]};
  t.weight=(i==k?1:(i==j||j==k?3:6));
  for(auto e:t.cube){t.weight*=e[0]==e[1]?1:2;t.colors[e[0]]++;t.colors[e[1]]++;}
  total_weight+=t.weight;types.push_back(t);
 }
 assert(types.size()==220&&total_weight==4096);
 ExactStats all,restricted;uint64_t multiset_count=0;std::vector<Cube> cubes(4);
 for(int a=0;a<220;a++){
  cubes[0]=types[a].cube;
  for(int b=a;b<220;b++){cubes[1]=types[b].cube;
   for(int c=b;c<220;c++){cubes[2]=types[c].cube;
    for(int d=c;d<220;d++){
     cubes[3]=types[d].cube;auto result=solve(cubes);multiset_count++;
     int indices[4]={a,b,c,d},den=1,run=1;
     for(int i=1;i<=4;i++){
      if(i<4&&indices[i]==indices[i-1])run++;
      else{for(int k=2;k<=run;k++)den*=k;run=1;}
     }
     uint64_t weight=(24/den)*types[a].weight*types[b].weight*types[c].weight*types[d].weight;
     all.add(result,weight);bool ok=true;
     for(int k=0;k<4;k++)if(types[a].colors[k]+types[b].colors[k]+types[c].colors[k]+types[d].colors[k]<5)ok=false;
     if(ok)restricted.add(result,weight);
    }
   }
  }
  if(a%20==0)std::cerr<<"first cube type "<<a<<", multisets "<<multiset_count<<std::endl;
 }
 all.print(false);restricted.print(true);
 std::cerr<<"total multisets "<<multiset_count<<", weighted cases "<<all.cases<<std::endl;
 assert(multiset_count==223ULL*222*221*220/24&&all.cases==(uint64_t(1)<<48));
 assert(all.strong==1214459412480ULL&&restricted.strong==179636797440ULL);
}
