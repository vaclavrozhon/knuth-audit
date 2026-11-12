#include <bits/stdc++.h>
using namespace std;using U=uint64_t;
struct V{U count;int best;U optimal;};
int n,k,m;vector<U> adj,rows;vector<int> cost;vector<vector<int>> by;unordered_map<U,V> memo;const int INF=100000000;
U component(U S){U seen=S&-S,front=seen;while(front){U b=front&-front;front-=b;U next=adj[__builtin_ctzll(b)]&S&~seen;seen|=next;front|=next;}return seen;}
V solve(U S){if(!S)return {1,0,1};auto it=memo.find(S);if(it!=memo.end())return it->second;U C=component(S);V ans={0,INF,0};if(__builtin_popcountll(C)%k)return memo[S]=ans;
 if(C!=S){V a=solve(C),b=solve(S^C);if(a.count&&b.count)ans={a.count*b.count,a.best+b.best,a.optimal*b.optimal};return memo[S]=ans;}
 vector<int> opts;size_t bestlen=SIZE_MAX;for(U t=S;t;){U b=t&-t;t-=b;int v=__builtin_ctzll(b);vector<int> tmp;for(int r:by[v])if((rows[r]&S)==rows[r]){tmp.push_back(r);if(tmp.size()>=bestlen)break;}if(tmp.size()<bestlen){opts=move(tmp);bestlen=opts.size();if(!bestlen)return memo[S]=ans;if(bestlen==1)break;}}
 for(int r:opts){V v=solve(S^rows[r]);ans.count+=v.count;if(v.count){int z=cost[r]+v.best;if(z<ans.best){ans.best=z;ans.optimal=v.optimal;}else if(z==ans.best)ans.optimal+=v.optimal;}}
 return memo[S]=ans;}
int main(){cin>>n>>k>>m;adj.resize(n);by.resize(n);for(auto &a:adj)cin>>a;for(int r=0;r<m;r++){U s;int c;cin>>s>>c;rows.push_back(s);cost.push_back(c);for(int i=0;i<n;i++)if(s>>i&1)by[i].push_back(r);}auto t=chrono::steady_clock::now();U S=(U(1)<<n)-1;V v=solve(S);cout<<"{\"count\":"<<v.count<<",\"minimum_cost\":"<<v.best<<",\"optimal_count\":"<<v.optimal<<",\"memo_states\":"<<memo.size()<<",\"seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-t).count()<<",\"witness_rows\":[";bool first=true;while(S){bool ok=false;for(int r:by[__builtin_ctzll(S)])if((rows[r]&S)==rows[r]){V a=solve(S^rows[r]);if(a.count&&cost[r]+a.best==solve(S).best){if(!first)cout<<",";first=false;cout<<r;S^=rows[r];ok=true;break;}}if(!ok)break;}cout<<"]}\n";}
