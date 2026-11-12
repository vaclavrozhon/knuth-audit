"""Actual word-level G and MIX answer 2.5-34; no shared model changes."""
from pathlib import Path
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from mix_machine import Word, number, field, Machine
from mixal import Assembly, put

LINK, SIZE, T = 4*8+5, 1*8+2, 3*8+3


def get(mem, p, f, b):
    return field(mem[p], f).value(b)


def setf(mem, p, f, v, b):
    mem[p] = put(mem[p], number(v, b), f)


def make_pool(spec, use_index=0, b=64):
    """spec=(size, target indices or None); one payload word per target."""
    mem = [number(0, b)] * 4000
    heads, at = [], 1
    for size, targets in spec:
        assert 0 <= len(targets) < size < b
        heads.append(at)
        at += size
    for i, ((size, targets), p) in enumerate(zip(spec, heads)):
        setf(mem, p, SIZE, size, b)
        setf(mem, p, T, len(targets), b)
        for k in range(1, size):
            # Distinguish the complete payload, including its sign and high bytes.
            mem[p+k] = Word(-1 if (i+k) % 2 else 1,
                            ((7*i+k) % b, (i+3*k) % b, (11+i+k) % b, 0, 0))
        for k, target in enumerate(targets, 1):
            setf(mem, p+k, LINK, 0 if target is None else heads[target], b)
    setf(mem, 0, LINK, 1, b)
    return mem, heads, at, heads[use_index]


def independent(mem, heads, avail, use, b):
    """Reachability and out-of-place stable copy, independent of book phases."""
    live, todo = set(), [use]
    while todo:
        p = todo.pop()
        if p in live:
            continue
        live.add(p)
        for k in range(1, get(mem, p, T, b)+1):
            q = get(mem, p+k, LINK, b)
            if q:
                assert q in heads
                todo.append(q)
    forward, at = {}, 1
    for p in heads:
        if p in live:
            forward[p] = at
            at += get(mem, p, SIZE, b)
    result = list(mem)
    for p in heads:
        if p not in live:
            continue
        q = forward[p]
        size = get(mem, p, SIZE, b)
        result[q:q+size] = mem[p:p+size]
        setf(result, q, LINK, 0, b)
        for k in range(1, get(mem, p, T, b)+1):
            target = get(mem, p+k, LINK, b)
            setf(result, q+k, LINK, forward[target] if target else 0, b)
    flags = [p in live for p in heads]
    a = len(live)
    links = sum(get(mem, p, T, b) for p in live)
    c = sum(not flag and (i == 0 or flags[i-1]) for i, flag in enumerate(flags))
    d = len(heads)-a-c
    stats = dict(a=a, b=links, c=c, d=d, w=at-1)
    return result, at, forward[use], stats


def algorithm_g(original, avail, use, b=64, save_move_size=True, limit=10000):
    """G1--G9, optionally reproducing the literal post-copy SIZE(P) read."""
    mem = list(original)
    p = 1
    while p != avail:
        setf(mem, p, LINK, 0, b)
        p += get(mem, p, SIZE, b)
    top = use
    setf(mem, top, LINK, avail, b)
    setf(mem, avail, LINK, 0, b)
    while True:
        p, top = top, get(mem, top, LINK, b)
        if not top:
            break
        for k in range(1, get(mem, p, T, b)+1):
            q = get(mem, p+k, LINK, b)
            if q and not get(mem, q, LINK, b):
                setf(mem, q, LINK, top, b)
                top = q
    q, p = 1, 1
    setf(mem, avail, LINK, q, b)
    setf(mem, avail, SIZE, 0, b)
    while True:
        if get(mem, p, LINK, b):
            size = get(mem, p, SIZE, b)
            if not size:
                break
            setf(mem, p, LINK, q, b)
            q += size
            p += size
        else:
            while not get(mem, p+get(mem, p, SIZE, b), LINK, b):
                size = get(mem, p, SIZE, b)
                setf(mem, p, SIZE, size+get(mem, p+size, SIZE, b), b)
            p += get(mem, p, SIZE, b)
    newuse, newavail = get(mem, use, LINK, b), q
    p = 1
    while get(mem, p, SIZE, b):
        if get(mem, p, LINK, b):
            for q in range(p+1, p+get(mem, p, T, b)+1):
                target = get(mem, q, LINK, b)
                if target:
                    setf(mem, q, LINK, get(mem, target, LINK, b), b)
        p += get(mem, p, SIZE, b)
    p, trace = 1, []
    for _ in range(limit):
        size = get(mem, p, SIZE, b)
        if not size:
            return mem, newavail, newuse, trace
        q = get(mem, p, LINK, b)
        if q:
            setf(mem, p, LINK, 0, b)
            for k in range(size):
                mem[q+k] = mem[p+k]
        after_size = get(mem, p, SIZE, b)
        trace.append(dict(p=p, q=q, size_before=size, size_after=after_size))
        p += size if save_move_size else after_size
    raise RuntimeError('G9 exceeded finite test limit')


def mix_rows(repair_null=False, initialize=False):
    """Exact instructions on 614--615; named local labels replace 1H etc."""
    rows = [
        ('LINK','EQU','4:5'),('INFO','EQU','0:3'),('SIZE','EQU','1:2'),
        ('T','EQU','3:3'),('USE','EQU','2000'),('AVAIL','EQU','2001'),
        ('','ORIG','1000'),
        ('G2','LD1','USE'),('','LD2','AVAIL'),('','ST2','0,1(LINK)'),
        ('','STZ','0,2(LINK)'),
        ('G3','ENT3','0,1'),('','LD1','0,1(LINK)'),('','J1Z','G5'),
        ('G4','LD4','0,3(T)'),('G4LOOP','J4Z','G3'),('','INC3','1'),
        ('','DEC4','1'),('','LD2','0,3(LINK)'),('','LDA','0,2(LINK)'),
        ('','JANZ','G4LOOP'),('','ST1','0,2(LINK)'),('','ENT1','0,2'),
        ('','JMP','G4LOOP'),
        ('G5','ENT2','1'),('','ST2','0,3'),('','ENT3','1'),('','JMP','G6'),
        ('G6LIVE','ST2','0,3(LINK)'),('','INC2','0,5'),('','INC3','0,5'),
        ('G6','LDA','0,3(LINK)'),('G6A','LD5','0,3(SIZE)'),
        ('','JAZ','G7'),('','J5NZ','G6LIVE'),
        ('G8','LD1','USE'),('','LDA','0,1(LINK)'),('','STA','USE'),
        ('','ST2','AVAIL'),('','ENT3','1'),('','JMP','G8P'),
        ('G7MORE','LD6','0,6(SIZE)'),('','INC5','0,6'),
        ('G7','ENT6','0,3'),('','INC6','0,5'),('','LDA','0,6(LINK)'),
        ('','JAZ','G7MORE'),('','ST5','0,3(SIZE)'),('','INC3','0,5'),
        ('','JMP','G6A'),
        ('G8LINK','DEC4','1'),('','INC2','1'),('','LD6','0,2(LINK)'),
        ('','LDA','0,6(LINK)'),('','STA','0,2(LINK)'),
        ('G8LOOP','J4NZ','G8LINK'),('G8NEXT','INC3','0,5'),
        ('G8P','LDA','0,3(LINK)'),('','LD5','0,3(SIZE)'),
        ('','JAZ','G8NEXT'),('','LD4','0,3(T)'),('','ENT2','0,3'),
        ('','J5NZ','G8LOOP'),
        ('G9','ENT3','1'),('','ENT1','1'),('','JMP','G9P'),
        ('G9LIVE','STZ','0,3(LINK)'),('','ST5','*+1(4:4)'),
        ('','MOVE','0,3(*)'),('G9NEXT','INC3','0,5'),
        ('G9P','LDA','0,3(LINK)'),('','LD5','0,3(SIZE)'),
        ('','JAZ','G9NEXT'),('','J5NZ','G9LIVE'),
        ('DONE','HLT','0'),('','END','G2')]
    if repair_null:
        ix = rows.index(('', 'LD6', '0,2(LINK)'))
        rows.insert(ix+1, ('', 'J6Z', 'G8LOOP'))
    if initialize:
        ix = rows.index(('', 'ORIG', '1000'))
        rows[ix:ix] = [('', 'ORIG', '980'),('G1','ENT3','1'),
                       ('G1LOOP','LD5','0,3(SIZE)'),('', 'STZ','0,3(LINK)'),
                       ('','INC3','0,5'),('','CMP3','AVAIL'),
                       ('','JL','G1LOOP'),('','JMP','G2')]
    return rows


_assemblies = {}


def mix_g(mem, avail, use, b=64, repair_null=False, initialize=False):
    key = b, repair_null, initialize
    a = _assemblies.setdefault(key, None)
    if a is None:
        a = _assemblies[key] = Assembly(mix_rows(repair_null, initialize), b)
    m = Machine(b)
    m.mem = list(mem)
    a.load(m)
    m.mem[2000], m.mem[2001] = number(use, b), number(avail, b)
    m.run(a.symbols['G1' if initialize else 'G2'].value(b),
          stop=a.symbols['DONE'].value(b))
    return m.mem, m.mem[2001].value(b), m.mem[2000].value(b), m.time
