% Same initial G=254 and zero values as the globally named variant.
        GREG    0
x       IS      $2
        LOC     #100
Main    SET     x,5
        SAVE    $255,0
        SET     $255,x
        TRAP    0,Halt,0
