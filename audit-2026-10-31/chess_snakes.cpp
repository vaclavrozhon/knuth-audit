// Direct enumeration of induced paths or cycles in chess-move graphs.
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
using U=uint64_t;
U adj[64],board;int n,target,start_vertex;bool cycle_mode;uint64_t nodes=0,found[65]={};std::ofstream output;
void emit(U used,int length){found[length]++;output<<"["<<start_vertex<<','<<length<<','<<used<<"]\n";}
void paths(int last,U used,U forbidden,int length){
  nodes++;if((nodes&((U(1)<<28)-1))==0)std::cerr<<nodes<<" nodes at start "<<start_vertex<<'\n';
  if(length>=target)emit(used,length);
  U available=board&~forbidden;
  if(length+__builtin_popcountll(available)<target)return;
  U choices=adj[last]&available;
  while(choices){int v=__builtin_ctzll(choices);choices&=choices-1;
    paths(v,used|(U(1)<<v),forbidden|adj[last]|(U(1)<<v),length+1);
  }
}
void cycles(int last,int second,U used,U forbidden,int length){
  nodes++;if((nodes&((U(1)<<28)-1))==0)std::cerr<<nodes<<" nodes at start "<<start_vertex<<'\n';
  U available=board&~(forbidden|used);
  // Every remaining vertex must exceed the canonical first vertex.
  available&=~U(0)<<start_vertex;
  if(length+__builtin_popcountll(available)<target)return;
  U choices=adj[last]&available;
  while(choices){int v=__builtin_ctzll(choices);choices&=choices-1;U bit=U(1)<<v;
    if(adj[start_vertex]&bit){if(length+1>=target&&second<v)emit(used|bit,length+1);}
    else cycles(v,second,used|bit,forbidden|adj[last],length+1);
  }
}
int main(int argc,char**argv){
  if(argc!=7)return 2;n=std::stoi(argv[1]);std::string piece=argv[2],mode=argv[3];target=std::stoi(argv[4]);
  int specified=std::stoi(argv[5]);output.open(argv[6]);cycle_mode=mode=="cycle";
  if(n<2||n>8||target<3)return 2;board=n==8?~U(0):(U(1)<<(n*n))-1;
  for(int v=0;v<n*n;v++)for(int w=0;w<n*n;w++)if(v!=w){
    int dr=abs(v/n-w/n),dc=abs(v%n-w%n);bool yes=false;
    if(piece=="king")yes=dr<=1&&dc<=1;
    if(piece=="knight")yes=dr*dc==2;
    if(piece=="bishop")yes=dr==dc;
    if(piece=="rook")yes=dr==0||dc==0;
    if(piece=="queen")yes=dr==dc||dr==0||dc==0;
    if(yes)adj[v]|=U(1)<<w;
  }
  auto began=std::chrono::steady_clock::now();
  for(int s=0;s<n*n;s++){
    if(specified>=0&&s!=specified)continue;
    if(specified<0){int r=s/n,c=s%n;if(r>c||r+c>=n||r>=(n+1)/2)continue;}
    start_vertex=s;U used=U(1)<<s;
    if(!cycle_mode)paths(s,used,used,1);
    else{U a=adj[s]&(~U(0)<<s);while(a){int v=__builtin_ctzll(a);a&=a-1;cycles(v,v,used|(U(1)<<v),0,2);}}
  }
  std::cout<<"{\"board_side\":"<<n<<",\"piece\":\""<<piece<<"\",\"mode\":\""<<mode<<"\",\"target_vertices\":"<<target
           <<",\"start\":"<<specified<<",\"nodes\":"<<nodes<<",\"seconds\":"<<std::chrono::duration<double>(std::chrono::steady_clock::now()-began).count()<<",\"counts\":{";
  bool first=true;for(int i=target;i<=64;i++)if(found[i]){std::cout<<(first?"":",")<<'"'<<i<<"\":"<<found[i];first=false;}
  std::cout<<"}}\n";
}
