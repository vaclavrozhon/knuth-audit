# F174: Three illustrative tableaux lose minwise independence

Status: confirmed locally; low severity. TAOCP4B, first edition,
second printing PDF, printed page388/file408, answer MPR112(b).
The physical copy has not been inspected; root acceptance is not asserted.

Use0 for a blank. In the first tableau after processing the blank set
{3,4}, the printed words at positions3,9,12 are1302,0213,3021.
They are inconsistent with the chosen word2103 at position6.
The required cyclic companions are1032,3210,0321 instead.
The same three incorrect words are copied into both later tableaux.
The second original branch, which chooses2130 at position6, is correct.

There is a direct probability contradiction. For the tested set{2,3},
the two rows with these blank positions both receive3 in position2.
This changes its winning probability from1/2 to7/12, leaving5/12
for position3. Later insertions cannot alter this pair's minimum.
After replacing the last blank in the first bottom tableau by4,
the two image values, in row order, are

```
23 32 34 12 13 14 41 41 21 34 24 42.
```

Position2 wins in rows1,3,4,5,6,10,11: seven of twelve, not six.
All twelve rows are distinct valid permutations, so this is a failure
of the claimed minwise example, independent of row ordering.

In the first, third and fourth tableaux on p388, replace the words
at positions3,9,12 as follows:

```
1302 -> 1032; 0213 -> 3210; 3021 -> 0321.
```

The exact bounded certificate checks every nonempty subset of every
printed tableau, all repaired versions and both final completions.
The repaired tableaux satisfy minwise independence and preserve the
specified cyclic orbits. The general construction remains correct;
its full proof, including periodic blank sets, is recorded separately.

The same nine entries appear in the original PDF and the author's
11September2019 Pre-Fascicle5A, printed page44/file50. All six local
official errata layers and their three TeX sources were assessed.
No applicable table correction was found. The published correction
to exercise112's truncation subscript is already incorporated in4B
and does not repair these tables.

Evidence: `sequential-mpr-ex112.md`, `verify_mpr112_tableaux.py`,
`results/sequential/mpr-112-tableaux-certificate.json`, the full
claim map and errata record, and original images `ref-407.png`,
`ref-408.png`, `fasc5a-50.png`. Only file408 is an error location.
