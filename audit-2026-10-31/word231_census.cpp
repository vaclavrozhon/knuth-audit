// Cell-by-cell intersection of row/column tries. Each leaf is validated afresh.
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
struct Node { array<int,26> next{}; uint32_t mask=0; bool end=false; };
struct Trie {
    vector<Node> nodes{1}; set<string> words;
    void add(const string& s) {
        if(!words.insert(s).second) throw runtime_error("duplicate word");
        int p=0;
        for(char c:s) {
            int a=c-'a'; if(a<0||a>=26) throw runtime_error("invalid letter");
            if(!nodes[p].next[a]) {
                int q=int(nodes.size()); nodes[p].next[a]=q;
                nodes[p].mask|=uint32_t(1)<<a; nodes.emplace_back();
            }
            p=nodes[p].next[a];
        }
        nodes[p].end=true;
    }
};
Trie rows,cols;
array<int,5> cp{};
array<array<char,5>,4> board{};
array<uint64_t,21> profile{};
array<int,26> value{1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10};
uint64_t count=0, validated=0;
int best=-1; vector<string> winners;
int letter(int i,int j) {return i==1&&j==1?3:i==2&&j==3?2:1;}
int row_multiplier(int i) {return i==0?2:i==3?3:1;}
int col_multiplier(int j) {return j==0?2:j==4?3:1;}
string validate(int cost) {
    string flat; int score=0;
    for(int i=0;i<4;++i) {
        string w; int s=0;
        for(int j=0;j<5;++j) {w+=board[i][j]; s+=value[board[i][j]-'a']*letter(i,j);}
        if(!rows.words.count(w)) throw runtime_error("invalid row");
        score+=s*row_multiplier(i); flat+=w;
    }
    for(int j=0;j<5;++j) {
        string w; int s=0;
        for(int i=0;i<4;++i) {w+=board[i][j]; s+=value[board[i][j]-'a']*letter(i,j);}
        if(!cols.words.count(w)) throw runtime_error("invalid column");
        score+=s*col_multiplier(j);
    }
    if(score!=cost) throw runtime_error("score mismatch");
    ++validated; return flat;
}
void visit(int k,int rp,int cost) {
    ++profile[k];
    if(k==20) {
        string flat=validate(cost); ++count;
        cout<<flat<<' '<<cost<<'\n';
        if(cost>best) {best=cost; winners.clear();}
        if(cost==best) winners.push_back(flat);
        return;
    }
    int i=k/5,j=k%5,p=cp[j];
    uint32_t choices=rows.nodes[rp].mask&cols.nodes[p].mask;
    while(choices) {
        int a=countr_zero(choices); choices&=choices-1;
        int r=rows.nodes[rp].next[a],c=cols.nodes[p].next[a];
        if(j==4&&!rows.nodes[r].end) throw runtime_error("nonterminal row");
        if(i==3&&!cols.nodes[c].end) throw runtime_error("nonterminal column");
        board[i][j]=char('a'+a); cp[j]=c;
        int price=value[a]*letter(i,j)*(row_multiplier(i)+col_multiplier(j));
        visit(k+1,j==4?0:r,cost+price); cp[j]=p;
    }
}
int main(int argc,char** argv) {
    if(argc!=4) return 2;
    int limit=stoi(argv[3]);
    for(auto entry:{pair<Trie*,string>{&rows,argv[1]}, {&cols,argv[2]}}) {
        ifstream f(entry.second); string w; int used=0;
        if(!f) throw runtime_error("cannot open words");
        while(used<limit&&getline(f,w)) {
            if(w.size()!=(entry.first==&rows?5:4)) throw runtime_error("wrong word length");
            entry.first->add(w); ++used;
        }
    }
    visit(0,0,0);
    cerr<<"{\"count\":"<<count<<",\"validated\":"<<validated<<",\"best\":"<<best<<",\"best_models\":[";
    for(size_t i=0;i<winners.size();++i) cerr<<(i?",":"")<<'"'<<winners[i]<<'"';
    cerr<<"],\"profile\":[";
    for(size_t i=0;i<profile.size();++i) cerr<<(i?",":"")<<profile[i];
    cerr<<"]}\n";
}
