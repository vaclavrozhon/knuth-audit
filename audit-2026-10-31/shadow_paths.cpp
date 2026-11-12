// Direct vertex-path enumeration with independently maintained forest shadows.
#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;
using U=uint32_t;
struct Move{int v;array<int,3> masks;};
vector<Move> adj[27];
U nb[27];
bool forest[4096];
vector<int> path;
vector<vector<int>> solutions;
uint64_t nodes=0,counts[28]={};
int mode,startv,lastv=-1;
U allowed;
bool timeout=false;
double limit_seconds=1800;
auto began=chrono::steady_clock::now();

array<int,3> xyz(int v){return {v/9,v/3%3,v%3};}
int shadow_edge(int a,int b,int c,int d){
 if(a!=c)return 1<<(3*min(a,c)+b);
 return 1<<(6+2*a+min(b,d));
}
void setup(){
 for(int m=0;m<4096;++m){
  int p[9];for(int i=0;i<9;++i)p[i]=i;
  auto root=[&](int i){while(p[i]!=i)i=p[i];return i;};
  bool ok=true;
  for(int e=0;e<12;++e)if(m>>e&1){
   int u,v;
   if(e<6)u=(e/3)*3+e%3,v=u+3;
   else u=((e-6)/2)*3+(e-6)%2,v=u+1;
   int a=root(u),b=root(v);if(a==b){ok=false;break;}p[a]=b;
  }
  forest[m]=ok;
 }
 for(int v=0;v<27;++v)for(int w=0;w<27;++w){
  auto a=xyz(v),b=xyz(w);
  int dist=0;for(int k=0;k<3;++k)dist+=abs(a[k]-b[k]);
  if(dist!=1)continue;
  Move t;t.v=w;
  int n=0;
  for(auto axes:vector<array<int,2>>{{0,1},{0,2},{1,2}}){
   int i=axes[0],j=axes[1];
   t.masks[n++]=(a[i]==b[i]&&a[j]==b[j])?0:shadow_edge(a[i],a[j],b[i],b[j]);
  }
  adj[v].push_back(t);nb[v]|=U(1)<<w;
 }
}
bool viable(int v,U seen){
 U rem=allowed&~seen;if(!rem)return true;
 U domain=rem|(U(1)<<v),found=U(1)<<v,front=found;
 while(front){int a=__builtin_ctz(front);front&=front-1;U next=nb[a]&domain&~found;found|=next;front|=next;}
 if(found!=domain)return false;
 int leaves=0;
 while(rem){int a=__builtin_ctz(rem);rem&=rem-1;int d=__builtin_popcount(nb[a]&domain);if(d==0)return false;if(d==1&&++leaves>1)return false;}
 return true;
}
void visit(int v,U seen,array<int,3> shadows){
 ++nodes;
 if((nodes&((1<<20)-1))==0){
  double elapsed=chrono::duration<double>(chrono::steady_clock::now()-began).count();
  if(elapsed>limit_seconds){timeout=true;return;}
 }
 int depth=path.size();
 if(mode==2&&depth==27){++counts[27];solutions.push_back(path);return;}
 if(mode==2&&!viable(v,seen))return;
 for(auto t:adj[v]){
  int w=t.v;
  if(!(allowed>>w&1))continue;
  auto next=shadows;bool ok=true;
  for(int j=0;j<3;++j){next[j]|=t.masks[j];if(!forest[next[j]]){ok=false;break;}}
  if(!ok)continue;
  if(mode!=2&&w==startv){
   if(depth>=4&&(lastv<0?path[1]<v:v==lastv)){++counts[depth];solutions.push_back(path);}
   continue;
  }
  if(seen>>w&1)continue;
  if(mode==0&&w==lastv){
   // This vertex must be the predecessor of the fixed starting corner.
   path.push_back(w);visit(w,seen|(U(1)<<w),next);path.pop_back();
   continue;
  }
  if(mode==0&&v==lastv)continue;
  path.push_back(w);visit(w,seen|(U(1)<<w),next);path.pop_back();
  if(timeout)return;
 }
}
void begin(int s,int first=-1){
 startv=s;path={s};array<int,3> shadow={0,0,0};U seen=U(1)<<s;
 if(first>=0){
  for(auto t:adj[s])if(t.v==first){shadow=t.masks;seen|=U(1)<<first;path.push_back(first);}
  assert(path.size()==2);
 }
 visit(path.back(),seen,shadow);
}
int main(int argc,char**argv){
 if(argc<2)return 2;mode=atoi(argv[1]);if(argc>2)limit_seconds=atof(argv[2]);setup();
 allowed=(U(1)<<27)-1;
 if(mode==0){lastv=3;begin(0,1);}
 else if(mode==1){
  U corner=0;for(int v=0;v<27;++v){auto p=xyz(v);if(p[0]!=1&&p[1]!=1&&p[2]!=1)corner|=U(1)<<v;}
  allowed&=~corner;
  for(int s=0;s<27&&!timeout;++s)if(allowed>>s&1){begin(s);allowed&=~(U(1)<<s);}
 }else if(mode==2){
  int s=argc>3?atoi(argv[3]):0;
  if(s==0)begin(0,1);
  else {begin(4,1);if(!timeout)begin(4,13);}
 }else return 2;
 cout<<"{\"complete\":"<<(timeout?"false":"true")<<",\"nodes\":"<<nodes<<",\"counts\":[";
 for(int i=0;i<28;++i)cout<<(i?",":"")<<counts[i];
 cout<<"],\"solutions\":[";
 for(size_t i=0;i<solutions.size();++i){if(i)cout<<',';cout<<'[';for(size_t j=0;j<solutions[i].size();++j)cout<<(j?",":"")<<solutions[i][j];cout<<']';}
 cout<<"],\"seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-began).count()<<"}\n";
}
