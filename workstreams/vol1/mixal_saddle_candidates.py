"""A tie-capable third variant: keep a minimum-maximum column as a selector.

All rows equal to its maximum are candidates. Testing each such row lazily
also rejects rows excluded by other minimum-maximum columns. This keeps a
superset of the intersection suggested in the book, never just one tied row.
"""
from fractions import Fraction as F
from mixal_saddle import solution2
from saddle_expectations import harmonic,distinct_intervals,probability_distinct


def program(m=9,n=8):
    rows=[]
    for label,op,addr in solution2(m,n):
        if label=='PHASE2':break
        if op=='JLE' and addr=='*+2':addr='*+3'
        rows.append((label,op,addr))
        if label=='1H' and op=='LDA':rows.append(('','ENT5','0,1'))
    return rows+[
        ('PHASE2','ENT3',str(m*n)),('','ENT2',str(m*n-n)+',5'),
        ('PICK','CMPA','A10,2'),('','JE','CHECK'),
        ('NEXT','DEC2',str(n)),('','DEC3',str(n)),('','J3P','PICK'),
        ('','ENT1','0'),('','HLT',''),
        ('CHECK','ENT1','A10,2'),('','ENT4','0,3'),('','ENT6',str(n)),
        ('ROW','CMPA','A10,4'),('','JG','NEXT'),('','DEC4','1'),
        ('','DEC6','1'),('','J6P','ROW'),('','HLT',''),('','END','PHASE1')]


def binary_mean(m,n):
    p=F(1,2**m);q=1-p;r=F(1,2**n);p0=1-q**n
    phase1=5*m*n+10*n-2*n*p+2*q*(1-q**(n-1))
    extra1=1+q*(1-q**(n-1))
    phase2=(6*n+8)*p0+2*q**n+(1-r)**m-p0
    for i in range(m):
        reached=(1-r)**i-p0
        prefixes=[F(1,2**k)*((1-r)**i+q**(n-k)-1) for k in range(1,n+1)]
        success=r*(1-r)**i
        phase2+=6*reached+6*prefixes[0]+6*sum(prefixes)-6*success
    return phase1+extra1+phase2+1


def distinct_mean(m,n):
    e=distinct_intervals(m,n)
    return (5*m*n+7*n+2*n*harmonic(m)+3*harmonic(n)+6*m
            +6*e['selected_row_scans']+2-(3*m-2)*probability_distinct(m,n))
