// Exact Algorithm-Z signature recursion for X262(a), column order, no MRV.
// One branch node is output for each successful child of each distinct state.
#include <gmpxx.h>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <vector>
using cpp_int = mpz_class;

struct Audit {
  int height, width, corner;
  std::vector<bool> board;
  std::unordered_map<uint64_t, cpp_int> memo;
  uint64_t nodes = 0, successful = 0, calls = 0;
  Audit(int h,int w,int c):height(h),width(w),corner(c),board(h*w) {
    for(int col=0;col<w;col++) for(int row=0;row<h;row++)
      board[col*h+row] = row+col>=c && h-1-row+col>=c &&
                         row+w-1-col>=c && h-1-row+w-1-col>=c;
  }
  cpp_int solve(int pos,uint64_t mask) {
    calls++;
    while(pos<height*width && ((mask&1) || !board[pos])) {
      mask >>= 1;pos++;
    }
    if(pos==height*width) {
      if(mask) throw std::runtime_error("leftover frontier");
      return 1;
    }
    uint64_t key=(uint64_t(pos)<<height)|mask;
    auto found=memo.find(key);
    if(found!=memo.end()) return found->second;
    cpp_int total=0;
    // A vertical neighbor occurs only within the same geometric column.
    if(pos%height+1<height && board[pos+1] && !(mask&2)) {
      cpp_int child=solve(pos+1,(mask|2)>>1);
      if(child!=0) nodes++;
      total+=child;
    }
    // Horizontal neighbor is one full column ahead of the current position.
    if(pos+height<height*width && board[pos+height] && !(mask&(uint64_t(1)<<height))) {
      cpp_int child=solve(pos+1,(mask|(uint64_t(1)<<height))>>1);
      if(child!=0) nodes++;
      total+=child;
    }
    if(total!=0) successful++;
    memo.emplace(key,total);
    return total;
  }
};

int main(int argc,char**argv) {
  if(argc!=4) {std::cerr<<"usage: aztec_zdd height width corner\n";return 2;}
  int h=std::stoi(argv[1]),w=std::stoi(argv[2]),c=std::stoi(argv[3]);
  if(h<1 || h>24 || w<1 || c<0) return 2;
  auto start=std::chrono::steady_clock::now();
  Audit audit(h,w,c);cpp_int count=audit.solve(0,0);
  std::cout<<"{\"height\":"<<h<<",\"width\":"<<w<<",\"corner\":"<<c
           <<",\"solutions\":\""<<count<<"\",\"zdd_nodes\":"<<(audit.nodes==0?1:audit.nodes+2)
           <<",\"cached_nonempty_states\":"<<audit.memo.size()
           <<",\"successful_nonempty_states\":"<<audit.successful
           <<",\"calls\":"<<audit.calls<<",\"seconds\":"
           <<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()
           <<"}\n";
}
