"""Independent literal XCC versus projected join and distinct-word matching."""
import hashlib
import json
import random
import time
from itertools import product
from pathlib import Path

from colored_dlx import ColoredDLX
from word_kernel91 import (DistinctWitness, graph, kernel_set, literal_encoding,
                           validate_completion, stair_kernels, LEFT36, RIGHT5)
from double_word_tools import dictionary, validate, down_words


class DiscardEvents(list):
    def append(self, event):
        pass


def main():
    started=time.monotonic();rng=random.Random(910026)
    universe=[''.join(x) for x in product('AB',repeat=5)]
    cases=[];models=0
    dictionaries=[[],['AAAAA'],['AAAAA','BBBBB']]
    dictionaries += [rng.sample(universe,n) for n in range(3,10) for _ in range(3)]
    for words in dictionaries:
        for kind in ['left','right']:
            joined=kernel_set(words,kind)
            dw=DistinctWitness(words,kind)
            filtered={k for k in joined if dw.witness(k)}
            for distinct,expected in [(False,joined),(True,filtered)]:
                enc=literal_encoding(words,kind,distinct)
                solver=ColoredDLX(len(enc['names']),8,enc['rows'])
                solver.events=DiscardEvents();solver.solve()
                actual=set()
                for model in solver.solutions:
                    chosen=[None]*8
                    for ri in model:
                        slot,rank=enc['info'][ri];assert chosen[slot] is None
                        chosen[slot]=words[rank]
                    actual.add(validate_completion(chosen,kind,distinct))
                assert actual==expected,(words,kind,distinct,len(actual),len(expected))
                models+=len(solver.solutions)
                cases.append(dict(W=len(words),kind=kind,distinct=distinct,
                                  models=len(solver.solutions),kernels=len(actual)))
    words=dictionary(5);printed={}
    for kind,rows in [('left',LEFT36),('right',RIGHT5)]:
        rank=validate(rows,words,kind)
        edges=graph(stair_kernels(rows,kind),kind)
        physical=[__import__('word_kernel91').edge(k,kind) for k in stair_kernels(rows,kind)]
        assert all(physical[i][1]==physical[(i+1)%len(rows)][0] for i in range(len(rows)))
        assert [e[2] for e in physical]==rows
        assert {e[3] for e in physical}==set(down_words(rows,kind))
        printed[kind]=dict(period=len(rows),rank=rank,rows=rows,down=down_words(rows,kind),
                           vertices=[e[0] for e in physical],simple=len({e[0] for e in physical})==len(rows))
    out=Path(__file__).resolve().parent/'results/stair_kernels/small-checked.json'
    out.write_text(json.dumps(dict(cases=cases,comparisons=len(cases),models=models,
          printed=printed,seconds=time.monotonic()-started,
          source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),indent=2)+'\n')
    print(json.dumps(dict(comparisons=len(cases),models=models,printed=printed,
                         seconds=time.monotonic()-started)))


if __name__=='__main__':main()
