% Complete expansion of the first printed exercise26 loop.
% Zero-initialized table, aligned finite input, signed64 counts.
        LOC     Data_Segment
freq    GREG    @
        LOC     @+8*256
p       GREG    @
        BYTE    "abracadabraa",0,"abc"
ones    GREG    #0101010101010101
a       IS      $0
b       IS      $1
bb      IS      $2
c       IS      $3
t       IS      $4
        LOC     #100
Main    PUSHJ   $0,Start
        TRAP    0,Halt,0
Start   LDOU    a,p,0
        INCL    p,8
        BDIF    t,ones,a
        BNZ     t,3F
2H      SRU     b,a,53
        LDO     c,freq,b
        SLU     bb,a,8
        INCL    c,1
        SRU     bb,bb,53
        STO     c,freq,b
        LDO     c,freq,bb
        SLU     b,a,16
        INCL    c,1
        SRU     b,b,53
        STO     c,freq,bb
        LDO     c,freq,b
        SLU     bb,a,24
        INCL    c,1
        SRU     bb,bb,53
        STO     c,freq,b
        LDO     c,freq,bb
        SLU     b,a,32
        INCL    c,1
        SRU     b,b,53
        STO     c,freq,bb
        LDO     c,freq,b
        SLU     bb,a,40
        INCL    c,1
        SRU     bb,bb,53
        STO     c,freq,b
        LDO     c,freq,bb
        SLU     b,a,48
        INCL    c,1
        SRU     b,b,53
        STO     c,freq,bb
        LDO     c,freq,b
        SLU     bb,a,56
        INCL    c,1
        SRU     bb,bb,53
        STO     c,freq,b
        LDO     c,freq,bb
        LDOU    a,p,0
        INCL    p,8
        INCL    c,1
        BDIF    t,ones,a
        STO     c,freq,bb
        PBZ     t,2B
3H      SRU     b,a,53
        LDO     c,freq,b
        INCL    c,1
        STO     c,freq,b
        SRU     b,b,3
        SLU     a,a,8
        PBNZ    b,3B
        POP     0,0
