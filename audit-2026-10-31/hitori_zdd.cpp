// Connected vertex covers and their inclusion-minimal members, X439--444.
// ZDD high branches mark black cells, so minimal covers are maximal black sets.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

struct Node {int v,lo,hi;bool operator==(const Node&o)const{return v==o.v&&lo==o.lo&&hi==o.hi;}};
struct NodeHash {size_t operator()(const Node&n)const {
  uint64_t x=(uint64_t(uint32_t(n.lo))<<32)|uint32_t(n.hi);
  x^=uint64_t(n.v)*0x9e3779b97f4a7c15ULL;x^=x>>30;x*=0xbf58476d1ce4e5b9ULL;
  return x^(x>>27);
}};

struct ZDD {
  std::vector<Node> nodes{{1000,0,0},{1000,0,0}};
  std::unordered_map<Node,int,NodeHash> unique;
  std::unordered_map<uint64_t,int> unions,nonsubs;
  std::unordered_map<int,int> maxima;
  static uint64_t pair(int a,int b){return (uint64_t(uint32_t(a))<<32)|uint32_t(b);}
  int node(int v,int lo,int hi) {
    if(!hi)return lo;
    Node n{v,lo,hi};auto old=unique.find(n);if(old!=unique.end())return old->second;
    int id=nodes.size();nodes.push_back(n);unique.emplace(n,id);return id;
  }
  int unite(int a,int b) {
    if(!a)return b;
    if(!b || a==b)return a;
    if(a>b)std::swap(a,b);
    auto key=pair(a,b);auto old=unions.find(key);if(old!=unions.end())return old->second;
    Node x=nodes[a],y=nodes[b];int v=std::min(x.v,y.v);
    int lo=unite(x.v==v?x.lo:a,y.v==v?y.lo:b);
    int hi=unite(x.v==v?x.hi:0,y.v==v?y.hi:0);
    int result=node(v,lo,hi);unions.emplace(key,result);return result;
  }
  // Keep those sets in A which are not subsets of any member of B.
  int nonsub(int a,int b) {
    if(!a || !b)return a;
    if(a==1 || a==b)return 0;
    auto key=pair(a,b);auto old=nonsubs.find(key);if(old!=nonsubs.end())return old->second;
    Node x=nodes[a],y=nodes[b];int result;
    if(x.v<y.v)result=node(x.v,nonsub(x.lo,b),x.hi);
    else if(x.v>y.v)result=nonsub(a,unite(y.lo,y.hi));
    else result=node(x.v,nonsub(x.lo,unite(y.lo,y.hi)),nonsub(x.hi,y.hi));
    nonsubs.emplace(key,result);return result;
  }
  int maximal(int a) {
    if(a<2)return a;
    auto old=maxima.find(a);if(old!=maxima.end())return old->second;
    Node x=nodes[a];int hi=maximal(x.hi),lo=nonsub(maximal(x.lo),hi);
    int result=node(x.v,lo,hi);maxima.emplace(a,result);return result;
  }
  uint64_t count(int root)const {
    std::unordered_map<int,uint64_t> cache;
    auto visit=[&](auto&&self,int id)->uint64_t {
      if(id<2)return id;
      auto old=cache.find(id);if(old!=cache.end())return old->second;
      Node n=nodes[id];uint64_t a=self(self,n.lo),b=self(self,n.hi);
      if(std::numeric_limits<uint64_t>::max()-a<b)throw std::runtime_error("count overflow");
      cache[id]=a+b;return a+b;
    };
    return visit(visit,root);
  }
  std::unordered_map<int,std::vector<uint64_t>> polynomials(int root)const {
    std::unordered_map<int,std::vector<uint64_t>> cache{{0,{}},{1,{1}}};
    auto visit=[&](auto&&self,int id)->void {
      if(cache.count(id))return;
      Node n=nodes[id];self(self,n.lo);self(self,n.hi);
      const auto&a=cache.at(n.lo);const auto&b=cache.at(n.hi);
      std::vector<uint64_t> result(std::max(a.size(),b.size()+1));
      for(size_t i=0;i<a.size();i++)result[i]=a[i];
      for(size_t i=0;i<b.size();i++) {
        if(std::numeric_limits<uint64_t>::max()-result[i+1]<b[i])throw std::runtime_error("polynomial overflow");
        result[i+1]+=b[i];
      }
      while(!result.empty() && !result.back())result.pop_back();
      cache.emplace(id,std::move(result));
    };
    visit(visit,root);return cache;
  }
  uint64_t export_large(int root,int minimum,const std::string&path)const {
    auto poly=polynomials(root);uint64_t total=0;
    for(size_t i=minimum;i<poly.at(root).size();i++)total+=poly.at(root)[i];
    if(total>2000000)throw std::runtime_error("too many large covers to export: "+std::to_string(total));
    std::ofstream out(path);if(!out)throw std::runtime_error("cannot open export");
    std::vector<int> selected;uint64_t written=0;
    auto visit=[&](auto&&self,int id)->void {
      if(id==0 || int(selected.size()+poly.at(id).size())<=minimum)return;
      if(id==1) {
        out<<'[';
        for(size_t i=0;i<selected.size();i++){if(i)out<<',';out<<selected[i];}
        out<<"]\n";written++;return;
      }
      Node n=nodes[id];self(self,n.lo);selected.push_back(n.v);self(self,n.hi);selected.pop_back();
    };
    visit(visit,root);if(written!=total)throw std::runtime_error("export count mismatch");
    std::cout<<"{\"minimum\":"<<minimum<<",\"exported\":"<<written<<",\"cardinality_counts\":[";
    const auto&p=poly.at(root);for(size_t i=0;i<p.size();i++){if(i)std::cout<<',';std::cout<<p[i];}
    std::cout<<"]}\n";return written;
  }
  std::pair<int,int> range(int root)const {
    std::unordered_map<int,std::pair<int,int>> cache;
    auto visit=[&](auto&&self,int id)->std::pair<int,int> {
      if(id==0)return {1000,-1000};
      if(id==1)return {0,0};
      auto old=cache.find(id);if(old!=cache.end())return old->second;
      Node n=nodes[id];auto a=self(self,n.lo),b=self(self,n.hi);
      auto result=std::make_pair(std::min(a.first,b.first+1),std::max(a.second,b.second+1));
      cache[id]=result;return result;
    };
    return visit(visit,root);
  }
  size_t size(int root)const {
    std::unordered_set<int> seen;std::vector<int> todo{root};
    while(!todo.empty()) {
      int id=todo.back();todo.pop_back();if(!seen.insert(id).second)continue;
      if(id>=2){todo.push_back(nodes[id].lo);todo.push_back(nodes[id].hi);}
    }
    return seen.size();
  }
  uint32_t small_family(int root)const {
    if(root==0)return 0;
    if(root==1)return 1;
    Node n=nodes[root];uint32_t result=small_family(n.lo),hi=small_family(n.hi);
    for(int s=0;s<8;s++)if(hi>>s&1)result|=1U<<(s|(1<<n.v));
    return result;
  }
  int from_small(uint32_t family,int v=0) {
    if(!family)return 0;
    if(v==3)return 1;
    uint32_t lo=0,hi=0;
    for(int s=0;s<8;s++)if(family>>s&1) {
      if(s>>v&1)hi|=1U<<(s^(1<<v));else lo|=1U<<s;
    }
    return node(v,from_small(lo,v+1),from_small(hi,v+1));
  }
};

void validate_operators() {
  ZDD z;std::vector<int> roots;
  for(int f=0;f<256;f++) {
    roots.push_back(z.from_small(f));if(z.small_family(roots.back())!=uint32_t(f))throw std::runtime_error("construction");
    uint32_t expected=0;
    for(int a=0;a<8;a++)if(f>>a&1) {
      bool maximal=true;
      for(int b=0;b<8;b++)if(a!=b && (f>>b&1) && (a&b)==a)maximal=false;
      if(maximal)expected|=1U<<a;
    }
    if(z.small_family(z.maximal(roots.back()))!=expected)throw std::runtime_error("maximal");
  }
  for(int f=0;f<256;f++)for(int g=0;g<256;g++) {
    uint32_t expected=0;
    for(int a=0;a<8;a++)if(f>>a&1) {
      bool keep=true;
      for(int b=0;b<8;b++)if((g>>b&1) && (a&b)==a)keep=false;
      if(keep)expected|=1U<<a;
    }
    if(z.small_family(z.nonsub(roots[f],roots[g]))!=expected)throw std::runtime_error("nonsub");
    if(z.small_family(z.unite(roots[f],roots[g]))!=uint32_t(f|g))throw std::runtime_error("union");
  }
  std::cout<<"{\"families\":256,\"nonsub_pairs\":65536,\"union_pairs\":65536,\"maximal_checks\":256}\n";
}

struct Frontier {
  std::array<uint8_t,9> labels{};uint16_t black=0;bool closed=false;
};

struct Hitori {
  int height,width;ZDD z;
  std::unordered_map<uint64_t,int> memo;
  Hitori(int h,int w):height(std::max(h,w)),width(std::min(h,w)){}
  void canonical(Frontier&s)const {
    std::array<uint8_t,10> names{};uint8_t next=0;
    for(int j=0;j<width;j++)if(s.labels[j]) {
      if(!names[s.labels[j]])names[s.labels[j]]=++next;
      s.labels[j]=names[s.labels[j]];
    }
  }
  uint64_t key(int pos,const Frontier&s)const {
    uint64_t k=pos;k=(k<<1)|s.closed;k=(k<<width)|s.black;
    for(int j=0;j<width;j++)k=(k<<4)|s.labels[j];
    return k;
  }
  int solve(int pos,Frontier state) {
    if(pos==height*width) {
      if(state.closed)return 1;
      int component=0;
      for(int j=0;j<width;j++)if(state.labels[j]) {
        if(component && component!=state.labels[j])return 0;
        component=state.labels[j];
      }
      return component?1:0;
    }
    auto signature=key(pos,state);auto old=memo.find(signature);if(old!=memo.end())return old->second;
    int column=pos%width,lo=0,hi=0;
    // Keep this cell white, joining its upper and left white components.
    if(!state.closed) {
      Frontier next=state;int up=next.labels[column],left=column?next.labels[column-1]:0;
      int component=up?up:left;
      if(up && left && up!=left)for(auto&v:next.labels)if(v==left)v=up;
      if(!component)component=1+*std::max_element(next.labels.begin(),next.labels.begin()+width);
      next.labels[column]=component;next.black&=~(1<<column);canonical(next);
      lo=solve(pos+1,next);
    }
    // Black cells form an independent set.
    if(!(state.black>>column&1) && !(column && (state.black>>(column-1)&1))) {
      Frontier next=state;int up=next.labels[column];next.labels[column]=0;next.black|=1<<column;
      bool valid=true;
      if(up && std::find(next.labels.begin(),next.labels.begin()+width,up)==next.labels.begin()+width) {
        if(std::any_of(next.labels.begin(),next.labels.begin()+width,[](int v){return v!=0;}))valid=false;
        else next.closed=true;
      }
      if(valid){canonical(next);hi=solve(pos+1,next);}
    }
    int result=z.node(pos,lo,hi);memo.emplace(signature,result);return result;
  }
};

int main(int argc,char**argv) {
  try {
    if(argc==2 && std::string(argv[1])=="--validate"){validate_operators();return 0;}
    if(argc!=3 && argc!=5){std::cerr<<"usage: hitori_zdd rows columns [--large-black output.jsonl] | --validate\n";return 2;}
    int rows=std::stoi(argv[1]),cols=std::stoi(argv[2]);if(rows<1||cols<1||rows>9||cols>9)return 2;
    auto start=std::chrono::steady_clock::now();Hitori h(rows,cols);int base=h.solve(0,{});
    uint64_t base_count=h.z.count(base);size_t base_nodes=h.z.size(base);
    std::cerr<<rows<<"x"<<cols<<" connected covers: "<<base_count<<", ZDD "<<base_nodes
             <<", frontier states "<<h.memo.size()<<"\n";
    if(argc==5) {
      if(std::string(argv[3])!="--large-black")return 2;
      h.z.export_large(base,(rows*cols+2)/3,argv[4]);return 0;
    }
    int maximal=h.z.maximal(base);auto range=h.z.range(maximal);
    std::cout<<"{\"rows\":"<<rows<<",\"columns\":"<<cols
             <<",\"connected_vertex_covers\":"<<base_count<<",\"hitori_covers\":"<<h.z.count(maximal)
             <<",\"min_black\":"<<range.first<<",\"max_black\":"<<range.second
             <<",\"base_zdd_nodes\":"<<base_nodes<<",\"maximal_zdd_nodes\":"<<h.z.size(maximal)
             <<",\"frontier_states\":"<<h.memo.size()<<",\"allocated_zdd_nodes\":"<<h.z.nodes.size()
             <<",\"union_memos\":"<<h.z.unions.size()<<",\"nonsub_memos\":"<<h.z.nonsubs.size()
             <<",\"seconds\":"<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"}\n";
  } catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 1;}
}
