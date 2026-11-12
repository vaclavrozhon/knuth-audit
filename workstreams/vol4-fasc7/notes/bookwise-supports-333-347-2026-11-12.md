# XCC supports and exercises 333–347

Read main printed 69–74, questions 333–347, and their complete answers
230–234 together. Original algorithm pages 232–233 and benchmark pages
73–74 were inspected to resolve notation and confirm findings. The printed
right-shift notation in the stage-stamp indices is c>>1, not c+1 as the
native text extraction suggests. The current corrections to SS's range,
the queue witness, example SIZE(24), trigger/fixit terminology and the
last example in 345 were applied.

The support matrices (126)–(127) and all alternative entries in 333 agree
with colored option compatibility. Purging 10 leaves 16 unsupported, and
purging 16 gives the four-option domain-consistent set. Removing 13 then
purges 05 and leaves 00,19, with the ages stated in 336. A remaining option
may contain a previously purified secondary item, explaining 335.

The marking test in 334 scans precisely the other nodes of a candidate
option; the skipped starting node belongs to an item known not to be in
the tested option. An uncolored secondary item receives the unmatched
marker -1. Wraparound clears all marks before restarting the stamp. The
FIFO queue permits reuse of the marks for an option's several holes.
The corrected four-option example in 338 really can queue an option
before another blocking call removes it.

Algorithms O and E preserve the support entries by moving each pair
between its support's trigger stack and its own option's fixit stack.
The primary first item lets O6 distinguish an inactive option by its sparse
position; a stale age greater than the current age is safely active after
restoration. Queue insertion marks the option with infinite age; a later
deactivation overwrites that marker, so E2 can discard its pending work.
E8 restores just the unprocessed fixits before purging. If an item would
be wiped out, O11 empties the queue and converts its fixits back to triggers
before the search restores sizes.

Algorithm A builds initial supports and delays propagation until its final
queue pass. Its primary-item loop has an actual missing end test when no
secondary items exist: F7-C0016. The official companion establish_dc scan
has the missing count bound. The initial age convention is the zero-initial
extra fields used by that program; no separate finding is inferred from
an unstated memory-allocation detail. After initial filtering, 342 removes
references to permanently purged options with the usual predecessor-link
update, preserving the rest of each list.

For O+, each rebuilt suffix is bucketed by deactivation age. A hint for
ages below c is usable only while its stage stamp matches SS[c>>1] and
the current age has reached c. Reentering that stage invalidates the old
hint. Newly encountered triggers sit before the old suffix; merging an
equal boundary avoids a redundant hint. Entries for permanently purged
options can be freed. Once hints are installed, opt_out is understood to
use the hint-aware routine; initial propagation uses the unhindered initial
scan. Stamp wraparound removes all hints before reassigning the live stage
codes, so their later reuse cannot validate a surviving old hint.

Algorithm J first deactivates the chosen option's items, then removes
incompatible options in descending sparse-list order. The chosen option
itself remains until J8, preventing a newly inactive primary list from being
wiped out in this blocking loop. Domain consistency supplies a compatible
option for every still-active primary item, so these calls cannot fail.
Zeroing the chosen primary sizes makes the chosen option inactive to O6;
its own trigger entries need no processing because its primary items are
now inactive. Algorithm S's size restoration and stage/level indices agree
with this protocol; forced stages require no separate saved alternatives.

The benchmark commentary was checked against its displayed tables with
the published corrections. F7-C0017 records a factor-60 claim inconsistent
with H's printed cost and node counts. Exact timing/census inputs and
performance claims in (130)–(131), 343 and 345 were not reproduced. The
mechanism and printed arguments of O+ were reviewed, but no exhaustive
implementation/state-space proof, solver port or large benchmark was added.
