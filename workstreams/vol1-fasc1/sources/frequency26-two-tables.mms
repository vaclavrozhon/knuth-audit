% Complete expansion of the second printed exercise26 loop.
% The book omits its terminal body and combination; those are supplied here.
% Zero-initialized disjoint tables, aligned finite input, signed64 counts.
        LOC     Data_Segment
freq    GREG    @
        LOC     @+8*256
freqq   GREG    @
        LOC     @+8*256
p       GREG    @
        BYTE    "abracadabraa",0,"abc"
ones    GREG    #0101010101010101
a       IS      $0
b       IS      $1
bb      IS      $2
bbb     IS      $3
bbbb    IS      $4
c       IS      $5
cc      IS      $6
t       IS      $7
        LOC     #100
Main    PUSHJ   $0,Start
        TRAP    0,Halt,0
Start   LDOU    a,p,0
        INCL    p,8
        BDIF    t,ones,a
        SLU     bb,a,8
        BNZ     t,3F
2H      SRU     b,a,53
        SRU     bb,bb,53
        LDO     c,freq,b
        LDO     cc,freqq,bb
        SLU     bbb,a,16
        SLU     bbbb,a,24
        INCL    c,1
        INCL    cc,1
        SRU     bbb,bbb,53
        SRU     bbbb,bbbb,53
        STO     c,freq,b
        STO     cc,freqq,bb
        LDO     c,freq,bbb
        LDO     cc,freqq,bbbb
        SLU     b,a,32
        SLU     bb,a,40
        INCL    c,1
        INCL    cc,1
        SRU     b,b,53
        SRU     bb,bb,53
        STO     c,freq,bbb
        STO     cc,freqq,bbbb
        LDO     c,freq,b
        LDO     cc,freqq,bb
        SLU     bbb,a,48
        SLU     bbbb,a,56
        INCL    c,1
        INCL    cc,1
        SRU     bbb,bbb,53
        SRU     bbbb,bbbb,53
        STO     c,freq,b
        STO     cc,freqq,bb
        LDO     c,freq,bbb
        LDO     cc,freqq,bbbb
        LDOU    a,p,0
        INCL    p,8
        INCL    c,1
        INCL    cc,1
        BDIF    t,ones,a
        SLU     bb,a,8
        STO     c,freq,bbb
        STO     cc,freqq,bbbb
        PBZ     t,2B
% It is enough to put every terminal byte in freq, then combine the tables.
3H      SRU     b,a,53
        LDO     c,freq,b
        INCL    c,1
        STO     c,freq,b
        SRU     b,b,3
        SLU     a,a,8
        PBNZ    b,3B
        SET     b,8*255
1H      LDO     c,freq,b
        LDO     cc,freqq,b
        ADD     c,c,cc
        STO     c,freq,b
        SUB     b,b,8
        PBP     b,1B
        POP     0,0
