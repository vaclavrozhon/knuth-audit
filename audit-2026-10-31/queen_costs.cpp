// Complete bit-mask enumeration: the several cost criteria of 232--236.
#include <array>
#include <vector>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <chrono>
#include <string>
using namespace std;

struct UInt192 {
  array<uint64_t,3> a{};
  UInt192(uint64_t x=0){a[0]=x;}
  UInt192& operator*=(uint32_t x){unsigned __int128 carry=0;for(int i=0;i<3;i++){carry+=(unsigned __int128)a[i]*x;a[i]=(uint64_t)carry;carry>>=64;}if(carry)abort();return *this;}
  bool operator<(const UInt192&b)const {for(int i=2;i>=0;i--)if(a[i]!=b.a[i])return a[i]<b.a[i];return false;}
  bool operator>(const UInt192&b)const{return b<*this;}
  bool operator==(const UInt192&b)const{return a==b.a;}
  string str()const {auto b=a;string s;do{unsigned __int128 rem=0;for(int i=2;i>=0;i--){auto z=(rem<<64)|b[i];b[i]=(uint64_t)(z/10);rem=z%10;}s.push_back('0'+(int)rem);}while(b[0]||b[1]||b[2]);reverse(s.begin(),s.end());return s;}
};
ostream& operator<<(ostream&o,const UInt192&v){return o<<v.str();}

using Perm=array<int,16>;
int n=16;uint32_t full;Perm pos;uint64_t solution_count=0,nodes=0;
int norm[16][16],fl[16][16],quart[16][16];long double dist[16][16],power20[16][16],power21[16][16];
struct Extreme {
  long double best,second;bool maximum;vector<Perm> models;
  Extreme(bool m=false):best(m?-1e100L:1e100L),second(best),maximum(m){}
  void add(long double v){
    long double eps=max(1.L,fabsl(v))*1e-16L;
    long double d=(maximum?-1:1)*(v-best);
    if(d < -eps){second=best;best=v;models.clear();models.push_back(pos);}
    else if(fabsl(v-best)<=eps)models.push_back(pos);
    else if((maximum?-1:1)*(v-second)<0)second=v;
  }
};
Extreme dmin,dmax(true),floor_minimum,qmin,qmax(true),p20min,p21min;
UInt192 minprod,maxprod;vector<Perm> prodmin,prodmax;
array<int,16> ultimate;vector<Perm> ultmodels;

void leaf(long double d,int f,int q,long double p20,long double p21){
  solution_count++;dmin.add(d);dmax.add(d);floor_minimum.add(f);qmin.add(q);qmax.add(q);p20min.add(p20);p21min.add(p21);
  UInt192 pr=1;array<int,16> radii;
  for(int i=0;i<n;i++){int w=norm[i][pos[i]];pr*=w;radii[i]=w;}
  if(prodmin.empty()||pr<minprod){minprod=pr;prodmin.clear();}
  if(pr==minprod)prodmin.push_back(pos);
  if(prodmax.empty()||pr>maxprod){maxprod=pr;prodmax.clear();}
  if(pr==maxprod)prodmax.push_back(pos);
  sort(radii.begin(),radii.begin()+n,greater<int>());
  if(ultmodels.empty()||lexicographical_compare(radii.begin(),radii.begin()+n,ultimate.begin(),ultimate.begin()+n)){
    ultimate=radii;ultmodels.clear();
  }
  if(equal(radii.begin(),radii.begin()+n,ultimate.begin()))ultmodels.push_back(pos);
}
void search(int r,uint32_t c,uint32_t a,uint32_t b,long double d,int f,int q,long double p20,long double p21){
  nodes++;
  if(r==n){leaf(d,f,q,p20,p21);return;}
  uint32_t avail=full&~(c|a|b);
  while(avail){uint32_t x=avail&-avail;avail-=x;int j=__builtin_ctz(x);pos[r]=j;
    search(r+1,c|x,((a|x)<<1)&full,(b|x)>>1,d+dist[r][j],f+fl[r][j],q+quart[r][j],p20+power20[r][j],p21+power21[r][j]);
  }
}
void printmodels(const vector<Perm>&v){cout<<"[";bool first=true;for(auto&p:v){if(!first)cout<<",";first=false;cout<<"[";for(int j=0;j<n;j++){if(j)cout<<",";cout<<p[j]+1;}cout<<"]";}cout<<"]";}
void printext(const char*name,const Extreme&e){cout<<"\""<<name<<"\":{\"value\":"<<e.best<<",\"second\":"<<e.second<<",\"models\":";printmodels(e.models);cout<<"},\n";}
int main(int argc,char**argv){
  if(argc>1)n=stoi(argv[1]);if(n<1||n>16)return 2;full=(1u<<n)-1;
  for(int r=0;r<n;r++)for(int c=0;c<n;c++){
    int x=2*r+1-n,y=2*c+1-n,w=x*x+y*y;norm[r][c]=w;
    dist[r][c]=sqrtl(w)/2;fl[r][c]=floorl(dist[r][c]);quart[r][c]=w*w;
    power20[r][c]=powl(dist[r][c],20);power21[r][c]=powl(dist[r][c],21);
  }
  auto start=chrono::steady_clock::now();search(0,0,0,0,0,0,0,0,0);
  cout<<setprecision(22)<<"{\"n\":"<<n<<",\"solutions\":"<<solution_count<<",\"nodes\":"<<nodes<<",\"seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<",\n";
  if(!solution_count){cout<<"\"empty\":true}\n";return 0;}
  printext("distance_min",dmin);printext("distance_max",dmax);printext("floor_min",floor_minimum);printext("norm_squared_min",qmin);printext("norm_squared_max",qmax);printext("power20_min",p20min);printext("power21_min",p21min);
  cout<<"\"product_norm_min\":{\"value\":\""<<minprod<<"\",\"models\":";printmodels(prodmin);cout<<"},\n";
  cout<<"\"product_norm_max\":{\"value\":\""<<maxprod<<"\",\"models\":";printmodels(prodmax);cout<<"},\n";
  cout<<"\"ultimate\":{\"radii\":[";for(int i=0;i<n;i++){if(i)cout<<",";cout<<ultimate[i];}cout<<"],\"models\":";printmodels(ultmodels);cout<<"}}\n";
}
