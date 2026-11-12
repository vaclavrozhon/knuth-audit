// DLX64: independent connected-box tilings and coordinate Sudoku search.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using U=uint64_t;
int n,N,full;U all;
std::vector<U> tiles,adj;
std::vector<std::vector<U>> at;
std::vector<U> chosen;
std::vector<std::vector<int>> transforms;
uint64_t packings=0,classes=0,nodes=0;
std::array<std::array<uint64_t,3>,2> census{};
std::vector<std::string> solutions;
std::vector<int> region,board,rm,cm,bm;
std::string encoded(const std::vector<int>&labels){
 std::vector<int> ren(n,-1);int next=0;std::string s;
 for(int k:labels){if(ren[k]<0)ren[k]=next++;s+=char('0'+ren[k]);}
 return s;
}
void solve(){
 ++nodes;int best=-1,avail=0,size=n+1;
 for(int v=0;v<N;++v)if(board[v]<0){
  int a=full&~(rm[v/n]|cm[v%n]|bm[region[v]]),k=__builtin_popcount(unsigned(a));
  if(k<size){best=v;avail=a;size=k;if(k==0)return;}
 }
 if(best<0){std::string s;for(int d:board)s+=char('1'+d);solutions.push_back(s);return;}
 int r=best/n,c=best%n,b=region[best];
 while(avail&&solutions.size()<2){
  int bit=avail&-avail;avail^=bit;board[best]=__builtin_ctz(unsigned(bit));
  rm[r]|=bit;cm[c]|=bit;bm[b]|=bit;solve();
  rm[r]^=bit;cm[c]^=bit;bm[b]^=bit;board[best]=-1;
 }
}
void process(){
 ++packings;region.assign(N,0);bool straight=false;
 for(int b=0;b<n;++b){U scan=chosen[b];int r0=-1,c0=-1;bool same_r=true,same_c=true;
  while(scan){int v=__builtin_ctzll(scan);scan&=scan-1;region[v]=b;
   if(r0<0){r0=v/n;c0=v%n;}else{same_r&=r0==v/n;same_c&=c0==v%n;}}
  straight|=same_r||same_c;
 }
 std::string key=encoded(region);int stabilizer=0;
 for(auto&m:transforms){std::vector<int> changed(N);for(int v=0;v<N;++v)changed[m[v]]=region[v];
  std::string s=encoded(changed);if(s<key)return;stabilizer+=s==key;}
 ++classes;solutions.clear();nodes=0;board.assign(N,-1);rm.assign(n,0);cm.assign(n,0);bm.assign(n,0);
 bool consistent=true;
 for(int c=0;c<n;++c){int bit=1<<c,b=region[c];if(bm[b]&bit)consistent=false;
  board[c]=c;rm[0]|=bit;cm[c]|=bit;bm[b]|=bit;}
 if(consistent)solve();
 ++census[straight][solutions.size()];
 std::cout<<"{\"regions\":\""<<key<<"\",\"straight\":"<<(straight?"true":"false")
  <<",\"stabilizer\":"<<stabilizer<<",\"coordinate_nodes\":"<<nodes<<",\"solutions\":[";
 for(size_t j=0;j<solutions.size();++j){if(j)std::cout<<',';std::cout<<'"'<<solutions[j]<<'"';}
 std::cout<<"]}\n";
}
void enumerate(U remaining){
 if(!remaining){process();return;}
 U unseen=remaining;
 while(unseen){U front=unseen&-unseen,component=front;unseen^=front;
  while(front){int v=__builtin_ctzll(front);front&=front-1;U more=adj[v]&unseen;unseen^=more;front|=more;component|=more;}
  if(__builtin_popcountll(component)%n)return;
 }
 int v=__builtin_ctzll(remaining);
 for(U t:at[v])if((t&remaining)==t){chosen.push_back(t);enumerate(remaining^t);chosen.pop_back();}
}
int main(int argc,char**argv){
 if(argc!=2)return 2;std::ifstream in(argv[1]);size_t k;if(!(in>>n>>k)||n<1||n>6)return 3;
 N=n*n;full=(1<<n)-1;all=(U(1)<<N)-1;at.resize(N);adj.resize(N);
 for(size_t j=0;j<k;++j){U t;if(!(in>>std::hex>>t>>std::dec))return 4;
  if(__builtin_popcountll(t)!=n||(t&all)!=t)return 5;tiles.push_back(t);
  U s=t;while(s){int v=__builtin_ctzll(s);s&=s-1;at[v].push_back(t);}}
 std::sort(tiles.begin(),tiles.end());if(std::adjacent_find(tiles.begin(),tiles.end())!=tiles.end())return 6;
 for(int v=0;v<N;++v){int r=v/n,c=v%n;if(r)adj[v]|=U(1)<<(v-n);if(r+1<n)adj[v]|=U(1)<<(v+n);
  if(c)adj[v]|=U(1)<<(v-1);if(c+1<n)adj[v]|=U(1)<<(v+1);}
 for(int g=0;g<8;++g){std::vector<int> m;
  for(int v=0;v<N;++v){int r=v/n,c=v%n;if(g&4)c=n-1-c;for(int a=0;a<(g&3);++a){int t=r;r=c;c=n-1-t;}m.push_back(r*n+c);}transforms.push_back(m);}
 enumerate(all);
 std::cerr<<"{\"packings\":"<<packings<<",\"classes\":"<<classes<<",\"census_nonstraight\":[";
 for(int i=0;i<3;++i){if(i)std::cerr<<',';std::cerr<<census[0][i];}
 std::cerr<<"],\"census_with_straight\":[";
 for(int i=0;i<3;++i){if(i)std::cerr<<',';std::cerr<<census[1][i];}std::cerr<<"]}\n";
}
