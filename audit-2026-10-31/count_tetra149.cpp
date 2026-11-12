// Independent vertex-color DFS. Physical type = missing color + permutation parity.
// No exact-cover rows, dancing links, or Python rotation-name table are used.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;
array<int,20> colors;
array<array<int,4>,10> cells;
array<vector<int>,20> incident, neighbors;
unsigned long long nodes=0,solutions=0;

int kind(const array<int,4>& vs) {
    int mask=0,inv=0;
    for(int i=0;i<4;i++) {
        int x=colors[vs[i]]; assert(x>=0); if(mask&(1<<x)) return -1; mask|=1<<x;
        for(int j=0;j<i;j++) inv+=colors[vs[j]]>x;
    }
    int absent=0; while(mask&(1<<absent)) absent++;
    return 2*absent+(inv%2);
}
int allowed(int v,int c,int used) {
    for(int u:neighbors[v]) if(colors[u]==c) return -1;
    colors[v]=c; int added=0;
    for(int t:incident[v]) {
        bool ready=true; for(int u:cells[t]) ready&=colors[u]>=0;
        if(!ready) continue;
        int k=kind(cells[t]); assert(k>=0); int bit=1<<k;
        if((used|added)&bit) {colors[v]=-1; return -1;} added|=bit;
    }
    colors[v]=-1; return added;
}
void dfs(int left,int used) {
    nodes++;
    if(!left) {
        assert(used==1023); solutions++;
        for(int c:colors) cout<<char('a'+c); cout<<'\n'; return;
    }
    int best=-1,bestn=6,bestdegree=-1; array<int,5> additions{};
    for(int v=0;v<20;v++) if(colors[v]<0) {
        int count=0;array<int,5> candidate;
        for(int c=0;c<5;c++) {candidate[c]=allowed(v,c,used);count+=candidate[c]>=0;}
        if(count==0) return;
        int degree=neighbors[v].size();
        if(count<bestn || (count==bestn && degree>bestdegree)) {
            best=v;bestn=count;bestdegree=degree;additions=candidate;
        }
    }
    assert(best>=0);
    for(int c=0;c<5;c++) if(additions[c]>=0) {
        colors[best]=c;dfs(left-1,used|additions[c]);colors[best]=-1;
    }
}
int main() {
    colors.fill(-1);
    for(int t=0;t<10;t++) {
        for(int& v:cells[t]) {cin>>v;assert(cin&&0<=v&&v<20);incident[v].push_back(t);}
        for(int v:cells[t]) for(int u:cells[t]) if(v!=u) neighbors[v].push_back(u);
    }
    for(auto& ns:neighbors) {sort(ns.begin(),ns.end());ns.erase(unique(ns.begin(),ns.end()),ns.end());}
    // S5 acts freely on the four different colors of the first unit tetrahedron.
    for(int j=0;j<4;j++) colors[cells[0][j]]=j;
    int k=kind(cells[0]);assert(k>=0);dfs(16,1<<k);
    cerr<<"COMPLETED "<<solutions<<' '<<nodes<<'\n';
}
