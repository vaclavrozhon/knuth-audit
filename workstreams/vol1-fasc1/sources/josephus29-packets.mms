% Immutable Ingalls-style MMIX packets; successors live in distinct GREG0 registers.
% The emitted program supports its chosen1<=N<=219 and unsigned1<=M<2^64.
N       IS      24
M       IS      11
        LOC     Data_Segment
Order   GREG    @
        LOC     @+4*N
Buf     GREG    @
        LOC     @+11*N+1
n       GREG    N
m       GREG    M
Next1 GREG 0
Next2 GREG 0
Next3 GREG 0
Next4 GREG 0
Next5 GREG 0
Next6 GREG 0
Next7 GREG 0
Next8 GREG 0
Next9 GREG 0
Next10 GREG 0
Next11 GREG 0
Next12 GREG 0
Next13 GREG 0
Next14 GREG 0
Next15 GREG 0
Next16 GREG 0
Next17 GREG 0
Next18 GREG 0
Next19 GREG 0
Next20 GREG 0
Next21 GREG 0
Next22 GREG 0
Next23 GREG 0
Next24 GREG 0
zero      IS      $0
left      IS      $1
step      IS      $2
count     IS      $3
prev      IS      $4
successor IS      $5
victim    IS      $6
tmp       IS      $7
off       IS      $8
width     IS      $9
person    IS      $10
outoff    IS      $11
end       IS      $12
digits    IS      $13
char      IS      $14
value     IS      $15
t         IS      $16
        LOC     #100
Main    SET     zero,0
        GETA    Next1,Entry2
        GETA    Next2,Entry3
        GETA    Next3,Entry4
        GETA    Next4,Entry5
        GETA    Next5,Entry6
        GETA    Next6,Entry7
        GETA    Next7,Entry8
        GETA    Next8,Entry9
        GETA    Next9,Entry10
        GETA    Next10,Entry11
        GETA    Next11,Entry12
        GETA    Next12,Entry13
        GETA    Next13,Entry14
        GETA    Next14,Entry15
        GETA    Next15,Entry16
        GETA    Next16,Entry17
        GETA    Next17,Entry18
        GETA    Next18,Entry19
        GETA    Next19,Entry20
        GETA    Next20,Entry21
        GETA    Next21,Entry22
        GETA    Next22,Entry23
        GETA    Next23,Entry24
        GETA    Next24,Entry1
        SET     left,n
        SET     step,1
        SET     count,m
        GETA    prev,Update24
        JMP     Entry1
Remove  SUB     tmp,victim,1
        SLU     off,tmp,2
        STTU    step,Order,off
        SUB     left,left,1
        BZ      left,Done
        INCL    step,1
        SET     count,m
        GO      $255,prev,0
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
Entry1 SUBU count,count,1
        PBNZ    count,Continue1
        SET     successor,Next1
        SET     victim,1
        JMP     Remove
Continue1 GO prev,Next1,0
Update1 SET Next1,successor
        JMP     Continue1
Entry2 SUBU count,count,1
        PBNZ    count,Continue2
        SET     successor,Next2
        SET     victim,2
        JMP     Remove
Continue2 GO prev,Next2,0
Update2 SET Next2,successor
        JMP     Continue2
Entry3 SUBU count,count,1
        PBNZ    count,Continue3
        SET     successor,Next3
        SET     victim,3
        JMP     Remove
Continue3 GO prev,Next3,0
Update3 SET Next3,successor
        JMP     Continue3
Entry4 SUBU count,count,1
        PBNZ    count,Continue4
        SET     successor,Next4
        SET     victim,4
        JMP     Remove
Continue4 GO prev,Next4,0
Update4 SET Next4,successor
        JMP     Continue4
Entry5 SUBU count,count,1
        PBNZ    count,Continue5
        SET     successor,Next5
        SET     victim,5
        JMP     Remove
Continue5 GO prev,Next5,0
Update5 SET Next5,successor
        JMP     Continue5
Entry6 SUBU count,count,1
        PBNZ    count,Continue6
        SET     successor,Next6
        SET     victim,6
        JMP     Remove
Continue6 GO prev,Next6,0
Update6 SET Next6,successor
        JMP     Continue6
Entry7 SUBU count,count,1
        PBNZ    count,Continue7
        SET     successor,Next7
        SET     victim,7
        JMP     Remove
Continue7 GO prev,Next7,0
Update7 SET Next7,successor
        JMP     Continue7
Entry8 SUBU count,count,1
        PBNZ    count,Continue8
        SET     successor,Next8
        SET     victim,8
        JMP     Remove
Continue8 GO prev,Next8,0
Update8 SET Next8,successor
        JMP     Continue8
Entry9 SUBU count,count,1
        PBNZ    count,Continue9
        SET     successor,Next9
        SET     victim,9
        JMP     Remove
Continue9 GO prev,Next9,0
Update9 SET Next9,successor
        JMP     Continue9
Entry10 SUBU count,count,1
        PBNZ    count,Continue10
        SET     successor,Next10
        SET     victim,10
        JMP     Remove
Continue10 GO prev,Next10,0
Update10 SET Next10,successor
        JMP     Continue10
Entry11 SUBU count,count,1
        PBNZ    count,Continue11
        SET     successor,Next11
        SET     victim,11
        JMP     Remove
Continue11 GO prev,Next11,0
Update11 SET Next11,successor
        JMP     Continue11
Entry12 SUBU count,count,1
        PBNZ    count,Continue12
        SET     successor,Next12
        SET     victim,12
        JMP     Remove
Continue12 GO prev,Next12,0
Update12 SET Next12,successor
        JMP     Continue12
Entry13 SUBU count,count,1
        PBNZ    count,Continue13
        SET     successor,Next13
        SET     victim,13
        JMP     Remove
Continue13 GO prev,Next13,0
Update13 SET Next13,successor
        JMP     Continue13
Entry14 SUBU count,count,1
        PBNZ    count,Continue14
        SET     successor,Next14
        SET     victim,14
        JMP     Remove
Continue14 GO prev,Next14,0
Update14 SET Next14,successor
        JMP     Continue14
Entry15 SUBU count,count,1
        PBNZ    count,Continue15
        SET     successor,Next15
        SET     victim,15
        JMP     Remove
Continue15 GO prev,Next15,0
Update15 SET Next15,successor
        JMP     Continue15
Entry16 SUBU count,count,1
        PBNZ    count,Continue16
        SET     successor,Next16
        SET     victim,16
        JMP     Remove
Continue16 GO prev,Next16,0
Update16 SET Next16,successor
        JMP     Continue16
Entry17 SUBU count,count,1
        PBNZ    count,Continue17
        SET     successor,Next17
        SET     victim,17
        JMP     Remove
Continue17 GO prev,Next17,0
Update17 SET Next17,successor
        JMP     Continue17
Entry18 SUBU count,count,1
        PBNZ    count,Continue18
        SET     successor,Next18
        SET     victim,18
        JMP     Remove
Continue18 GO prev,Next18,0
Update18 SET Next18,successor
        JMP     Continue18
Entry19 SUBU count,count,1
        PBNZ    count,Continue19
        SET     successor,Next19
        SET     victim,19
        JMP     Remove
Continue19 GO prev,Next19,0
Update19 SET Next19,successor
        JMP     Continue19
Entry20 SUBU count,count,1
        PBNZ    count,Continue20
        SET     successor,Next20
        SET     victim,20
        JMP     Remove
Continue20 GO prev,Next20,0
Update20 SET Next20,successor
        JMP     Continue20
Entry21 SUBU count,count,1
        PBNZ    count,Continue21
        SET     successor,Next21
        SET     victim,21
        JMP     Remove
Continue21 GO prev,Next21,0
Update21 SET Next21,successor
        JMP     Continue21
Entry22 SUBU count,count,1
        PBNZ    count,Continue22
        SET     successor,Next22
        SET     victim,22
        JMP     Remove
Continue22 GO prev,Next22,0
Update22 SET Next22,successor
        JMP     Continue22
Entry23 SUBU count,count,1
        PBNZ    count,Continue23
        SET     successor,Next23
        SET     victim,23
        JMP     Remove
Continue23 GO prev,Next23,0
Update23 SET Next23,successor
        JMP     Continue23
Entry24 SUBU count,count,1
        PBNZ    count,Continue24
        SET     successor,Next24
        SET     victim,24
        JMP     Remove
Continue24 GO prev,Next24,0
Update24 SET Next24,successor
        JMP     Continue24
