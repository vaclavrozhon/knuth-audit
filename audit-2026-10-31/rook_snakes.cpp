// All maximum rook paths/cycles on boards up to6: permutation representation.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <unordered_set>
#include <vector>
using U=uint64_t;
int n;
std::array<U,8> images(U mask){
  std::array<U,8> out={};while(mask){int v=__builtin_ctzll(mask);mask&=mask-1;int r=v/n,c=v%n;
    for(int f=0;f<2;f++){int x=r,y=f?n-1-c:c;for(int k=0;k<4;k++){out[f*4+k]|=U(1)<<(x*n+y);int z=x;x=y;y=n-1-z;}}
  }return out;
}
int type(int r,int c){int a=std::min(r,n-1-r),b=std::min(c,n-1-c);if(a>b)std::swap(a,b);return a*n+b;}
int main(int argc,char**argv){
  if(argc!=3)return 2;n=std::stoi(argv[1]);bool cycle=std::string(argv[2])=="cycle";
  if(n<2||n>6)return 2;std::vector<int> p(n),q(n);std::iota(p.begin(),p.end(),0);std::unordered_set<U> canonical;
  uint64_t count=0,fixed[8]={},categories[64]={};
  do{if(cycle&&p[0]!=0)continue;std::iota(q.begin(),q.end(),0);
    do{if(cycle&&q[0]>q[1])continue;U mask=0;
      for(int j=0;j<n;j++){
        mask|=U(1)<<(p[j]*n+q[j]);
        if(cycle)mask|=U(1)<<(p[j]*n+q[(j+1)%n]);
        else if(j+1<n)mask|=U(1)<<(p[j+1]*n+q[j]);
      }
      count++;auto im=images(mask);for(int g=0;g<8;g++)fixed[g]+=im[g]==mask;
      U key=*std::min_element(im.begin(),im.end());
      if(canonical.insert(key).second&&!cycle)categories[std::min(type(p[0],q[0]),type(p[n-1],q[n-1]))]++;
    }while(std::next_permutation(q.begin(),q.end()));
  }while(std::next_permutation(p.begin(),p.end()));
  std::cout<<"{\"n\":"<<n<<",\"mode\":\""<<(cycle?"cycle":"path")<<"\",\"positions\":"<<count<<",\"D4_classes\":"<<canonical.size()<<",\"fixed\":[";
  for(int g=0;g<8;g++)std::cout<<(g?",":"")<<fixed[g];std::cout<<"],\"endpoint_categories\":{";bool first=true;
  for(int j=0;j<n*n;j++)if(categories[j]){std::cout<<(first?"":",")<<'"'<<j<<"\":"<<categories[j];first=false;}std::cout<<"}}\n";
}
