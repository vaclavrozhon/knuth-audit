% Complete Josephus program: elimination rank at each original position.
% Core supports1<=N<2^32,1<=M<2^64 with the allocated memory available.
% The formatter uses the number of decimal digits of N, at most10.
N       IS      24
M       IS      11
        LOC     Data_Segment
Tree    GREG    @
        LOC     @+8*(N+1)
Order   GREG    @
        LOC     @+4*N
Buf     GREG    @
        LOC     @+11*N+1
n       GREG    N
m       GREG    M
zero    IS      $0
j       IS      $1
low     IS      $2
off     IS      $3
t       IS      $4
top     IS      $5
tmp     IS      $6
left    IS      $7
rank    IS      $8
mm      IS      $9
step    IS      $10
bit     IS      $11
idx     IS      $12
cand    IS      $13
remain  IS      $14
value   IS      $15
pos     IS      $16
width   IS      $17
person  IS      $18
outoff  IS      $19
end     IS      $20
digits  IS      $21
char    IS      $22
        LOC     #100
Main    SET     zero,0
        SET     j,1
Init    NEG     low,0,j
        AND     low,j,low
        SLU     off,j,3
        STO     low,Tree,off
        INCL    j,1
        CMPU    t,j,n
        PBNP    t,Init
        SET     top,1
Grow    SLU     tmp,top,1
        CMPU    t,tmp,n
        BP      t,Grown
        SET     top,tmp
        JMP     Grow
Grown   SET     left,n
        SET     rank,0
        SUBU    mm,m,1
        SET     step,1
        PUT     rD,0
Kill    DIVU    tmp,mm,left
        GET     off,rR
        ADD     rank,rank,off
        SUB     tmp,rank,left
        CSNN    rank,tmp,tmp
        SET     idx,0
        SET     bit,top
        SET     remain,rank
Find    ADD     cand,idx,bit
        CMPU    t,cand,n
        BP      t,Skip
        SLU     off,cand,3
        LDO     value,Tree,off
        CMPU    t,value,remain
        BP      t,Skip
        SUB     remain,remain,value
        SET     idx,cand
Skip    SRU     bit,bit,1
        PBNZ    bit,Find
        ADD     pos,idx,1
        SUB     tmp,pos,1
        SLU     off,tmp,2
        STTU    step,Order,off
        SET     j,pos
Delete  SLU     off,j,3
        LDO     value,Tree,off
        SUB     value,value,1
        STO     value,Tree,off
        NEG     low,0,j
        AND     low,j,low
        ADD     j,j,low
        CMPU    t,j,n
        PBNP    t,Delete
        SUB     left,left,1
        BZ      left,Done
        CMPU    t,rank,left
        CSZ     rank,t,0
        INCL    step,1
        JMP     Kill
Done    SET     width,0
        SET     tmp,n
Width   DIV     tmp,tmp,10
        INCL    width,1
        PBNZ    tmp,Width
        SET     person,0
        SET     outoff,0
Format  SLU     tmp,person,2
        LDTU    value,Order,tmp
        SET     end,outoff
        ADD     end,end,width
        SUB     end,end,1
        SET     digits,width
Digits  DIV     value,value,10
        GET     tmp,rR
        ADD     char,tmp,'0'
        STB     char,Buf,end
        SUB     end,end,1
        SUB     digits,digits,1
        PBNZ    digits,Digits
        SET     char,' '
        INCL    person,1
        CMPU    t,person,n
        CSZ     char,t,10
        ADD     outoff,outoff,width
        STB     char,Buf,outoff
        INCL    outoff,1
        PBN     t,Format
        STB     zero,Buf,outoff
        SET     $255,Buf
        TRAP    0,Fputs,StdOut
        BN      $255,OutputFailure
        SET     $255,0
        TRAP    0,Halt,0
OutputFailure SET $255,1
        TRAP    0,Halt,0
