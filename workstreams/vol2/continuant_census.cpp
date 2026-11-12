// Complete finite-word census for TAOCP 3.3.4-31.
// Every nonempty word over 1,...,alphabet with denominator <= limit
// is visited, including the noncanonical terminal 1 representation.
// The two output arrays store a numerator witness for each denominator.
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

std::uint32_t limit;
int alphabet;
std::uint64_t nodes = 0;
std::vector<std::uint32_t> any_word, canonical;

void visit(std::uint32_t p0, std::uint32_t p1,
           std::uint32_t q0, std::uint32_t q1, int last) {
    ++nodes;
    if (p1 < q1 && q1 >= 2) {
        if (!any_word[q1]) any_word[q1] = p1;
        if (last >= 2 && !canonical[q1]) canonical[q1] = p1;
    }
    for (int d = 1; d <= alphabet; ++d) {
        std::uint64_t q2 = std::uint64_t(d) * q1 + q0;
        if (q2 > limit) break;
        visit(p1, d * p1 + p0, q1, q2, d);
    }
}

void save(const std::string &path, const std::vector<std::uint32_t> &v) {
    // Portable explicitly little-endian format.
    std::ofstream f(path, std::ios::binary | std::ios::trunc);
    for (auto x : v) {
        char b[4];
        for (int i = 0; i != 4; ++i) b[i] = char((x >> (8*i)) & 255);
        f.write(b, 4);
    }
    if (!f) { std::cerr << "write failed: " << path << '\n'; std::exit(2); }
}

int main(int argc, char **argv) {
    if (argc != 4) return 2;
    alphabet = std::stoi(argv[1]); limit = std::stoul(argv[2]);
    if (alphabet < 2 || alphabet > 5 || limit < 2 || limit > 10000000) return 2;
    std::string prefix = argv[3];
    any_word.resize(limit + 1); canonical.resize(limit + 1);
    for (int d = 1; d <= alphabet; ++d) {
        visit(0, 1, 1, d, d);
        // A complete root branch is a durable checkpoint; partial files
        // are never claimed complete without the final summary line.
        save(prefix + ".any.u32", any_word);
        save(prefix + ".canonical.u32", canonical);
        std::cout << "completed first digit " << d << " nodes " << nodes << std::endl;
    }
    std::uint32_t a = 0, c = 0;
    for (std::uint32_t m = 2; m <= limit; ++m) {
        a += bool(any_word[m]); c += bool(canonical[m]);
    }
    std::cout << "COMPLETE alphabet " << alphabet << " limit " << limit
              << " nodes " << nodes << " any " << a << " canonical " << c << std::endl;
}
