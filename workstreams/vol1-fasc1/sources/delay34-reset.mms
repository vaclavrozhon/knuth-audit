% Exact printed Delay body; the harness selects an admissible equality boundary.
delta       GREG    18
ref_time    GREG    0
delay_go    GREG    0
t           IS      $255
            LOC     #100
Main        GETA    delay_go,Returned
            JMP     Delay
2H          SUBU    delta,delta,t
1H          SET     ref_time,t
            GET     t,rI
            CMPU    ref_time,ref_time,t
            PBP     ref_time,1B
Delay       GET     t,rI
            SUBU    ref_time,t,delta
            BN      t,1F
            BN      ref_time,2B
1H          GET     t,rI
            SUBU    t,t,ref_time
            PBP     t,1B
            GO      delay_go,delay_go,0
Returned    SET     t,0
            TRAP    0,Halt,0
