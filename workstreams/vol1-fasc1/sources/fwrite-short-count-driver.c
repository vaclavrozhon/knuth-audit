/* Audit harness: exact MMIX-IO code, deterministic legal fwrite outcomes,
   plus one actual libc write to stderr redirected by the caller to /dev/full. */
#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static size_t audit_fwrite(const void *, size_t, size_t, FILE *);
#define fwrite audit_fwrite
#include "mmix-io.c"
#undef fwrite

octa zero_octa = {0, 0}, neg_one = {0xffffffffu, 0xffffffffu};
static uint64_t unpack(octa a) { return ((uint64_t)a.h << 32) | a.l; }
static octa pack(uint64_t a) { octa r = {(tetra)(a >> 32), (tetra)a}; return r; }
octa oplus(octa a, octa b) { return pack(unpack(a) + unpack(b)); }
octa ominus(octa a, octa b) { return pack(unpack(a) - unpack(b)); }
octa incr(octa a, int b) { return pack(unpack(a) + (uint64_t)b); }

static unsigned char memory[1024];
static size_t responses[4], requested[4], returned[4];
static unsigned response_count, call_count;
static int real_write;
static uint64_t successful_bytes;

int mmgetchars(char *buf, int count, octa address, int stop) {
  uint64_t a = unpack(address);
  assert(stop == -1 && count >= 0 && count <= 256 && a + count <= sizeof memory);
  memcpy(buf, memory + a, count);
  return count;
}
void mmputchars(unsigned char *buf, int count, octa address) {
  (void)buf; (void)count; (void)address; abort();
}
char stdin_chr(void) { abort(); }

static size_t audit_fwrite(const void *ptr, size_t size, size_t count, FILE *stream) {
  assert(size == 1 && call_count < 4);
  size_t k;
  if (real_write) k = fwrite(ptr, size, count, stream);
  else k = call_count < response_count ? responses[call_count] : count;
  assert(k <= count);
  requested[call_count] = count;
  returned[call_count++] = k;
  successful_bytes += k;
  return k;
}

int main(int argc, char **argv) {
  _Static_assert(sizeof(tetra) == 4, "MMIXware requires 32-bit tetra");
  _Static_assert(sizeof(int) >= 4, "At least 32-bit int required");
  if (argc < 4 || argc > 8) return 2;
  uint64_t size = strtoull(argv[1], NULL, 10);
  assert(size <= 600);
  int mode = atoi(argv[2]);
  real_write = !strcmp(argv[3], "real");
  for (int j = 4; j < argc; ++j) responses[response_count++] = strtoul(argv[j], NULL, 10);
  for (unsigned j = 0; j < sizeof memory; ++j) memory[j] = (unsigned char)(j + 1);
  mmix_io_init();
  unsigned char handle = real_write ? 2 : 1;
  sfile[handle].mode = mode;
  octa actual = mmix_fwrite(handle, pack(16), pack(size));
  uint64_t expected = successful_bytes - size;
  printf("%08x%08x %016llx %llu %u %d", actual.h, actual.l,
         (unsigned long long)expected, (unsigned long long)successful_bytes,
         call_count, real_write ? !!ferror(stderr) : 0);
  for (unsigned j = 0; j < call_count; ++j)
    printf(" %zu:%zu", requested[j], returned[j]);
  putchar('\n');
  return 0;
}
