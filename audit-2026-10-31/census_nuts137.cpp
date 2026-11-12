// Enumerate all solutions with central type123456, quotient seven-type sets by S6.
// For a set orbit with stabilizer h and q solutions per set, the anchored tally
// is c=(720/h)*q/120=6*q/h. Thus q=c*h/6, with720/h equally likely type sets.
#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using Word=std::array<int,6>;
using Set=std::array<int,7>;
std::vector<Word> types,permutations;
unsigned char rename_type[720][120];
int maps_to_zero[120][6];
int left_digit[120][7],right_digit[120][7];
std::vector<int> choices[6][7];
uint64_t model_count=0;
std::unordered_map<uint64_t,uint32_t> census;
auto start=std::chrono::steady_clock::now();

int type_id(Word w) {
  std::rotate(w.begin(),std::find(w.begin(),w.end(),1),w.end());
  auto p=std::lower_bound(types.begin(),types.end(),w);
  assert(p!=types.end() && *p==w);
  return p-types.begin();
}

void initialize() {
  Word w{1,2,3,4,5,6};
  do { types.push_back(w); } while(std::next_permutation(w.begin()+1,w.end()));
  w={1,2,3,4,5,6};
  do { permutations.push_back(w); } while(std::next_permutation(w.begin(),w.end()));
  assert(types.size()==120 && permutations.size()==720);
  for(int p=0;p<720;++p) for(int t=0;t<120;++t) {
    Word renamed;
    for(int i=0;i<6;++i) renamed[i]=permutations[p][types[t][i]-1];
    rename_type[p][t]=type_id(renamed);
  }
  for(int t=0;t<120;++t) {
    int count=0;
    for(int p=0;p<720;++p) if(rename_type[p][t]==0) maps_to_zero[t][count++]=p;
    assert(count==6);
    for(int i=0;i<6;++i) {
      left_digit[t][types[t][i]]=types[t][(i+1)%6];
      right_digit[t][types[t][i]]=types[t][(i+5)%6];
    }
  }
  for(int k=0;k<6;++k) for(int t=1;t<120;++t)
    choices[k][left_digit[t][k+1]].push_back(t);
}

uint64_t encode(Set a) {
  std::sort(a.begin(),a.end());
  assert(a[0]==0 && std::adjacent_find(a.begin(),a.end())==a.end());
  uint64_t key=0;
  for(int i=1;i<7;++i) key=(key<<7)|a[i];
  return key;
}

Set decode(uint64_t key) {
  Set result{};
  for(int i=6;i>=1;--i) { result[i]=key&127; key>>=7; }
  assert(key==0);
  return result;
}

uint64_t canonical(const Set& a) {
  uint64_t best=UINT64_MAX;
  for(int t:a) for(int j=0;j<6;++j) {
    auto table=rename_type[maps_to_zero[t][j]];
    Set b;
    int least_positive=120;
    for(int i=0;i<7;++i) {
      b[i]=table[a[i]];
      if(b[i]) least_positive=std::min(least_positive,b[i]);
    }
    if(least_positive>static_cast<int>(best>>35)) continue;
    best=std::min(best,encode(b));
  }
  return best;
}

int stabilizer(const Set& a) {
  uint64_t key=encode(a);
  int count=0;
  for(int t:a) for(int j=0;j<6;++j) {
    auto table=rename_type[maps_to_zero[t][j]];
    Set b;
    for(int i=0;i<7;++i) b[i]=table[a[i]];
    count+=encode(b)==key;
  }
  assert(count==1 || count==2 || count==3 || count==6);
  return count;
}

Set selected{};
bool used[120]={};
void dfs(int k,int first_left,int previous_right) {
  if(k==6) {
    if(previous_right!=first_left) return;
    ++census[canonical(selected)];
    ++model_count;
    if(model_count%1000000==0)
      std::cerr<<"models "<<model_count<<", orbits "<<census.size()<<", seconds "
        <<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<'\n';
    return;
  }
  for(int t:choices[k][previous_right]) {
    if(used[t]) continue;
    used[t]=true; selected[k+1]=t;
    dfs(k+1,first_left,right_digit[t][k+1]);
    used[t]=false;
  }
}

int main(int argc,char** argv) {
  initialize();
  if(argc==2 && std::string(argv[1])=="--maps") {
    for(int p=0;p<720;++p) {
      for(int t=0;t<120;++t) std::cout<<int(rename_type[p][t])<<(t==119?'\n':' ');
    }
    return 0;
  }
  if(argc==2 && std::string(argv[1])=="--canonical") {
    Set a;
    while(std::cin>>a[0]) {
      for(int i=1;i<7;++i) { std::cin>>a[i]; assert(std::cin); }
      auto key=canonical(a);
      std::cout<<key<<' '<<stabilizer(decode(key))<<'\n';
    }
    return 0;
  }
  if(argc!=2) { std::cerr<<"Usage: binary census.tsv | --maps | --canonical\n";return 2; }
  census.reserve(7000000);
  selected[0]=0; used[0]=true;
  for(int first=1;first<120;++first) {
    selected[1]=first; used[first]=true;
    dfs(1,left_digit[first][1],right_digit[first][1]);
    used[first]=false;
  }
  // Stable sorted output is independently inspectable without the original solver.
  std::vector<std::pair<uint64_t,uint32_t>> entries(census.begin(),census.end());
  std::sort(entries.begin(),entries.end());
  std::ofstream output(argv[1]);assert(output);
  output<<"key\tanchored_models\tstabilizer\tsolutions\tsets\n";
  std::array<uint64_t,5041> histogram{};
  for(auto [key,count]:entries) {
    int h=stabilizer(decode(key));
    assert((count*h)%6==0);
    int solutions=count*h/6;
    assert(solutions>0 && solutions<=5040);
    histogram[solutions]+=720/h;
    output<<key<<'\t'<<count<<'\t'<<h<<'\t'<<solutions<<'\t'<<720/h<<'\n';
  }
  output.close();assert(output);
  uint64_t nonempty=0,total_solutions=0;
  for(int i=1;i<=5040;++i) { nonempty+=histogram[i];total_solutions+=i*histogram[i]; }
  assert(total_solutions==120*model_count && nonempty<=59487568920ULL);
  histogram[0]=59487568920ULL-nonempty;
  std::cout<<"{\"anchored_models\":"<<model_count<<",\"orbits\":"<<entries.size()<<",\"histogram\":[";
  for(int i=0;i<=5040;++i) if(histogram[i]) {
    if(i) std::cout<<',';
    std::cout<<'['<<i<<','<<histogram[i]<<']';
  }
  std::cout<<"],\"total_solutions\":"<<total_solutions<<",\"elapsed_seconds\":"
    <<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"}\n";
}
