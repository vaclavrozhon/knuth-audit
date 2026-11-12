// Independent row-bitboard enumeration of square-multiset tilings.
// TAOCP 4B X155 (authentic n=6) and X156 (ordinary n=8).
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using U=uint64_t;
struct Tile {int r,c,k; auto operator<=>(const Tile&) const=default;};
int L,K;bool wedge=false,affinity=false,stop_first=false;U full,rows[64];int remaining[64];
std::vector<Tile> chosen;U nodes=0,solutions=0;std::map<int,U>hist;
std::ofstream models;std::set<std::vector<Tile>>canonical;
std::chrono::steady_clock::time_point start;

std::vector<Tile> transform(int flipr,int flipc,int swaprc){
 std::vector<Tile> v;
 for(auto t:chosen){if(swaprc)std::swap(t.r,t.c);if(flipr)t.r=L-t.r-t.k;if(flipc)t.c=L-t.c-t.k;v.push_back(t);}
 std::sort(v.begin(),v.end());return v;
}
void accept(){
 ++solutions;auto best=transform(0,0,0);std::set<std::vector<Tile>> orbit;
 for(int a=0;a<2;++a)for(int b=0;b<2;++b)for(int c=0;c<2;++c){auto t=transform(a,b,c);best=std::min(best,t);orbit.insert(t);}
 canonical.insert(best);int score=0;
 if(affinity){int ids[64][64],sizes[64][64];
  for(int i=0;i<(int)chosen.size();++i){auto t=chosen[i];for(int r=t.r;r<t.r+t.k;++r)for(int c=t.c;c<t.c+t.k;++c){ids[r][c]=i;sizes[r][c]=t.k;}}
  for(int r=0;r<L;++r)for(int c=0;c<L;++c){if(r+1<L&&ids[r][c]!=ids[r+1][c]&&sizes[r][c]==sizes[r+1][c])++score;if(c+1<L&&ids[r][c]!=ids[r][c+1]&&sizes[r][c]==sizes[r][c+1])++score;}
  ++hist[score];
 }
 if(models){models<<"{\"tiles\":[";bool sep=false;for(auto t:chosen){if(sep)models<<',';sep=true;models<<'['<<t.r<<','<<t.c<<','<<t.k<<']';}models<<"],\"affinity\":"<<score<<",\"orbit_size\":"<<orbit.size()<<"}\n";}
}
void visit(int r){
 ++nodes;
 if((nodes&((1ULL<<28)-1))==0){double sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();std::cerr<<"nodes="<<nodes<<" solutions="<<solutions<<" seconds="<<sec<<'\n';}
 while(r<L&&rows[r]==full)++r;
 if(r==L){accept();return;}
 int c=__builtin_ctzll(full^rows[r]);int width=__builtin_ctzll((rows[r]>>c)|(~0ULL<<(L-c)));int maxk=std::min({K,L-r,width});
 for(int k=1;k<=maxk;++k){
  if(!remaining[k])continue;
  if(k==1&&wedge&&(r>=L/2||c<L-1-r))continue;
  U mask=((1ULL<<k)-1)<<c;bool fits=true;
  for(int rr=r+1;rr<r+k;++rr)if(rows[rr]&mask){fits=false;break;}
  if(!fits)continue;
  for(int rr=r;rr<r+k;++rr)rows[rr]^=mask;
  --remaining[k];chosen.push_back({r,c,k});visit(r);chosen.pop_back();++remaining[k];
  for(int rr=r;rr<r+k;++rr)rows[rr]^=mask;
  if(stop_first&&solutions)return;
 }
}
int main(int argc,char**argv){
 if(argc<4){std::cerr<<"usage: partridge side counts(comma-separated) models.jsonl [wedge] [affinity]\n";return 1;}
 L=std::stoi(argv[1]);if(L<1||L>63)return 2;full=(1ULL<<L)-1;
 std::istringstream ss(argv[2]);std::string s;int area=0;
 while(std::getline(ss,s,',')){remaining[++K]=std::stoi(s);area+=remaining[K]*K*K;}
 if(area!=L*L){std::cerr<<"area mismatch\n";return 3;}
 for(int i=4;i<argc;++i){std::string a=argv[i];if(a=="wedge")wedge=true;else if(a=="affinity")affinity=true;else if(a=="first")stop_first=true;else return 4;}
 if(wedge&&(L%2||remaining[1]!=1)){std::cerr<<"wedge assumes even side and one unit square\n";return 5;}
 models.open(argv[3]);if(!models)return 6;start=std::chrono::steady_clock::now();visit(0);models.close();
 std::cout<<"{\"side\":"<<L<<",\"nodes\":"<<nodes<<",\"solutions\":"<<solutions<<",\"symmetry_classes\":"<<canonical.size()<<",\"complete\":"<<(!(stop_first&&solutions)?"true":"false")<<",\"wedge\":"<<(wedge?"true":"false")<<",\"seconds\":"<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<",\"affinity_histogram\":{";
 bool sep=false;for(auto [a,b]:hist){if(sep)std::cout<<',';sep=true;std::cout<<'"'<<a<<"\":"<<b;}std::cout<<"}}\n";
}
