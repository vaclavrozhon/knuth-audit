// Independent DSATUR enumeration of color partitions, without exact cover.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
int n,limit;
array<uint64_t,64> adj{};
array<unsigned,64> forbidden{};
array<uint64_t,65> counts{};
uint64_t nodes=0;
void visit(uint64_t todo,int used){
    ++nodes;
    if(!todo){++counts[used];return;}
    int v=-1,bs=-1,bd=-1;
    for(uint64_t t=todo;t;t&=t-1){
        int u=__builtin_ctzll(t),s=__builtin_popcount(forbidden[u]),d=__builtin_popcountll(adj[u]&todo);
        if(s>bs || (s==bs && d>bd)){v=u;bs=s;bd=d;}
    }
    uint64_t next=todo&~(uint64_t(1)<<v),neighbors=adj[v]&next;
    for(int c=0;c<min(limit,used+1);++c){
        unsigned bit=1u<<c;
        if(forbidden[v]&bit)continue;
        array<pair<int,unsigned>,64> undo{};int k=0;bool possible=true;
        for(uint64_t t=neighbors;t;t&=t-1){
            int u=__builtin_ctzll(t);undo[k++]={u,forbidden[u]};forbidden[u]|=bit;
            if(__builtin_popcount(forbidden[u])==limit)possible=false;
        }
        if(possible)visit(next,max(used,c+1));
        for(int i=0;i<k;++i)forbidden[undo[i].first]=undo[i].second;
    }
}
int main(){
    int m;if(!(cin>>n>>limit>>m)||n<1||n>64||limit<1||limit>30)return 2;
    for(int i=0;i<m;++i){int u,v;if(!(cin>>u>>v)||u<0||u>=n||v<0||v>=n||u==v)return 3;adj[u]|=uint64_t(1)<<v;adj[v]|=uint64_t(1)<<u;}
    visit(n==64?~uint64_t(0):(uint64_t(1)<<n)-1,0);
    cout<<"{\"vertices\":"<<n<<",\"colors\":"<<limit<<",\"nodes\":"<<nodes<<",\"partitions_by_used_colors\":[";
    for(int i=0;i<=limit;++i)cout<<(i?",":"")<<counts[i];
    cout<<"]}\n";
}
