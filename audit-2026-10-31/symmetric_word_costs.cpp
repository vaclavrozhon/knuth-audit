// An explicit adaptation of answer 7.2.2--30, not recovered author code.
// Fill the upper triangle using one compressed trie in both directions.
// Every (character, link) pair and every pair of continuation pointers fits
// in one 64-bit word. Count logical word accesses, not processor cache misses.
// Validation, output, and statistics are excluded, as in the author's programs.
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;
using U64 = uint64_t;
using U32 = uint32_t;
struct Node { array<U32, 26> next{}; };
struct Costs {
  U64 trie_reads=0, prefix_reads=0, prefix_writes=0;
  U64 stack_reads=0, stack_writes=0;
  U64 total() const {
    return trie_reads+prefix_reads+prefix_writes+stack_reads+stack_writes;
  }
};

int main(int argc, char** argv) {
  if (argc<2 || argc>3 || (argc==3 && string(argv[2])!="--emit")) {
    cerr << "Usage: symmetric-word-costs dictionary [--emit]\n";
    return 2;
  }
  try {
    const bool emit=argc==3;
    ifstream input(argv[1]);
    if (!input) throw runtime_error("Cannot open dictionary");
    vector<string> words;
    unordered_set<string> unique;
    string word;
    while (input>>word) {
      if (!unique.insert(word).second) throw runtime_error("Duplicate word");
      words.push_back(word);
    }
    if (words.empty()) throw runtime_error("Empty dictionary");
    const int n=int(words[0].size());
    if (n<1 || n>12) throw runtime_error("Word length must be between 1 and 12");
    if (emit && words.size()>30) throw runtime_error("--emit is for small checks only");
    vector<Node> nodes(1);
    for (size_t id=0; id<words.size(); ++id) {
      const auto& w=words[id];
      if (int(w.size())!=n) throw runtime_error("Mixed word lengths");
      U32 p=0;
      for (int k=0; k<n; ++k) {
        const int c=w[k]-'a';
        if (c<0 || c>=26) throw runtime_error("Non-lowercase character");
        if (k==n-1) nodes[p].next[c]=U32(id+1);
        else {
          U32 q=nodes[p].next[c];
          if (!q) {
            q=U32(nodes.size()); nodes[p].next[c]=q;
            nodes.emplace_back();
          }
          p=q;
        }
      }
    }
    // Record depth separately for compression; this is initialization only.
    vector<int> depth(nodes.size(),0);
    for (size_t p=0; p<nodes.size(); ++p)
      if (depth[p]<n-1)
        for (U32 q:nodes[p].next) if (q) depth[q]=depth[p]+1;
    vector<U32> base(nodes.size());
    U32 size=0;
    for (size_t p=0; p<nodes.size(); ++p) {
      base[p]=size;
      for (U32 q:nodes[p].next) if (q) ++size;
      ++size; // One zero sentinel after each node.
    }
    vector<U64> trie(size,0);
    for (size_t p=0; p<nodes.size(); ++p) {
      U32 at=base[p];
      for (int c=0; c<26; ++c) {
        U32 q=nodes[p].next[c];
        if (q) {
          U32 link=depth[p]==n-1 ? q : base[q];
          trie[at++]=(U64(link)<<8)|U64(c+1);
        }
      }
    }
    const U64 prefixes=nodes.size(), edges=prefixes-1+words.size();
    if (trie.size()!=prefixes+edges) throw runtime_error("Trie size invariant");
    // Conservative construction bound for flat arrays: input and insertion
    // <=(4n+10)W, zeroing and three 26-way scans plus metadata <=128P,
    // and writing/relocating edges <=4E. Host allocation and file I/O are not
    // search mems. This bound includes initialization, unlike search_mems.
    const U64 initialization_bound=U64(4*n+10)*words.size()+128*prefixes+4*edges;
    array<array<U32,13>,12> a{};
    array<U64,78> stack{};
    array<array<char,12>,12> grid{}; // Independent validation; not search state.
    vector<U64> profile(n*(n+1)/2+1,0);
    vector<vector<string>> emitted;
    Costs cost;
    for (int k=0; k<n; ++k) {a[k][0]=0; ++cost.prefix_writes;}
    U64 count=0, hash_sum=0, hash_xor=0;
    int i=0,j=0,l=0;
    U32 p=0,q=0;
    U64 left=0,right=0;
    auto read_trie=[&](U32 index) {++cost.trie_reads; return trie.at(index);};
enter:
    ++profile[l];
    if (i==n) {
      // Validate every emitted square against the original dictionary strings,
      // including consistency with the independently maintained letter grid.
      vector<string> solution;
      U64 h=14695981039346656037ULL;
      for (int r=0; r<n; ++r) {
        U32 id=a[r][n];
        if (id==0 || id>words.size()) throw runtime_error("Invalid terminal ID");
        const string& w=words[id-1];
        for (int c=0; c<n; ++c) {
          if (w[c]!=grid[r][c] || grid[r][c]!=grid[c][r])
            throw runtime_error("Invalid symmetric square");
          h^=static_cast<unsigned char>(w[c]); h*=1099511628211ULL;
        }
        if (emit) solution.push_back(w);
      }
      ++count; hash_sum+=h; hash_xor^=h;
      if (emit) emitted.push_back(solution);
      goto backtrack;
    }
    p=a[i][j]; ++cost.prefix_reads;
    if (i==j) q=p;
    else {q=a[j][i]; ++cost.prefix_reads;}
    left=read_trie(p);
    right=i==j ? left : read_trie(q);
choose:
    if (!(left&255) || !(right&255)) goto backtrack;
    if ((left&255)<(right&255)) {left=read_trie(++p); goto choose;}
    if ((right&255)<(left&255)) {right=read_trie(++q); goto choose;}
    stack[l]=(U64(p)<<32)|q; ++cost.stack_writes;
    a[i][j+1]=U32(left>>8); ++cost.prefix_writes;
    if (i!=j) {a[j][i+1]=U32(right>>8); ++cost.prefix_writes;}
    grid[i][j]=grid[j][i]=char('a'+int(left&255)-1);
    ++l; ++j;
    if (j==n) {++i; j=i;}
    goto enter;
backtrack:
    if (!l) goto done;
    --l;
    if (i==j) {--i; j=n-1;} else --j;
    {U64 saved=stack[l]; ++cost.stack_reads; p=U32(saved>>32); q=U32(saved);}
    left=read_trie(++p);
    right=i==j ? left : read_trie(++q);
    goto choose;
done:
    cout << "{\"n\":"<<n<<",\"vocabulary\":"<<words.size()
         <<",\"prefix_nodes\":"<<prefixes<<",\"compressed_entries\":"<<trie.size()
         <<",\"count\":"<<count<<",\"validated_models\":"<<count
         <<",\"hash_sum_mod_2_64\":"<<hash_sum<<",\"hash_xor\":"<<hash_xor
         <<",\"search_mems\":"<<cost.total()
         <<",\"initialization_upper_bound\":"<<initialization_bound
         <<",\"total_upper_bound\":"<<cost.total()+initialization_bound
         <<",\"accesses\":{\"trie_reads\":"<<cost.trie_reads
         <<",\"prefix_reads\":"<<cost.prefix_reads
         <<",\"prefix_writes\":"<<cost.prefix_writes
         <<",\"stack_reads\":"<<cost.stack_reads
         <<",\"stack_writes\":"<<cost.stack_writes<<"},\"profile\":[";
    for (size_t k=0;k<profile.size();++k) {if(k)cout<<',';cout<<profile[k];}
    cout<<"],\"solutions\":[";
    for (size_t k=0;k<emitted.size();++k) {
      if(k)cout<<',';
      cout<<'[';
      for (int r=0;r<n;++r) {if(r)cout<<',';cout<<'"'<<emitted[k][r]<<'"';}
      cout<<']';
    }
    cout<<"]}\n";
  } catch (const exception& e) {
    cerr<<e.what()<<'\n'; return 1;
  }
}
