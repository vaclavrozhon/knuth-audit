// Complete exchange histories through n=8; independent graph predicates.
#include <array>
#include <vector>
#include <iostream>
#include <cstdint>
#include <algorithm>
using namespace std;
bool right_family(const array<int,9>& a,int l,int r){
 if(l>r)return true;
 int k=a[r];if(k<l||k>r)return false;
 if(k==r){for(int i=l;i<=r;i++)if(a[i]!=r)return false;return true;}
 for(int i=l;i<k;i++)if(a[i]!=r)return false;
 return right_family(a,k,r-1);
}
bool bst_interval(const array<int,9>&a,int l,int r,int parent){
 if(l>r)return true;
 int root=0;
 for(int i=l;i<=r;i++)if(a[i]==parent){if(root)return false;root=i;}
 if(!root)return false;
 return bst_interval(a,l,root-1,root)&&bst_interval(a,root+1,r,root);
}
bool bst(const array<int,9>&a,int n){
 int root=0;for(int i=1;i<=n;i++)if(a[i]==i){if(root)return false;root=i;}
 return root && bst_interval(a,1,root-1,root)&&bst_interval(a,root+1,n,root);
}
int main(){
 for(int n=1;n<=8;n++){
  uint64_t hist=1;for(int j=0;j<n;j++)hist*=n;
  vector<uint32_t> counts(hist,0);array<int,9>a{},p{};uint64_t ca=0,cb=0,cc=0;
  for(uint64_t h=0;h<hist;h++){
   uint64_t q=h;for(int j=1;j<=n;j++){a[j]=int(q%n)+1;q/=n;p[j]=j;}
   for(int j=1;j<=n;j++)swap(p[j],p[a[j]]);
   uint64_t code=0;bool aa=true,bb=true,ccc=true;
   for(int j=1;j<=n;j++){
    code=code*n+(p[j]-1);aa &= p[j]==(j==1?n:j-1);bb &= p[j]==j;ccc &=p[j]==(j==n?1:j+1);
   }
   counts[code]++;
   // Check both directions for every graph, not only target representations.
   bool invol=true;for(int j=1;j<=n;j++)invol &= a[a[j]]==j;
   if(aa!=right_family(a,1,n)||bb!=invol||ccc!=bst(a,n))return 2;
   ca+=aa;cb+=bb;cc+=ccc;
  }
  uint32_t lo=UINT32_MAX,hi=0;uint64_t perm=0,lowest=0,highest=0;
  for(auto c:counts)if(c){perm++;lo=min(lo,c);hi=max(hi,c);}
  for(auto c:counts){lowest+=c==lo;highest+=c==hi;}
  cout<<"{\"n\":"<<n<<",\"histories\":"<<hist<<",\"permutations\":"<<perm<<",\"right\":"<<ca<<",\"identity\":"<<cb<<",\"left\":"<<cc<<",\"min\":"<<lo<<",\"max\":"<<hi<<",\"minimizers\":"<<lowest<<",\"maximizers\":"<<highest<<"}"<<endl;
 }
}
