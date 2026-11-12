// Independent completeness count via six shared edge labels; then check EVERY
// reported set orbit using a complete seven-piece solver and all720 relabelings.
#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using Word=std::array<int,6>;
using Set=std::array<int,7>;
std::vector<Word> types;
int left_digit[120][7],right_digit[120][7];
unsigned char maps[720][120],zero_preimage[720];
std::vector<int> domains[6][7][7];
bool used[120]={};
std::array<int,6> edges;
uint64_t edge_pattern_models=0,valid_patterns=0;
auto start=std::chrono::steady_clock::now();

int type_id(Word w) {
  std::rotate(w.begin(),std::find(w.begin(),w.end(),1),w.end());
  auto it=std::lower_bound(types.begin(),types.end(),w);assert(it!=types.end() && *it==w);
  return it-types.begin();
}

void initialize() {
  Word w{1,2,3,4,5,6};
  do {types.push_back(w);} while(std::next_permutation(w.begin()+1,w.end()));
  int p=0;w={1,2,3,4,5,6};
  do {
    for(int t=0;t<120;++t) {
      Word b;
      for(int i=0;i<6;++i) b[i]=w[types[t][i]-1];
      maps[p][t]=type_id(b);
      if(maps[p][t]==0) zero_preimage[p]=t;
    }
    ++p;
  } while(std::next_permutation(w.begin(),w.end()));
  assert(p==720);
  for(int t=0;t<120;++t) for(int i=0;i<6;++i) {
    left_digit[t][types[t][i]]=types[t][(i+1)%6];
    right_digit[t][types[t][i]]=types[t][(i+5)%6];
  }
  // This enumeration starts from edge labels, without the outer-nut search.
  for(int k=0;k<6;++k) for(int l=1;l<=6;++l) for(int r=1;r<=6;++r) {
    if(l==r || l==k+1 || r==k+1) continue;
    std::vector<int> remaining;
    for(int v=1;v<=6;++v) if(v!=l && v!=r && v!=k+1) remaining.push_back(v);
    assert(remaining.size()==3);
    do {
      Word a{k+1,l,remaining[0],remaining[1],remaining[2],r};
      int t=type_id(a);
      if(t!=0) domains[k][l][r].push_back(t);
    } while(std::next_permutation(remaining.begin(),remaining.end()));
  }
}

void assign_remaining_faces(int k) {
  if(k==6) {++edge_pattern_models;return;}
  for(int t:domains[k][edges[(k+5)%6]][edges[k]]) if(!used[t]) {
    used[t]=true;assign_remaining_faces(k+1);used[t]=false;
  }
}

void enumerate_edges(int k) {
  if(k==6) {
    for(int i=0;i<6;++i) if(domains[i][edges[(i+5)%6]][edges[i]].empty()) return;
    ++valid_patterns;assign_remaining_faces(0);return;
  }
  for(int v=1;v<=6;++v) {edges[k]=v;enumerate_edges(k+1);}
}

struct FixedSetSearch {
  int left[6][7],right[6][7],count=0;
  void dfs(int k,unsigned available,int first,int previous) {
    if(k==6) {count+=(previous==first);return;}
    unsigned rest=available;
    while(rest) {
      int i=__builtin_ctz(rest);rest&=rest-1;
      if(k && previous!=left[k][i]) continue;
      dfs(k+1,available^(1u<<i),k?first:left[k][i],right[k][i]);
    }
  }
  int solve(const Set& nuts) {
    count=0;
    for(int c=0;c<7;++c) {
      for(int k=0;k<6;++k) for(int i=0;i<7;++i) {
        int d=types[nuts[c]][k];
        left[k][i]=left_digit[nuts[i]][d];right[k][i]=right_digit[nuts[i]][d];
      }
      dfs(0,127u^(1u<<c),0,0);
    }
    return count;
  }
};

int main(int argc,char** argv) {
  if(argc!=2) return 2;
  initialize();used[0]=true;enumerate_edges(0);
  std::cerr<<"Independent shared-edge count: "<<edge_pattern_models<<", patterns "<<valid_patterns<<'\n';
  std::ifstream input(argv[1]);assert(input);
  std::string header;std::getline(input,header);
  assert(header=="key\tanchored_models\tstabilizer\tsolutions\tsets");
  uint64_t key,c,h,q,weight,previous=0,rows=0,weighted_models=0,anchored=0,nonempty=0;
  std::array<uint64_t,5041> histogram{};
  FixedSetSearch search;
  while(input>>key>>c>>h>>q>>weight) {
    assert(key>previous);previous=key;
    Set a{};uint64_t tmp=key;
    for(int i=6;i>=1;--i) {a[i]=tmp&127;tmp>>=7;}
    assert(tmp==0 && a[6]<120 && std::is_sorted(a.begin(),a.end()) && std::adjacent_find(a.begin(),a.end())==a.end());
    bool member[120]={};for(int t:a) member[t]=true;
    unsigned stabilizer=0,eligible=0;
    // Full group loop with an inverse-image test; different from generator's
    // seven anchors times six special permutations.
    for(int p=0;p<720;++p) if(member[zero_preimage[p]]) {
      ++eligible;Set b;
      for(int i=0;i<7;++i) b[i]=maps[p][a[i]];
      std::sort(b.begin(),b.end());assert(b[0]==0);
      uint64_t candidate=0;
      for(int i=1;i<7;++i) candidate=(candidate<<7)|b[i];
      assert(candidate>=key);
      stabilizer+=(candidate==key);
    }
    assert(eligible==42 && stabilizer==h && 720%h==0 && weight==720/h && c*h==6*q);
    assert(q==static_cast<uint64_t>(search.solve(a)) && q>0 && q<=5040);
    histogram[q]+=weight;weighted_models+=weight*q;nonempty+=weight;anchored+=c;++rows;
    if(rows%500000==0) std::cerr<<"Verified orbits "<<rows<<", seconds "
      <<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<'\n';
  }
  assert(input.eof() && rows>0);
  assert(anchored==edge_pattern_models && weighted_models==120*edge_pattern_models);
  histogram[0]=59487568920ULL-nonempty;
  std::cout<<"{\"orbits_verified\":"<<rows<<",\"shared_edge_patterns\":"<<valid_patterns
    <<",\"independent_anchored_models\":"<<edge_pattern_models<<",\"histogram\":[";
  for(int i=0;i<=5040;++i) if(histogram[i]) {
    if(i) std::cout<<',';
    std::cout<<'['<<i<<','<<histogram[i]<<']';
  }
  std::cout<<"],\"weighted_models\":"<<weighted_models<<",\"elapsed_seconds\":"
    <<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"}\n";
}
