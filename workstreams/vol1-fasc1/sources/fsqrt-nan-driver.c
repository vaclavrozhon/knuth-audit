/* Audit harness only; original MMIXware sources are unchanged. */
#include <stdint.h>
#include <stdlib.h>
#include "mmix-arith.c"

int main(int argc, char **argv) {
  _Static_assert(sizeof(tetra) == 4, "MMIXware requires 32-bit tetra");
  _Static_assert(sizeof(int) >= 4, "Audit execution uses at least 32-bit int");
  if (argc != 2) return 2;
  uint64_t raw = strtoull(argv[1], NULL, 16);
  octa z = {(tetra)(raw >> 32), (tetra)raw};
  cur_round = ROUND_NEAR;
  octa x = froot(z, 0);
  printf("%08x%08x %x\n", x.h, x.l, exceptions);
  return 0;
}
