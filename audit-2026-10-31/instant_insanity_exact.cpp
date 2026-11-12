// Exact strong-uniqueness probability, using transitivity on a chosen 4-cycle.
#define main monte_carlo_main
#include "instant_insanity.cpp"
#undef main
#include <algorithm>
int main(){
 std::vector<Cube> cubes(4);for(int i=0;i<4;i++)cubes[i][0]={i,(i+1)%4};
 std::vector<std::array<int,2>> hidden;for(int a=0;a<4;a++)for(int b=a;b<4;b++)hidden.push_back({a,b});
 std::array<int,3> order{1,2,3};uint64_t visited=0,weight_all=0,strong=0,strong_restricted=0;
 do {
  if(order[0]>order[2])continue;
  std::array<int,4> v{0,order[0],order[1],order[2]},perm{0,1,2,3};
  do {
   for(int i=0;i<4;i++)cubes[i][1]={v[perm[i]],v[(perm[i]+1)%4]};
   for(int code=0;code<10000;code++){
    int x=code,weight=1;std::array<int,4> count{4,4,4,4};
    for(int i=0;i<4;i++){auto h=hidden[x%10];x/=10;cubes[i][2]=h;weight*=h[0]==h[1]?1:2;count[h[0]]++;count[h[1]]++;}
    visited++;weight_all+=weight;auto s=solve(cubes);assert(s.pair_count>=1);
    if(s.strong){strong+=weight;if(*std::min_element(count.begin(),count.end())>=5)strong_restricted+=weight;}
   }
  }while(std::next_permutation(perm.begin(),perm.end()));
 }while(std::next_permutation(order.begin(),order.end()));
 assert(visited==720000&&weight_all==72*65536);
 uint64_t multiplier=1296ULL*1152*16/2;
 std::cout<<"{\"canonical_cases\":"<<visited<<",\"weighted_cases\":"<<weight_all<<",\"strong_weight\":"<<strong
  <<",\"strong_restricted_weight\":"<<strong_restricted<<",\"multiplier\":"<<multiplier
  <<",\"strong_face_colorings\":"<<strong*multiplier<<",\"strong_restricted_face_colorings\":"<<strong_restricted*multiplier
  <<",\"all_face_colorings\":"<<(uint64_t(1)<<48)<<"}"<<std::endl;
}
