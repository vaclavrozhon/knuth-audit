# F206: Reset the variable entry, not the encoded literal entry

Volume 4B, step X2, printed 228 / PDF 248.

On page 221 VAL is indexed by variables: VAL[k] stores the value of x_k.
A literal l is encoded as 2k or 2k+1, and its underlying variable is
|l|=k. Step X2 nevertheless says to set VAL[l] to zero for each free
literal l. It should set **VAL[|l|] ← 0**, or iterate over free variables
x and set VAL[x] to zero.

A reachable, entirely in-range example is the formula

    (x2) AND (x3) AND (x1 OR x2).

After accepting the two input units, F=2, x2 and x3 are really true,
and x1 is free. Step X1 does not terminate because F<n=3. The encoded
free literals are 2 and 3. Printed X2 therefore erases VAL[2] and
VAL[3], destroying both real truths while F still says that two
variables are fixed. The corrected index touches only VAL[1] and
preserves them. For other free variables the printed indices can also
exceed the declared variable range. No claim about a complete solver’s
ultimate answer is needed: this step directly violates its invariant.

The original page image confirms the missing absolute-value bars.
This particular line was introduced by the public Fascicle 6 erratum
of July 9, 2020 (page 44, X2); its TeX also explicitly contains VAL[l].
The older September 2015 draft predates that reset and therefore is not
independent evidence of this specific typo. The existing erratum
introduces the defective line; it does not correct its index. No later
matching index correction was found in the inspected lists.

The current official SAT11 source iterates over `x=freevar[k]` and
correctly executes `stamp[x]=0` (lines 2215–2217). The fixed three-variable
state is checked by `check_bookwise_sat134_x2.py`, with results in
`results/bookwise-sat134-x2.json`.
