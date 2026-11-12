"""Own actual MIX solution to1.4.3.1-6/7. Only units16 and18.

The printed core and the separately checked SHIFT/MOVE answers stay unchanged.
All exercises2/3/6/7/9 fit together while retaining the complete3500-word
simulated address space on a4000-word MIX.
"""
from programs import parse,SPEC,simulator

IO = parse('''
001|READY|CON|0
002||CON|0
003|DUE|CON|-1
004||CON|-1
005|COMMAND|CON|0
006||CON|0
007|DURATION|CON|10000
008||CON|10000
009||CON|7500
010|DELAY|CON|5000
011||CON|5000
012||CON|3750
013|MAXBUF|CON|3484
014||CON|3476
015|UNIT|STJ|9F
016||ENT1|0
017||DEC3|16
018||J3Z|9F
019||DEC3|2
020||J3NZ|FERROR
021||INC1|1
022|9H|JMP|*
023|BUFCHK|STJ|9F
024||J5N|MEMERROR
025||CMP5|MAXBUF,1
026||JG|MEMERROR
027|9H|JMP|*
028|IN|JMP|UNIT
029||J1NZ|FERROR
030||JMP|BUFCHK
031||JMP|ISSUE
032|OUT|JMP|UNIT
033||J1Z|FERROR
034||JMP|BUFCHK
035||JMP|ISSUE
036|IOC|JMP|UNIT
037||J1Z|FERROR
038||J5NZ|ADDRERROR
039|ISSUE|JMP|WAIT
040||LDA|INST
041||STA|COMMAND,1
042||ST5|COMMAND,1(0:2)
043||STZ|COMMAND,1(3:3)
044||LDA|DELAY+28,4
045||ADD|CLOCK
046||STA|DUE,1
047||LDA|DURATION+28,4
048||ADD|CLOCK
049||STA|READY,1
050||JMP|TICK
051||JMP|CYCLE
052|WAIT|STJ|9F
053||LDA|READY,1
054||CMPA|CLOCK
055||JLE|9F
056||STA|CLOCK
057||JMP|TICK
058|9H|JMP|*
059|JBUS|JMP|UNIT
060||LDA|READY,1
061||CMPA|CLOCK
062||JLE|CYCLE
063||ENTX|-1,6
064||CMPX|M
065||JNE|JMP
066||JMP|WAIT
067||ST6|JREG
068||JMP|CYCLE
069|JRED|JMP|UNIT
070||LDA|READY,1
071||CMPA|CLOCK
072||JG|CYCLE
073||JMP|JMP
074|TICK|STJ|9F
075||ST1|RESTORE(0:2)
076||ENT1|0
077|1H|LDA|DUE,1
078||JAN|2F
079||CMPA|CLOCK
080||JG|2F
081||LDA|COMMAND,1
082||STA|GOIO
083||ENNA|1
084||STA|DUE,1
085|GOIO|NOP|0
086||LDA|COMMAND,1(4:4)
087||STA|WAITIO(4:4)
088|WAITIO|JBUS|*(0)
089|2H|INC1|1
090||CMP1|=1=
091||JLE|1B
092|RESTORE|ENT1|0
093|9H|JMP|*
''')


def assembly(b=64,delayed=False):
    io=[(n,r if delayed or not 10<=n<=12 else (r[0],'CON','0')) for n,r in IO]
    spec=[]
    for n,r in SPEC:
        if n==13:
            spec += [(12.1,('HALTED','ENT1','0')),(12.2,('','JMP','WAIT')),
                     (12.3,('','ENT1','1')),(12.4,('','JMP','WAIT'))]
            r=('',r[1],r[2])
        spec.append((n,r))
    return simulator(b,extensions=True,extra_io=(spec,io))


if __name__=='__main__':
    for delayed in (False,True):
        a,_=assembly(64,delayed)
        print({'delayed':delayed,'first':min(a.memory),'last':max(a.memory),'words':len(a.memory)})
