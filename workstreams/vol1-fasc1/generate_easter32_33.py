#!/usr/bin/env python3
"""Emit two complete MMIX programs with the identical proved calendar core."""
from pathlib import Path

BASE = Path(__file__).resolve().parent
ALIASES = """y       IS      $0
mode    IS      $1
date    IS      $2
gold    IS      $3
cent    IS      $4
x       IS      $5
z       IS      $6
weekday IS      $7
raw     IS      $8
epact   IS      $9
t       IS      $10
q       IS      $11
rem     IS      $12
day     IS      $13
month   IS      $14
digit   IS      $15
value   IS      $16
pos     IS      $17
left    IS      $18
good    IS      $19
status  IS      $20
"""
CORE = """% Input y=1583..99999; mode0 uses floor modulo, mode1 truncates raw modulo30.
% Output date is a March ordinal; y,good and link pret are preserved.
EasterCore DIV   q,y,19
        GET     gold,rR
        INCL    gold,1
        DIV     cent,y,100
        INCL    cent,1
        MUL     x,cent,3
        SR      x,x,2
        SUB     x,x,12
        SL      z,cent,3
        ADD     z,z,5
        DIV     z,z,25
        SUB     z,z,5
        MUL     weekday,y,5
        SR      weekday,weekday,2
        SUB     weekday,weekday,x
        SUB     weekday,weekday,10
        MUL     raw,gold,11
        ADD     raw,raw,20
        ADD     raw,raw,z
        SUB     raw,raw,x
        DIV     q,raw,30
        GET     epact,rR
        PBZ     mode,CorrectModulo
        BNN     raw,CorrectModulo
        BZ      epact,CorrectModulo
        SUB     epact,epact,30
CorrectModulo CMP t,epact,24
        BZ      t,IncrementEpact
        CMP     t,epact,25
        PBNZ    t,EpactReady
        CMP     t,gold,11
        BNP     t,EpactReady
IncrementEpact INCL epact,1
EpactReady SET  date,44
        SUB     date,date,epact
        CMP     t,date,21
        PBNN    t,FullMoonReady
        INCL    date,30
FullMoonReady ADD q,weekday,date
        DIV     q,q,7
        GET     rem,rR
        INCL    date,7
        SUB     date,date,rem
        GO      $255,ret,0
"""
TABLE = """% Complete solution to1.3.2'-32: callable calendar+print routine and51rows.
        LOC     Data_Segment
Line    GREG    @
        BYTE    "00 MARCH, 00000",10,0
ARCH    GREG    #41524348
PRIL    GREG    #5052494c
LastYear GREG   2001
ret     GREG    0
pret    GREG    0
""" + ALIASES + """        LOC     #100
Main    SET     y,1950
NextYear GETA   t,EasterPrint
        GO      pret,t,0
        BNZ     status,Abort
        INCL    y,1
        CMP     t,y,LastYear
        PBN     t,NextYear
        SET     $255,0
        TRAP    0,Halt,0
Abort   SET     $255,1
        TRAP    0,Halt,0
% Input y; output status0 on successful output,1 on failure. y is preserved.
EasterPrint SET mode,0
        GETA    t,EasterCore
        GO      ret,t,0
        SET     day,date
        CMP     t,date,31
        SUB     digit,date,31
        CSP     day,t,digit
        SET     month,ARCH
        CSP     month,t,PRIL
        SET     digit,'M'
        CSP     digit,t,'A'
        STB     digit,Line,3
        STTU    month,Line,4
        DIV     q,day,10
        GET     rem,rR
        ADD     digit,q,'0'
        STB     digit,Line,0
        ADD     digit,rem,'0'
        STB     digit,Line,1
        SET     value,y
        SET     pos,14
        SET     left,5
YearDigit DIV   value,value,10
        GET     digit,rR
        ADD     digit,digit,'0'
        STB     digit,Line,pos
        SUB     pos,pos,1
        SUB     left,left,1
        PBNZ    left,YearDigit
        SET     $255,Line
        TRAP    0,Fputs,StdOut
        BN      $255,PrintFailure
        SET     status,0
        GO      $255,pret,0
PrintFailure SET status,1
        GO      $255,pret,0
""" + CORE
SEARCH = """% Complete solution to1.3.2'-33; the proved skip leaves only12candidates.
% All earlier years are excluded algebraically; the first difference terminates.
        LOC     Data_Segment
Line    GREG    @
        BYTE    "00000",10,0
ret     GREG    0
""" + ALIASES + """        LOC     #100
Main    SET     y,10108
Search  SET     mode,0
        GETA    t,EasterCore
        GO      ret,t,0
        SET     good,date
        SET     mode,1
        GETA    t,EasterCore
        GO      ret,t,0
        CMP     t,date,good
        BNZ     t,Found
        INCL    y,19
        JMP     Search
Found   SET     value,y
        SET     pos,4
        SET     left,5
YearDigit DIV   value,value,10
        GET     digit,rR
        ADD     digit,digit,'0'
        STB     digit,Line,pos
        SUB     pos,pos,1
        SUB     left,left,1
        PBNZ    left,YearDigit
        SET     $255,Line
        TRAP    0,Fputs,StdOut
        BN      $255,Abort
        SET     $255,0
        TRAP    0,Halt,0
Abort   SET     $255,1
        TRAP    0,Halt,0
""" + CORE

if __name__ == '__main__':
    (BASE/'sources/easter32-table.mms').write_text(TABLE)
    (BASE/'sources/easter33-search.mms').write_text(SEARCH)
