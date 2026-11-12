% Only x's register number changes: permutation2<->254 fixes0,1,255.
        GREG    0
x       IS      $254
        LOC     #100
Main    SET     x,5
        SAVE    $255,0
        SET     $255,x
        TRAP    0,Halt,0
