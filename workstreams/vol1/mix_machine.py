"""Small integer MIX model for the Volume 1 audit (not a MIXAL assembler).

The byte radix is b, 64 <= b <= 100. Words retain their sign even at zero.
Unsupported/undefined instructions raise; no floating-point approximation is
silently substituted. Card input has explicit, configurable asynchronous delay.
Book programs and independent algebraic invariants are checked by the caller.
"""
from dataclasses import dataclass


class Undefined(ValueError):
    pass


@dataclass(frozen=True)
class Word:
    sign: int
    digits: tuple

    def magnitude(self, b):
        v = 0
        for d in self.digits:
            v = b * v + d
        return v

    def value(self, b):
        return self.sign * self.magnitude(b)

    def neg(self):
        return Word(-self.sign, self.digits)


def number(v, b, sign_zero=1):
    sign = -1 if v < 0 else 1 if v > 0 else sign_zero
    v = abs(v)
    if v >= b**5:
        raise Undefined('word magnitude overflow')
    a = [0] * 5
    for k in range(4, -1, -1):
        v, a[k] = divmod(v, b)
    return Word(sign, tuple(a))


def field(w, f):
    l, r = divmod(f, 8)
    if not 0 <= l <= r <= 5:
        raise Undefined('field')
    a = w.digits[max(l, 1)-1:r]
    return Word(w.sign if l == 0 else 1, (0,)*(5-len(a)) + a)


OPS = {'NOP': (0, 0), 'ADD': (1, 5), 'SUB': (2, 5),
       'MUL': (3, 5), 'DIV': (4, 5), 'NUM': (5, 0),
       'CHAR': (5, 1), 'HLT': (5, 2), 'MOVE': (7, 1),
       'STJ': (32, 2), 'STZ': (33, 5), 'JBUS': (34, 0),
       'IOC': (35, 0), 'IN': (36, 0), 'OUT': (37, 0), 'JRED': (38, 0)}
for f, name in enumerate(['SLA', 'SRA', 'SLAX', 'SRAX', 'SLC', 'SRC']):
    OPS[name] = (6, f)
for f, name in enumerate(['JMP', 'JSJ', 'JOV', 'JNOV', 'JL', 'JE', 'JG', 'JGE', 'JNE', 'JLE']):
    OPS[name] = (39, f)
for r, name in enumerate(['A', '1', '2', '3', '4', '5', '6', 'X']):
    for prefix, c in [('LD', 8), ('ST', 24), ('CMP', 56)]:
        OPS[prefix + name] = (c+r, 5)
    OPS['LD'+name+'N'] = (16+r, 5)
    for f, prefix in enumerate(['INC', 'DEC', 'ENT', 'ENN']):
        OPS[prefix+name] = (48+r, f)
    for f, suffix in enumerate(['N', 'Z', 'P', 'NN', 'NZ', 'NP']):
        OPS['J'+name+suffix] = (40+r, f)


def instruction(b, op, address=0, index=0, f=None, sign_zero=1):
    c, default = OPS[op]
    f = default if f is None else (8*f[0]+f[1] if isinstance(f, tuple) else f)
    if abs(address) >= b*b or not 0 <= index < b or not 0 <= f < b:
        raise Undefined('instruction encoding')
    a, z = divmod(abs(address), b)
    return Word(-1 if address < 0 else 1 if address > 0 else sign_zero, (a, z, index, f, c))


class Machine:
    def __init__(self, b=64, card_delay=0):
        assert 64 <= b <= 100
        self.b, self.B = b, b**5
        self.zero = number(0, b)
        self.mem = [self.zero] * 4000
        self.reg = [self.zero] * 8  # A, I1,...,I6,X
        self.j, self.pc, self.time, self.steps = 0, 0, 0, 0
        self.overflow, self.comparison, self.halted = False, 0, False
        self.cards, self.pending, self.card_delay = [], None, card_delay
        self.writes = set()

    def _finish_input(self):
        if self.pending and self.time >= self.pending[0]:
            _, m, card = self.pending
            self.pending = None
            for k, w in enumerate(card):
                self.write(m+k, w)

    def _address(self, m):
        if not 0 <= m < 4000:
            raise Undefined(('memory address', m))
        if self.pending and self.pending[1] <= m < self.pending[1]+len(self.pending[2]):
            raise Undefined(('access before input completed', m))

    def read(self, m):
        self._address(m)
        return self.mem[m]

    def write(self, m, w):
        self._address(m)
        self.mem[m] = w
        self.writes.add(m)

    def put_register(self, r, w):
        if 1 <= r <= 6 and w.magnitude(self.b) >= self.b**2:
            raise Undefined('index register overflow')
        self.reg[r] = w

    def add(self, r, v):
        old = self.reg[r]
        n = old.value(self.b) + v
        sign = -1 if n < 0 else 1 if n > 0 else old.sign
        if 1 <= r <= 6:
            self.put_register(r, number(n, self.b, sign))
        else:
            self.overflow |= abs(n) >= self.B
            self.reg[r] = number(sign*(abs(n) % self.B), self.b, sign)

    def jump(self, m, save=True):
        if not 0 <= m < 4000:
            raise Undefined('jump address')
        if save:
            self.j = self.pc
        self.pc = m

    def step(self):
        if self.halted:
            raise Undefined('step after halt')
        self._finish_input()
        w = self.read(self.pc)
        a, z, i, f, c = w.digits
        if not 0 <= i <= 6:
            raise Undefined('index selector')
        m = w.sign*(a*self.b+z)+(self.reg[i].value(self.b) if i else 0)
        if abs(m) >= self.b**2:
            raise Undefined('effective address overflow')
        self.pc += 1
        cost = 1
        if c == 0:
            pass
        elif c in (1, 2, 3, 4):
            v = field(self.read(m), f)
            if c in (1, 2):
                self.add(0, v.value(self.b)*(1 if c == 1 else -1))
                cost = 2
            elif c == 3:
                n = self.reg[0].magnitude(self.b)*v.magnitude(self.b)
                sign = self.reg[0].sign*v.sign
                h, l = divmod(n, self.B)
                self.reg[0], self.reg[7] = number(sign*h, self.b, sign), number(sign*l, self.b, sign)
                cost = 10
            else:
                d = v.magnitude(self.b)
                if self.reg[0].magnitude(self.b) >= d:
                    self.overflow = True
                    raise Undefined('division overflow; A and X undefined')
                n = self.reg[0].magnitude(self.b)*self.B+self.reg[7].magnitude(self.b)
                q, r = divmod(n, d)
                sa, sx = self.reg[0].sign*v.sign, self.reg[0].sign
                self.reg[0], self.reg[7] = number(sa*q, self.b, sa), number(sx*r, self.b, sx)
                cost = 12
        elif c == 5:
            if f == 0:
                n = 0
                for d in self.reg[0].digits+self.reg[7].digits:
                    n = 10*n+d % 10
                self.overflow |= n >= self.B
                sign = self.reg[0].sign
                self.reg[0] = number(sign*(n % self.B), self.b, sign)
                cost = 10
            elif f == 1:
                digits = tuple(30+int(d) for d in f'{self.reg[0].magnitude(self.b):010d}')
                self.reg[0] = Word(self.reg[0].sign, digits[:5])
                self.reg[7] = Word(self.reg[7].sign, digits[5:])
                cost = 10
            elif f == 2:
                self.halted = True
            else:
                raise Undefined('special operation')
        elif c == 6:
            if m < 0 or f > 5:
                raise Undefined('shift')
            a = list(self.reg[0].digits + (() if f < 2 else self.reg[7].digits))
            n = len(a)
            if f >= 4:
                k = (m if f == 4 else -m) % n
                a = a[k:] + a[:k]
            else:
                k = min(m, n)
                a = a[k:]+[0]*k if f % 2 == 0 else [0]*k+a[:n-k]
            self.reg[0] = Word(self.reg[0].sign, tuple(a[:5]))
            if f >= 2:
                self.reg[7] = Word(self.reg[7].sign, tuple(a[5:]))
            cost = 2
        elif c == 7:
            dest = self.reg[1].value(self.b)
            for k in range(f):
                self.write(dest+k, self.read(m+k))
            self.add(1, f)
            cost = 1+2*f
        elif 8 <= c <= 23:
            v = field(self.read(m), f)
            self.put_register(c % 8, v if c < 16 else v.neg())
            cost = 2
        elif 24 <= c <= 33:
            v = self.reg[c-24] if c < 32 else number(self.j, self.b) if c == 32 else self.zero
            old = self.read(m)
            l, r = divmod(f, 8)
            if not 0 <= l <= r <= 5:
                raise Undefined('store field')
            start = max(l, 1)-1
            a = list(old.digits)
            k = r-start
            a[start:r] = v.digits[5-k:] if k else ()
            self.write(m, Word(v.sign if l == 0 else old.sign, tuple(a)))
            cost = 2
        elif c in (34, 36, 38):
            if f != 16:
                raise Undefined('only card reader I/O implemented')
            if c == 36:
                if self.pending:
                    self.time = max(self.time, self.pending[0])
                    self._finish_input()
                if not self.cards:
                    raise Undefined('empty card deck')
                self.pending = (self.time+1+self.card_delay, m, self.cards.pop(0))
            elif (c == 34) == bool(self.pending):
                self.jump(m)
        elif c == 39:
            tests = [True, True, self.overflow, not self.overflow,
                     self.comparison < 0, self.comparison == 0, self.comparison > 0,
                     self.comparison >= 0, self.comparison != 0, self.comparison <= 0]
            if f >= len(tests):
                raise Undefined('jump variant')
            if f in (2, 3):
                self.overflow = False
            if tests[f]:
                self.jump(m, f != 1)
        elif 40 <= c <= 47:
            v = self.reg[c-40].value(self.b)
            tests = [v < 0, v == 0, v > 0, v >= 0, v != 0, v <= 0]
            if f >= len(tests):
                raise Undefined('register jump variant')
            if tests[f]:
                self.jump(m)
        elif 48 <= c <= 55:
            if f < 2:
                self.add(c-48, m if f == 0 else -m)
            elif f in (2, 3):
                v = number(m, self.b, w.sign)
                self.put_register(c-48, v if f == 2 else v.neg())
            else:
                raise Undefined('address-transfer variant')
        elif 56 <= c <= 63:
            a = field(self.reg[c-56], f).value(self.b)
            v = field(self.read(m), f).value(self.b)
            self.comparison = (a > v)-(a < v)
            cost = 2
        else:
            raise Undefined('operation code')
        self.time += cost
        self.steps += 1

    def run(self, start, stop=None, limit=100000):
        self.pc = start
        for _ in range(limit):
            if self.halted or (stop is not None and self.pc == stop):
                return
            self.step()
        raise RuntimeError('step limit, not a proof of nontermination')

    def program(self, start, rows):
        for k, row in enumerate(rows):
            self.mem[start+k] = instruction(self.b, *row)

    def go(self):
        card = self.cards.pop(0)
        self.mem[:16] = card
        self.j, self.pc, self.overflow = 0, 0, False
