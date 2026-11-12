// Backtrack exercise 7: independent row-order and minimum-domain enumerations.
// Four fixed queens are (0,1),(1,n-1),(n-2,0),(n-1,n-2), zero based.
// Optional arguments fix the columns of rows 2 and 3 to partition a large run.
// --orbit-filter keeps boards whose row-2 column is least under the four rotations.
// A kept board with t tied rotations has weight 4/t. No reflections are used.
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
using U=uint64_t;
using Big=__uint128_t;
int n;
U full;
std::array<int,32> fixed_col,board,inverse;
std::array<U,32> allowed,orbit_mask;
std::array<std::array<U,32>,32> salt;
Big nodes=0,solutions=0;
U hash_sum=0,hash_xor=0;
bool validate=false;
bool orbit_filter=false;
std::array<Big,5> multiplicities{};

U mix(U x) {
    x+=0x9e3779b97f4a7c15ULL;
    x=(x^(x>>30))*0xbf58476d1ce4e5b9ULL;
    x=(x^(x>>27))*0x94d049bb133111ebULL;
    return x^(x>>31);
}
std::string decimal(Big x) {
    if(!x)return "0";
    std::string s;
    while(x){s=char('0'+x%10)+s;x/=10;}
    return s;
}
void solution(U hash) {
    ++solutions;
    hash_sum+=hash;
    hash_xor^=hash;
    if(orbit_filter) {
        int c=board[2],v1=n-1-inverse[2],v2=n-1-board[n-3],v3=inverse[n-3];
        assert(c<=v1&&c<=v2&&c<=v3);
        ++multiplicities[1+(c==v1)+(c==v2)+(c==v3)];
    } else ++multiplicities[4];
    if(validate) for(int r=0;r<n;r++) {
        assert(board[r]>=0 && board[r]<n);
        if(fixed_col[r]>=0)assert(board[r]==fixed_col[r]);
        for(int s=r+1;s<n;s++) {
            assert(board[r]!=board[s]);
            assert(std::abs(board[r]-board[s])!=s-r);
        }
    }
}
// Shifting diagonal attacks; precomputed masks exclude every fixed queen.
void rows(int r,U col,U left,U right,U hash) {
    ++nodes;
    if(r==n){solution(hash);return;}
    if(fixed_col[r]>=0){rows(r+1,col,left<<1,right>>1,hash);return;}
    U opts=allowed[r]&~(col|left|right);
    while(opts) {
        U b=opts&-opts;opts-=b;int c=__builtin_ctzll(b);board[r]=c;inverse[c]=r;
        rows(r+1,col|b,(left|b)<<1,(right|b)>>1,hash^salt[r][c]);
    }
}
// Absolute sum/difference diagonals; choose any unfilled row of least degree.
// Does not use the row-order algorithm's fixed-queen attack masks.
void mrv(U unfilled,U col,U sum,U diff,U hash) {
    ++nodes;
    if(!unfilled){solution(hash);return;}
    int chosen=-1,best=99;U opts=0;
    for(U todo=unfilled;todo;) {
        U b=todo&-todo;todo-=b;int r=__builtin_ctzll(b);
        U available=orbit_mask[r]&~(col|(sum>>r)|(diff>>(n-1-r)));
        int size=__builtin_popcountll(available);
        if(size==0)return;
        if(size<best){chosen=r;best=size;opts=available;if(size==1)break;}
    }
    unfilled^=U(1)<<chosen;
    while(opts) {
        U b=opts&-opts;opts-=b;int c=__builtin_ctzll(b);board[chosen]=c;inverse[c]=chosen;
        mrv(unfilled,col|b,sum|(U(1)<<(chosen+c)),diff|(U(1)<<(n-1-chosen+c)),hash^salt[chosen][c]);
    }
}
int main(int argc,char**argv) {
    if(argc<3){std::cerr<<"usage: framed_queens n rows|mrv [col_of_row2 [col_of_row3]] [--orbit-filter]\n";return 2;}
    n=std::stoi(argv[1]);std::string mode=argv[2];
    assert(n>=4&&n<=31&&(mode=="rows"||mode=="mrv"));
    full=(U(1)<<n)-1;fixed_col.fill(-1);board.fill(-1);inverse.fill(-1);
    fixed_col[0]=1;fixed_col[1]=n-1;fixed_col[n-2]=0;fixed_col[n-1]=n-2;
    int prefix_count=0;
    for(int arg=3;arg<argc;arg++) {
        if(std::string(argv[arg])=="--orbit-filter"){orbit_filter=true;continue;}
        assert(n>=8&&prefix_count<2);
        int c=std::stoi(argv[arg]);assert(c>=0&&c<n);
        fixed_col[2+prefix_count++]=c;
    }
    assert(!orbit_filter || (n>=8&&prefix_count>=1));
    orbit_mask.fill(full);
    if(orbit_filter) for(int r=0;r<n;r++) {
        int c=fixed_col[2];
        if(r==n-3)orbit_mask[r]&=(U(1)<<(n-c))-1;
        if(r>n-1-c)orbit_mask[r]&=~(U(1)<<2);
        if(r<c)orbit_mask[r]&=~(U(1)<<(n-3));
    }
    U col=0,sum=0,diff=0,unfilled=full,hash=0;bool consistent=true;
    for(int r=0;r<n;r++)for(int c=0;c<n;c++)salt[r][c]=mix(U(n)*1024+32*r+c);
    for(int r=0;r<n;r++) if(fixed_col[r]>=0) {
        int c=fixed_col[r];assert(c<n);
        U cb=U(1)<<c,sb=U(1)<<(r+c),db=U(1)<<(n-1-r+c);
        if((col&cb)||(sum&sb)||(diff&db)||!(orbit_mask[r]&cb))consistent=false;
        col|=cb;sum|=sb;diff|=db;unfilled^=U(1)<<r;board[r]=c;inverse[c]=r;hash^=salt[r][c];
    }
    for(int r=0;r<n;r++) {
        allowed[r]=0;
        for(int c=0;c<n;c++) {
            bool ok=true;
            for(int s=0;s<n;s++) if(fixed_col[s]>=0 &&
                (c==fixed_col[s] || std::abs(c-fixed_col[s])==std::abs(r-s)))ok=false;
            if(ok&&(orbit_mask[r]&(U(1)<<c)))allowed[r]|=U(1)<<c;
        }
    }
    validate=n<=22;
    auto start=std::chrono::steady_clock::now();
    if(consistent) {
        if(mode=="rows")rows(0,col,0,0,hash);
        else mrv(unfilled,col,sum,diff,hash);
    }
    double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
    Big weighted=12*multiplicities[1]+6*multiplicities[2]+4*multiplicities[3]+3*multiplicities[4];
    std::cout<<"{\"n\":"<<n<<",\"method\":\""<<mode<<"\",\"count\":"<<decimal(solutions)
      <<",\"nodes\":"<<decimal(nodes)<<",\"hash_sum_mod_2_64\":"<<hash_sum<<",\"hash_xor\":"<<hash_xor
      <<",\"orbit_filter\":"<<(orbit_filter?"true":"false")
      <<",\"minimum_multiplicities_1_to_4\":["<<decimal(multiplicities[1])<<","<<decimal(multiplicities[2])
      <<","<<decimal(multiplicities[3])<<","<<decimal(multiplicities[4])<<"]"
      <<",\"full_count_numerator\":"<<decimal(weighted)<<",\"full_count_denominator\":3"
      <<",\"all_models_pairwise_validated\":"<<(validate?"true":"false")<<",\"seconds\":"<<seconds<<"}\n";
}
