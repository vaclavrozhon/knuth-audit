// Exhaustive inverse of one K2--K12 pass, using exact integer interval bounds.
// A floating sqrt is only an initial guess: isqrt corrects it with uint128.
// Compile with g++ -O3 -std=c++17; arguments: target output.json.
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>

using U = uint64_t;
using W = __uint128_t;
constexpr U M = 10000000000ULL, B = 100000;
U square_intervals = 0, product_intervals = 0;

U isqrt(W x) {
    U r = U(sqrtl((long double)x));
    while (W(r) * r > x) --r;
    while (W(r + 1) * (r + 1) <= x) ++r;
    assert(W(r) * r <= x && W(r + 1) * (r + 1) > x);
    return r;
}

std::vector<U> inverse_quadratic(U y, bool falling) {
    std::vector<U> out;
    W max_product = W(M - 1) * (falling ? M - 2 : M - 1);
    for (W lo = W(y) * B; lo <= max_product; lo += W(M) * B) {
        if (falling) ++product_intervals; else ++square_intervals;
        W hi = std::min(lo + B - 1, max_product);
        U x;
        if (falling) {
            if (lo == 0) out.push_back(0);
            x = (1 + isqrt(1 + 4 * lo)) / 2;
            if (W(x) * (x - 1) < lo) ++x;
        } else {
            x = isqrt(lo);
            if (W(x) * x < lo) ++x;
        }
        while (x < M && W(x) * (falling ? x - 1 : x) <= hi) {
            out.push_back(x);
            ++x;
        }
    }
    return out;
}

std::vector<U> inverse_step(int step, U y) {
    std::vector<U> out;
    switch (step) {
    case 3:
        if (y >= M / 2) { out.push_back(y); out.push_back(y - M / 2); }
        break;
    case 4:
        return inverse_quadratic(y, false);
    case 5: case 8:
        out.push_back(U((W(y) * 9999999001ULL) % M));
        break;
    case 6:
        if (y > 0 && M - y >= 100000000) out.push_back(M - y);
        if (y >= 9814055677ULL && y < 9914055677ULL) out.push_back(y - 9814055677ULL);
        break;
    case 7:
        out.push_back((y % B) * B + y / B);
        break;
    case 9: {
        out.push_back(0);
        for (U place = 1; place < M; place *= 10) {
            U digit = (y / place) % 10;
            if (digit == 9) return {};
            if (digit == 0) {
                size_t old = out.size();
                for (size_t i = 0; i < old; ++i) out.push_back(out[i] + place);
            } else {
                for (U& x : out) x += (digit + 1) * place;
            }
        }
        break;
    }
    case 10:
        if (y + 99999 >= B && y + 99999 < M) out.push_back(y + 99999);
        if (y >= 99999) {
            U x = isqrt(y - 99999);
            if (x < B && x * x == y - 99999) out.push_back(x);
        }
        break;
    case 11:
        if (y >= M / 10) {
            out.push_back(y);
            while (y % 10 == 0) { y /= 10; out.push_back(y); }
        }
        break;
    case 12:
        return inverse_quadratic(y, true);
    }
    return out;
}

U forward(U x) {
    int start = 3 + (x / 100000000) % 10;
    for (int step = start; step <= 12; ++step) {
        switch (step) {
        case 3: if (x < M / 2) x += M / 2; break;
        case 4: x = U((W(x) * x / B) % M); break;
        case 5: case 8: x = U((W(1001001001) * x) % M); break;
        case 6: x = x < 100000000 ? x + 9814055677ULL : M - x; break;
        case 7: x = (x % B) * B + x / B; break;
        case 9: {
            U y = 0;
            for (U p = 1; p < M; p *= 10) {
                U digit = (x / p) % 10;
                y += (digit > 0 ? digit - 1 : 0) * p;
            }
            x = y; break;
        }
        case 10: x = x < B ? x * x + 99999 : x - 99999; break;
        case 11: assert(x > 0); while (x < M / 10) x *= 10; break;
        case 12: x = U((W(x) * (x - 1) / B) % M); break;
        }
        assert(x < M);
    }
    return x;
}

std::set<U> predecessors(U y) {
    std::set<U> current{y}, result;
    for (int step = 12; step >= 3; --step) {
        std::set<U> previous;
        for (U x : current) {
            for (U p : inverse_step(step, x)) {
                assert(p < M);
                previous.insert(p);
                if (int(3 + (p / 100000000) % 10) == step) {
                    assert(forward(p) == y);
                    result.insert(p);
                }
            }
        }
        current = std::move(previous);
    }
    return result;
}

int main(int argc, char** argv) {
    assert(argc == 3);
    U target = std::stoull(argv[1]);
    assert(target < M);
    assert(U((W(1001001001) * 9999999001ULL) % M) == 1);
    std::set<U> seen{target};
    std::queue<U> queue;
    queue.push(target);
    std::map<U, std::set<U>> inverse;
    while (!queue.empty()) {
        U y = queue.front(); queue.pop();
        inverse[y] = predecessors(y);
        for (U x : inverse[y]) {
            if (seen.insert(x).second) queue.push(x);
        }
        if (inverse.size() % 100 == 0) std::cerr << "expanded=" << inverse.size() << " found=" << seen.size() << '\n';
    }
    std::ofstream out(argv[2]);
    assert(out.good());
    out << "{\n\"target\":" << target << ",\n\"count\":" << seen.size()
        << ",\n\"minimum\":" << *seen.begin() << ",\n\"maximum\":" << *seen.rbegin()
        << ",\n\"square_intervals\":" << square_intervals
        << ",\n\"product_intervals\":" << product_intervals << ",\n\"inverse_edges\":[\n";
    bool first = true;
    for (const auto& [y, pre] : inverse) {
        for (U x : pre) {
            if (!first) out << ",\n";
            first = false;
            out << '[' << x << ',' << y << ']';
        }
    }
    out << "\n]}\n";
    std::cerr << "completed target=" << target << " count=" << seen.size() << '\n';
}
