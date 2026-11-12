# V3-C0041 — The six-key tree is requested one level too deep

Confirmed, low. Volume 3, second edition, first printing (1998),
exercise 5.3.1-24, printed p.196 / file p.207.

The exercise requests a sorting tree for six elements with all leaves
at levels 10 and 11. The intended levels are 9 and 10. The root is
explicitly on level 0 in Fig.34, so this is not a change of convention.
The main discussion on p.193 correctly describes the target procedure
as using nine or ten comparisons; answer 24 on p.656 constructs that
procedure.

There is also a direct obstruction to the requested levels under the
section's convention of no redundant comparisons. Such a sorting tree
has exactly `6! = 720` leaves (p.182). A full binary tree whose shallowest
leaf is at depth 10 has at least `2^10 = 1024` leaves. Equivalently,
720 leaves at depths at least 10 have Kraft sum at most 720/1024<1.

For the corrected depths, the minimum-path-length tree has 304 leaves
at depth 9 and 416 at depth 10; its external path length is 6896, in
agreement with the table on p.193. Change “10 and 11” to “9 and 10”.

Original pages 181–182, 193, 196 and 656 were inspected. Saved evidence
is `images/bookwise-p196.png` and `images/bookwise-p656.png`. No matching
change was found in the five errata layers screened in
`sources/minimum-sorting-errata-review.json` or the targeted public
searches. Absolute priority and later physical printings remain
unverified. No enumeration or computer search was needed.
