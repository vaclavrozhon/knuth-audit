@x
if (o.h>=0x7ff00000) exceptions |= O_BIT+X_BIT; /* overflow */
@y
if (o.h>=0x7ff00000) {
  exceptions |= O_BIT+X_BIT; /* overflow */
  if (r==ROUND_OFF || (r==ROUND_UP && s=='-') ||
      (r==ROUND_DOWN && s!='-')) o.h=0x7fefffff, o.l=0xffffffff;
}
@z

@x
if (o>=0x7f800000) exceptions |= O_BIT+X_BIT; /* overflow */
@y
if (o>=0x7f800000) {
  exceptions |= O_BIT+X_BIT; /* overflow */
  if (r==ROUND_OFF || (r==ROUND_UP && s=='-') ||
      (r==ROUND_DOWN && s!='-')) o=0x7f7fffff;
}
@z
