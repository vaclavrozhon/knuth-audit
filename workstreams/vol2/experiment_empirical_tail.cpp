// Reproducible illustrations for section3.3.2; no historical walk seeds assumed.
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

static unsigned bit(std::uint64_t& state) {
    unsigned out=state&1;
    state=(state>>1)|(((state^(state>>31))&1)<<54);
    return out;
}

int main(int argc,char** argv) {
    if (argc<2) return 2;
    std::string mode=argv[1];
    if (mode=="walks") {
        if (argc!=3) return 2;
        std::ifstream input(argv[2],std::ios::binary);
        if (!input) return 3;
        std::vector<std::uint64_t> seeds;
        unsigned char bytes[8];
        while (input.read(reinterpret_cast<char*>(bytes),8)) {
            std::uint64_t s=0;
            for(unsigned i=0;i<8;++i) s|=std::uint64_t(bytes[i])<<(8*i);
            s&=(std::uint64_t(1)<<55)-1;
            if (s==0) return 4;
            seeds.push_back(s);
        }
        if (seeds.empty()) return 5;
        std::cout<<"{\"trials_per_row\":"<<seeds.size()<<",\"rows\":[\n";
        bool first=true;
        for(unsigned length: {79u,101u,1001u,10001u,1001u}) {
            bool discard=(!first && length==1001 && !seeds.empty());
            // The last case alone uses55 output bits from every165 generated.
            static unsigned case_index=0;
            discard=(case_index++==4);
            std::uint64_t right=0,ones=0;
            for(auto state:seeds) {
                unsigned sum=0,emitted=0;
                while(emitted<length) {
                    unsigned take=discard?55:length;
                    for(unsigned j=0;j<take && emitted<length;++j,++emitted) sum+=bit(state);
                    if(discard && emitted<length) for(unsigned j=0;j<110;++j) bit(state);
                }
                right+=(sum>length/2);ones+=sum;
            }
            if(!first) std::cout<<",\n";
            first=false;
            std::cout<<"{\"length\":"<<length<<",\"discard110_after55\":"<<(discard?"true":"false")
                     <<",\"right\":"<<right<<",\"total_ones\":"<<ones<<"}"<<std::flush;
        }
        std::cout<<"\n]}\n";
    } else if(mode=="even") {
        if(argc!=3) return 2;
        std::ifstream input(argv[2],std::ios::binary);
        if(!input) return 3;
        std::vector<std::pair<std::uint64_t,std::uint64_t>> seeds;
        unsigned char bytes[16];
        while(input.read(reinterpret_cast<char*>(bytes),16)) {
            std::uint64_t a=0,b=0;
            for(unsigned j=0;j<8;++j) { a|=std::uint64_t(bytes[j])<<(8*j);b|=std::uint64_t(bytes[j+8])<<(8*j); }
            if((a&((std::uint64_t(1)<<55)-1))==0) return 4;
            seeds.emplace_back(a,b);
        }
        if(seeds.empty()) return 5;
        std::cout<<"{\"trials_per_row\":"<<seeds.size()<<",\"rows\":[\n";
        bool first=true;
        for(bool subtract: {false,true}) {
            std::uint64_t right=0;
            for(auto seed:seeds) {
                unsigned state[55];
                for(unsigned j=0;j<55;++j) state[j]=((seed.first>>j)&1)+2*((seed.second>>j)&1);
                unsigned i=0,sum=0,taken=0;
                while(taken<79) {
                    unsigned x=state[i];
                    state[i]=(x+(subtract?4-state[(i+31)%55]:state[(i+31)%55]))&3;
                    i=(i+1)%55;
                    if(!(x&1)) {sum+=x>>1;++taken;}
                }
                right+=(sum>39);
            }
            if(!first) std::cout<<",\n";
            first=false;
            std::cout<<"{\"subtract\":"<<(subtract?"true":"false")<<",\"length\":79,\"right\":"<<right<<"}";
        }
        std::cout<<"\n]}\n";
    } else if(mode=="monkey") {
        constexpr std::uint64_t a=62605,c=113218009,mask=(std::uint64_t(1)<<29)-1;
        constexpr unsigned n=1u<<21, categories=1u<<20;
        std::uint64_t x=1234567;
        std::cout<<"{\"a\":62605,\"c\":113218009,\"modulus\":536870912,\"n\":2097152,\"rows\":[\n";
        for(unsigned trial=0;trial<6;++trial) {
            auto start=x;std::vector<unsigned char> seen(categories);unsigned prev=x>>19;
            unsigned occupied=0;
            for(unsigned j=1;j<n;++j) {
                x=(a*x+c)&mask;unsigned next=x>>19;unsigned pair=(prev<<10)|next;
                occupied+=!seen[pair];seen[pair]=1;prev=next;
            }
            auto last=x;x=(a*x+c)&mask;
            if(trial) std::cout<<",\n";
            std::cout<<"{\"trial\":"<<trial+1<<",\"first\":"<<start<<",\"last\":"<<last
                     <<",\"next\":"<<x<<",\"missing\":"<<categories-occupied<<"}";
        }
        std::cout<<"\n]}\n";
    } else return 2;
}
