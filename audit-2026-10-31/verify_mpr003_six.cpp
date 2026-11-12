// Exact bounded verification of MPR3's eight conventional six-spot solutions.
// Fair six-face dice, unordered triples of face multisets; no random search.
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <functional>
#include <iostream>
#include <vector>

using Die = std::array<int, 6>;
using Hist = std::array<int, 7>;
using Kernel = std::array<std::uint8_t, 7>;

void print_die(const Die &d) {
    std::cout << '[';
    for (int j = 0; j < 6; ++j) std::cout << (j ? "," : "") << d[j];
    std::cout << ']';
}

int main() {
    const auto started = std::chrono::steady_clock::now();
    std::vector<Die> dice;
    Die d{};
    std::function<void(int,int)> extend = [&](int pos, int least) {
        if (pos == 6) { dice.push_back(d); return; }
        for (int v = least; v <= 6; ++v) {
            d[pos] = v;
            extend(pos + 1, v);
        }
    };
    extend(0, 1);
    const int n = static_cast<int>(dice.size());
    assert(n == 462);
    std::vector<Hist> hist(n);
    for (int a = 0; a < n; ++a)
        for (int v : dice[a]) ++hist[a][v];

    // kernel[b,c][v] counts ordered face pairs with B+C < 2v.
    std::vector<Kernel> kernel(n*n);
    for (int b = 0; b < n; ++b)
        for (int c = 0; c < n; ++c)
            for (int x : dice[b])
                for (int y : dice[c])
                    for (int v = 1; v <= 6; ++v)
                        if (x+y < 2*v) ++kernel[b*n+c][v];
    auto score = [&](int a, int b, int c) {
        int s = 0;
        const Kernel &k = kernel[b*n+c];
        for (int v = 1; v <= 6; ++v) s += hist[a][v]*k[v];
        return s;
    };

    std::uint64_t examined = 0;
    int solutions = 0;
    std::cout << "{\"dice_profiles\":" << n << ",\"denominator\":216,"
              << "\"minimum_above_count\":128,\"solutions\":[";
    for (int a = 0; a < n; ++a)
        for (int b = a; b < n; ++b)
            for (int c = b; c < n; ++c) {
                ++examined;
                const int sa = score(a,b,c);
                if (sa < 128) continue;
                const int sb = score(b,a,c);
                if (sb < 128) continue;
                const int sc = score(c,a,b);
                if (sc < 128) continue;
                // Independent face-by-face acceptance check, only on survivors.
                std::array<int,3> direct{};
                std::array<int,4> above_multiplicity{};
                for (int x : dice[a]) for (int y : dice[b]) for (int z : dice[c]) {
                    const std::array<int,3> w{2*x>y+z,2*y>x+z,2*z>x+y};
                    for (int i = 0; i < 3; ++i) direct[i] += w[i];
                    ++above_multiplicity[w[0]+w[1]+w[2]];
                }
                assert(direct == (std::array<int,3>{sa,sb,sc}));
                if (solutions++) std::cout << ',';
                std::cout << "{\"faces\":[";
                print_die(dice[a]); std::cout << ',';
                print_die(dice[b]); std::cout << ',';
                print_die(dice[c]);
                std::cout << "],\"above_counts\":[" << sa << ',' << sb << ',' << sc
                          << "],\"rolls_by_number_above\":[";
                for (int i = 0; i < 4; ++i)
                    std::cout << (i ? "," : "") << above_multiplicity[i];
                std::cout << "]}";
            }
    const auto elapsed = std::chrono::duration<double>(
        std::chrono::steady_clock::now()-started).count();
    std::cout << "],\"unordered_triples_examined\":" << examined
              << ",\"solution_count\":" << solutions
              << ",\"elapsed_seconds\":" << elapsed << "}\n";
}
