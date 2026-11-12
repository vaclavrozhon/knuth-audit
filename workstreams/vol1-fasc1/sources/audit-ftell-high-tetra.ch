% Audit-only correction: preserve every successful host long position.
% Two 16-bit shifts are defined even when unsigned long is only 32 bits.
@x
  o.h=0, o.l=x;
@y
  o.h=(unsigned long)x>>16>>16, o.l=x;
@z
