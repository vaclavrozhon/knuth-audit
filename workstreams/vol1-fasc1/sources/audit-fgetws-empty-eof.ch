% Audit-only correction for EOF before the first complete wyde.
% EOF after a nonempty unterminated prefix is deliberately not changed.
@x
    @<Read |n<128| wyde characters into |buf|@>;
    mmputchars((unsigned char*)buf,2*n+2,buffer);
@y
    @<Read |n<128| wyde characters into |buf|@>;
    if (eof && !o.h && !o.l && !n) return neg_one;
    mmputchars((unsigned char*)buf,2*n+2,buffer);
@z
