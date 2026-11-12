"""Standalone parity certificate for the impossible printed DLX150 inventory.

No solver, external data or third-party package is needed. Rows are numbered
left to right, first the nine top strips and then the nine bottom strips.
Each direction is a boundary crossing of the chain's center path, not an
individual ink stroke outlining a metal link.
"""
from itertools import product

# Empty strings denote blank strips. N/S are the long upper/lower sides;
# W/E are the left/right ends. The final two strips' special half-link
# connection is counted as one path end on each of their matching sides.
PORTS = ['', '', 'NW', '', '', 'NS', 'NS', 'NS', 'NN',
         'NS', 'NS', '', 'NS', 'NE', 'NN', 'WE', 'NSSE', 'NS']
LENGTHS = [2,2,2,4,4,4,4,5,5,2,2,3,3,3,4,4,5,6]


def main():
    assert len(PORTS)==len(LENGTHS)==18 and sum(LENGTHS)==64
    horizontal=[sum(c in 'WE' for c in p) for p in PORTS]
    vertical=[sum(c in 'NS' for c in p) for p in PORTS]
    assert sum(horizontal)==5 and sum(vertical)==23
    assert all((h-v)%2==0 for h,v in zip(horizontal,vertical))
    odd=[i+1 for i,h in enumerate(horizontal) if h%2]
    assert odd==[3,14,17]
    # A quarter turn swaps horizontal and vertical counts. Because each
    # strip has an even number of ends, its parity cannot change.
    parity={0}
    for h,v in zip(horizontal,vertical):parity={(a+b)%2 for a,b in product(parity,[h,v])}
    assert parity=={1}
    print('Printed strips3,14,17 have odd horizontal-end parity; all others even.')
    print('Every orientation has an odd total. Internal joins pair horizontal ends,')
    print('so no closed arrangement exists, even if several loops or flips are allowed.')
    corrected=PORTS.copy();corrected[9]=PORTS[2]
    assert sum(sum(c in 'WE' for c in p) for p in corrected)%2==0
    print('Replacing one bottom-row S-domino by a second top-row L-domino removes this obstruction.')
    print('This last assertion is only the necessary parity condition; concrete witnesses are checked separately.')


if __name__=='__main__':main()
