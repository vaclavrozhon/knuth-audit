// Independent cell-first enumeration for DLX72--74. No dancing links.
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using U = std::uint64_t;
constexpr U FULL = (U(1) << 56) - 1;
int cell[56], typ[7][7], edge[56][56], next_id;
std::array<unsigned char, 28> chosen{}, first{};
std::array<U, 97> frequency{};
U solutions, nodes;
bool geometry, details;
std::ofstream binary;

void visit(U occupied, unsigned used, int depth) {
  ++nodes;
  if (occupied == FULL) {
    if (!solutions) first = chosen;
    ++solutions;
    if (geometry) binary.write(reinterpret_cast<char*>(chosen.data()), 28);
    else if (details) for (auto e : chosen) ++frequency[e];
    return;
  }
  const int u = __builtin_ctzll(FULL ^ occupied);
  for (int v : {u + 1, u + 8}) {
    if ((v == u + 1 && u % 8 == 7) || v >= 56 || (occupied & (U(1) << v))) continue;
    unsigned bit = geometry ? 0 : 1u << typ[cell[u]][cell[v]];
    if (used & bit) continue;
    chosen[depth] = edge[u][v];
    visit(occupied | (U(1) << u) | (U(1) << v), used | bit, depth + 1);
  }
}

int main(int argc, char** argv) {
  for (int x = 0, t = 0; x < 7; ++x)
    for (int y = x; y < 7; ++y, ++t) typ[x][y] = typ[y][x] = t;
  for (int r = 0; r < 7; ++r)
    for (int c = 0; c < 7; ++c) edge[8*r+c][8*r+c+1] = next_id++;
  for (int r = 0; r < 6; ++r)
    for (int c = 0; c < 8; ++c) edge[8*r+c][8*r+c+8] = next_id++;
  geometry = argc == 3 && std::string(argv[1]) == "tilings";
  details = argc == 2 && std::string(argv[1]) == "details";
  if (geometry) {
    binary.open(argv[2], std::ios::binary);
    if (!binary) return 2;
    visit(0, 0, 0);
    binary.close();
    if (!binary) return 3;
    std::cout << "{\"count\":" << solutions << ",\"nodes\":" << nodes << "}\n";
    return 0;
  }
  std::string s;
  while (std::cin >> s) {
    if (s.size() != 56) return 4;
    for (int i = 0; i < 56; ++i) {
      if (s[i] < '0' || s[i] > '6') return 5;
      cell[i] = s[i] - '0';
    }
    solutions = nodes = 0; frequency.fill(0);
    visit(0, 0, 0);
    std::cout << "{\"count\":" << solutions << ",\"nodes\":" << nodes;
    if (details) {
      std::cout << ",\"frequency\":[";
      for (int i = 0; i < 97; ++i) std::cout << (i ? "," : "") << frequency[i];
      std::cout << "],\"first\":[";
      if (solutions) for (int i = 0; i < 28; ++i) std::cout << (i ? "," : "") << int(first[i]);
      std::cout << "]";
    }
    std::cout << "}\n";
  }
}
