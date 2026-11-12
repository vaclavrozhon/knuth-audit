// Independent exhaustive queen domination on the 8x8 board.
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <array>
using U=uint64_t;
U attack[64];U kernels[9]={};std::ofstream file;U total=0,independent=0,totaldom=0,clique=0;std::map<int,U> quadrants;
void kernel(int row,U chosen,U forbidden,U covered,int count){
 if(row==8){if(covered==~0ULL)++kernels[count];return;}
 kernel(row+1,chosen,forbidden,covered,count);
 for(int c=0;c<8;++c){int v=8*row+c;U bit=1ULL<<v;if(!(forbidden&bit))kernel(row+1,chosen|bit,forbidden|attack[v],covered|attack[v],count+1);}
}
int main(int argc,char**argv){
 if(argc!=2)return 1;
 file.open(argv[1]);
 for(int v=0;v<64;++v)for(int w=0;w<64;++w)if(v/8==w/8||v%8==w%8||std::abs(v/8-w/8)==std::abs(v%8-w%8))attack[v]|=1ULL<<w;
 for(int a=0;a<60;++a)for(int b=a+1;b<61;++b)for(int c=b+1;c<62;++c)for(int d=c+1;d<63;++d){U partial=attack[a]|attack[b]|attack[c]|attack[d];for(int e=d+1;e<64;++e){if((partial|attack[e])!=~0ULL)continue;
  U chosen=(1ULL<<a)|(1ULL<<b)|(1ULL<<c)|(1ULL<<d)|(1ULL<<e);++total;file<<chosen<<'\n';
  bool ind=true,tot=true,cli=true;int q[4]={};
  for(int v:{a,b,c,d,e}){int degree=std::popcount(attack[v]&chosen)-1;ind&=degree==0;tot&=degree>0;cli&=degree==4;++q[2*(v/8/4)+(v%8/4)];}
  independent+=ind;totaldom+=tot;clique+=cli;++quadrants[1000*q[0]+100*q[1]+10*q[2]+q[3]];
 }}
 kernel(0,0,0,0,0);
 std::cout<<"{\"dominating5\":"<<total<<",\"independent5\":"<<independent<<",\"total5\":"<<totaldom<<",\"clique5\":"<<clique<<",\"kernels\":[";
 for(int i=0;i<=8;++i){if(i)std::cout<<',';std::cout<<kernels[i];}std::cout<<"],\"quadrants\":{";bool comma=false;for(auto [q,n]:quadrants){if(comma)std::cout<<',';comma=true;std::cout<<'"'<<q<<"\":"<<n;}std::cout<<"}}\n";
}
