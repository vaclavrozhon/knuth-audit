/* Audit harness only; original MMIXware sources are unchanged. */
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include "mmix-arith.c"

static octa bits(const char *s) {
  uint64_t u = strtoull(s, NULL, 16);
  octa o = {(tetra)(u >> 32), (tetra)u};
  return o;
}

int main(int argc, char **argv) {
  _Static_assert(sizeof(tetra) == 4, "MMIXware requires 32-bit tetra");
  if (argc != 5) return 2;
  octa z = bits(argv[2]), w = bits(argv[3]), x = zero_octa;
  cur_round = atoi(argv[4]);
  if (cur_round < ROUND_OFF || cur_round > ROUND_NEAR) return 3;
  if (strcmp(argv[1], "STSF") == 0) x.l = store_sf(z);
  else if (strcmp(argv[1], "FMUL") == 0) x = fmult(z, w);
  else if (strcmp(argv[1], "FLOTU") == 0) x = floatit(z, 0, 1, 0);
  else if (strcmp(argv[1], "SFLOT") == 0) x = floatit(z, 0, 0, 1);
  else if (strcmp(argv[1], "LDSF") == 0) x = load_sf(z.l);
  else return 4;
  printf("%08x%08x %x\n", x.h, x.l, exceptions);
  return 0;
}
