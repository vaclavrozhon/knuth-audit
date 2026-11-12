/* Audit harness only; not part of MMIXware. No changes to MMIXware sources. */
#include <stdint.h>
#include <stdlib.h>
#include "mmix-arith.c"

static octa bits(const char *s) {
  uint64_t u = strtoull(s, NULL, 16);
  octa o = {(tetra)(u >> 32), (tetra)u};
  return o;
}

int main(int argc, char **argv) {
  _Static_assert(sizeof(tetra) == 4, "MMIXware requires 32-bit tetra");
  if (argc != 5) return 2;
  octa y = bits(argv[1]), z = bits(argv[2]), e = bits(argv[3]);
  int similarity = atoi(argv[4]);
  int relation = fepscomp(y, z, e, similarity);
  int ordered = fcomp(y, z);
  int instruction = similarity ? (relation ? 0 : ordered) : relation;
  printf("%d %d %d\n", relation, ordered, instruction);
  return 0;
}
