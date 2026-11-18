# F266 — The double-lookahead example counts variables instead of literals

**Location:** Volume 4B, first edition, second printing (2022), printed
page 229 (file page 249), the paragraph beginning “Going back to our
example.” Compare equation (70) on page 226 and step Y2 on page 230.

**Correction:** Replace `S = 8` by `S = 16`, and `DT = 130` by
`DT = 258`. This is a numerical error in the worked example; the stated
algorithm does not need this change.

Here `S` is the number of candidate **literals** retained after contracting
the strongly connected components of the binary implication graph. It is
the number of entries in the lookahead arrays, indexed from `0` to `S-1`.
A literal is a variable or its negation. The example has eight free
variables, but all sixteen of their literals are separate components.

The preorder row in equation (70) explicitly lists them:

```text
1, 2, not 8, 3, 4, 6, not 4, 7,
not 3, not 6, not 9, 8, not 2, 9, not 1, not 7.
```

The corresponding truth offsets end at 32 and are twice the postorder
positions of these sixteen entries. Thus `S = 16`; eight is the number
of free variables, not the number of lookahead entries.

The paragraph considers the first entry, literal 1. As stated immediately
below (70), its context is `T = 2`; its offset is `LO[0] = 2`. With the
paragraph's parameter `Y = 8`, step Y2 gives

```text
BASE  = T - 2            = 0,
LBASE = BASE + 2*S*Y     = 0 + 2*16*8 = 256,
DT    = LBASE + LO[0]    = 256 + 2    = 258.
```

The printed 130 is precisely what results from substituting the erroneous
`S = 8`. The later statement that the next lookahead uses context 6
agrees with the same sixteen-entry forest. No new solver execution or
enumeration is needed for this discrepancy.

The original images for pages 226, 229, and 230 were inspected and saved
in the focused-run sources directory. The September 23, 2015 Fascicle 6A
draft has the same numerical example on page 45 (file page 53).

All six current/historical errata text layers and the three official TeX
errata sources were checked. Nearby published corrections concern other
steps of Algorithms X and Y, including Y3, Y7, and Y8; none changes this
example. Focused public searches found the original passage and program
material, but no matching correction. This does not establish absolute
priority. See `../results/focused-lookahead-dt-sources.json` for the source
record and hashes.
