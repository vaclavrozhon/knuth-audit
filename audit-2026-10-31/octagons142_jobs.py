"""Finite DLX142 census queue; no import-time searches."""
JOBS = [
    dict(label='iii-tb',case='iii',periodic=['tb'],expected=0,every=1),
    dict(label='iii-lr',case='iii',periodic=['lr'],expected=0,every=1),
    dict(label='i-both',case='i',periodic=['tb','lr'],expected=192,every=1),
    dict(label='ii-lr',case='ii',periodic=['lr'],expected=11960,every=1),
    dict(label='i-lr',case='i',periodic=['lr'],expected=21024,every=1),
    dict(label='iii',case='iii',periodic=[],expected=239198,every=1),
    dict(label='i-tb',case='i',periodic=['tb'],expected=387840,every=1),
    dict(label='ii-tb',case='ii',periodic=['tb'],expected=None,every=1),
    dict(label='i',case='i',periodic=[],expected=264093722,every=10000),
    dict(label='ii',case='ii',periodic=[],expected=3317206,every=10000),
]
