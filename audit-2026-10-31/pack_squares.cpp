// Existence of a rectangular tiling by prescribed square multiplicities.
// Failed frontier states are memoized; stopping a timed run is not a proof.
#include <algorithm>
#include <array>
#include <bit>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>
using U=uint64_t;
struct Key {std::array<uint32_t,8>rows{};U counts=0;uint16_t row=0;bool operator==(const Key&)const=default;};
struct Hash {size_t operator()(const Key&k)const{U h=k.counts^(U(k.row)<<48);for(U x:k.rows){h^=x+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2);}return h;}};
struct Tile{int r,c,k;};
int H,W,K;U full;U rows[4096]{};int remaining[8]{};std::vector<Tile>chosen;
std::unordered_set<Key,Hash>failed;size_t cache_limit=2000000;U nodes=0,hits=0;bool found=false;
std::chrono::steady_clock::time_point started;
bool visit(int r){
 ++nodes;
 if((nodes&((1ULL<<26)-1))==0)std::cerr<<"nodes="<<nodes<<" cache="<<failed.size()<<" hits="<<hits<<" seconds="<<std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count()<<'\n';
 while(r<H&&rows[r]==full)++r;
 if(r==H)return true;
 Key key;key.row=r;for(int j=0;j<K;++j)if(r+j<H)key.rows[j]=rows[r+j];for(int k=1;k<=K;++k)key.counts|=U(remaining[k])<<(8*(k-1));
 if(failed.contains(key)){++hits;return false;}
 int c=std::countr_zero(full^rows[r]);int width=std::countr_zero((rows[r]>>c)|(~0ULL<<(W-c)));int maxk=std::min({K,H-r,width});
 for(int k=maxk;k>=1;--k){if(!remaining[k])continue;U mask=((1ULL<<k)-1)<<c;bool fits=true;
  for(int rr=r+1;rr<r+k;++rr)if(rows[rr]&mask){fits=false;break;}
  if(!fits)continue;
  for(int rr=r;rr<r+k;++rr)rows[rr]^=mask;
  --remaining[k];chosen.push_back({r,c,k});
  if(visit(r))return true;
  chosen.pop_back();++remaining[k];for(int rr=r;rr<r+k;++rr)rows[rr]^=mask;
 }
 if(failed.size()<cache_limit)failed.insert(key);
 return false;
}
int main(int argc,char**argv){
 if(argc<4){std::cerr<<"usage: pack_squares height width comma-separated-counts [cache_limit]\n";return 1;}
 H=std::stoi(argv[1]);W=std::stoi(argv[2]);if(H<1||H>4096||W<1||W>32)return 2;full=(1ULL<<W)-1;
 std::istringstream ss(argv[3]);std::string s;int area=0;
 while(std::getline(ss,s,',')){if(++K>7)return 3;remaining[K]=std::stoi(s);if(remaining[K]<0||remaining[K]>255)return 4;area+=K*K*remaining[K];}
 if(area!=H*W){std::cerr<<"area mismatch\n";return 5;}
 if(argc>4)cache_limit=std::stoull(argv[4]);failed.reserve(cache_limit);started=std::chrono::steady_clock::now();found=visit(0);
 std::cout<<"{\"height\":"<<H<<",\"width\":"<<W<<",\"found\":"<<(found?"true":"false")<<",\"search_exhausted\":"<<(found?"false":"true")<<",\"nodes\":"<<nodes<<",\"cache_hits\":"<<hits<<",\"cache_size\":"<<failed.size()<<",\"seconds\":"<<std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count()<<",\"tiles\":[";
 bool sep=false;for(auto t:chosen){if(sep)std::cout<<',';sep=true;std::cout<<'['<<t.r<<','<<t.c<<','<<t.k<<']';}std::cout<<"]}\n";
}
