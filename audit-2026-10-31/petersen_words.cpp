// Induced Petersen embeddings in the common-letter graph of a word list.
// Explicit pairwise constraints and rank inequalities; no MCC encoding.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using U=uint64_t;using Bits=std::array<U,16>;using Domains=std::array<Bits,10>;
int N,blocks,p[10];bool G[10][10],lesser[10][10];
std::vector<std::string> words;std::vector<Bits> adjacency;
uint64_t nodes=0,solutions=0;std::ofstream output;
int size(const Bits&a){int k=0;for(int j=0;j<blocks;j++)k+=__builtin_popcountll(a[j]);return k;}
void rank_bound(Bits&a,int w,bool greater){
  for(int j=0;j<blocks;j++){
    int lo=j*64,hi=lo+63;
    if(greater){if(hi<=w)a[j]=0;else if(lo<=w)a[j]&=~U(0)<<(w-lo+1);}
    else{if(lo>=w)a[j]=0;else if(hi>=w)a[j]&=(U(1)<<(w-lo))-1;}
  }
}
void visit(const Domains&d,int assigned){
  nodes++;if((nodes&((1<<24)-1))==0)std::cerr<<nodes<<" nodes, "<<solutions<<" solutions\n";
  if(assigned==1023){solutions++;output<<'[';for(int i=0;i<10;i++)output<<(i?",":"")<<p[i];output<<"]\n";output.flush();return;}
  int v=-1,best=N+1;
  for(int i=0;i<10;i++)if(!(assigned>>i&1)){int k=size(d[i]);if(!k)return;if(k<best){v=i;best=k;}}
  for(int j=0;j<blocks;j++){
    U a=d[v][j];while(a){int w=64*j+__builtin_ctzll(a);a&=a-1;Domains next=d;bool good=true;
      for(int u=0;u<10;u++)if(u!=v&&!(assigned>>u&1)){
        for(int b=0;b<blocks;b++)next[u][b]&=G[v][u]?adjacency[w][b]:~adjacency[w][b];
        next[u][w/64]&=~(U(1)<<(w%64));
        if(lesser[v][u])rank_bound(next[u],w,true);
        if(lesser[u][v])rank_bound(next[u],w,false);
        if(!size(next[u])){good=false;break;}
      }
      if(good){p[v]=w;visit(next,assigned|(1<<v));}
    }
  }
}
int main(int argc,char**argv){
  if(argc!=4)return 2;N=std::stoi(argv[1]);if(N<10||N>1024)return 2;blocks=(N+63)/64;
  std::ifstream input(argv[2]);std::string s;while((int)words.size()<N&&input>>s)words.push_back(s);
  if((int)words.size()!=N)return 2;output.open(argv[3]);
  int edges[][2]={{0,1},{1,2},{2,3},{3,4},{4,0},{0,5},{1,6},{2,7},{3,8},{4,9},{5,7},{7,9},{9,6},{6,8},{8,5}};
  for(auto&e:edges)G[e[0]][e[1]]=G[e[1]][e[0]]=true;
  for(int i=1;i<10;i++)lesser[0][i]=true;
  lesser[1][4]=lesser[1][5]=lesser[2][6]=lesser[3][7]=true;
  std::vector<U> masks(N);for(int i=0;i<N;i++)for(char c:words[i])masks[i]|=U(1)<<(c-'a');
  adjacency.resize(N);for(int i=0;i<N;i++)for(int j=0;j<N;j++)if(i!=j&&(masks[i]&masks[j]))adjacency[i][j/64]|=U(1)<<(j%64);
  Domains d={};for(auto&a:d)for(int j=0;j<N;j++)a[j/64]|=U(1)<<(j%64);
  auto start=std::chrono::steady_clock::now();visit(d,0);
  std::cout<<"{\"dictionary_size\":"<<N<<",\"solutions\":"<<solutions<<",\"nodes\":"<<nodes
           <<",\"seconds\":"<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"}\n";
}
