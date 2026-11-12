// Independent coordinate-MRV alternative-solution oracle. No DLX data structure.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

std::array<int,81> board, answer, reference;
std::array<int,9> rows, columns, boxes;
std::uint64_t nodes;

bool visit(bool differs) {
    ++nodes;
    int chosen=-1, bits=0, length=10;
    for (int v=0; v<81; ++v) if (!board[v]) {
        int r=v/9, c=v%9, b=3*(r/3)+c/3;
        int available=1022 & ~(rows[r]|columns[c]|boxes[b]);
        int count=__builtin_popcount((unsigned)available);
        if (count<length) { chosen=v; bits=available; length=count; }
        if (!count) return false;
    }
    if (chosen<0) {
        if (differs) { answer=board; return true; }
        return false;
    }
    int r=chosen/9, c=chosen%9, b=3*(r/3)+c/3;
    int known=bits & (1<<reference[chosen]);
    bits ^= known;
    // Try values different from the reference first, then the reference value.
    while (bits || known) {
        int bit;
        if (bits) { bit=bits & -bits; bits-=bit; }
        else { bit=known; known=0; }
        int value=__builtin_ctz((unsigned)bit);
        board[chosen]=value;
        rows[r]|=bit; columns[c]|=bit; boxes[b]|=bit;
        bool found=visit(differs || value!=reference[chosen]);
        rows[r]^=bit; columns[c]^=bit; boxes[b]^=bit;
        board[chosen]=0;
        if (found) return true;
    }
    return false;
}

int main() {
    std::string initial, ref;
    if (!(std::cin>>initial>>ref) || initial.size()!=81 || ref.size()!=81) return 2;
    std::vector<int> positions;
    for (int v=0; v<81; ++v) {
        assert(ref[v]>='1' && ref[v]<='9');
        reference[v]=ref[v]-'0';
        if (initial[v]!='0' && initial[v]!='.') {
            assert(initial[v]==ref[v]);
            positions.push_back(v);
        }
    }
    assert(positions.size()<=64);
    std::uint64_t mask;
    while (std::cin>>mask) {
        board.fill(0); rows.fill(0); columns.fill(0); boxes.fill(0); nodes=0;
        for (unsigned j=0; j<positions.size(); ++j) if ((mask>>j)&1) {
            int v=positions[j], k=reference[v], r=v/9, c=v%9, b=3*(r/3)+c/3, bit=1<<k;
            assert(!((rows[r]|columns[c]|boxes[b])&bit));
            board[v]=k; rows[r]|=bit; columns[c]|=bit; boxes[b]|=bit;
        }
        bool found=visit(false);
        std::cout<<mask<<' '<<nodes<<' ';
        if (found) for (int k:answer) std::cout<<k;
        else std::cout<<'-';
        std::cout<<std::endl;
    }
}
