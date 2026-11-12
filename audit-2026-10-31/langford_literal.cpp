// Literal L + answers20,21,22, used for the historical n=15 node count.
// One node is one entry to L2. This is not a mem-count model.
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
using namespace std;
int main(int argc,char **argv) {
  int n=argc>1?atoi(argv[1]):15;
  if(n<4 || n>30)return 2;
  array<int,64>x{},p{},y{},a{};
  array<uint64_t,32>profile{};
  int sub[]={0,1,2,0},add[]={0,1,2,1};
  int special=n-sub[n%4],half=n/4+add[n%4],start=(n+1)/2;
  int l=1,k,j,depth=0,q;
  uint64_t nodes=0,solutions=0;
  for(k=0;k<n;k++)p[k]=k+1;
L2:
  ++nodes;++profile[depth];
  k=p[0];
  if(k==0){++solutions;goto L5;}
  j=0;
  while(x[l]<0){
    if((l==half && a[special]==0) || (l>=start && a[(4*n+2-2*l)/3]==0))goto L5;
    ++l;
  }
L3:
  if(l+(3*k)/2>2*n)goto L5;
  if(l==half && a[special]==0){
    q=(4*n+2-2*l)/3;
    // The n=6 conflict; has no effect on the historical n=15 run.
    if(l>=start && a[q]==0 && q!=special)goto L5;
    while(k!=special){j=k;k=p[k];}
  }
  if(l>=start && a[(4*n+2-2*l)/3]==0)
    while(l+(3*k)/2!=2*n){j=k;k=p[k];}
  if(x[l+(3*k)/2]==0){
    x[l]=k;x[l+(3*k)/2]=-k;y[l]=j;p[j]=p[k];a[k]=1;
    ++l;++depth;goto L2;
  }
L4:
  // Necessary when a forced symmetry choice has an occupied second cell.
  if(l==half && k==special)goto L5;
  j=k;k=p[j];if(k)goto L3;
L5:
  --l;
  if(l>0){
    while(x[l]<0)--l;
    k=x[l];x[l]=0;x[l+(3*k)/2]=0;j=y[l];p[j]=k;a[k]=0;--depth;
    if(l==half && k==special)goto L5;
    goto L4;
  }
  cout<<"{\"n\":"<<n<<",\"nodes\":"<<nodes<<",\"representatives\":"<<solutions<<",\"profile\":[";
  for(int t=0;t<=n;t++){if(t)cout<<",";cout<<profile[t];}cout<<"]}\n";
}
