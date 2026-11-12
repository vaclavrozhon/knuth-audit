// Independent samples for the two additional estimates on printed pp.48 and 51.
#include <array>
#include <cassert>
#include <cstdint>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <random>
uint64_t adj[64];
long double queen(std::mt19937_64 &rng){
 uint64_t a=0,b=0,c=0;long double weight=1,total=1;
 while(a!=UINT64_MAX){
  uint64_t choices=~(a|b|c);int d=__builtin_popcountll(choices);
  if(!d)break;
  int k=std::uniform_int_distribution<int>(0,d-1)(rng);
  while(k--)choices&=choices-1;
  uint64_t x=choices&-choices;weight*=d;total+=weight;
  a|=x;b=(b|x)<<1;c=(c|x)>>1;
 }
 return total;
}
long double knight(std::mt19937_64 &rng){
 uint64_t used=0;int current=0;long double weight=1;
 while(current!=63){
  used|=uint64_t(1)<<current;
  uint64_t reached=uint64_t(1)<<63,front=reached;
  while(front){uint64_t next=0;
   while(front){int u=__builtin_ctzll(front);front&=front-1;next|=adj[u];}
   front=next&~used&~reached;reached|=front;
  }
  uint64_t choices=adj[current]&reached;int d=__builtin_popcountll(choices);assert(d>0);
  int k=std::uniform_int_distribution<int>(0,d-1)(rng);while(k--)choices&=choices-1;
  current=__builtin_ctzll(choices);weight*=d;
 }
 return weight;
}
int main(){
 for(int a=0;a<64;a++)for(int b=0;b<64;b++){
  int dx=a/8-b/8,dy=a%8-b%8;if(dx*dx+dy*dy==5)adj[a]|=uint64_t(1)<<b;
 }
 std::cout<<std::setprecision(20);
 for(int mode=0;mode<2;mode++)for(int batch=0;batch<20;batch++){
  uint64_t seed=20261101048ULL+1000*mode+batch;std::mt19937_64 rng(seed);
  int n=mode?10000:1000;long double sum=0,sq=0,mx=0;
  for(int i=0;i<n;i++){long double v=mode?knight(rng):queen(rng);sum+=v;sq+=v*v;mx=std::max(mx,v);}
  long double var=(sq-sum*sum/n)/(n-1);
  std::cout<<"{\"problem\":\""<<(mode?"knight8":"queens64")<<"\",\"batch\":"<<batch<<",\"seed\":"<<seed
   <<",\"trials\":"<<n<<",\"mean\":"<<sum/n<<",\"standard_error\":"<<sqrtl(var/n)<<",\"chi\":"<<mx/sum<<"}"<<std::endl;
 }
}
