# Wrong line range in the Heap-program generalization

**Location.** Volume 4A, first edition, first printing (2011), first
sentence of answer 7.2.1.2–78, printed page 716 / file page 733.

The sentence says that lines 31–38 of answer 77 become 2r-1
instructions when r entries are kept in registers. At r=3, those are
eight instructions, whereas 2r-1=5.

The intended range is **34–38**: one conditional assignment for each
of the r cached entries, separated by r-1 decrements of j. Lines
31–33 (the even-k adjustment, the load of a[j], and its replacement)
remain separately necessary.

Change 31–38 to 34–38. The final running-time formula is already
consistent with this correction: summing its memory operations and
branch costs reproduces the printed coefficients.

The original listing and answer were inspected. Relevant 4A/Fascicle 2
errata contain no matching correction. Public search found the same
line range in an earlier draft, not an explicit correction. Absolute
priority is not established. See sources/mmix-topological-source-check.json.
