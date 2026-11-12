// Independent finite-domain CSP. Outer facets share a variable; physical types
// are all-different. No exact-cover rows or Algorithm C operations are used.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
constexpr int W=12;
struct Bits {
  array<uint64_t,W> a{};
  void set(int i){a[i/64]|=1ULL<<(i%64);}
  Bits operator&(const Bits& b)const{Bits r;for(int i=0;i<W;i++)r.a[i]=a[i]&b.a[i];return r;}
  Bits minus(const Bits& b)const{Bits r;for(int i=0;i<W;i++)r.a[i]=a[i]&~b.a[i];return r;}
  int count()const{int n=0;for(auto x:a)n+=__builtin_popcountll(x);return n;}
};
struct Cube{array<int,6> color;int type;};
array<Cube,720> cubes;
Bits face[6][6],types[30],all;
vector<array<int,6>> cells;
vector<int> values,chosen;
uint64_t nodes=0,models=0;

void visit(int remaining,const Bits& available){
  ++nodes;
  if(!remaining){
    ++models;cout<<"M";for(int c:chosen)cout<<' '<<c;cout<<'\n';return;
  }
  int best=-1,size=721;Bits choices;
  for(int i=0;i<(int)cells.size();++i)if(chosen[i]<0){
    Bits candidates=available;
    for(int f=0;f<6;++f)if(values[cells[i][f]]>=0)candidates=candidates&face[f][values[cells[i][f]]];
    if(i==0){Bits one;one.set(0);candidates=candidates&one;}
    int n=candidates.count();if(!n)return;
    if(n<size){best=i;size=n;choices=candidates;if(n==1)break;}
  }
  assert(best>=0);
  for(int b=0;b<W;++b){
    uint64_t bits=choices.a[b];
    while(bits){int i=64*b+__builtin_ctzll(bits);bits&=bits-1;assert(i<720);
      const Cube& c=cubes[i];array<int,6> changed;int n=0;
      for(int f=0;f<6;++f){int v=cells[best][f];
        if(values[v]<0){values[v]=c.color[f];changed[n++]=v;}
        else assert(values[v]==c.color[f]);
      }
      chosen[best]=i;visit(remaining-1,available.minus(types[c.type]));chosen[best]=-1;
      for(int j=0;j<n;++j)values[changed[j]]=-1;
    }
  }
}

int main(){
  int n,nv;cin>>n>>nv;assert(n>=1&&n<=30&&nv>=6);cells.resize(n);chosen.assign(n,-1);values.assign(nv,-1);
  for(int i=0;i<720;++i){string w;int t;cin>>w>>t;assert(cin&&w.size()==6&&t>=0&&t<30);unsigned colors=0;
    for(int f=0;f<6;++f){int c=w[f]-'a';assert(c>=0&&c<6);cubes[i].color[f]=c;face[f][c].set(i);colors|=1u<<c;}
    assert(colors==63);cubes[i].type=t;types[t].set(i);all.set(i);
    if(i==0)assert(w=="abcdef");
  }
  for(auto& cell:cells)for(int& v:cell){cin>>v;assert(cin&&v>=0&&v<nv);}
  visit(n,all);cout<<"C "<<models<<' '<<nodes<<'\n';cerr<<"COMPLETED "<<models<<' '<<nodes<<'\n';
}
