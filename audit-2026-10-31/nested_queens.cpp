// Independent geometric search: choose disjoint k-blocks in increasing row order,
// then complete all remaining rows by MRV. No exact-cover solver is used.
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
using U=uint64_t;
int n,k,t,p[32]; U full; uint64_t blocknodes=0,queennodes=0,models=0;
std::vector<std::vector<int>> patterns;std::ofstream output;
void emit(){models++;output<<'[';for(int r=0;r<n;r++)output<<(r?",":"")<<p[r];output<<"]\n";}
void complete(U rows,U cols,U plus,U minus){
  queennodes++;if(rows==full){emit();return;}
  int best=-1,bcount=100;U choices=0;
  for(int r=0;r<n;r++)if(!(rows>>r&1)){
    U a=0;
    for(int c=0;c<n;c++)if(!(cols>>c&1)&&!(plus>>(r+c)&1)&&!(minus>>(r-c+n-1)&1))a|=U(1)<<c;
    int count=__builtin_popcountll(a);if(!count)return;
    if(count<bcount){best=r;bcount=count;choices=a;}
  }
  while(choices){int c=__builtin_ctzll(choices);choices&=choices-1;p[best]=c;
    complete(rows|(U(1)<<best),cols|(U(1)<<c),plus|(U(1)<<(best+c)),minus|(U(1)<<(best-c+n-1)));
  }
}
void blocks(int left,int first,U rows,U cols,U plus,U minus){
  blocknodes++;if(!left){complete(rows,cols,plus,minus);return;}
  for(int r=first;r<=n-left*k;r++)for(int c=0;c<=n-k;c++){
    U cs=((U(1)<<k)-1)<<c;if(cs&cols)continue;
    for(const auto& q:patterns){
      U a=0,b=0;
      for(int i=0;i<k;i++){a|=U(1)<<(r+i+c+q[i]);b|=U(1)<<(r+i-c-q[i]+n-1);}
      if((a&plus)||(b&minus))continue;
      for(int i=0;i<k;i++)p[r+i]=c+q[i];
      blocks(left-1,r+k,rows|(((U(1)<<k)-1)<<r),cols|cs,plus|a,minus|b);
    }
  }
}
int main(int argc,char**argv){
  if(argc!=5)return 2;n=std::stoi(argv[1]);k=std::stoi(argv[2]);t=std::stoi(argv[3]);
  if(n>31||k>n||k*t>n||k<1)return 2;full=(U(1)<<n)-1;output.open(argv[4]);
  std::vector<int> q(k);std::iota(q.begin(),q.end(),0);
  do{bool good=true;for(int i=0;i<k;i++)for(int j=0;j<i;j++)if(abs(q[i]-q[j])==i-j)good=false;
     if(good)patterns.push_back(q);
  }while(std::next_permutation(q.begin(),q.end()));
  auto start=std::chrono::steady_clock::now();blocks(t,0,0,0,0,0);
  double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
  std::cout<<"{\"n\":"<<n<<",\"k\":"<<k<<",\"t\":"<<t<<",\"models\":"<<models
           <<",\"block_nodes\":"<<blocknodes<<",\"queen_nodes\":"<<queennodes<<",\"seconds\":"<<seconds<<"}\n";
}
