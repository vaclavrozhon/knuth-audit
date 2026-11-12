@x
  if (zs=='-' && zt!=zro) exceptions|=I_BIT, x=standard_NaN;
@y
  if (zs=='-' && (zt==num || zt==inf)) exceptions|=I_BIT, x=standard_NaN;
@z
