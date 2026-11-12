"""Audit assembler for structured (label, opcode, address) MIXAL rows.

Implements the integer expression/W-value and local/future-reference rules
used by the audited programs. It is not a card/terminal input parser. Literals
containing * are rejected rather than guessing their location-counter meaning.
"""
import re
from mix_machine import Word, number, OPS, Undefined


CHARACTERS = ' ABCDEFGHIΔJKLMNOPQRΣΠSTUVWXYZ0123456789.,()+-*/=$<>@;:\u2019'
CHAR_CODE = {c: i for i, c in enumerate(CHARACTERS)}
OPERATORS = dict(OPS, FADD=(1, 6), FSUB=(2, 6), FMUL=(3, 6),
                 FDIV=(4, 6), FCMP=(56, 6))


def put(old, value, f):
    l, r = divmod(f, 8)
    if not 0 <= l <= r <= 5:
        raise Undefined('W-value field')
    start = max(l, 1)-1
    count = r-start
    a = list(old.digits)
    a[start:r] = value.digits[5-count:] if count else ()
    return Word(value.sign if l == 0 else old.sign, tuple(a))


class Assembly:
    def __init__(self, rows, b=64, reverse_literals=False):
        self.b, self.B = b, b**5
        self.symbols, self.memory, self.locations = {}, {}, []
        self.pc, self.start = 0, None
        self.pending, self.literals = [], []
        rows = self._locals(rows)
        for label, op, addr in rows:
            self.locations.append(self.pc)
            if op == 'END':
                for symbol in dict.fromkeys(s for _, s in self.pending):
                    # An END label is a real LOC definition (rules 11f/13),
                    # at the first address after implicit words and literals.
                    if (symbol not in self.symbols and symbol != label
                            and not symbol.startswith('@L')):
                        self.symbols[symbol] = number(self.pc, b)
                        self.memory[self.pc] = number(0, b)
                        self.pc += 1
                for name, value in (reversed(self.literals) if reverse_literals else self.literals):
                    self.symbols[name] = number(self.pc, b)
                    self.memory[self.pc] = value
                    self.pc += 1
            if label:
                if label in self.symbols:
                    raise ValueError(('duplicate symbol', label))
                self.symbols[label] = number(self.pc, b)
            if op == 'EQU':
                value = self.wvalue(addr)
                if label:
                    self.symbols[label] = value
            elif op == 'ORIG':
                self.pc = self.wvalue(addr).value(b)
                if not 0 <= self.pc < b*b:
                    raise Undefined('location counter')
            elif op == 'END':
                self.start = self.wvalue(addr).magnitude(b) % (b*b)
                break
            else:
                if op == 'CON':
                    word = self.wvalue(addr)
                elif op == 'ALF':
                    if len(addr) != 5:
                        raise ValueError('ALF requires exactly five characters')
                    word = Word(1, tuple(CHAR_CODE[c] for c in addr))
                else:
                    word = self.instruction(op, addr)
                if not 0 <= self.pc < 4000:
                    raise Undefined('assembled memory address')
                self.memory[self.pc] = word
                self.pc += 1
        for location, symbol in self.pending:
            self.memory[location] = put(self.memory[location], self.symbols[symbol], 2)

    @staticmethod
    def _locals(rows):
        definitions = {d: [] for d in '0123456789'}
        for k, (label, _, _) in enumerate(rows):
            if re.fullmatch(r'[0-9]H', label):
                definitions[label[0]].append(k)
        result = []
        for k, (label, op, addr) in enumerate(rows):
            def replace(m):
                d, direction = m[0]
                choices = [j for j in definitions[d] if (j < k if direction == 'B' else j > k)]
                if not choices:
                    raise ValueError(('unresolved local reference', m[0], k))
                return f'@{d}_{max(choices) if direction == "B" else min(choices)}'
            if op != 'ALF':
                addr = re.sub(r'(?<![A-Z0-9])[0-9][BF](?![A-Z0-9])', replace, addr)
            if re.fullmatch(r'[0-9]H', label):
                label = f'@{label[0]}_{k}'
            result.append((label, op, addr))
        return result

    def expression(self, text):
        token = r'(?:[A-Z0-9@_]+|\*)'
        m = re.match(r'([+-]?)('+token+')', text)
        if not m:
            raise ValueError(('expression', text))
        def atom(t):
            if t == '*':
                return number(self.pc, self.b)
            if t.isdigit():
                return number(int(t), self.b)
            if t not in self.symbols:
                raise ValueError(('future reference inside expression', t))
            return self.symbols[t]
        value = atom(m[2])
        if m[1] == '-':
            value = value.neg()
        rest = text[m.end():]
        while rest:
            m = re.match(r'(//|[+*/:\-])('+token+')', rest)
            if not m:
                raise ValueError(('expression suffix', rest))
            other = atom(m[2]); op = m[1]
            a, c = value.value(self.b), other.value(self.b)
            sign = value.sign * other.sign
            if op in ('+', '-'):
                n = a+c if op == '+' else a-c
                sign = -1 if n < 0 else 1 if n > 0 else value.sign
            elif op == '*':
                n = a*c
            elif op in ('/', '//'):
                if c == 0:
                    raise Undefined('expression division by zero')
                n = sign*(abs(a)*(self.B if op == '//' else 1)//abs(c))
                if abs(n) >= self.B:
                    raise Undefined('expression division overflow')
            else:
                av = number(value.sign*(8*abs(a) % self.B), self.b, value.sign)
                n = av.value(self.b)+c
                sign = -1 if n < 0 else 1 if n > 0 else av.sign
            value = number(sign*(abs(n) % self.B), self.b, sign)
            rest = rest[m.end():]
        return value

    def wvalue(self, text):
        word = number(0, self.b)
        for term in text.split(','):
            m = re.fullmatch(r'([^()]+)(?:\(([^()]+)\))?', term)
            if not m:
                raise ValueError(('W-value', term))
            f = 5 if m[2] is None else self.expression(m[2]).value(self.b)
            word = put(word, self.expression(m[1]), f)
        return word

    def instruction(self, op, text):
        code, default = OPERATORS[op]
        # A literal's parentheses/commas belong to its W-value, not the instruction.
        if text.startswith('='):
            close = text.index('=', 1)
            literal, suffix = text[1:close], text[close+1:]
            if len(literal) >= 10 or '*' in literal:
                raise ValueError('unsupported literal length or location counter')
            name = f'@L{len(self.literals)}'
            self.literals.append((name, self.wvalue(literal)))
            text = name+suffix
        m = re.fullmatch(r'([^,()]*)(?:,([^()]+))?(?:\(([^()]+)\))?', text)
        if not m:
            raise ValueError(('instruction address', text))
        a, index, f = m.groups()
        if re.fullmatch(r'[A-Z0-9@_]+', a) and not a.isdigit() and a not in self.symbols:
            self.pending.append((self.pc, a))
            address = number(0, self.b)
        else:
            address = self.expression(a) if a else number(0, self.b)
        word = number(code, self.b)
        word = put(word, self.expression(f) if f else number(default, self.b), 36)
        word = put(word, self.expression(index) if index else number(0, self.b), 27)
        return put(word, address, 2)

    def load(self, machine):
        for location, word in self.memory.items():
            machine.mem[location] = word
        if self.start is not None:
            machine.pc = self.start
