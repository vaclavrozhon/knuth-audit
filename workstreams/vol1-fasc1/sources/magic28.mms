% Complete MMIX solution to1.3.2'-28:19x19 square and standard output.
% All matrix and output bytes are explicitly initialized before use.
N       IS      19
Half    IS      N/2
        LOC     Data_Segment
X       GREG    @
        LOC     @+4*N*N
Buf     GREG    @
        LOC     @+4*N*N+1
zero    IS      $0
row     IS      $1
col     IS      $2
val     IS      $3
limit   IS      $4
idx     IS      $5
rr      IS      $6
cc      IS      $7
cell    IS      $8
t       IS      $9
off     IS      $10
d       IS      $11
rem     IS      $12
q       IS      $13
        LOC     #100
Main    SET     zero,0
        SET     off,4*N*N-4
Clear   STTU    zero,X,off
        SUB     off,off,4
        PBNN    off,Clear
        SET     row,Half+1
        SET     col,Half
        SET     val,1
        SET     limit,N*N
Place   MUL     idx,row,N
        ADD     idx,idx,col
        SLU     idx,idx,2
        STTU    val,X,idx
        CMP     t,val,limit
        BZ      t,Generated
        INCL    val,1
        ADD     rr,row,1
        CMP     t,rr,N
        CSZ     rr,t,0
        ADD     cc,col,1
        CMP     t,cc,N
        CSZ     cc,t,0
        MUL     idx,rr,N
        ADD     idx,idx,cc
        SLU     idx,idx,2
        LDTU    cell,X,idx
        PBZ     cell,Free
        ADD     rr,row,2
        SUB     t,rr,N
        CSNN    rr,t,t
        SET     cc,col
Free    SET     row,rr
        SET     col,cc
        JMP     Place
Generated SET   off,0
        SET     col,N
        SET     limit,4*N*N
Format  LDTU    val,X,off
        DIV     q,val,100
        GET     rem,rR
        ADD     d,q,'0'
        STB     d,Buf,off
        INCL    off,1
        DIV     q,rem,10
        GET     rem,rR
        ADD     d,q,'0'
        STB     d,Buf,off
        INCL    off,1
        ADD     d,rem,'0'
        STB     d,Buf,off
        INCL    off,1
        SET     d,' '
        SUB     col,col,1
        CSZ     d,col,10
        CSZ     col,col,N
        STB     d,Buf,off
        INCL    off,1
        CMP     t,off,limit
        PBN     t,Format
        STB     zero,Buf,off
        SET     $255,Buf
        TRAP    0,Fputs,StdOut
        BN      $255,OutputFailure
        SET     $255,0
        TRAP    0,Halt,0
OutputFailure SET $255,1
        TRAP    0,Halt,0
