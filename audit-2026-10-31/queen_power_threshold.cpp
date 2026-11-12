// Exact interval certificate for every integer exponent 21,...,159.
#include <array>
#include <vector>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <cstdint>
#include <chrono>
using namespace std;
constexpr int n=16;constexpr uint32_t mask=65535;
int p[16],norm_index[16][16],m;vector<int> values;vector<int64_t> weight;
array<int,64> ultimate_counts{};
uint64_t leaves=0,classes=0,ultimate_classes=0,nodes=0;
int64_t margins[160];uint64_t checked[160]{};
uint64_t code(int mode){
  uint64_t out=0;
  for(int i=0;i<n;i++){
    int r=i,c=p[i];if(mode>=4)c=15-c;
    for(int j=0;j<mode%4;j++){int t=r;r=c;c=15-t;}
    out|=uint64_t(c)<<(4*(15-r));
  }
  return out;
}
void visit(){
  leaves++;uint64_t c=code(0);for(int g=1;g<8;g++)if(code(g)<c)return;
  classes++;array<int,64> diff{};
  for(int i=0;i<m;i++)diff[i]=-ultimate_counts[i];
  for(int i=0;i<n;i++)diff[norm_index[i][p[i]]]++;
  int v=m-1;while(v>=0&&!diff[v])v--;
  if(v<0){ultimate_classes++;return;}
  if(diff[v]<0){cerr<<"Lexicographically better than claimed ultimate\n";exit(3);}
  vector<pair<int,int>> terms;
  for(int i=0;i<=v;i++)if(diff[i])terms.push_back({i,diff[i]});
  for(int power=21;power<=159;power++){
    int64_t delta=0;size_t offset=(size_t(v)*160+power)*m;
    for(auto [i,k]:terms)delta+=k*weight[offset+i];
    margins[power]=min(margins[power],delta);checked[power]++;
    if(delta<=16){
      cerr<<"Uncertified comparison N="<<power<<" delta="<<delta<<" q=";
      for(int x:p)cerr<<x+1<<",";cerr<<"\n";exit(4);
    }
  }
}
void walk_board(int r,uint32_t c,uint32_t a,uint32_t b){
  nodes++;if(r==n){visit();return;}
  uint32_t avail=mask&~(c|a|b);if(r==0)avail&=255;
  while(avail){uint32_t x=avail&-avail;avail-=x;p[r]=__builtin_ctz(x);walk_board(r+1,c|x,((a|x)<<1)&mask,(b|x)>>1);}
}
int main(int argc,char**argv){
  if(argc!=2)return 2;ifstream in(argv[1]);in>>m;values.resize(m);for(int&x:values)in>>x;
  for(int w:{226,202,194,58})ultimate_counts[find(values.begin(),values.end(),w)-values.begin()]=4;
  weight.resize(size_t(m)*160*m);for(auto &x:weight)in>>x;if(!in){cerr<<"Bad table\n";return 2;}
  for(int r=0;r<n;r++)for(int c=0;c<n;c++){
    int w=(2*r-15)*(2*r-15)+(2*c-15)*(2*c-15);norm_index[r][c]=find(values.begin(),values.end(),w)-values.begin();
  }
  fill(margins,margins+160,INT64_MAX);auto start=chrono::steady_clock::now();walk_board(0,0,0,0);
  cout<<"{\"half_board_solutions\":"<<leaves<<",\"classes\":"<<classes<<",\"ultimate_classes\":"<<ultimate_classes<<",\"nodes\":"<<nodes<<",\"seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<",\"margins\":[";
  for(int power=21;power<=159;power++){if(power>21)cout<<",";cout<<"{\"N\":"<<power<<",\"minimum_scaled_margin\":"<<margins[power]<<",\"comparisons\":"<<checked[power]<<"}";}cout<<"]}\n";
}
