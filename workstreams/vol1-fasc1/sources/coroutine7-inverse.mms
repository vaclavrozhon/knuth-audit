% Exercise1.4.2'-7: shortest non-newline inverse code.
% Reads the standard input file one byte at a time; skips every byte<=32.
% Each emitted token has its own newline. A period ends the translation.
% Halt0=success, Halt1=input/output failure (including premature EOF).
        LOC     Data_Segment
DataBase GREG   @
RawByte BYTE    0
One     GREG    @
        BYTE    0,10,0
TwoBuf  GREG    @
        BYTE    0,0,10,0
ReadArgs GREG   @
        OCTA    RawByte,1
        LOC     #100
ReadChar SET    $255,ReadArgs
        TRAP    0,Fread,StdIn
        BNZ     $255,IOError
        LDBU    $0,DataBase,0
        CMPU    $255,$0,32
        BNP     $255,ReadChar
        POP     1,0

% Arguments: $0=count in1..10, $1=character in33..255.
% A terminal period is passed only with count1.
EmitRun CMP     $2,$0,1
        BNZ     $2,Two
        SUB     $2,$1,'0'
        CMPU    $2,$2,9
        BNP     $2,Two
        STBU    $1,One,0
        SET     $255,One
        JMP     Write
Two     ADD     $2,$0,'0'-1
        STBU    $2,TwoBuf,0
        STBU    $1,TwoBuf,1
        SET     $255,TwoBuf
Write   TRAP    0,Fputs,StdOut
        BN      $255,IOError
        POP     0,0

% Main: $0=run character, $1=count, $2=next character, $3=test.
% ReadChar returns through hole2; EmitRun uses hole4 and preserves0..3.
Main    SET     $1,0
Read    PUSHJ   $2,ReadChar
        CMP     $3,$2,'.'
        BZ      $3,Finish
        BZ      $1,NewRun
        CMP     $3,$2,$0
        BZ      $3,SameRun
        SET     $5,$1
        SET     $6,$0
        PUSHJ   $4,EmitRun
NewRun  SET     $0,$2
        SET     $1,1
        JMP     Read
SameRun INCL    $1,1
        CMP     $3,$1,10
        PBNZ    $3,Read
        SET     $5,$1
        SET     $6,$0
        PUSHJ   $4,EmitRun
        SET     $1,0
        JMP     Read
Finish  BZ      $1,Period
        SET     $5,$1
        SET     $6,$0
        PUSHJ   $4,EmitRun
Period  SET     $5,1
        SET     $6,'.'
        PUSHJ   $4,EmitRun
        SET     $255,0
        TRAP    0,Halt,0
IOError SET     $255,1
        TRAP    0,Halt,0
