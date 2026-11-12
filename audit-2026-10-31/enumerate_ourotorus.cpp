// Independent cell assignment, with uniqueness checks only on closed windows.
// No exact-cover data structures or option encodings are used.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
struct Window { vector<int> cells, offsets; };
int radix, height, width, window_width, total;
array<int,32> board, order, rankof;
vector<Window> windows;
array<vector<int>,32> finishes;
uint64_t nodes=0, solutions=0;

int pattern(const Window& w) {
    int base=(board[w.cells[0]]+w.offsets[0])%radix;
    int value=0;
    for (size_t i=1;i<w.cells.size();++i)
        value=value*radix+(board[w.cells[i]]+w.offsets[i]-base+radix)%radix;
    return value;
}

void visit(int depth,uint64_t seen) {
    ++nodes;
    if (nodes%100000000==0) cerr<<"progress "<<nodes<<" nodes "<<solutions<<" solutions\n";
    if (depth==total) {
        assert(__builtin_popcountll(seen)==total);
        ++solutions;
        for(int i=0;i<total;++i)cout<<board[i];
        cout<<'\n';
        return;
    }
    int cell=order[depth];
    // All-zero top-left window: 6 cells in96, 4 cells in97. For97 this
    // also fixes the global color; add all three colors after enumeration.
    bool fixed=cell/width<2 && cell%width<window_width;
    for(int value=0;value<(fixed?1:radix);++value) {
        board[cell]=value;
        uint64_t added=0;
        bool okay=true;
        for(int wi:finishes[depth]) {
            uint64_t bit=uint64_t(1)<<pattern(windows[wi]);
            if((seen|added)&bit) {okay=false;break;}
            added|=bit;
        }
        if(okay)visit(depth+1,seen|added);
    }
}

int main(int argc,char**argv) {
    assert(argc==2);
    int exercise=stoi(argv[1]);assert(exercise==96||exercise==97);
    radix=exercise==96?2:3;
    height=exercise==96?4:3;
    width=exercise==96?8:9;
    window_width=exercise==96?3:2;
    total=height*width;
    for(int i=0;i<total;++i)order[i]=rankof[i]=i;
    for(int r=0;r<height;++r)for(int c=0;c<width;++c) {
        Window w;
        for(int dr=0;dr<2;++dr)for(int dc=0;dc<window_width;++dc) {
            int rr=r+dr,cc=(c+dc)%width,offset=0;
            if(rr==height) {rr=0;offset=1;if(exercise==97)cc=(cc+width-3)%width;}
            w.cells.push_back(rr*width+cc);w.offsets.push_back(offset);
        }
        int last=0;for(int cell:w.cells)last=max(last,rankof[cell]);
        finishes[last].push_back(windows.size());windows.push_back(w);
    }
    visit(0,0);
    cerr<<"COMPLETED "<<exercise<<" "<<nodes<<" nodes "<<solutions<<" solutions\n";
}
