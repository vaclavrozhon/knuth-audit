% A concrete comparison routine for exercise1.3.2'-25, not a claim
% that this is the book's unspecified "simple one-phase approach".
% The table starts at zero; counts fit signed64; p is eight-byte aligned.
% The first zero ends the input. freq[0] is deliberately ignored.
        LOC     Data_Segment
freq    GREG    @
        LOC     @+8*256
p       GREG    @
        BYTE    "abracadabraa",0,"abc"
ones    GREG    #0101010101010101
a       IS      $0
b       IS      $1
c       IS      $2
t       IS      $3
        LOC     #100
Main    PUSHJ   $0,OnePhase
        TRAP    0,Halt,0
2H      SRU     b,a,53
        LDO     c,freq,b
        INCL    c,1
        STO     c,freq,b
        SLU     a,a,8
        PBNZ    a,2B
OnePhase LDOU   a,p,0
        INCL    p,8
        BDIF    t,ones,a
        PBZ     t,2B
2H      SRU     b,a,53
        LDO     c,freq,b
        INCL    c,1
        STO     c,freq,b
        SRU     b,t,56
        SLU     a,a,8
        BDIF    t,ones,a
        PBZ     b,2B
        POP     0,0
