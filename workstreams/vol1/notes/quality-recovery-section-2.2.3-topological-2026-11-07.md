# Recovery of §2.2.3: complete Algorithm/Program T and11,17–24

This block covers all remaining main text263–268, every step and
field of Algorithm/Program T, figures8–9, the exact time table and
input/output conventions, every part of11,17–24, and the complete
cycle diagnostic548–549. Original263–268,270–271,546–549 were viewed
directly. The full prior `topological-sort.md`, `cycle-example-output.md`,
root review and sequential review were read, together with the literal
TOPO/CYCLE_END/with_cycles code and the entire topological checker
range. Their proofs and completed executions are reused without rerun.
The finite-extension theorem and matrix16 are in the preceding orders
recovery; all13,25–28 remain separate.

## 1. Input, representations and every construction step

There are n numbered vertices and a finite sequence of m directed
edges j→k. Multiplicities are retained. A topological output is a
permutation satisfying every edge; it then satisfies every path by
transitivity of positions. Hence adding an edge already implied by
a path, such as9→8 via9→5→8, changes no valid output. Supplying any
generating subset of the strict relation is sufficient. A directed
cycle makes such an output impossible.

T1 zeroes the incoming counts and heads; N=n. After any input prefix,
T2–T3 maintain COUNT[k] equal to the number of prefix edges ending at k,
and TOP[j] the head of exactly the prefix edges starting at j, in
reverse input order. A fresh node stores SUC=k and NEXT=old TOP[j],
then becomes TOP[j]. Induction proves these statements, including
duplicate edges. Fresh allocation makes the edge lists disjoint and
each list acyclic. No edge node is later reused, so allocation can
simply advance through successive unused addresses. Returning nodes
to a free list is unnecessary for this one sorting operation.

For(18), figure8 has COUNT[1..9]=(0,1,1,1,2,2,1,2,0) and successor
lists respectively (3),(8),(7),(6),(8),(),(4,5),(6),(5,2).
These values account for all ten input edges exactly once. In
particular TOP7 starts with4, and TOP9 starts with5. Every arrow and
termination marker of the representation agrees with this list.

The X table permits direct access to a vertex's count/head by its
number; per-source linked edge lists permit constant-time insertion
despite arbitrary input order. Queue links hold vertex numbers, not
addresses; a link k refers to X+k. Once a count is no longer needed,
the same two bytes hold QLINK. Queue nodes are the existing vertices,
so queue operations allocate or free no storage. Symbolic names would
first require a dictionary from names to these indices; this is the
stated purpose of the Chapter6 pointer, not a claim that alphabetic
strings can themselves be used as array indices at constant cost.

## 2. Queue invariant, safe aliasing, termination and cycle criterion

At entry to T5 let U be the vertices not yet output and Q the vertices
in the current queue, in its linked order. The exact invariant is:

1. Already output vertices are distinct and each was output after all
   its predecessors. N=|U|.
2. Q is exactly the vertices of U with zero incoming degree in the
   induced remaining graph, each once. F is its first vertex or0;
   R is its last vertex when nonempty and QLINK[R]=0.
3. For each vertex in U outside Q, its COUNT field is its positive
   remaining indegree. For a queued/output vertex the field is QLINK,
   and is no longer asserted to contain its degree.
4. There is no remaining edge into a queued/output vertex whose count
   has been repurposed. Thus no future decrement can touch that link.

T4 initializes R=0 and QLINK[0]=0, scans every vertex once, and
appends precisely the initial zero counts. Appending changes only the
link of the previous tail, a vertex already scanned; it never corrupts
an unscanned count. The new tail's field is already zero. This proves
the invariant and the implicit tail terminator even when there are
no initial sources. The zero-vertex abstract input also gives F=0,N=0.

If F≠0, T5 outputs this zero-indegree vertex, decreases N and saves
its successor head in P. T6 traverses its finite edge list once and
decrements each target once per outgoing edge. During this traversal
the counts correspond to deleting the processed edge prefix; after
it they correspond to removing F altogether. A target enters the
queue exactly when its final remaining incoming edge is removed.
That count reaches zero once, so no duplicate queue insertion occurs.
No subsequent decrement can occur at that target: such an edge would
contradict its count having reached zero. Thus aliasing COUNT with
QLINK is safe, including when different input edges repeat the same
pair. The new tail again has its zero terminator automatically.

T7 advances F only after those appends. If the old queue consisted of
just F, appending writes QLINK[F], which T7 then follows. Otherwise
the old next vertex remains available. This restores the whole
invariant. If F=0 at T5, it outputs the terminating0 and goes to T8.
For N=0 all vertices have been output correctly. For N>0 every vertex
of U has a predecessor in U. Following predecessors for |U|+1 terms
repeats a vertex, giving a directed cycle. Thus T8 diagnoses exactly
the obstruction, not merely failure to find a convenient next vertex.

Every successful output decreases N; every traversal step advances
through an acyclic edge list. Initialization/input/scanning take
O(n+m), each vertex is queued/output once and each edge is traversed
once, giving total O(n+m) time and O(n+m) storage. These statements
also bound work on cyclic inputs, where only a prefix is output.
The explicit stream-consuming model itself needs Omega(m) input
operations and Omega(n) output operations on successful inputs; this
explains the main text's qualitative efficiency claim. No optimum
MIX constant or stronger computational-model lower bound is asserted.
Figure9 has exactly the control transfers just proved: T2/T3 input
loop, T4 then T5, T5 empty exit to T8, T6 edge loop, and T7 back to T5.

## 3. Program T: fields, addresses and all control groups

The stated machine domain is valid finite input with positive n and
enough disjoint memory for code, buffers, X[0..n], and m edge words.
Use a byte radix b≥64 and addresses0..3999. All vertices, counts≤m,
and node addresses are below4000, hence fit two bytes even for b=64.
The count and link fields are respectively2:3 and4:5, with sign and
byte1 unused in the diagram. Partial stores preserve the other field.
The known COUNT[j]→COUNT[k] correction in the equivalence paragraph
fixes its index notation, not a machine instruction.

rI6=N, rI5 is the input address or output-buffer offset, rI4=k,
rI3 is j during construction and R during sorting, rI2 is the last
allocated address during construction and P during traversal, and
rI1=F. The general algorithm's AVAIL extraction becomes incrementing
rI2, which initially equals X+n, so the first edge occupies X+n+1.
All such addresses remain representable under the memory premise.

Lines12–20 initiate and await the first tape block, load n from its
second word, zero X[n],...,X[0], set the last allocation address and
point rI5 at the first actual relation. The downward initialization
tests nonnegativity after decrement, so X[0] is included exactly once;
it supplies the initial dummy QLINK[0]=0 without an extra T4 store.

Lines21–27 read a first component. Positive goes to recording, zero
ends the input, and the negative boundary sentinel requests the next
block and resets the pointer. Lines28–38 load the target, increment
its count, allocate the next word, copy the old source head into NEXT,
store SUC and the new source head, then advance the input pointer by2.
This is exactly the construction invariant in §1. Input rewinding
at39 occurs after the input has been consumed and no later phase uses
the input unit.

Lines40–50 initialize output state and scan k=n,...,1. LDA/JAP tests
the still-valid count; zero values append to the queue by ST4 and
ENT3. Descending rather than ascending scanning is allowed by T4,
but changes which source is first. LD1 X(QLINK) then supplies F.

Lines51–59 wait for safe output-buffer access, store F, branch on
zero, advance the buffer offset and flush a full block when necessary,
then decrease N and save TOP[F]. Lines60–69 skip an empty successor
list or process each target: load SUC, decrement its count, append
when it reaches zero, and load NEXT. The count cannot go negative
under the invariant, so JAP distinguishes positive from exactly zero.
Lines70–71 follow QLINK[F] after all outgoing edges have been processed.
Lines72–74 flush the final block, rewind the output tape and halt with
N displayed. They implement both successful and cyclic exits.

No initial arbitrary register value is used before being overwritten
by these assignments. Mutable X and edge words lie beyond the program
and buffers. The memory premise is about the actual available region,
including any resident loader, not only the numerical inequality
n+m<4000. In the cycle extension an otherwise undefined NO receives
its implicit CON0 before X under MIXAL END rules11(f),13; saving n
there therefore does not alias X[0]. The checker expands exactly that
specified rule to avoid its assembler's forward-END-label limitation.

## 4. Complete tape and printer-boundary reasoning

Input records contain100 words, hence50 complete pairs. The first pair
is(0,n), and(0,0) terminates the sequence. Starting at BUFFER+2 and
advancing by2 always addresses the first component of a whole pair.
After the last pair in a block the pointer is BUFFER+100, where CON−1
is just outside the block overwritten by IN. Thus no legitimate
positive edge component is confused with the sentinel. Every IN is
followed by JBUS before any block word is read; a pair never straddles
two blocks. With m edges, the header and terminator require exactly
b_in=ceil((m+2)/50) input blocks, including boundary cases where the
terminator starts the next record. This use of b_in avoids confusing
record counts with the byte radix b above.

Output rI5 starts at−100 and identifies the next free word as
BUFFER+100+rI5. Each nonzero F increments it; when it becomes0 the
full100-word buffer is output and rI5 resets to−100. F=0 is stored
before testing it, so the last OUT always includes a terminator.
There are c=ceil((q+1)/100) records for q actual nonzero outputs,
including a separate final record when q is a multiple of100.
For successful sorting q=n. Old words after the first terminator in
the final record are outside the specified output stream.

The JBUS at51 precedes every write to this shared buffer and prevents
modification while a preceding OUT still reads it. Input is complete
before the same buffer is used for output. The final IOC on the output
unit waits for its outstanding OUT before beginning rewind; mechanical
rewind may finish after HLT. These are the given asynchronous device
semantics, not an assumption of zero transfer time. No double buffering
or overlap-dependent performance claim is made.

For the cycle extension, printer blocks are24 words. The title block
starting at LINE1 overlaps the later numeric block starting at LINE2,
so JBUS must precede changing VALUE; line99 does precisely that before
every STX, including the first number after the title. CHAR leaves
the index registers unchanged. For1≤k≤n<4000 its last five decimal
characters in rX contain all digits of k, with leading zeros. The
remaining blank words are justified by the explicit ordinary MIXAL
loading convention on printed151: unspecified memory is zero except
the loader area. The displayed output buffers are below that area.
The original151 was viewed directly; no uninitialized-memory objection
is being inferred from the omitted CON declarations. A last printer
operation may finish after HLT, with its source words left intact.

## 5. Every frequency and the exact time convention

For successful inputs with n≥1, let a be the number of initial sources,
b_in=ceil((m+2)/50), and c=ceil((n+1)/100). The frequency groups are:

| Program lines | Frequency and reason |
|---|---|
|12,14,15,19,20|once: input/initial state|
|16–18|n+1: X[n] through X[0]|
|21–22|m+b_in: m edges, b_in−1 sentinels, one terminator|
|23|b_in: all nonpositive first components|
|24,26–27|b_in−1: block refills|
|28–38|m: exactly one new edge node per relation|
|39–42,50|once: phase transition and initial F|
|43–44,47–48|n: each positive vertex index once|
|45–46|a: initial queue insertions|
|52–53|n+1: vertices and terminating zero|
|54–55,58–60,70–71|n: each nonzero output|
|56–57|c−1: full nonfinal output blocks|
|61–65,68–69|m: edge removals|
|66–67|n−a: vertices that become ready after initialization|
|72–74|once: final output, rewind, halt|

JBUS13,25,51 have device-dependent repetition counts and are excluded
from the time table. The final HLT is likewise excluded. The book's
“exclusive of input-output operations” convention still includes1u
for issuing each IN, OUT and IOC, while excluding device transfer and
waiting. Its algebra is exactly reproduced as follows; loads/stores
cost2u, ordinary enters/increments/decrements/jumps cost1u.

| Disjoint instruction group | Time/u |
|---|---|
|14–20 initialization, excluding IN|4n+9|
|All input issuance and21–38|21m+7b_in−2|
|39–42 including input rewind|4|
|43–48 initial source scan|5n+3a|
|50,52–73 sorting/output, excluding waits|11m+15n−3a+2c+5|

The sum is32m+24n+7b_in+2c+16. For example the last group includes
3(n−a) for later appends and11m for edge-processing instructions;
the apparent source dependence cancels. If instead every I/O opcode
is excluded entirely and HLT is included, the CPU sum is
32m+24n+6b_in+c+15. Adding b_in+c+2 issuance units and subtracting
the halt unit recovers the printed sum. The saved book-example
profile has CPU558 and four issues, giving558−1+4=561, equal to
32·10+24·9+7+2+16. Thus a difference in I/O accounting is not a new
constant-term error. Cyclic partial outputs and n=0 do not have the
advertised successful-positive-n frequencies; the abstract algorithm
still handles the empty set. Exercise22 expressly selects positive n.

## 6. Exercise11: all52 outputs with an exhaustive hand classification

Vertex6 must be last:4 and8 precede it, and every other vertex
precedes one of those. Before vertex7, vertices1 and3 must occur in
that order; only9 and then2 can intervene, since4 requires7,5 requires
7 and9, and8 requires2 and5. This gives the following disjoint cases.

* If9 is after7 and4 is before9, the prefix is forced to13749.
  The remaining2 and5 can occur in either order, then8,6. This gives
  13749(25+52)86, two outputs.
* If neither2 nor4 appears before both7 and9 have appeared, the first
  four entries are1,3,7,9 in any interleaving of the chain137 and9:
  1379,1397,1937,9137. The remaining4,2,5,8 have only2<8 and5<8.
  If8 is last among these, permute425 arbitrarily (six possibilities);
  if8 is next to last, the first two must be25 or52 and4 is last.
  These are exactly4258,4528,2458,5428,2548,5248,2584,5284.
  Appending6 gives4·8 outputs.
* Otherwise2 is before7, which also places9 before7. The four entries
  before7 are exactly an interleaving of13 and92:1392,1932,1923,
  9132,9123,9213. Then7 is forced, followed by an interleaving of4
  and58, namely458,548,584, then6. This gives6·3 outputs.

These cases exhaust the alternatives around7 and9; in the first
case nothing else is available before9, and in the third nothing else
can appear before7. Every listed suffix satisfies all remaining edges,
and distinct choices give distinct permutations. The total is
2+4·8+6·3=52, exactly answer11's complete expression546. The old
`all_orders` recursion independently chooses every current minimal
vertex: any valid output starts at such a vertex, and induction gives
all suffixes once. Its saved52-element set agrees with the printed
expression. That completed enumeration is accepted without rerun.

## 7. Exercises17–21: each operation and comparison

For17, ascending T4 initializes the queue(1,9). Removing1 appends3;
removing9 visits5 then2 and appends only2; removing3 appends7;
removing2 reduces8 but does not append it; removing7 visits4 then5
and appends both; removing4 reduces6; removing5 appends8; removing8
appends6. Thus the output is1932745860. Descending T4 initializes
(9,1): removing9 appends2, removing1 appends3, removing2 leaves8
positive, removing3 appends7, and the remaining actions are the same.
The result is9123745860, exactly Program T and answer17.

For18, each appended vertex becomes the successor of the previous
tail, and that particular predecessor link is never written again:
the tail variable advances permanently. QLINK[0] therefore points to
the first-ever enqueued vertex, and following links gives the complete
output sequence, ending in0. On an acyclic input this contains all n
vertices. On a cyclic input it contains only the output prefix; the
remaining COUNT fields are positive degrees, not further list links.

For19, take n=2 with the sole edge1→2. At T5 the queue contains only1.
After saving TOP1, an early F=QLINK[F] sets F=0. T6 appends2 after
the still-current tail1, but does not change F, so the next T5 falsely
terminates with N=1. Keeping T7 at the printed place avoids this.
A repaired early-pop version may set F to the new vertex whenever
an append sees F=0, in addition to maintaining R/links; that is the
extra empty-front test mentioned in the answer.

For20, initialize a stack by T=0 and, for every initial zero count k,
SLINK[k]=T,T=k. At each T5, output T and stop on0; otherwise decrement
N, save P=TOP[T], and pop T=SLINK[T] before traversing successors.
Whenever a successor's count reaches zero, push it with the same
two assignments. The set of ready vertices and count invariant are
unchanged; LIFO instead of FIFO only chooses a different permissible
next ready vertex. There is no T7. Every stack link is written only
after its count becomes zero, each node is pushed/popped once, and
cost/storage remain O(n+m). One head replaces front/rear variables;
these stack links generally do not retain the output chain of18.
No exact MIX speed advantage is asserted without code and a cost sum.

For21, r copies of j→k increment the count r times and are removed
r times when j is output. Thus zero is reached at the correct event;
extra copies add linear storage and processing but change no validity
condition. A self-loop j→j keeps a positive incoming count until j
is output, preventing it from becoming ready in the first place.
The remaining-cycle diagnostic correctly detects it. Redundant
transitively implied edges are harmless by §1 for the same reason.

## 8. Exercise22: a concrete complete validation design

The requested suggestions(a)–(c) can be implemented without allowing
an invalid word to become an address. Fix the actual upper exclusive
limit L of the table/pool, below resident code and at most4000.

1. Read a complete header block, check the first word equals0, and
   load the second into the full accumulator before any index load.
   Require a positive integer n with X+n<L. Only after that check
   copy n to rI6 and initialize X[0..n]. Signed zero is not positive.
2. Track the pair position in the100-word buffer explicitly. Refill
   only at its actual boundary, awaiting completion. Read both words
   into full-word temporaries before narrowing to an index register.
   The only terminating pair is(0,0). Any other zero, negative value,
   or value above n is an input error. This prevents a negative in-band
   word from impersonating the physical−1 boundary sentinel.
3. Before modifying a count or source head, require next_pool<L. Then
   store the edge and advance next_pool. Otherwise report insufficient
   memory and stop. Because at most L−X−n−1 edges fit, all counts
   remain below4000 and their two-byte fields cannot overflow.

Each error exit occurs before the first table access using its invalid
quantity. Full-word comparisons avoid undefined oversized LDi loads.
The header and pool guards protect code, buffers and table boundaries;
validating only the low two bytes would not. Rejecting a malformed
terminator also avoids silently ignoring a nonzero second component.
A finite readable tape must contain a complete terminator; unavailable
or incomplete records require the surrounding I/O system's read-error
exit. A guard on complete valid pairs reaches the pool limit after
finitely many pairs even if a terminator is missing. Device completion
and reporting of physical read failures remain I/O assumptions, not
a mathematical claim that software can repair failed hardware.
Valid duplicates are accepted; a self-loop can be rejected immediately
or left for the already-proved cycle diagnostic. This realizes every
printed protection(a)–(c) and specifies the missing narrowing order.

## 9. Exercise23: all diagnostic steps and optional forward output

After saving P=TOP[F] in T5, add TOP[F]=Lambda. This removes the head
of an output vertex while leaving P available for T6. The uncancelled
edges of every vertex still awaiting output retain their heads.
When T8 finds N>0, every such edge ends at another remaining vertex:
an edge into an already output vertex would contradict its earlier
zero remaining indegree. Every remaining vertex has at least one
incoming edge from the remaining set U.

Reset QLINK[1..n]=0. T9 saves each TOP head in P and clears TOP[k]
before T10 scans that list, assigning QLINK[SUC(P)]=k at each edge.
Clearing one source head does not alter its already saved list or
any other source's disjoint list. After all sources, TOP is all zero
and QLINK on U is a function p:U→U selecting one actual predecessor
of each vertex. The other QLINK values remain0. T11's scan therefore
finds a nonzero entry within1..n.

T12 marks the current vertex and follows p. Before the first repeated
vertex it visits distinct vertices of finite U, so within |U| moves
it reaches a mark. If c is that first repeat, the segment from its
previous occurrence to the repeat is a simple cycle; subsequent
iteration of p starting at c stays on that cycle. T13 prints a vertex,
clears its mark, and advances. Every cycle mark was set by T12 and
none outside the completed cycle interferes. Exactly on returning
to c does it encounter the first cleared mark. T14 then prints c
again. Thus the output contains each cycle vertex once followed by
the initial vertex, with each step an actual input edge in reverse.
For a self-loop it prints j,j. The construction scans O(n+m) data and
the marking/printing needs O(n) further operations and existing fields.

For the suggested forward output, reverse p only on the identified
cycle before T13. Set prev=c,cur=p(c); while cur≠c save next=p(cur),
set p(cur)=prev, and advance prev=cur,cur=next; finally set p(c)=prev.
The usual reversed-prefix invariant applies until the finite cycle
returns to c. Each new link is the actual forward successor, all
marks remain, and T13–T14 now print forward. A one-vertex cycle
performs no loop iteration and remains valid. This supplies the
exact adaptation of the linear-list reversal hinted by the answer.

## 10. Exercise24: every MIX diagnostic group and C0040's exact scope

PRINTER=18 specifies the24-word device; ST6 NO after loading n preserves
the original size, and STZ X,1(TOP) after saving its head implements
the added T5 action. At74, J6Z DONE avoids all diagnostics if the main
sort succeeded. Otherwise75 prints the title,76–79 zero QLINK over
the full original vertex set, and80 reloads n for the source scan.

Lines81–89 save each TOP, clear it, and traverse its entire saved edge
list. LD1 SUC and ST6 QLINK store the current source as predecessor;
LD2 NEXT/J2P traverse the finite list. DEC6/J6P visits sources n,...,1
and leaves rI6=0. Lines90–92 increment before testing, so their first
candidate is1; some nonzero QLINK exists within n by §9, preventing
any out-of-range read. Lines93–96 use TOP[k]=k, a positive mark,
instead of1; zero/nonzero tests are equivalent and rI1 holds the mark
of the newly reached vertex.

Lines97–106 print the current k by ENTA,CHAR,JBUS,STX,OUT, then test
the saved rI1 mark. These operations preserve rI1. If the mark is
zero, the repeated initial vertex has just been printed and DONE is
correct. Otherwise the code clears TOP[k], follows QLINK and loads
the next mark before repeating. This merges T13 and T14 without
losing the final repeated vertex. The data-layout/overlapping-output
and implicit NO rules are covered in §§3–4. All paths implement the
general diagnostic, including success, a tail leading into a cycle,
multiple possible cycles, and a single self-loop.

The specific note549 remains the existing confirmed C0040, not a new
finding. Add9→1 and6→9 to(18). All nine counts are now positive,
so the main program outputs only0 and preserves every successor list.
The lists are(3),(8),(7),(6),(8),(9),(4,5),(6),(1,5,2).
Descending source scan overwrites each chosen predecessor with the
smallest source, giving QLINK[1..9]=(9,9,1,7,7,4,3,2,6).
The first candidate is1, and following these links is
1,9,6,4,7,3,1. Thus the program prints precisely that cycle.
Changing the source scan to ascending would select the largest
predecessors, follow1,9,6,8,5,9 and print9,6,8,5,9 as in the note.
Both are valid cycles; only the prediction of this printed program's
particular output is wrong. Input-list permutation cannot repair the
prediction because a given source always stores the same predecessor
value regardless of its internal successor order.

## 11. Saved execution evidence, historical scope and disposition

The old checker has56 topological input cases, each with both basic
and diagnostic programs, radix64/100 and device delay0/97:448 runs.
All448 saved profile records were read structurally and have exactly
that Cartesian coverage, with no missing/duplicate dimensions. The
180 successful basic-program profiles all satisfy the exact time
identity above. Cases include input record boundaries, output lengths
99/100/101 and199/200/201, duplicate edges near input-block boundaries,
self-loops, an isolated cycle, a cycle with a tail, and24 fixed-seed
graphs. Output, edge precedence, retained QLINK chains, residual-cycle
conditions and printed cycle edges are checked by the old validator.
The4494 total assertions in its file also include primitives and a
loader; they are not4494 topological runs. No program execution or
enumeration was restarted in this recovery. Reading and reconciling
the saved profiles is a metadata/evidence check.

The complete topological checker code and its literal programs were
compared with the originals. Its local tape extension models100-word records,
busy ownership and IOC0 rewind, not arbitrary tape seek operations.
The END expansion is the prescribed MIXAL expansion, not a change to
the algorithm. Finite cases supplement, rather than replace, the
general invariants and cost derivation in this note.

All four errata layers and current TeX were searched by the complete
263–271/546–549 range, algorithm/source names and the two exact cycle
outputs. Known corrections cover terminology264–265, the slight
implementation differences266, COUNT[k], QLINK[F] in a comment,
the CHAR wording alpha→alphameric549, the journal title, and the2021
replacement of the future cross-reference. None corrects C0040's
predicted sequence. Adjacent13 corrections are retained as navigation
but do not close that separately pending exercise.

The corrected future pointer to7.2.1.2 concerns generating all
topological orders, as directly verified in the original4A p342.
That establishes the cross-reference's subject; it does not audit
4A's algorithms here. The superseded promise of an “even better”
algorithm in7.4.1 is a known replaced statement. Kahn1962's full
article remains inaccessible in the recorded primary-source attempts;
the specific absence of queue links and absolute priority are now
explicit bibliography skips under the user's permission. The primary
metadata's author/journal/year/pages remain checked, and the complete
mathematics above is independent of that attribution. Szpilrajn's
theorem/source and priority limit are covered by the preceding block.

This closes all main-text claims of2.2.3 and all11,17–24 to the stated
proof standard, retaining C0040 and the explicit bibliography skips.
It creates no new finding or mathematical gap. The section's complete
exercise recovery still awaits13 and25–28.
