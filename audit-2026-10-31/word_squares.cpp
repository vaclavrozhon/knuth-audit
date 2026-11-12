// Independent row-by-row symmetric word-square enumeration.
// Forward checks keep every not-yet-completed column in the dictionary trie.
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
struct Node { array<int,26> next{}; vector<int> words; int terminal=-1; };
vector<Node> trie;
vector<string> words;
array<int,13> rows{}, cols{};
int n, best, diagonal_best;
uint64_t square_count, within372, within500, diagonal_count;
array<uint64_t,14> profile{};
vector<int> best_rows, diagonal_best_rows;
vector<vector<int>> small_squares, diagonal_squares;

int rank_of(const string& s) {
  int p=0;
  for(char c:s){p=trie[p].next[c-'a'];if(!p)return 0;}
  return trie[p].terminal+1;
}
void search(int r,int maxrank) {
  ++profile[r];
  if(r==n){
    ++square_count;
    if(maxrank<best){best=maxrank;best_rows.assign(rows.begin(),rows.begin()+n);}
    if(maxrank<=372)++within372;
    if(maxrank<=500){++within500;if(n==5)small_squares.emplace_back(rows.begin(),rows.begin()+n);}
    if(n==5){
      string d,e;
      for(int i=0;i<n;i++){d+=words[rows[i]][i];e+=words[rows[i]][n-1-i];}
      int a=rank_of(d),b=rank_of(e);
      if(a && b){
        ++diagonal_count;
        diagonal_squares.emplace_back(rows.begin(),rows.begin()+n);
        int allrank=max(maxrank,max(a,b));
        if(allrank<diagonal_best){diagonal_best=allrank;diagonal_best_rows.assign(rows.begin(),rows.begin()+n);}
      }
    }
    return;
  }
  int node=cols[r];
  for(int id:trie[node].words){
    array<int,13> saved=cols;
    bool ok=true;
    for(int j=r+1;j<n;j++){
      int next=trie[cols[j]].next[words[id][j]-'a'];
      if(!next){ok=false;break;}
      cols[j]=next;
    }
    if(ok){rows[r]=id;search(r+1,max(maxrank,id+1));}
    cols=saved;
  }
}
void print_square(const vector<int>& ids){
  cout<<"[";
  for(size_t i=0;i<ids.size();i++){if(i)cout<<",";cout<<'"'<<words[ids[i]]<<'"';}
  cout<<"]";
}
void run(const string& file){
  ifstream in(file);if(!in){cerr<<"Cannot read "<<file<<"\n";exit(2);}
  words.clear();string w;while(in>>w)words.push_back(w);
  n=words[0].size();assert(n<=12);
  trie.clear();trie.emplace_back();
  for(size_t id=0;id<words.size();id++){
    assert((int)words[id].size()==n);int p=0;
    for(char c:words[id]){
      trie[p].words.push_back(id);
      if(!trie[p].next[c-'a']){
        int q=trie.size();trie[p].next[c-'a']=q;trie.emplace_back();
      }
      p=trie[p].next[c-'a'];
    }
    trie[p].words.push_back(id);assert(trie[p].terminal==-1);trie[p].terminal=id;
  }
  cols.fill(0);profile.fill(0);square_count=within372=within500=diagonal_count=0;
  best=diagonal_best=words.size()+1;best_rows.clear();diagonal_best_rows.clear();
  small_squares.clear();diagonal_squares.clear();search(0,0);
  cout<<"{\"file\":\""<<file<<"\",\"n\":"<<n<<",\"vocabulary\":"<<words.size()
      <<",\"count\":"<<square_count<<",\"minimax_rank\":"<<best<<",\"best_square\":";
  print_square(best_rows);cout<<",\"within372\":"<<within372<<",\"within500\":"<<within500
      <<",\"diagonal_count\":"<<diagonal_count<<",\"diagonal_minimax_rank\":"<<diagonal_best
      <<",\"diagonal_best_square\":";print_square(diagonal_best_rows);
  cout<<",\"small_squares\":[";
  for(size_t i=0;i<small_squares.size();i++){if(i)cout<<",";print_square(small_squares[i]);}
  cout<<"],\"diagonal_squares\":[";
  for(size_t i=0;i<diagonal_squares.size();i++){if(i)cout<<",";print_square(diagonal_squares[i]);}
  cout<<"],\"profile\":[";
  for(int i=0;i<=n;i++){if(i)cout<<",";cout<<profile[i];}cout<<"]}\n"<<flush;
  cerr<<file<<": "<<square_count<<" symmetric squares; minimax "<<best<<"\n";
}
int main(int argc,char**argv){for(int i=1;i<argc;i++)run(argv[i]);}
