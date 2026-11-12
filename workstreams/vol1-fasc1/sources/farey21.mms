% Independent solution to MMIX 1.3.2' exercise 21.
% Caller supplies n in $0 and disjoint aligned global-register bases X,Y.
% Requires 1<=n<2^32 and enough writable storage. No simulator run claimed.
a       IS      $1
b       IS      $2
c       IS      $3
d       IS      $4
h       IS      $5
nx      IS      $6
ny      IS      $7
off     IS      $8
t       IS      $9
Farey   SET     a,0
        SET     b,1
        SET     c,1
        SET     d,$0
        SET     off,0
        STTU    a,X,off
        STTU    b,Y,off
        SET     off,4
        STTU    c,X,off
        STTU    d,Y,off
1H      CMP     t,c,d
        BZ      t,9F
        ADD     h,b,$0
        DIV     h,h,d
        MUL     nx,h,c
        SUB     nx,nx,a
        MUL     ny,h,d
        SUB     ny,ny,b
        SET     a,c
        SET     b,d
        SET     c,nx
        SET     d,ny
        INCL    off,4
        STTU    c,X,off
        STTU    d,Y,off
        JMP     1B
9H      POP     0,0
