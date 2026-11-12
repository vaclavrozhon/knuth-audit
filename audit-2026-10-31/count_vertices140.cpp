// Independent vertex-color search. A completed triangle claims one cyclic type.
// Global color renaming is removed by introducing colors in their first-use order.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int n,tid[4][4][4],colors[100];
vector<array<int,3>> triangles;
vector<int> at[100];
uint64_t models,nodes;
string label;
constexpr uint32_t invalid=0xffffffffu;

uint32_t completed(int v,int c,uint32_t used) {
    uint32_t added=0;
    for(int t:at[v]) {
        int cc[3];bool full=true;
        for(int j=0;j<3;++j) {
            int w=triangles[t][j];cc[j]=w==v?c:colors[w];
            if(cc[j]<0)full=false;
        }
        if(!full)continue;
        uint32_t bit=1u<<tid[cc[0]][cc[1]][cc[2]];
        if((used|added)&bit)return invalid;
        added|=bit;
    }
    return added;
}

void visit_vertex(int assigned,int max_color,uint32_t used) {
    ++nodes;
    if(assigned==n) {
        assert(__builtin_popcount(used)==24);
        int rename[4]={-1,-1,-1,-1},next=0;string word;
        for(int v=0;v<n;++v) {
            if(rename[colors[v]]<0)rename[colors[v]]=next++;
            word+=char('a'+rename[colors[v]]);
        }
        ++models;cout<<"M "<<label<<' '<<word<<'\n';return;
    }
    int best=-1,best_count=5,best_score=-1;
    vector<pair<int,uint32_t>> options;
    for(int v=0;v<n;++v)if(colors[v]<0) {
        vector<pair<int,uint32_t>> choices;
        for(int c=0;c<=min(3,max_color+1);++c) {
            uint32_t added=completed(v,c,used);
            if(added!=invalid)choices.push_back({c,added});
        }
        if(choices.empty())return;
        int score=at[v].size();
        for(int t:at[v])for(int w:triangles[t])if(colors[w]>=0)score+=10;
        if(int(choices.size())<best_count || (int(choices.size())==best_count && score>best_score)) {
            best=v;best_count=choices.size();best_score=score;options=choices;
        }
    }
    assert(best>=0);
    for(auto [c,added]:options) {
        colors[best]=c;visit_vertex(assigned+1,max(max_color,c),used|added);colors[best]=-1;
    }
}

int main() {
    vector<array<int,3>> types;
    for(int a=0;a<4;++a)for(int b=0;b<4;++b)for(int c=0;c<4;++c) {
        array<int,3> v={a,b,c},w={b,c,a},z={c,a,b};v=min(v,min(w,z));
        auto it=find(types.begin(),types.end(),v);
        if(it==types.end()){tid[a][b][c]=types.size();types.push_back(v);}
        else tid[a][b][c]=it-types.begin();
    }
    assert(types.size()==24);
    int cases=0;
    while(cin>>label>>n) {
        assert(n>0 && n<100);triangles.clear();
        for(int v=0;v<n;++v){colors[v]=-1;at[v].clear();}
        for(int t=0;t<24;++t) {
            array<int,3> tr;cin>>tr[0]>>tr[1]>>tr[2];
            assert(cin && tr[0]!=tr[1] && tr[0]!=tr[2] && tr[1]!=tr[2]);
            for(int v:tr){assert(v>=0&&v<n);at[v].push_back(t);}
            triangles.push_back(tr);
        }
        nodes=models=0;visit_vertex(0,-1,0);
        cout<<"C "<<label<<' '<<models<<' '<<nodes<<'\n';cout.flush();
        cerr<<"COMPLETED "<<label<<' '<<models<<' '<<nodes<<'\n';cerr.flush();++cases;
    }
    cerr<<"ALL_COMPLETED "<<cases<<'\n';
}
