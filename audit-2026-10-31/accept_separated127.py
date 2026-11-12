"""Accept the already completed separated101 job; never launch a search."""
from datetime import datetime,timezone
import json
import borders127_128 as b
from puzzle_xcc import sha,save
from check_symmetries129_checkpoint import native
from run_border_counts127 import validate_samples

def main():
 out=b.OUT;checked=json.loads((out/'separated101-count-checked.json').read_text());terminal=native(out/'counts-native/separated101.json')
 assert checked['native_sha256']==terminal['sha256'] and checked['color_orbits']==terminal['solutions']==24970520
 assert checked['model_sha256']==sha(b.__file__) and checked['runner_sha256']==sha(b.ROOT/'run_border_counts127.py')
 assert checked['labeled_solutions']==49941040 and checked['free_color_symmetry_factor']==2
 samples=validate_samples('separated101',b.problem127(checked['word']));assert len(samples)==checked['validated_samples']==249
 save(out/'separated101-accepted.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),source_sha256=sha(__file__),checked_sha256=sha(out/'separated101-count-checked.json'),native=terminal,labeled_solutions=49941040,validated_samples=249,scope='Saved terminal and all emitted samples accepted; c/d normalisation reused from earlier checked invariant instances. The independent full count and other127 gaps are not claimed here.'))
 print('PASS127 saved separated101:49941040 labeled solutions,249 valid samples; no search repeated.')

if __name__=='__main__':main()
