# V3-C0080 — Earlier methods do not all require linear retrieval time

Confirmed in volume 3, second edition, first printing (1998), printed
p.574 (file p.585), the comparison following the Nk/m hash-address
estimate (that is, N to the power k/m).

The text says that all other methods discussed in the section, except
Gustafson's, require order N retrieval steps, and concludes that
Rivest's method will therefore win for sufficiently large N. This
omits the section's own sublinear methods.

For example, p.566 gives O(sqrt(N)) partial-match retrieval in a
balanced two-dimensional k-d tree when one coordinate is specified.
This is the same two-key, one-unspecified-key situation for which
the present paragraph gives approximately sqrt(N) hash addresses.
It does not imply an asymptotic improvement over that earlier tree.

The compound sorted lists on p.567 are another exception. For a fixed
number of attributes, the relevant matching records form a contiguous
interval in one of the lists. Binary searches locate its ends in
O(log N) comparisons, followed by O(q) work to report q records. The
additional lists cost storage, but the blanket linear-time claim is
about retrieval and contains no storage restriction that excludes them.

Restrict the comparison to the appropriate scanning/intersection
methods and state the storage and data assumptions. This does not
invalidate Rivest's mapping itself.

Original pp.566, 567 and 574 inspected. No matching correction found
in the screened official layers or limited public searches; see
`sources/secondary-keys-errata-review.json`.
