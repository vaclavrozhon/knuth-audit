"""Rounded harmonic sum, §1.3.2-16, original pp.518–519."""

def program():
    return [
        ('BUF','ORIG','*+24'),('START','ENT2','0'),('','ENT1','3'),('','ENTA','20'),
        ('OUTER','MUL','=10='),('','STX','CONST'),('','DIV','=2='),
        ('','ENTX','2'),('','JMP','1F'),('INNER','STA','R'),('','ADD','R'),
        ('','DECA','1'),('','STA','TEMP'),('','LDX','CONST'),('','ENTA','0'),
        ('','DIV','TEMP'),('','INCA','1'),('','STA','TEMP'),('','SUB','M'),
        ('','MUL','R'),('','SLAX','5'),('','ADD','S'),('','LDX','TEMP'),
        ('1H','STA','S'),('','STX','M'),('','LDA','M'),('','ADD','M'),
        ('','STA','TEMP'),('','LDA','CONST'),('','ADD','M'),('','SRAX','5'),
        ('','DIV','TEMP'),('','JAP','INNER'),('','LDA','S'),('','CHAR',''),
        ('','SLAX','0,1'),('','SLA','1'),('','INCA','40'),('','STA','BUF,2'),
        ('','STX','BUF+1,2'),('','INC2','3'),('','DEC1','1'),('','LDA','CONST'),
        ('','J1NN','OUTER'),('','OUT','BUF(18)'),('','HLT',''),('','END','START')]


def rounded_sum(M):
    """Exact scaled sum, grouping equal rounded reciprocals."""
    total=M;m=2;groups=0
    while True:
        r=(2*M+m)//(2*m)
        if not r:return total,groups
        high=2*M//(2*r-1)
        total+=(high-m+1)*r;m=high+1;groups+=1


def layer_sum(M):
    """Independent layer-count sum: sum_r floor(2M/(2r-1))."""
    total=0;r=1;groups=0
    while r<=M:
        q=2*M//(2*r-1)
        high=min(M,(2*M//q+1)//2)
        total+=(high-r+1)*q;r=high+1;groups+=1
    return total,groups



def hybrid_program():
    """Explicit realization of the book's optional speed suggestion.

    Thresholds are ceil(sqrt(2*10**n)) for the requested n=2,3,4,5.
    This is our program, not a transcription or a claim of optimality.
    """
    rows=program();at=rows.index(('','ENTX','2'))
    rows[at:at+2]=[
        ('','STA','S'),('','ENT3','2'),('','ENT4','4'),
        ('FLAT','ST4','TEMP'),('','LDA','CONST'),('','INCA','0,3'),
        ('','SRAX','5'),('','DIV','TEMP'),('','ADD','S'),('','STA','S'),
        ('','INC3','1'),('','INC4','2'),('','CMP3','LIMIT,1'),('','JL','FLAT'),
        ('','LDA','S'),('','ENTX','0,3'),('','JMP','1F')]
    rows[-1:-1]=[('LIMIT','CON','448'),('','CON','142'),('','CON','45'),('','CON','15')]
    return rows
