// Exhaust all C(38,6) choices of internal white edges, without a tile solver.
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
struct E{int a,b,ba,bb;};
vector<E> edges;
array<int,24> masks{};
uint64_t choices=0,accepted=0;
vector<int> selected;
int type(int m){int k=__builtin_popcount((unsigned)m);return k==2?((m==5||m==10)?3:2):(k==3?4:(k==4?5:k));}
const array<int,6> target={6,8,4,3,2,1};
void run(int next,int left){
 if(!left){
  ++choices;array<int,6> count{};for(int m:masks)++count[type(m)];if(count!=target)return;
  ++accepted;for(int i=0;i<38;++i){bool yes=false;for(int k:selected)if(k==i)yes=true;cout<<(yes?'a':'b');}cout<<'\n';return;
 }
 for(int i=next;i<=int(edges.size())-left;++i){auto e=edges[i];masks[e.a]|=e.ba;masks[e.b]|=e.bb;selected.push_back(i);run(i+1,left-1);selected.pop_back();masks[e.a]^=e.ba;masks[e.b]^=e.bb;}
}
int main(){
 // Edge order: all horizontal interior segments x-major, then vertical x-major.
 for(int x=0;x<6;++x)for(int y=1;y<4;++y)edges.push_back({4*x+y-1,4*x+y,4,1});
 for(int x=1;x<6;++x)for(int y=0;y<4;++y)edges.push_back({4*(x-1)+y,4*x+y,2,8});
 for(int x=0;x<6;++x)for(int y=0;y<4;++y)masks[4*x+y]=(y==0?1:0)|(x==5?2:0)|(y==3?4:0)|(x==0?8:0);
 run(0,6);cerr<<"choices "<<choices<<" accepted "<<accepted<<'\n';
}
