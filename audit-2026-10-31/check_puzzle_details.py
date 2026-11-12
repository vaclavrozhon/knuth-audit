"""Accept existing finite outputs; resolve raw pi counts and zebra tie order."""
from math import comb
import json
from check_arrows102 import pi_graph
from check_zebra101 import instance,NoEvents
from colored_dlx import ColoredDLX
from puzzle_xcc import OUT,encode,native,read_models,save,sha


def main():
    adj,given,cells=pi_graph();degree=list(map(len,adj));delta=max(degree)
    H=sum(sum(comb(delta+1,d) for d in ([given[v]] if v in given else range(degree[v]+1))) for v in range(100))
    I=sum(1 if v in given else degree[v]+1 for v in range(100))
    E=100*(delta+1)+sum(degree[w]+1 for a in adj for w in a)
    raw=dict(primary=100*2+100*(delta+1),secondary=100+100*(delta+1)+sum(d+1 for d in degree),
             H_options=H,I_options=I,E_options=E,total_options=H+I+E)
    assert (raw['primary'],raw['secondary'],raw['total_options'])==(1200,1831,59871)
    e=instance(True)
    opts=[[(e['names'][i-1],c) for i,c in row] for row in e['rows']]
    enc=encode(sorted(e['names'][:16]),e['names'][16:],opts)
    meta=native('zebra-inverse-lexical',enc)
    dlx=ColoredDLX(len(enc['names']),16,enc['rows']);dlx.events=NoEvents();dlx.solve()
    assert meta['status']=='completed' and meta['nodes']==32 and meta['solutions']==1
    assert read_models('zebra-inverse-lexical',enc)==dlx.solutions and sum(dlx.profile.values())==32
    save(OUT/'details-checked.json',dict(script_sha256=sha(__file__),pi_day_unsimplified=raw,
         zebra_lexical_primary_order=enc['names'][:16],zebra_lexical_nodes=32,
         zebra_lexical_initial_mems=meta['initial_mems'],zebra_lexical_search_mems=meta['net_search_mems'],
         conclusion='112direct numerical;34inverse numerical;32inverse lexical. No primary tie order is specified by the book; all have the same unique model.'))
    print(raw,'Zebra inverse lexical:',meta['nodes'])


if __name__=='__main__':main()
