% Complete25x25 crossword: explicit border, queue flood, all input/output.
        LOC     Data_Segment
Queue   GREG    @
        LOC     Data_Segment+2500
Grid    GREG    @
        LOC     Data_Segment+3232
Input   GREG    @
        LOC     Data_Segment+3888
ReadArgs GREG   @
        OCTA    Data_Segment+3232,650
Header  GREG    @
        BYTE    98,101,103,105,110,102,105,103,40,49,56,41,59,10,116,114,97,110,115,102,111,114,109,32
        BYTE    116,59,32,116,61,105,100,101,110,116,105,116,121,32,114,111,116,97,116,101,100,32,45,57
        BYTE    48,32,115,99,97,108,101,100,32,49,55,112,116,59,10,118,97,114,100,101,102,32,99,101
        BYTE    108,108,112,97,116,104,40,101,120,112,114,32,105,44,106,41,61,10,32,32,40,40,105,44
        BYTE    106,41,45,45,40,105,43,49,44,106,41,45,45,40,105,43,49,44,106,43,49,41,45,45
        BYTE    40,105,44,106,43,49,41,45,45,99,121,99,108,101,41,32,116,114,97,110,115,102,111,114
        BYTE    109,101,100,32,116,10,101,110,100,100,101,102,59,10,100,101,102,32,99,40,101,120,112,114
        BYTE    32,105,44,106,41,61,32,100,114,97,119,32,99,101,108,108,112,97,116,104,40,105,44,106
        BYTE    41,59,32,101,110,100,100,101,102,59,10,100,101,102,32,98,40,101,120,112,114,32,105,44
        BYTE    106,41,61,32,102,105,108,108,32,99,101,108,108,112,97,116,104,40,105,44,106,41,59,32
        BYTE    100,114,97,119,32,99,101,108,108,112,97,116,104,40,105,44,106,41,59,32,101,110,100,100
        BYTE    101,102,59,10,100,101,102,32,110,40,101,120,112,114,32,105,44,106,44,107,41,61,32,108
        BYTE    97,98,101,108,46,108,114,116,40,100,101,99,105,109,97,108,32,107,32,105,110,102,111,110
        BYTE    116,32,34,99,109,114,56,34,44,40,105,44,106,41,32,116,114,97,110,115,102,111,114,109
        BYTE    101,100,32,116,41,59,32,101,110,100,100,101,102,59,10,0
CellText GREG   @
        BYTE    "c(00,00);",10,0
NumberText GREG @
        BYTE    "n(00,00,000);",10,0
Footer  GREG    @
        BYTE    101,110,100,102,105,103,59,32,101,110,100,10,0
EnqAddr GREG    0
EnqRet  GREG    0
EmitAddr GREG   0
EmitRet GREG    0
row     IS      $0
col     IS      $1
idx     IS      $2
inoff   IS      $3
head    IS      $4
tail    IS      $5
current IS      $6
cell    IS      $7
t       IS      $8
digit   IS      $9
q       IS      $10
rem     IS      $11
fmt     IS      $12
seq     IS      $13
probe   IS      $14
val     IS      $15
mark    IS      $16
        LOC     #100
Main    SET     $255,ReadArgs
        TRAP    0,Fread,StdIn
        BNZ     $255,BadInput
        GETA    EnqAddr,Enqueue
        GETA    EmitAddr,Emit
        SET     mark,255
        SET     idx,728
InitGrid STB    mark,Grid,idx
        SUB     idx,idx,1
        PBNN    idx,InitGrid
        SET     inoff,0
        SET     row,1
        SET     idx,28
        SET     head,0
        SET     tail,0
ReadRow SET     col,1
ReadCell LDBU   digit,Input,inoff
        SUB     digit,digit,'0'
        CMPU    t,digit,1
        BP      t,BadInput
        STB     digit,Grid,idx
        CMP     t,row,1
        BZ      t,Border
        CMP     t,row,25
        BZ      t,Border
        CMP     t,col,1
        BZ      t,Border
        CMP     t,col,25
        BNZ     t,NotBorder
Border  GO      EnqRet,EnqAddr,0
NotBorder INCL  inoff,1
        INCL    idx,1
        INCL    col,1
        CMP     t,col,26
        PBNZ    t,ReadCell
        LDBU    digit,Input,inoff
        CMP     t,digit,10
        BNZ     t,BadInput
        INCL    inoff,1
        INCL    idx,2
        INCL    row,1
        CMP     t,row,26
        PBNZ    t,ReadRow
Flood   CMP     t,head,tail
        BNN     t,Generate
        LDTU    current,Queue,head
        INCL    head,4
        SUB     idx,current,27
        GO      EnqRet,EnqAddr,0
        ADD     idx,current,27
        GO      EnqRet,EnqAddr,0
        SUB     idx,current,1
        GO      EnqRet,EnqAddr,0
        ADD     idx,current,1
        GO      EnqRet,EnqAddr,0
        JMP     Flood
Generate SET    $255,Header
        TRAP    0,Fputs,StdOut
        BN      $255,IoError
        SET     row,1
        SET     idx,28
        SET     seq,0
RenderRow SET   col,1
RenderCell LDB  cell,Grid,idx
        BN      cell,NextCell
        SET     digit,'c'
        CMP     t,cell,1
        CSZ     digit,t,'b'
        STB     digit,CellText,0
        SET     fmt,CellText
        GO      EmitRet,EmitAddr,0
        BNZ     cell,NextCell
        ADD     probe,idx,27
        LDB     val,Grid,probe
        BNZ     val,CheckAcross
        SUB     probe,idx,27
        LDB     val,Grid,probe
        BNZ     val,NumberIt
CheckAcross ADD probe,idx,1
        LDB     val,Grid,probe
        BNZ     val,NextCell
        SUB     probe,idx,1
        LDB     val,Grid,probe
        BZ      val,NextCell
NumberIt INCL   seq,1
        DIV     q,seq,100
        GET     rem,rR
        ADD     digit,q,'0'
        STB     digit,NumberText,8
        DIV     q,rem,10
        GET     rem,rR
        ADD     digit,q,'0'
        STB     digit,NumberText,9
        ADD     digit,rem,'0'
        STB     digit,NumberText,10
        SET     fmt,NumberText
        GO      EmitRet,EmitAddr,0
NextCell INCL   idx,1
        INCL    col,1
        CMP     t,col,26
        PBNZ    t,RenderCell
        INCL    idx,2
        INCL    row,1
        CMP     t,row,26
        PBNZ    t,RenderRow
        SET     $255,Footer
        TRAP    0,Fputs,StdOut
        BN      $255,IoError
        SET     $255,0
        TRAP    0,Halt,0
BadInput SET    $255,2
        TRAP    0,Halt,0
IoError SET     $255,1
        TRAP    0,Halt,0
% idx is an interior cell or its padded neighbor. Append each black cell once.
Enqueue LDB     cell,Grid,idx
        CMP     t,cell,1
        BNZ     t,EnqDone
        STB     mark,Grid,idx
        STTU    idx,Queue,tail
        INCL    tail,4
EnqDone GO      $255,EnqRet,0
% Write the two coordinates and emit the selected explicit terminated template.
Emit    DIV     q,row,10
        GET     rem,rR
        ADD     digit,q,'0'
        STB     digit,fmt,2
        ADD     digit,rem,'0'
        STB     digit,fmt,3
        DIV     q,col,10
        GET     rem,rR
        ADD     digit,q,'0'
        STB     digit,fmt,5
        ADD     digit,rem,'0'
        STB     digit,fmt,6
        SET     $255,fmt
        TRAP    0,Fputs,StdOut
        BN      $255,IoError
        GO      $255,EmitRet,0
