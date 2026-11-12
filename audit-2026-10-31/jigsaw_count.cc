// Independent cell-mask recursion, component factorization and bounded memoization.
#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using U=__uint128_t;
struct Hash {size_t operator()(U a)const{return uint64_t(a)^((uint64_t(a>>64)+0x9e3779b97f4a7c15ULL)*0xbf58476d1ce4e5b9ULL);}};
int n;U full;uint64_t calls=0,hits=0,splits=0;
std::vector<U> neighbors;
std::vector<std::vector<U>> options;
std::unordered_set<U,Hash> allowed;
std::unordered_map<U,uint64_t,Hash> memo;
int pop(U a){return __builtin_popcountll(uint64_t(a))+__builtin_popcountll(uint64_t(a>>64));}
int first(U a){return uint64_t(a)?__builtin_ctzll(uint64_t(a)):64+__builtin_ctzll(uint64_t(a>>64));}
uint64_t count(U remaining){
 ++calls;
 if(!remaining)return 1;
 if(pop(remaining)==n)return allowed.count(remaining);
 auto old=memo.find(remaining);if(old!=memo.end()){++hits;return old->second;}
 // Distinct connected components can be tiled independently.
 U unseen=remaining;std::vector<U> components;
 while(unseen){
  U component=U(1)<<first(unseen),front=component;unseen^=component;
  while(front){int v=first(front);front&=front-1;U added=neighbors[v]&unseen;
   unseen^=added;component|=added;front|=added;}
  if(pop(component)%n)return 0;
  components.push_back(component);
 }
 uint64_t answer=0;
 if(components.size()>1){
  ++splits;answer=1;for(U c:components){answer*=count(c);if(!answer)break;}
 }else{
  int v=first(remaining);
  for(U row:options[v])if((row&remaining)==row)answer+=count(remaining^row);
 }
 if(memo.size()<2000000)memo.emplace(remaining,answer);
 return answer;
}
int main(int argc,char**argv){
 if(argc!=2)return 2;
 std::ifstream in(argv[1]);size_t total;in>>n>>total;
 if(n<2||n>9)return 3;
 full=(U(1)<<(n*n))-1;options.resize(n*n);neighbors.resize(n*n);
 for(int v=0;v<n*n;++v){int r=v/n,c=v%n;
  if(r)neighbors[v]|=U(1)<<(v-n);if(r+1<n)neighbors[v]|=U(1)<<(v+n);
  if(c)neighbors[v]|=U(1)<<(v-1);if(c+1<n)neighbors[v]|=U(1)<<(v+1);}
 for(size_t i=0;i<total;++i){std::string s;in>>s;U mask=0;
  for(char ch:s){int x=ch<='9'?ch-'0':ch-'a'+10;if(x<0||x>15)return 4;mask=16*mask+x;}
  if(pop(mask)!=n||(mask&full)!=mask||!allowed.insert(mask).second)return 5;
  U scan=mask;while(scan){int v=first(scan);scan&=scan-1;options[v].push_back(mask);}
 }
 std::string extra;if(in>>extra)return 6;
 uint64_t answer=count(full);
 std::cout<<"{\"solutions\":"<<answer<<",\"calls\":"<<calls<<",\"cache_hits\":"<<hits
  <<",\"component_splits\":"<<splits<<",\"cached_states\":"<<memo.size()<<"}\n";
}
