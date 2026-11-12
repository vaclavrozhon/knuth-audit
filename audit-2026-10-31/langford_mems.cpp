// Literal L, L+20, L+20+21, and the corrected loose variant of answer22.
// Count one mem per array-word access; reuse x[l] after the L5 loop test.
// This is an explicit implementation of the printed method, not author code.
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
using U64=uint64_t;

template<bool Loose,int Variant> void run(int n,bool emit) {
  constexpr bool Force=Variant>0,Symmetry=Variant>1;
  if(n<1 || n>30 || (Loose && Symmetry && n<4)) throw runtime_error("Unsupported n");
  if(emit && n>10) throw runtime_error("--emit is only for small validation cases");
  array<int,64>x{},y{};
  array<int,32>p{},a{};
  array<U64,32>profile{};
  vector<vector<int>>models;
  int sub[]={0,1,2,0},add[]={0,1,2,1};
  int special=Loose?n-sub[n%4]:n-(n%2==0);
  int half=Loose?n/4+add[n%4]:n/2;
  int force_start=Loose?(n+1)/2:n-1;
  int l=1,k,j,depth=0,q,old_x;
  U64 nodes=0,solutions=0,mems=3*n+1+(Force?n:0);
  for(k=0;k<n;++k)p[k]=k+1;
  auto distance=[](int v){return Loose?(3*v)/2:v+1;};
  auto deadline=[&](){return Loose?(4*n+2-2*l)/3:2*n-l-1;};
L2:
  ++nodes;++profile[depth];
  if((nodes&((U64(1)<<30)-1))==0)
    cerr<<"nodes="<<nodes<<" mems="<<mems<<" representatives="<<solutions<<'\n';
  ++mems;k=p[0];
  if(k==0){
    ++solutions;
    if(emit)models.emplace_back(x.begin()+1,x.begin()+2*n+1);
    goto L5;
  }
  j=0;
  while((++mems,x[l])<0){
    if constexpr(Force){
      if constexpr(Symmetry) if(l==half && (++mems,a[special])==0)goto L5;
      if(l>=force_start && (++mems,a[deadline()])==0)goto L5;
    }
    ++l;
  }
L3:
  if(l+distance(k)>2*n)goto L5;
  if constexpr(Symmetry){
    if(l==half && (++mems,a[special])==0){
      // F082: two distinct forced labels cannot occupy the same cell.
      if constexpr(Loose){
        q=deadline();
        if(l>=force_start && (++mems,a[q])==0 && q!=special)goto L5;
      }
      while(k!=special){j=k;++mems;k=p[k];if(!k)throw runtime_error("Missing symmetry label");}
    }
  }
  if constexpr(Force){
    if(l>=force_start && (++mems,a[deadline()])==0)
      while(l+distance(k)!=2*n){j=k;++mems;k=p[k];if(!k)throw runtime_error("Missing deadline label");}
  }
  if((++mems,x[l+distance(k)])==0){
    x[l]=k;x[l+distance(k)]=-k;y[l]=j;p[j]=p[k];mems+=5;
    if constexpr(Force){a[k]=1;++mems;}
    ++l;++depth;goto L2;
  }
L4:
  // F082: a failed symmetry-forced choice must not try a larger label.
  // For the n15 loose benchmark the label is already the largest; this
  // affects at most the redundant p[special] read, not its search tree.
  if constexpr(Loose && Symmetry) if(l==half && k==special)goto L5;
  j=k;++mems;k=p[j];if(k)goto L3;
L5:
  --l;
  if(l>0){
    while((++mems,old_x=x[l])<0)--l;
    // old_x is the positive word already fetched by the final loop test.
    k=old_x;x[l]=0;x[l+distance(k)]=0;j=y[l];p[j]=k;mems+=4;
    if constexpr(Force){a[k]=0;++mems;}
    --depth;
    if constexpr(Symmetry) if(l==half && k==special)goto L5;
    goto L4;
  }
  cout<<"{\"n\":"<<n<<",\"loose\":"<<(Loose?"true":"false")
      <<",\"variant\":"<<Variant<<",\"nodes\":"<<nodes
      <<",\"representatives\":"<<solutions<<",\"mems\":"<<mems
      <<",\"mems_without_cached_L5_read\":"<<mems+nodes-1<<",\"profile\":[";
  for(int t=0;t<=n;++t){if(t)cout<<',';cout<<profile[t];}
  cout<<"],\"models\":[";
  for(size_t i=0;i<models.size();++i){
    if(i)cout<<',';
    cout<<'[';
    for(int t=0;t<2*n;++t){if(t)cout<<',';cout<<models[i][t];}
    cout<<']';
  }
  cout<<"]}\n";
}

int main(int argc,char**argv){
  if(argc<3 || argc>4)return 2;
  int n=atoi(argv[1]);string mode=argv[2];bool emit=argc==4 && string(argv[3])=="--emit";
  try{
    if(mode=="L")run<false,0>(n,emit);
    else if(mode=="L20")run<false,1>(n,emit);
    else if(mode=="L21")run<false,2>(n,emit);
    else if(mode=="loose21")run<true,2>(n,emit);
    else return 2;
  }catch(const exception&e){cerr<<e.what()<<'\n';return 1;}
}
