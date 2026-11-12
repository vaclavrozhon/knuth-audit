// Independent row-bit enumeration for the symmetry counts in DLX22--24.
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Counts {
  uint64_t total=0, half=0, quarter=0, weak=0, stronger=0, oriented=0;
};
int n;
uint32_t full;
array<int,32> pos;
array<Counts,5> counts;
uint64_t nodes=0;
bool emit=false;
vector<vector<int>> models;

void leaf(int main_diag, int anti_diag) {
  bool center=(n%2 && pos[n/2]==n/2);
  int kind=main_diag+anti_diag==0 ? (n%2 ? 0 : 3)
          : main_diag+anti_diag==1 ? 1 : center ? 4 : 2;
  auto &s=counts[kind]; s.total++;
  bool half=true,quarter=true;
  for(int r=0;r<n;r++) {
    if(pos[n-1-r]!=n-1-pos[r]) half=false;
    if(pos[pos[r]]!=n-1-r) quarter=false;
  }
  s.half+=half;s.quarter+=quarter;
  int mid=n/2;
  if(kind==0) {
    int i=0;while(pos[i]!=mid)i++;
    int j=pos[mid];s.oriented+=(i<j && j<mid);
  } else if(kind==1) {
    int diag=-1,right=0;
    for(int r=0;r<n;r++) {if(pos[r]==r)diag=r;if(pos[r]==n-1)right=r;}
    s.oriented+=(diag>=0 && diag<mid && pos[n-1]>right);
  } else if(kind==2) {
    int i=-1,j=-1;
    for(int r=0;r<n;r++){if(pos[r]==r)i=r;if(pos[r]+r==n-1)j=r;}
    s.oriented+=(i<j && j<mid);
  } else {
    int a=pos[0]+1,b=0,c=n-pos[n-1],d=0;
    for(int r=0;r<n;r++){if(pos[r]==n-1)b=r+1;if(pos[r]==0)d=n-r;}
    bool weak=a<=b && a<=c && a<=d && b<n+1-a && c<n+1-a && d<n+1-a;
    bool tie=(a<b && a<c && a<d) || (a==b && a<c && a<d)
            || (a==b && a==c && a<d) || (a==b && a==c && a==d)
            || (a==c && a<b && a<d);
    s.weak+=weak;s.stronger+=weak && tie;
  }
  if(emit){vector<int> model;for(int r=0;r<n;r++)model.push_back(pos[r]+1);models.push_back(model);}
}

void search(int r,uint32_t cols,uint32_t down,uint32_t up,int main_diag,int anti_diag) {
  nodes++;
  if(r==n){leaf(main_diag,anti_diag);return;}
  uint32_t available=full & ~(cols|down|up);
  while(available){uint32_t bit=available & -available;available-=bit;
    int c=__builtin_ctz(bit);pos[r]=c;
    search(r+1,cols|bit,((down|bit)<<1)&full,(up|bit)>>1,
           main_diag+(r==c),anti_diag+(r+c==n-1));
  }
}

int main(int argc,char**argv) {
  if(argc<2)return 2;
  n=stoi(argv[1]);if(n<2||n>17)return 2;
  emit=argc>2 && string(argv[2])=="--models";
  full=(1u<<n)-1;
  auto start=chrono::steady_clock::now();search(0,0,0,0,0,0);
  const char* labels[]={"22a","22b","22c","23a","23b"};
  uint64_t total=0,half=0,quarter=0;
  cout<<"{\"n\":"<<n<<",\"nodes\":"<<nodes<<",\"cases\":{";
  for(int k=0;k<5;k++){auto s=counts[k];total+=s.total;half+=s.half;quarter+=s.quarter;
    if(k)cout<<",";
    cout<<"\""<<labels[k]<<"\":{\"total\":"<<s.total<<",\"half\":"<<s.half
        <<",\"quarter\":"<<s.quarter<<",\"weak\":"<<s.weak<<",\"stronger\":"<<s.stronger
        <<",\"oriented\":"<<s.oriented<<"}";
  }
  cout<<"},\"total\":"<<total<<",\"half\":"<<half<<",\"quarter\":"<<quarter
      <<",\"Qa\":"<<(total-half)/8<<",\"Qs\":"<<(half-quarter)/4
      <<",\"Qd\":"<<quarter/2<<",\"seconds\":"
      <<chrono::duration<double>(chrono::steady_clock::now()-start).count();
  if(emit){cout<<",\"models\":[";bool first=true;
    for(auto m:models){if(!first)cout<<",";first=false;cout<<"[";
      for(int r=0;r<n;r++){if(r)cout<<",";cout<<m[r];}cout<<"]";}cout<<"]";}
  cout<<"}\n";
}
