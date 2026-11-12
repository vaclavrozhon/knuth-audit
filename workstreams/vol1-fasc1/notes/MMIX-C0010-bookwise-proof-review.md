# MMIX-C0010: the recursive-simulation guarantee uses the wrong capacity unit

Confirmed error in the printed argument, medium severity. This review does
not establish that the numerical conclusion itself is false. Location:
answer 1.4.3′–21, printed126 / file134, second paragraph, digital release3
(May2023). The original page image was inspected again on12November2026.

Let C=4096 be the number of virtual data bytes in a chunk and let a_k be the
scalar upper bound obtained from the printed recurrence, starting at a_0=0:

```
a_(k+1) = 4 + ceil((4112 + 4120 a_k)/4096)
        = a_k + 5 + ceil((3 a_k + 2)/512).
```

The sequence counts chunks. Each chunk occupies a 4120-byte node in the
host's data segment: 4096 data bytes, two eight-byte fields and eight padding
bytes. The fixed preceding allocation occupies4112 bytes. Thus the available
number of complete nodes is

```
K = floor((2^61 - 4112)/4120) = 559670633304293.
```

This is also the integer capacity in answer4 on printed117. The retained
exact scalar calculation gives

```
a_4640 = 557373330226371 <= K,
a_4641 = 560639189583172 > K,
a_6065 = 2300134210731528098 < 2^61.
```

No calculation was repeated. The result and both equivalent recurrence
forms are recorded in `results/recurse21-scalar-bound.json`.

To infer that allocation fits from an upper bound n_k <= a_k, the bound
must fit the node capacity K. The printed comparison a_k < 2^61 compares
chunks with bytes and does not supply that condition. Its resulting
100^6065 instruction guarantee therefore does not follow from this
argument, even granting the separate stipulated factor100 per level.
The weaker condition allows chunk counts more than four thousand times
the available node count. A generic count equal to the displayed upper
bound already illustrates the missing logical implication; it is not
claimed to be the actual simulator's count.

The earlier candidate assessment correctly observed that crossing an upper
bound cannot prove an actual failure time. It incorrectly treated such a
failure witness as necessary to confirm the flaw in the printed proof.
The current scope distinguishes those conclusions: the dimensional
inference is wrong; actual recursive allocation depth and the truth of the
numerical lower bound remain unresolved. Merely replacing6065 by4640 is
not presented as a complete repair of every assumption in that bound.

The original pages117/126, existing capacity proof and scalar certificate
were read together. The current TEX and cumulative fascicle errata, current
MMIXware errata and public bug index were downloaded again; all four were
byte-identical to the previously checked sources. Thirteen relevant saved
historical/current layers were searched for this argument, and the current
TEX answer corrections were read through the transition from125 to the
index127. No correction of126 is present. Targeted public searches found
no relevant correction. This is not a claim of absolute priority.

Evidence: `results/bookwise-C0010-source-check.json`,
`results/bookwise-errata-refresh-2026-11-12.json`,
`results/recurse21-scalar-bound.json`, `results/node-capacity4.json`,
`images/file-134-p126.png` and `images/file-125-p117.png`.
