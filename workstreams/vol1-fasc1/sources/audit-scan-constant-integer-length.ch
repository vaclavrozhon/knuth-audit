Audit-only correction of the decimal position lost when integer digits
exceed the significant-digit buffer. The proof covers finite input strings
shorter than 10^9 bytes and literal exponent magnitude at most 999999999;
all integer arithmetic introduced below then fits a signed 32-bit int.
This does not claim to repair unrelated exponent saturation or all scan_const
rounding/exception behavior. Original source files remain unchanged.

@x
  for (q=buf0,dec_pt=(char*)0;isdigit(*p);p++) {
    val=oplus(val,shift_left(val,2)); /* multiply by 5 */
    val=incr(shift_left(val,1),*p-'0');
    if (q>buf0 || *p!='0')
       if (q<buf_max) *q++=*p;
       else if (*(q-1)=='0') *(q-1)=*p;
  }
@y
  discarded_integer_digits=0;
  for (q=buf0,dec_pt=(char*)0;isdigit(*p);p++) {
    val=oplus(val,shift_left(val,2)); /* multiply by 5 */
    val=incr(shift_left(val,1),*p-'0');
    if (q>buf0 || *p!='0') {
       if (q<buf_max) *q++=*p;
       else {
         discarded_integer_digits++;
         if (*(q-1)=='0') *(q-1)=*p;
       }
    }
  }
@z

@x
register int zeros; /* leading zeros removed after decimal point */
@y
register int zeros; /* leading zeros removed after decimal point */
int discarded_integer_digits; /* omitted places before the decimal point */
@z

@x
  @<Move the digits from |buf| to |ff|@>;
  @<Determine the binary fraction and binary exponent@>;
@y
  exp+=discarded_integer_digits;
  @<Move the digits from |buf| to |ff|@>;
  @<Determine the binary fraction and binary exponent@>;
@z
