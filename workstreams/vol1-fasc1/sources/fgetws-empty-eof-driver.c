/* Tiny real binary input streams; no host wchar_t conversion is assumed. */
#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "mmix-io.c"

octa zero_octa = {0,0}, neg_one = {0xffffffffu,0xffffffffu};
static uint64_t unpack(octa a) { return ((uint64_t)a.h << 32) | a.l; }
static octa pack(uint64_t a) { octa r = {(tetra)(a >> 32),(tetra)a}; return r; }
octa oplus(octa a,octa b) { return pack(unpack(a)+unpack(b)); }
octa ominus(octa a,octa b) { return pack(unpack(a)-unpack(b)); }
octa incr(octa a,int b) { return pack(unpack(a)+(uint64_t)b); }
static unsigned char memory[64];
static unsigned puts_calls, stored;
int mmgetchars(char *b,int n,octa a,int s) {
  (void)b;(void)n;(void)a;(void)s;abort();
}
void mmputchars(unsigned char *b,int n,octa a) {
  assert(n>=0 && unpack(a)+n<=sizeof memory);
  memcpy(memory+unpack(a),b,n);puts_calls++;stored+=n;
}
char stdin_chr(void) { abort(); }
int main(int argc,char **argv) {
  _Static_assert(sizeof(tetra)==4,"32-bit tetra required");
  assert(argc==4);
  uint64_t size=strtoull(argv[1],NULL,10);
  int mode=atoi(argv[2]);
  const char *hex=argv[3];assert(strlen(hex)%2==0 && strlen(hex)<=32);
  FILE *f=tmpfile();assert(f);
  for (size_t i=0;i<strlen(hex);i+=2) {
    unsigned byte;assert(sscanf(hex+i,"%2x",&byte)==1);
    assert(fputc(byte,f)!=EOF);
  }
  assert(fflush(f)==0 && fseek(f,0,SEEK_SET)==0);
  memset(memory,0xaa,sizeof memory);mmix_io_init();
  sfile[3].fp=f;sfile[3].mode=mode;
  octa r=mmix_fgetws(3,pack(16),pack(size));
  printf("%08x%08x %d %d %ld %u %u ",r.h,r.l,!!feof(f),!!ferror(f),
         ftell(f),puts_calls,stored);
  for (unsigned i=16;i<24;i++)printf("%02x",memory[i]);
  putchar('\n');assert(fclose(f)==0);return 0;
}
