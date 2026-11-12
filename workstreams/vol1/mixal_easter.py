"""The Easter subroutine and driver, §1.3.2-14, pp.516–518."""

def program():
    return [
        ('','ORIG','200'),('EASTER','STJ','EASTX'),('','STX','Y'),
        ('','ENTA','0'),('','DIV','=19='),('','STX','GMINUS1(0:2)'),
        ('','LDA','Y'),('','MUL','=1//100+1='),('','INCA','61'),
        ('','STA','CPLUS60(1:2)'),('','MUL','=3//4+1='),
        ('','STA','XPLUS57(1:2)'),('CPLUS60','ENTA','*'),
        ('','MUL','=8//25+1='),('GMINUS1','ENT2','*'),('','ENT1','1,2'),
        ('','INC2','1,1'),('','INC2','0,2'),('','INC2','0,1'),
        ('','INC2','0,2'),('','INC2','773,1'),('XPLUS57','INCA','-*,2'),
        ('','SRAX','5'),('','DIV','=30='),('','DECX','24'),('','JXN','4F'),
        ('','DECX','1'),('','JXP','2F'),('','JXN','3F'),('','DEC1','11'),
        ('','J1NP','2F'),('3H','INCX','1'),('2H','DECX','29'),
        ('4H','STX','20MINUSN(0:2)'),('','LDA','Y'),('','MUL','=1//4+1='),
        ('','ADD','Y'),('','SUB','XPLUS57(1:2)'),('20MINUSN','ENN1','*'),
        ('','INCA','67,1'),('','SRAX','5'),('','DIV','=7='),('','SLAX','5'),
        ('','DECA','-4,1'),('','JAN','1F'),('','DECA','31'),('','CHAR',''),
        ('','LDA','MARCH'),('','JMP','2F'),('1H','CHAR',''),('','LDA','APRIL'),
        ('2H','JBUS','*(18)'),('','STA','MONTH'),('','STX','DAY(1:2)'),
        ('','LDA','Y'),('','CHAR',''),('','STX','YEAR'),('','OUT','ANS(18)'),
        ('EASTX','JMP','*'),('MARCH','ALF','MARCH'),('APRIL','ALF','APRIL'),
        ('ANS','ALF','     '),('DAY','ALF','DD   '),('MONTH','ALF','MMMMM'),
        ('','ALF',',    '),('YEAR','ALF','YYYYY'),('','ORIG','*+20'),
        ('BEGIN','ENTX','1950'),('','ENT6','1950-2000'),('','JMP','EASTER'),
        ('','INC6','1'),('','ENTX','2000,6'),('','J6NP','EASTER+1'),
        ('','HLT',''),('','END','BEGIN')]


def algorithm(y,negative_remainder=False):
    g=y%19+1;c=y//100+1;x=3*c//4-12;z=(8*c+5)//25-5
    d=5*y//4-x-10;raw=11*g+20+z-x
    e=-(abs(raw)%30) if negative_remainder and raw<0 else raw%30
    if e==24 or e==25 and g>11:e+=1
    n=44-e
    if n<21:n+=30
    n+=7-(d+n)%7
    return n


def fixed_march0(y):
    """Absolute Gregorian day of the day before March 1, RD1=Monday."""
    return 365*y-306+y//4-y//100+y//400


def reingold(y):
    """Dershowitz–Reingold 1990 p.920 shifted-epact/absolute-day algorithm."""
    c=y//100+1
    shifted=(14+11*(y%19)-(3*c)//4+(5+8*c)//25+30*c)%30
    adj=shifted+int(shifted==0 or shifted==1 and y%19>10)
    march0=fixed_march0(y);moon=march0+50-adj
    sunday=moon+7-(moon+7)%7
    return sunday-march0


def search_program():
    """Complete MIX solution of exercise 15, printing the first incorrect year.

    Same arithmetic routine in both calls; EPBASE selects the safe +720 offset
    or the faulty signed remainder. Return value is 31 minus the March-day.
    The independent scalar checker does not share this implementation.
    """
    rows=program()
    end=rows.index(('','JAN','1F'))
    core=rows[:end]
    core[1]=('EASTER','STJ','CALCRET')
    core[core.index(('','INC2','773,1'))]=('EPBASE','INC2','773,1')
    return core+[
        ('CALCRET','JMP','*'),('','ORIG','100'),
        ('BEGIN','LDA','=773='),('','STA','EPBASE(0:2)'),
        ('','LDX','YEARCOUNT'),('','JMP','EASTER'),('','STA','GOOD'),
        ('','LDA','=53='),('','STA','EPBASE(0:2)'),
        ('','LDX','YEARCOUNT'),('','JMP','EASTER'),('','CMPA','GOOD'),
        ('','JNE','FOUND'),('','LDA','YEARCOUNT'),('','ADD','=1='),
        ('','STA','YEARCOUNT'),('','JMP','BEGIN'),
        ('FOUND','LDA','YEARCOUNT'),('','CHAR',''),('','STX','ANS'),
        ('','OUT','ANS(18)'),('','HLT',''),('YEARCOUNT','CON','1583'),
        ('GOOD','CON','0'),('','ORIG','1600'),('ANS','CON','0'),
        ('','ORIG','*+23'),('','END','BEGIN')]
