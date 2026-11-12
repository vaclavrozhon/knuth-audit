/* Audit harness only: the original MMIXware source remains unchanged. */
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include "mmix-arith.c"

int main(int argc, char **argv) {
  _Static_assert(sizeof(tetra) == 4, "MMIXware requires 32-bit tetra");
  _Static_assert(sizeof(int) >= 4, "Audit execution requires at least 32-bit int");
  if (argc != 4) return 2;
  uint64_t raw = strtoull(argv[2], NULL, 16);
  octa z = {(tetra)(raw >> 32), (tetra)raw}, x;
  int mode = atoi(argv[3]);
  if (mode < 0 || mode > 4) return 2;
  cur_round = ROUND_NEAR;
  if (!strcmp(argv[1], "FINT")) x = fintegerize(z, mode);
  else if (!strcmp(argv[1], "FIX")) x = fixit(z, mode);
  else if (!strcmp(argv[1], "FIXU")) {
    x = fixit(z, mode);
    exceptions &= ~W_BIT; /* exact FIXU dispatcher operation */
  } else return 2;
  printf("%08x%08x %x\n", x.h, x.l, exceptions);
  return 0;
}
