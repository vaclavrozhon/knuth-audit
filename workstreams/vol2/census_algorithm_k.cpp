// Census all 10^10 inputs of one K pass, then all cycles of Algorithm K.
// --map: stdin integers -> one-pass outputs, for independent validation.
// --bench N: timing only. --full FILE: exhaustive census (about 1.25 GB RAM).
#include <algorithm>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <unistd.h>
using U = uint64_t;
using W = __uint128_t;
constexpr U M = 10000000000ULL, B = 100000;
uint32_t reduced[B];

U pass(U x) {
    switch ((x / 100000000) % 10) {
    case 0: if (x < M / 2) x += M / 2; [[fallthrough]];
    case 1: x = U((W(x) * x / B) % M); [[fallthrough]];
    case 2: x = U((W(1001001001) * x) % M); [[fallthrough]];
    case 3: x = x < 100000000 ? x + 9814055677ULL : M - x; [[fallthrough]];
    case 4: x = B * (x % B) + x / B; [[fallthrough]];
    case 5: x = U((W(1001001001) * x) % M); [[fallthrough]];
    case 6: x = B * reduced[x / B] + reduced[x % B]; [[fallthrough]];
    case 7: x = x < B ? x * x + 99999 : x - 99999; [[fallthrough]];
    case 8: assert(x != 0); while (x < M / 10) x *= 10; [[fallthrough]];
    case 9: x = U((W(x) * (x - 1) / B) % M);
    }
    assert(x < M);
    return x;
}

void print_cycles(std::ostream& out, const std::vector<std::vector<U>>& cs) {
    out << '[';
    for (size_t i = 0; i < cs.size(); ++i) {
        if (i) out << ',';
        out << "\n[";
        for (size_t j = 0; j < cs[i].size(); ++j) {
            if (j) out << ',';
            out << cs[i][j];
        }
        out << ']';
    }
    out << "\n]";
}

int main(int argc, char** argv) {
    assert(argc >= 2);
    for (U x = 0; x < B; ++x) {
        U r = 0;
        for (U p = 1; p < B; p *= 10) {
            U d = (x / p) % 10;
            r += (d ? d - 1 : 0) * p;
        }
        reduced[x] = r;
    }
    std::string mode = argv[1];
    auto started = std::chrono::steady_clock::now();
    auto elapsed = [&]() { return std::chrono::duration<double>(std::chrono::steady_clock::now() - started).count(); };
    if (mode == "--map") {
        U x;
        while (std::cin >> x) { assert(x < M); std::cout << pass(x) << '\n'; }
        return 0;
    }
    assert(argc == 3);
    if (mode == "--bench") {
        U count = std::stoull(argv[2]), checksum = 0;
        assert(count <= M);
        for (U x = 0; x < count; ++x) checksum += pass(x);
        std::cout << "{\"mode\":\"benchmark_only\",\"inputs\":" << count
                  << ",\"seconds\":" << elapsed() << ",\"checksum\":" << checksum << "}\n";
        return 0;
    }
    assert(mode == "--full");
    std::cerr << "pid=" << getpid() << " domain=" << M << " memory_bytes=" << (M + 63) / 64 * 8 << std::endl;
    std::vector<U> visited((M + 63) / 64, 0), path;
    std::vector<std::vector<U>> gcycles, fcycles;
    U counted = 0;
    auto seen = [&](U x) { return (visited[x >> 6] >> (x & 63)) & 1; };
    for (U root = 0; root < M; ++root) {
        if (root % 100000000 == 0)
            std::cerr << "root=" << root << " visited=" << counted << " gcycles=" << gcycles.size()
                      << " seconds=" << elapsed() << std::endl;
        if (seen(root)) continue;
        path.clear();
        U x = root;
        while (!seen(x)) {
            visited[x >> 6] |= U(1) << (x & 63);
            ++counted;
            path.push_back(x);
            x = pass(x);
        }
        auto it = std::find(path.begin(), path.end(), x);
        if (it != path.end()) {
            gcycles.emplace_back(it, path.end());
            std::cerr << "gcycle length=" << gcycles.back().size() << " at root=" << root << std::endl;
        }
    }
    assert(counted == M);
    // f(x) = g^(1+floor(x/10^9))(x). Every f-cycle lies on a g-cycle.
    for (const auto& cycle : gcycles) {
        const size_t n = cycle.size();
        std::vector<bool> done(n, false);
        for (size_t start = 0; start < n; ++start) {
            if (done[start]) continue;
            std::vector<size_t> p;
            size_t i = start;
            while (!done[i]) {
                done[i] = true;
                p.push_back(i);
                i = (i + 1 + cycle[i] / 1000000000) % n;
            }
            auto it = std::find(p.begin(), p.end(), i);
            if (it != p.end()) {
                std::vector<U> fc;
                for (; it != p.end(); ++it) fc.push_back(cycle[*it]);
                fcycles.push_back(std::move(fc));
            }
        }
    }
    std::ofstream out(argv[2]);
    assert(out.good());
    out << "{\n\"status\":\"exhaustive census completed\",\n\"domain_size\":" << M
        << ",\n\"visited\":" << counted << ",\n\"elapsed_seconds\":" << elapsed()
        << ",\n\"g_cycles\":";
    print_cycles(out, gcycles);
    out << ",\n\"algorithm_k_cycles\":";
    print_cycles(out, fcycles);
    out << "\n}\n";
    out.close();
    assert(out.good());
    std::cerr << "completed visited=" << counted << " fcycles=" << fcycles.size() << " seconds=" << elapsed() << std::endl;
}
