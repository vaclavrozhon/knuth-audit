"""Actual MIX transcription of answer 2.3.5-4, original pages 601--602."""
from functools import lru_cache
from mix_machine import Machine, Word, number
from mixal import Assembly

@lru_cache(None)
def program(radix):
    rows = [
        ('MARK','EQU','0:0'),('ATOM','EQU','1:1'),
        ('ALINK','EQU','2:3'),('BLINK','EQU','4:5'),
        ('P0','EQU','700'),('','ORIG','100'),
        ('E1','LD1','P0'),('','ENT2','0'),('','ENTX','-1'),
        ('E2','STX','0,1(MARK)'),('E3','LDA','0,1(ATOM)'),
        ('','JAZ','E4'),
        ('E6','J2Z','DONE'),('','ENT3','0,2'),('','LDA','0,3(ATOM)'),
        ('','JANZ','1F'),('','LD2','0,3(BLINK)'),('','ST1','0,3(BLINK)'),
        ('','ENT1','0,3'),('','JMP','E6'),
        ('1H','STZ','0,2(ATOM)'),('','LD2','0,3(ALINK)'),
        ('','ST1','0,3(ALINK)'),('','ENT1','0,3'),
        ('E5','LD3','0,1(BLINK)'),('','J3Z','E6'),('','LDA','0,3'),
        ('','STX','0,3(MARK)'),('','JANP','E6'),
        ('','LDA','0,3(ATOM)'),('','JANZ','E6'),
        ('','ST2','0,1(BLINK)'),('E4A','ENT2','0,1'),('','ENT1','0,3'),
        ('E4','LD3','0,1(ALINK)'),('','J3Z','E5'),('','LDA','0,3'),
        ('','STX','0,3(MARK)'),('','JANP','E5'),('','LDA','0,3(ATOM)'),
        ('','JANZ','E5'),('SETATOM','STX','0,1(ATOM)'),
        ('','ST2','0,1(ALINK)'),('','JMP','E4A'),
        ('DONE','HLT','0'),('','END','100')]
    return Assembly(rows, radix)


def execute(mem, root, radix=64, offset=1000):
    asm = program(radix)
    m = Machine(radix)
    asm.load(m)
    addr = lambda p: offset+p if p else 0
    original = {}
    for p,v in mem.items():
        a,b = (v.a,v.b) if v.atom else (addr(v.a),addr(v.b))
        original[p] = Word(-1 if v.mark else 1,
                           (v.atom,a//radix,a%radix,b//radix,b%radix))
        m.mem[addr(p)] = original[p]
    m.mem[700] = number(addr(root),radix)
    m.pc = 100
    e4 = asm.symbols['E4'].value(radix)
    setatom = asm.symbols['SETATOM'].value(radix)
    done = asm.symbols['DONE'].value(radix)
    active, t1 = [],0
    for _ in range(100000):
        if m.pc == done:
            break
        if m.pc == e4:
            active.append(m.reg[1].value(radix)-offset)
        if m.pc == setatom:
            t1 += 1
        m.step()
    else:
        raise RuntimeError('MIX instruction limit; no conclusion about nontermination')
    marked = {p for p in mem if m.mem[addr(p)].sign < 0}
    assert all(m.mem[addr(p)].digits == w.digits for p,w in original.items())
    assert m.reg[1].value(radix) == addr(root)
    assert m.reg[2].value(radix) == 0
    n = len(active)
    atoms = sum(mem[p].atom and not mem[p].mark for p in marked)
    nulls = sum((mem[p].a==0)+(mem[p].b==0) for p in active)
    predicted = 10 if mem[root].atom else 34*n+4*t1+3*atoms-5*nulls-8
    assert m.time == predicted, (m.time,predicted,n,t1,atoms,nulls,mem)
    # n excludes nonroot all-zero words, as explicitly qualified on p. 601.
    return dict(marked=marked,time=m.time,n_active=n,t1=t1,atoms=atoms,nulls=nulls)
