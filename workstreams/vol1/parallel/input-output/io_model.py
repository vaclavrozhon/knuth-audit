"""Local convenience extension of the unchanged shared asynchronous I/O model."""
from mix_io import IOMachine


class TapeIO(IOMachine):
    LENGTH={**IOMachine.LENGTH, **{u:100 for u in range(8)}}

    def step(self):
        self._finish_input()
        w=self.read(self.pc)
        a,z,i,f,c=w.digits
        if c==34 and i==0 and w.sign*(a*self.b+z)==self.pc and f in self.devices:
            iterations=self.devices[f][0]-self.time
            assert iterations>0
            self.j=self.pc+1
            self.time+=iterations
            self.steps+=iterations
            return
        super().step()
