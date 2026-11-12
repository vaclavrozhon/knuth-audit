"""Asynchronous I/O extension used by the MIXAL audit.

Supports block IN/OUT on units needed here and printer page advance. It checks
buffer ownership until completion; no disk addressing or tape motion is modeled.
"""
from collections import defaultdict, deque
from mix_machine import Machine, Undefined


class IOMachine(Machine):
    LENGTH = {0: 100, 1: 100, 16: 16, 17: 16, 18: 24, 19: 14, 20: 14}

    def __init__(self, b=64, delay=0):
        super().__init__(b)
        self.delay = delay
        self.devices = {}
        self.inputs = defaultdict(deque)
        self.outputs = defaultdict(list)
        self.controls = []

    def _finish_input(self):
        for unit, (end, op, addr, data) in list(self.devices.items()):
            if self.time < end:
                continue
            del self.devices[unit]
            if op == 36:
                for k, word in enumerate(data):
                    self.write(addr+k, word)
            elif op == 37:
                self.outputs[unit].append(tuple(self.mem[addr:addr+self.LENGTH[unit]]))
            else:
                self.controls.append((unit, addr))

    def _guard(self, m, writing):
        for _, op, addr, data in self.devices.values():
            length = len(data) if op == 36 else len(data) if op == 37 else 0
            if addr <= m < addr+length and (writing or op == 36):
                raise Undefined(('access to busy I/O buffer', m, op))

    def read(self, m):
        self._guard(m, False)
        return super().read(m)

    def write(self, m, w):
        self._guard(m, True)
        super().write(m, w)

    def step(self):
        self._finish_input()
        word = self.read(self.pc)
        a, z, i, unit, code = word.digits
        if not 34 <= code <= 38:
            return super().step()
        if self.halted or i > 6 or unit not in self.LENGTH:
            raise Undefined('unsupported I/O instruction')
        m = word.sign*(a*self.b+z)+(self.reg[i].value(self.b) if i else 0)
        if abs(m) >= self.b*self.b:
            raise Undefined('I/O effective address')
        self.pc += 1
        if code in (34, 38):
            if (code == 34) == (unit in self.devices):
                self.jump(m)
        else:
            if unit in self.devices:
                self.time = max(self.time, self.devices[unit][0])
                self._finish_input()
            if code == 35:
                if unit != 18 or m != 0:
                    raise Undefined('only printer page advance IOC implemented')
                data = ()
            else:
                n = self.LENGTH[unit]
                if not 0 <= m <= 4000-n:
                    raise Undefined('I/O block address')
                if code == 36:
                    if unit in (17, 18) or not self.inputs[unit]:
                        raise Undefined('unsupported/empty input')
                    data = tuple(self.inputs[unit].popleft())
                    if len(data) != n:
                        raise Undefined('input block length')
                else:
                    if unit == 16:
                        raise Undefined('card reader output')
                    data = tuple(self.read(m+k) for k in range(n))
                for k in range(n):
                    self._guard(m+k, code == 36)
            delay = self.delay(unit, code) if callable(self.delay) else self.delay
            if delay < 0:
                raise ValueError('negative I/O delay')
            self.devices[unit] = (self.time+1+delay, code, m, data)
        self.time += 1
        self.steps += 1

    def finish_io(self):
        if self.devices:
            self.time = max(v[0] for v in self.devices.values())
            self._finish_input()
