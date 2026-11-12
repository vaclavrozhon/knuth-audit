/* Legal LP64 fseek/ftell state model; no large file is created. */
#include <assert.h>
#include <limits.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
static int audit_fseek(FILE *,long,int);
static long audit_ftell(FILE *);
#define fseek audit_fseek
#define ftell audit_ftell
#include "mmix-io.c"
#undef fseek
#undef ftell

octa zero_octa={0,0},neg_one={0xffffffffu,0xffffffffu};
static uint64_t unpack(octa a) { return ((uint64_t)a.h<<32)|a.l; }
static octa pack(uint64_t a) { octa r={(tetra)(a>>32),(tetra)a};return r; }
octa oplus(octa a,octa b) { return pack(unpack(a)+unpack(b)); }
octa ominus(octa a,octa b) { return pack(unpack(a)-unpack(b)); }
octa incr(octa a,int b) { return pack(unpack(a)+(uint64_t)b); }
int mmgetchars(char *b,int n,octa a,int s) {(void)b;(void)n;(void)a;(void)s;abort();}
void mmputchars(unsigned char *b,int n,octa a) {(void)b;(void)n;(void)a;abort();}
char stdin_chr(void) {abort();}
static FILE *model_stream;
static long model_length,model_position;
static int tell_error,seek_calls,tell_calls;
static int audit_fseek(FILE *f,long offset,int origin) {
  assert(f==model_stream && offset==0 && origin==SEEK_END);
  seek_calls++;model_position=model_length;return 0;
}
static long audit_ftell(FILE *f) {
  assert(f==model_stream);tell_calls++;
  return tell_error?-1:model_position;
}
int main(int argc,char **argv) {
  _Static_assert(sizeof(tetra)==4 && sizeof(int)==4,"MMIX 32-bit tetra/int host");
  _Static_assert(sizeof(long)==8,"This reproduction models LP64 specifically");
  assert(argc==4 && (int)0xffffffffu==-1);
  uint64_t length=strtoull(argv[1],NULL,10);assert(length<=(uint64_t)LONG_MAX);
  int mode=atoi(argv[2]);tell_error=atoi(argv[3]);
  model_length=(long)length;model_stream=tmpfile();assert(model_stream);
  mmix_io_init();sfile[3].fp=model_stream;sfile[3].mode=mode;
  octa seek=mmix_fseek(3,neg_one);
  octa actual=mmix_ftell(3);
  uint64_t expected=(mode&4)&&!tell_error?length:UINT64_MAX;
  assert(unpack(seek)==((mode&4)?0:UINT64_MAX));
  printf("%08x%08x %016llx %08x%08x %d %d %ld\n",actual.h,actual.l,
         (unsigned long long)expected,seek.h,seek.l,seek_calls,tell_calls,model_position);
  assert(fclose(model_stream)==0);return 0;
}
