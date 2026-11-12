% Audit-only correction: account for actual bytes in a short fwrite block.
% The original MMIXware source remains unchanged.
@x
octa mmix_fwrite(handle,buffer,size)
  unsigned char handle;
  octa buffer,size;
{
  char buf[256];
  register int n;
  if (!(sfile[handle].mode&0x2)) return ominus(zero_octa,size);
  if (sfile[handle].mode&0x8) sfile[handle].mode &=~ 0x1;
  while (1) {
    if (size.h || size.l>=256) n=mmgetchars(buf,256,buffer,-1);
    else n=mmgetchars(buf,size.l,buffer,-1);
    size=incr(size,-n);
    if (fwrite(buf,1,n,sfile[handle].fp)!=n) return ominus(zero_octa,size);
@y
octa mmix_fwrite(handle,buffer,size)
  unsigned char handle;
  octa buffer,size;
{
  char buf[256];
  register int n,written;
  if (!(sfile[handle].mode&0x2)) return ominus(zero_octa,size);
  if (sfile[handle].mode&0x8) sfile[handle].mode &=~ 0x1;
  while (1) {
    if (size.h || size.l>=256) n=mmgetchars(buf,256,buffer,-1);
    else n=mmgetchars(buf,size.l,buffer,-1);
    written=fwrite(buf,1,n,sfile[handle].fp);
    if (written!=n) return ominus(incr(zero_octa,written),size);
    size=incr(size,-n);
@z
