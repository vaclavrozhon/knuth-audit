# The example reinserts the symbols instead of applying the exchanges

Volume 4A, first edition, first printing (2011), exercise 7.2.1.3–48,
printed page 383, file page 400. Its answer is on page 733.

The exercise defines a list by embedding the symbols `12` into the
first binary string, then applying the successive exchanges of a
revolving-door list. In a revolving-door list, each transition exchanges
one zero with one one. The given binary list is

```
0110, 0101, 1100, 1001, 0011, 1010.
```

Starting at `0120`, those exchanges give

```
0120, 0102, 2100, 2001, 0021, 1020.
```

The book instead prints `0120, 0102, 1200, 1002, 0012, 1020`.
Already its transition `0102 -> 1200` changes three positions, so it
cannot be one interchange. The transition of binary masks
`0101 -> 1100` swaps the first and last positions; applied to `0102`
it gives `2100`, not `1200`.

Replace the three middle terms `1200, 1002, 0012` by
`2100, 2001, 0021`. The printed example appears to embed the original
ordered symbols afresh in every mask. That operation need not coincide
with the successive exchanges when the binary listing is not homogeneous
(an exchange can pass over another nonzero symbol).

The general construction and the answer's proof remain valid: after a
fixed number of exchanges, the order of the nonzero symbols is changed
by a fixed permutation, independent of their values. Thus the example,
not the stated generalization, requires repair.

Original exercise and answer images were inspected. The screened
4A/Fascicle 3 errata and public searches yielded no matching correction;
see `../sources/chase-combinations-source-check.json`. Absolute novelty
is not established.
