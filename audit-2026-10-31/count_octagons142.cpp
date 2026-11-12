// Direct color-variable CSP with orientation bitsets; no exact-cover matrix/DLX.
// Each branch fills a cell, using a type once. Repeated sectors are allowed.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
using Bits = unsigned __int128;
struct Option { array<int,4> colors; int type; };
vector<Option> options;
vector<array<int,4>> cells;
vector<pair<int,int>> boundary[2];
Bits compatible[24][256], type_options[24];
int colors[128], palette, nv, ns, nt, complete;
uint64_t nodes, models, cylinders[2], toroidal, emitted, period;
string label;

int popcount(Bits x) { return __builtin_popcountll(uint64_t(x))+__builtin_popcountll(uint64_t(x>>64)); }
int first(Bits x) { assert(x);return uint64_t(x)?__builtin_ctzll(uint64_t(x)):64+__builtin_ctzll(uint64_t(x>>64)); }
int pattern(const array<int,4>& cell) {
    int p=0;
    for(int j=0;j<4;++j) p|=(colors[cell[j]]<0?3:colors[cell[j]])<<(2*j);
    return p;
}

void visit(uint32_t remaining,int highest,Bits used) {
    ++nodes;
    if((nodes&((1ULL<<26)-1))==0) {
        cerr<<"PROGRESS "<<label<<' '<<nodes<<' '<<models<<'\n';cerr.flush();
    }
    if(!remaining) {
        ++models;
        bool matches[2]={true,true};
        for(int axis=0;axis<2;++axis) {
            for(auto pair:boundary[axis]) if(colors[pair.first]!=colors[pair.second]) {matches[axis]=false;break;}
            cylinders[axis]+=matches[axis];
        }
        toroidal+=(matches[0]&&matches[1]);
        if(models==1 || models%period==0) {
            int names[3]={-1,-1,-1},next=0;string word;
            for(int v=0;v<nv;++v) {
                assert(colors[v]>=0);
                if(names[colors[v]]<0) names[colors[v]]=next++;
                word+=char('a'+names[colors[v]]);
            }
            cout<<"M "<<label<<' '<<models<<' '<<word<<'\n';++emitted;
        }
        return;
    }
    int best=-1,best_amount=1000;Bits choices=0;
    for(uint32_t scan=remaining;scan;scan&=scan-1) {
        int cell=__builtin_ctz(scan);
        Bits available=compatible[cell][pattern(cells[cell])]&~used;
        int amount=popcount(available);
        if(!amount) return;
        if(amount<best_amount) {best=cell;best_amount=amount;choices=available;if(amount==1) break;}
    }
    assert(best>=0);
    while(choices) {
        int index=first(choices);choices&=choices-1;
        const Option& option=options[index];int added[4],amount=0,hi=highest;bool good=true;
        for(int j=0;j<4;++j) {
            int v=cells[best][j],c=option.colors[j];
            if(colors[v]>=0) {assert(colors[v]==c);continue;}
            if(c>hi+1) {good=false;break;}
            hi=max(hi,c);colors[v]=c;added[amount++]=v;
        }
        if(good) visit(remaining^(1u<<best),hi,used|type_options[option.type]);
        while(amount) colors[added[--amount]]=-1;
    }
}

void prepare() {
    options.clear();vector<array<int,4>> types;
    fill(type_options,type_options+24,Bits(0));
    for(int a=0;a<palette;++a) for(int b=0;b<palette;++b)
    for(int c=0;c<palette;++c) for(int d=0;d<palette;++d) {
        array<int,4> word={a,b,c,d},key=word,rotation=word;
        for(int r=1;r<4;++r) {rotate(rotation.begin(),rotation.begin()+1,rotation.end());key=min(key,rotation);}
        auto at=find(types.begin(),types.end(),key);int type=at-types.begin();
        if(at==types.end()) types.push_back(key);
        type_options[type]|=Bits(1)<<options.size();options.push_back({word,type});
    }
    nt=types.size();assert(nt<=24 && options.size()<=81);
    for(int cell=0;cell<ns;++cell) for(int pat=0;pat<256;++pat) {
        Bits result=0;
        for(unsigned index=0;index<options.size();++index) {
            auto word=options[index].colors;bool good=true;
            for(int j=0;j<4;++j) {
                int known=(pat>>(2*j))&3;
                if(known!=3 && known!=word[j]) good=false;
                for(int k=0;k<j;++k) if(cells[cell][j]==cells[cell][k] && word[j]!=word[k]) good=false;
            }
            if(good) result|=Bits(1)<<index;
        }
        compatible[cell][pat]=result;
    }
}

int main() {
    int cases=0;
    while(cin>>label>>palette>>nv>>ns>>complete>>period) {
        assert(palette>=1 && palette<=3 && nv>0 && nv<128 && ns>0 && ns<=24 && period>0);
        cells.clear();fill(colors,colors+nv,-1);vector<int> seen(nv);
        for(int cell=0;cell<ns;++cell) {
            array<int,4> ids;
            for(int& v:ids) {cin>>v;assert(cin && v>=0 && v<nv);++seen[v];}
            cells.push_back(ids);
        }
        assert(all_of(seen.begin(),seen.end(),[](int n){return n>0;}));
        for(int axis=0;axis<2;++axis) {
            int amount;cin>>amount;assert(cin && amount>=0 && amount<1000);boundary[axis].clear();
            for(int j=0;j<amount;++j) {
                int a,b;cin>>a>>b;assert(cin && a>=0 && a<nv && b>=0 && b<nv);boundary[axis].push_back({a,b});
            }
        }
        prepare();if(complete) assert(ns==nt);
        nodes=models=cylinders[0]=cylinders[1]=toroidal=emitted=0;
        visit((1u<<ns)-1,-1,0);
        cout<<"C "<<label<<' '<<models<<' '<<nodes<<' '<<cylinders[0]<<' '<<cylinders[1]<<' '<<toroidal<<' '<<emitted<<'\n';cout.flush();
        cerr<<"COMPLETED "<<label<<' '<<models<<' '<<nodes<<' '<<cylinders[0]<<' '<<cylinders[1]<<' '<<toroidal<<' '<<emitted<<'\n';cerr.flush();++cases;
    }
    cerr<<"ALL_COMPLETED "<<cases<<'\n';
}
