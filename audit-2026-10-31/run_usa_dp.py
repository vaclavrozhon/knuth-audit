from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json,subprocess
R=Path(__file__).parent/'results/usa_partitions'
def run(name):
 d=json.loads((R/(name+'.json')).read_text());data=f"{d['n']} {d['k']} {len(d['rows'])}\n"+' '.join(map(str,d['adjacency']))+'\n'+'\n'.join(f"{r['mask']} {r['cost']}" for r in d['rows'])+'\n';p=subprocess.run(['/tmp/knuth-usa-partition-dp'],input=data,text=True,capture_output=True,timeout=1200);assert p.returncode==0;pout=json.loads(p.stdout);(R/(name+'-dp.json')).write_text(json.dumps(pout,indent=2)+'\n');print(name,pout,flush=True)
with ThreadPoolExecutor(max_workers=3) as ex:list(ex.map(run,['n48-k6','n48-k8','n49-k7']))
