@x
  if (oo.l!=zf.l || oo.h!=zf.h) xf.l|=1; /* sticky bit */
@^sticky bit@>
}
switch (r) {
@y
  if (oo.l!=zf.l || oo.h!=zf.h) xf.l|=1; /* sticky bit */
@^sticky bit@>
}
if (xf.l&3) exceptions|=X_BIT;
switch (r) {
@z

@x
  octa zf,o;
  zt=funpack(z,&zf,&ze,&zs);
@y
  octa zf,o;
  int ex;
  zt=funpack(z,&zf,&ze,&zs);
@z

@x
 case num:@+if (funpack(fintegerize(z,r),&zf,&ze,&zs)==zro) return zero_octa;
@y
 case num:@+o=fintegerize(z,r);
   ex=exceptions;
   zt=funpack(o,&zf,&ze,&zs);
   exceptions=ex;
   if (zt==zro) return zero_octa;
@z
