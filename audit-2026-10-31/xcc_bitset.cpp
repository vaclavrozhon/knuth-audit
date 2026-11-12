// Independent exact-cover-with-colors counter: immutable conflict bitsets.
// No dancing links, purification, or code from Knuth's implementation.
#include <algorithm>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <fstream>
#include <map>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
using U=uint64_t;
struct Row { U primary=0; map<int,string> colors; };
vector<Row> rows;
vector<vector<U>> byitem, conflict;
int np, words;
U solutions=0,nodes=0;
ofstream models;
int color_count=0;
vector<int> selected;

void search(U remaining,const vector<U>& available) {
  ++nodes;
  if(!remaining){
    ++solutions;
    if(color_count){
      string value(color_count,'?');
      for(int r:selected)for(auto [i,c]:rows[r].colors)if(i>=np&&i<np+color_count){
        assert(c.size()==1);char& target=value[i-np];
        assert(target=='?'||target==c[0]);target=c[0];
      }
      assert(value.find('?')==string::npos);models<<value<<'\n';
    }
    return;
  }
  int best=-1,bcount=1000000;
  U q=remaining;
  while(q){
    int i=__builtin_ctzll(q);q&=q-1;
    int c=0;
    for(int w=0;w<words;++w)c+=__builtin_popcountll(available[w]&byitem[i][w]);
    if(c<bcount){best=i;bcount=c;if(c<=1)break;}
  }
  if(bcount==0)return;
  for(int w=0;w<words;++w){
    U opts=available[w]&byitem[best][w];
    while(opts){
      int r=64*w+__builtin_ctzll(opts);opts&=opts-1;
      vector<U> next(words);
      for(int k=0;k<words;++k)next[k]=available[k]&~conflict[r][k];
      selected.push_back(r);
      search(remaining&~rows[r].primary,next);
      selected.pop_back();
    }
  }
}

int main(int argc,char** argv){
  if(argc>1){assert(argc==3);models.open(argv[1]);assert(models);color_count=stoi(argv[2]);assert(color_count>0);}
  auto start=chrono::steady_clock::now();
  string line,token;map<string,int> names;bool primary=true;
  while(getline(cin,line)){
    if(line.empty()||line[0]=='|')continue;
    istringstream ss(line);
    while(ss>>token){
      if(token=="|"){primary=false;np=names.size();continue;}
      assert(!names.count(token));int id=names.size();names[token]=id;
    }
    if(primary)np=names.size();break;
  }
  assert(np>0&&np<64);
  while(getline(cin,line)){
    if(line.empty()||line[0]=='|')continue;
    istringstream ss(line);Row r;map<int,bool> seen;
    while(ss>>token){
      auto c=token.find(':');string n=token.substr(0,c);
      assert(names.count(n));int id=names[n];assert(!seen[id]);seen[id]=true;
      if(id<np){assert(c==string::npos);r.primary|=U(1)<<id;}
      else {assert(c!=string::npos);r.colors[id]=token.substr(c+1);}
    }
    assert(r.primary);rows.push_back(r);
  }
  int nr=rows.size();words=(nr+63)/64;
  byitem.assign(np,vector<U>(words));conflict.assign(nr,vector<U>(words));
  for(int i=0;i<nr;++i){
    for(int j=0;j<np;++j)if(rows[i].primary>>j&1)byitem[j][i/64]|=U(1)<<(i%64);
    for(int j=0;j<nr;++j){
      bool bad=rows[i].primary&rows[j].primary;
      if(!bad)for(auto [a,c]:rows[i].colors){
        auto f=rows[j].colors.find(a);
        if(f!=rows[j].colors.end()&&f->second!=c){bad=true;break;}
      }
      if(bad)conflict[i][j/64]|=U(1)<<(j%64);
    }
  }
  vector<U> available(words,~U(0));
  if(nr%64)available.back()=(U(1)<<(nr%64))-1;
  search((U(1)<<np)-1,available);
  double seconds=chrono::duration<double>(chrono::steady_clock::now()-start).count();
  cout<<"{\"solutions\":"<<solutions<<",\"nodes\":"<<nodes<<",\"seconds\":"<<seconds<<",\"options\":"<<nr<<"}\n";
}
