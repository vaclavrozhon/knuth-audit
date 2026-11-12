"""The single long benchmark of answer95; no timeout is accepted as a count."""
from run_universal_native import run
from universal_cycles import cycle95

if __name__=='__main__':
    run('native95-7-0-3-a-secondary',cycle95(7,0,3,'a-secondary'),False)
