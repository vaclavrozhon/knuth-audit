% Complete non-frame-pointer variant suggested in answer1.4.1'-15.
% Input/output n=fn is global; sp denotes the previous frame base.
% Test driver N=10; it exits with F_10=55 for observation.
N       IS      10
n       GREG    0
fn      IS      n
sp      GREG    0
        LOC     #100
        GREG    @
FibNoFp CMP     $1,n,2
        PBN     $1,Return
        INCL    sp,24
        STO     $0,sp,0
        STO     n,sp,8
        SUB     n,n,1
        GO      $0,FibNoFp
        STO     fn,sp,16
        LDO     n,sp,8
        SUB     n,n,2
        GO      $0,FibNoFp
        LDO     $0,sp,16
        ADDU    fn,fn,$0
        LDO     $0,sp,0
        SUB     sp,sp,24
Return  GO      $0,$0,0
Main    SETH    sp,#2000
        SET     n,N
        GO      $0,FibNoFp
        SET     $255,fn
        TRAP    0,Halt,0
