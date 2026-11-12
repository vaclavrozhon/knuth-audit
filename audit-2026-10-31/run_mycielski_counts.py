"""Detached independent counts for DLX117(e--g), with a small complete oracle."""
from collections import Counter
from datetime import datetime,timezone
from itertools import combinations,product
from pathlib import Path
import fcntl,json,math,os,subprocess,tempfile,time
from graph_native import ROOT,OUT,save,sha

def mycielski(n,edges):
    return 2*n+1,sorted(set(edges)|{(min(u+n,v),max(u+n,v)) for u,v in edges}|{(min(u,v+n),max(u,v+n)) for u,v in edges}|{(n+v,2*n) for v in range(n)})

def text(n,d,edges):return f'{n} {d} {len(edges)}\n'+''.join(f'{u} {v}\n' for u,v in edges)

def main():
    lock=(OUT/'mycielski-counts.lock').open('w');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    assert not (OUT/'mycielski-counts-queue.json').exists()
    work=Path(tempfile.mkdtemp(prefix='knuth-vol4b-colorings-',dir='/tmp'))
    src=ROOT/'count_graph_colorings.cpp';binary=work/'colorings'
    command=['g++','-O3','-std=c++17','-Wall','-Wextra',str(src),'-o',str(binary)]
    p=subprocess.run(command,capture_output=True,text=True)
    save(OUT/'mycielski-counts-build.json',dict(command=command,returncode=p.returncode,stdout=p.stdout,stderr=p.stderr,source_sha256=sha(src)))
    assert p.returncode==0,p.stderr
    # Exhaustive labeled-color oracle checks every graph on <=4 vertices and d<=4.
    checks=[]
    for n in range(1,5):
        possible=list(combinations(range(n),2))
        for mask in range(1<<len(possible)):
            edges=[e for i,e in enumerate(possible) if mask>>i&1]
            for d in range(1,5):
                q=subprocess.run([str(binary)],input=text(n,d,edges),text=True,capture_output=True,check=True)
                result=json.loads(q.stdout);counts=result['partitions_by_used_colors']
                expected=sum(all(a[u]!=a[v] for u,v in edges) for a in product(range(d),repeat=n))
                actual=sum(z*math.factorial(d)//math.factorial(d-k) for k,z in enumerate(counts))
                assert actual==expected,(n,mask,d,actual,expected)
                checks.append(dict(n=n,mask=mask,colors=d,labeled_count=expected,partitions=counts))
    save(OUT/'coloring-small-oracle.json',dict(source_sha256=sha(src),script_sha256=sha(__file__),instances=len(checks),cases=checks))
    q=dict(status='running',wrapper_pid=os.getpid(),started_utc=datetime.now(timezone.utc).isoformat(),script_sha256=sha(__file__),done=[])
    save(OUT/'mycielski-counts-queue.json',q)
    n,edges=2,[(0,1)];summary=[]
    for c,want,deleted in [(2,1,{1}),(3,5,{1}),(4,520,{5,7}),(5,23713820,{1432,1544,1600,2200,2492,2680,3744,4602,6640})]:
        cases=[('c',c,edges),('c-minus1',c-1,edges)]+[(f'delete-{i}',c-1,edges[:i]+edges[i+1:]) for i in range(len(edges))]
        deleted_counts=[]
        for name,d,ee in cases:
            label=f'mycielski{c}-{name}';q['current']=label;save(OUT/'mycielski-counts-queue.json',q)
            inp=OUT/(label+'.in');inp.write_text(text(n,d,ee));start=time.monotonic()
            command=['timeout','172800',str(binary)]
            meta=dict(status='running',wrapper_pid=os.getpid(),command=command,started_utc=datetime.now(timezone.utc).isoformat(),source_sha256=sha(src),script_sha256=sha(__file__),binary_sha256=sha(binary),input_sha256=sha(inp),timeout_seconds=172800)
            with inp.open() as fin,(OUT/(label+'.out')).open('w') as fout,(OUT/(label+'.log')).open('w') as ferr:
                p=subprocess.Popen(command,stdin=fin,stdout=fout,stderr=ferr);meta['pid']=p.pid;save(OUT/(label+'-run.json'),meta);rc=p.wait()
            meta.update(status='completed' if rc==0 else 'incomplete',returncode=rc,elapsed_seconds=time.monotonic()-start,finished_utc=datetime.now(timezone.utc).isoformat(),stdout_sha256=sha(OUT/(label+'.out')),stderr_sha256=sha(OUT/(label+'.log')))
            if rc==0:
                result=json.loads((OUT/(label+'.out')).read_text());meta.update(result)
                counts=result['partitions_by_used_colors'];total=sum(counts)
                if name=='c':assert total==want
                elif name=='c-minus1':assert total==0
                else:assert total in deleted;deleted_counts.append(total)
            save(OUT/(label+'-run.json'),meta);assert rc==0,meta
            q['done'].append(label);save(OUT/'mycielski-counts-queue.json',q)
        assert set(deleted_counts)==deleted
        summary.append(dict(c=c,n=n,edges=len(edges),color_partitions=want,edge_deletion_histogram=dict(sorted(Counter(deleted_counts).items()))))
        print(summary[-1],flush=True);n,edges=mycielski(n,edges)
    save(OUT/'mycielski-counts-checked.json',dict(source_sha256=sha(src),script_sha256=sha(__file__),small_instances=len(checks),graphs=summary))
    q.update(status='completed',finished_utc=datetime.now(timezone.utc).isoformat());save(OUT/'mycielski-counts-queue.json',q)

if __name__=='__main__':main()
