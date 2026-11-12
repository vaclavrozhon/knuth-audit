"""Our complete MIX realization of §1.3.2-21; no printed answer is supplied.

Stores the square in row-major order and prints one120-character line per row.
Supports the requested n=23 and smaller positive odd n. Each cell uses five
columns: two spaces and three zero-padded digits. OUT buffers are respected.
"""

def program(n=23):
    assert 1<=n<=23 and n%2
    return [('N','EQU',str(n)),('NSQ','EQU','N*N'),('X','EQU','500'),
        ('BUF','EQU','2000'),('','ORIG','100'),('START','ENT4','NSQ-1'),
        ('1H','STZ','X,4'),('','DEC4','1'),('','J4NN','1B'),
        ('','ENT1',str(((n//2+1)%n)*n)),('','ENT2','N/2'),('','ENT3','1'),
        ('PUT','ENT4','0,1'),('','INC4','0,2'),('','ST3','X,4'),
        ('','CMP3','=NSQ='),('','JE','PRINT'),('','INC3','1'),
        ('','ENT5','0,1'),('','ENT6','0,2'),('','INC1','N'),
        ('','CMP1','=NSQ='),('','JL','1F'),('','DEC1','NSQ'),
        ('1H','INC2','1'),('','CMP2','=N='),('','JL','2F'),('','ENT2','0'),
        ('2H','ENT4','0,1'),('','INC4','0,2'),('','LDA','X,4'),('','JAZ','PUT'),
        ('','ENT1','0,5'),('','INC1','N*2'),('','CMP1','=NSQ='),
        ('','JL','3F'),('','DEC1','NSQ'),('3H','ENT2','0,6'),('','JMP','PUT'),
        ('PRINT','ENT2','23'),('1H','STZ','BUF,2'),('','DEC2','1'),('','J2NN','1B'),
        ('','ENT4','0'),('','ENT5','N'),('ROW','JBUS','*(18)'),('','ENT2','0'),
        ('1H','LDA','X,4'),('','CHAR',''),('','STX','BUF,2(3:5)'),
        ('','INC4','1'),('','INC2','1'),('','CMP2','=N='),('','JL','1B'),
        ('','OUT','BUF(18)'),('','DEC5','1'),('','J5P','ROW'),('','HLT',''),
        ('','END','START')]


def coordinate_square(n):
    """Independent formula in block q and position s; all n positive odd."""
    assert n>0 and n%2
    square=[[None]*n for _ in range(n)]
    h=n//2
    for q in range(n):
        for s in range(n):
            r=(h+1+q+s)%n;c=(h-q+s)%n
            assert square[r][c] is None
            square[r][c]=n*q+s+1
    return square


def walking_square(n):
    square=[[0]*n for _ in range(n)];r=(n//2+1)%n;c=n//2
    for k in range(1,n*n+1):
        assert square[r][c]==0
        square[r][c]=k
        rr=(r+1)%n;cc=(c+1)%n
        if square[rr][cc]:r=(r+2)%n
        else:r,c=rr,cc
    return square
