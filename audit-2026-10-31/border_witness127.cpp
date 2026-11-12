// First completion for every supplied boundary, with immutable conflicts.
// All returned colorings are checked independently in Python geometry.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
using U=uint64_t;
struct Row { U primary=0; map<int,char> colors; };
vector<Row> rows;
vector<vector<U>> byitem,conflict;
vector<int> selected;
int np,words,ns;
U nodes;

bool first(U remaining,const vector<U>& available) {
  ++nodes;
  if(!remaining)return true;
  int best=-1,bcount=1000000;
  for(U q=remaining;q;q&=q-1){
    int i=__builtin_ctzll(q),c=0;
    for(int w=0;w<words;++w)c+=__builtin_popcountll(available[w]&byitem[i][w]);
    if(c<bcount){best=i;bcount=c;if(c<=1)break;}
  }
  if(!bcount)return false;
  for(int w=0;w<words;++w){
    U opts=available[w]&byitem[best][w];
    while(opts){
      int r=64*w+__builtin_ctzll(opts);opts&=opts-1;
      vector<U> next(words);
      for(int k=0;k<words;++k)next[k]=available[k]&~conflict[r][k];
      selected.push_back(r);
      if(first(remaining&~rows[r].primary,next))return true;
      selected.pop_back();
    }
  }
  return false;
}

int main(int argc,char** argv){
  assert(argc==3);ifstream borders(argv[1]),boundary(argv[2]);assert(borders&&boundary);
  string line,token;map<string,int> names;bool primary=true;
  assert(bool(getline(cin,line)));istringstream header(line);
  while(header>>token){
    if(token=="|"){primary=false;np=names.size();continue;}
    assert(!names.count(token));int id=names.size();names[token]=id;
  }
  assert(!primary&&np==48);ns=names.size()-np;assert(ns==42);
  while(getline(cin,line)){
    if(line.empty())continue;
    Row r;map<int,bool> seen;istringstream ss(line);
    while(ss>>token){
      auto k=token.find(':');string name=token.substr(0,k);assert(names.count(name));int i=names[name];
      assert(!seen[i]);seen[i]=true;
      if(i<np){assert(k==string::npos);r.primary|=U(1)<<i;}
      else {assert(k!=string::npos&&k+2==token.size());r.colors[i]=token[k+1];}
    }
    assert(__builtin_popcountll(r.primary)==2&&r.colors.size()==3);rows.push_back(r);
  }
  int nr=rows.size();assert(nr==1536);words=(nr+63)/64;
  byitem.assign(np,vector<U>(words));conflict.assign(nr,vector<U>(words));
  for(int i=0;i<nr;++i){
    for(int j=0;j<np;++j)if(rows[i].primary>>j&1)byitem[j][i/64]|=U(1)<<(i%64);
    for(int j=0;j<nr;++j){
      bool bad=rows[i].primary&rows[j].primary;
      if(!bad)for(auto [a,c]:rows[i].colors){auto f=rows[j].colors.find(a);if(f!=rows[j].colors.end()&&f->second!=c){bad=true;break;}}
      if(bad)conflict[i][j/64]|=U(1)<<(j%64);
    }
  }
  vector<int> border;while(boundary>>token){assert(names.count(token));border.push_back(names[token]);}
  assert(border.size()==12);
  int done=0;
  while(borders>>line){
    assert(line.size()==12);vector<U> available(words,~U(0));
    if(nr%64)available.back()=(U(1)<<(nr%64))-1;
    for(int r=0;r<nr;++r)for(int j=0;j<12;++j){
      auto it=rows[r].colors.find(border[j]);
      if(it!=rows[r].colors.end()&&it->second!='a'+line[j]-'0')available[r/64]&=~(U(1)<<(r%64));
    }
    selected.clear();nodes=0;bool ok=first((U(1)<<np)-1,available);
    if(!ok){cout<<line<<" UNSAT "<<nodes<<endl;return 2;}
    string value(ns,'?');
    assert(selected.size()==24);
    for(int r:selected)for(auto [i,c]:rows[r].colors){char& x=value[i-np];assert(x=='?'||x==c);x=c;}
    assert(value.find('?')==string::npos);
    cout<<line<<' '<<value<<' '<<nodes<<'\n';
    if(++done%100==0)cout.flush();
  }
  cerr<<"completed "<<done<<" boundaries\n";
}
