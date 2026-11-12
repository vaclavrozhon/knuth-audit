% Independent concrete third variant for MMIX exercise1.3.2'-20.
% Caller provides signed bytes at Data_Segment+8*i+j (i=1..9,j=1..8)
% and a valid return frame. This subroutine returns the address or0 in$0.
% It preserves the matrix; no stored column-maxima table is needed.
t       IS      $255
ans     IS      $0
a10     GREG    Data_Segment+8
a20     GREG    Data_Segment+16
ij      GREG    0
ii      GREG    0
j       GREG    0
x       GREG    0
y       GREG    0
z       GREG    0
best    GREG    0
        LOC     #100
Saddle3 SET     j,8
        SET     z,1000
MinCol  ADD     ij,j,56
        LDB     x,a20,ij
MaxLoop LDB     y,a10,ij
        CMP     t,x,y
        CSN     x,t,y
        SUB     ij,ij,8
        PBP     ij,MaxLoop
        CMP     t,x,z
        CSN     z,t,x
        CSN     best,t,j
        SUB     j,j,1
        PBP     j,MinCol
        SET     ii,64
RowTry  ADD     ans,ii,best
        LDB     x,a10,ans
        CMP     t,x,z
        PBNZ    t,NextRow
        ADD     ij,ii,8
        SET     j,8
TestRow LDB     x,a10,ij
        CMP     t,x,z
        PBN     t,NextRow
        SUB     j,j,1
        SUB     ij,ij,1
        PBP     j,TestRow
        LDA     ans,a10,ans
        POP     1,0
NextRow SUB     ii,ii,8
        PBNN    ii,RowTry
        SET     ans,0
        POP     1,0
