/* Audit-only direct client of the unchanged arithmetic module. */
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include "mmix-arith.c"

int main(int argc, char **argv) {
  _Static_assert(sizeof(tetra) == 4, "MMIXware requires a32-bit tetra");
  if (argc != 2) return 2;
  cur_round = ROUND_NEAR;
  exceptions = 0;
  int kind = scan_const(argv[1]);
  printf("%d %08x%08x %td\n", kind, val.h, val.l, next_char - argv[1]);
  return 0;
}
