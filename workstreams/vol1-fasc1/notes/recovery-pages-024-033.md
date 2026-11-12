# Recovery: complete scope of file pages 24–33 and both endpapers

2026-11-06. This is a reconciliation of every paragraph, table and exercise
on printed pages 16–25, not a sample of the old inventory. Original page 20,
page 21 and both endpaper images were inspected; native text was read for
all ten consecutive pages and for the corresponding answers on pages 94–95.
The earlier notes remain the proofs cited below, only within their actual
domains. In particular, accepted SAVE/UNSAVE and RESUME counterexamples were
not rerun or replaced by new examples.

## File 24 / page 16

The three continued probable-branch conditions are respectively nonzero,
nonpositive and even. The truth predicates in V0044 and the branch proof
in V0064 cover every 64-bit pattern. Expected costs are `1+2p` for B and
`3−2p` for PB, so PB is preferable exactly when `p>1/2`; equality has equal
cost. The prose about anticipation motivates this stipulated model and is
not a quantitative claim about every processor.

For V0066 the precise logical PUSH/POP proof is
`independent-arguments-052-065.md`, V0121–V0123. Its permitted states have
`0≤L≤G≤255` and `32≤G`. Local, marginal and global intervals partition
all 256 names. A source in `[L,G)` is zero; writing such a name k first
extends L to k+1≤G. A push changes the local-frame origin, leaves globals
unchanged, and records the hole needed by the inverse pop. The prose here
explicitly says “roughly speaking”; the global-X and short-local-frame
cases are those in the cited complete proof, not the informal renaming
formula applied outside its domain. Both PUSHJ and PUSHGO set rJ to the
next tetrabyte; POP's unsigned YZ displacement is exactly `4*YZ`.

For V0067 use the already accepted valid-image inverse proof in
`exercises-1.4.3-001-014.md`, exercises 10–12, with C0007's correction to
the book implementation. The image includes all local and global values,
the old L marker, the named special values and the packed G/A header.
SAVE's destination is global and therefore survives L←0; UNSAVE follows
the image address and restores the old L and values. The proof includes
L=0, G=255, and wrapped physical-ring positions. This page promises an
image made by SAVE, not arbitrary malformed UNSAVE input. No proof of
malformed contexts is being imported from that valid-image result.

All substantive claims on this page consequently have matching arguments.
The rO/rS sentence continuing onto file 25 uses the same ring invariant.

## File 25 / page 17

V0068's printed architectural definitions are now completely reconciled.
The primary `mmix-doc-20131017.w`, system-instruction sections 1780–1980
and LDVTS section 2980–3008, was read directly:

* LDUNC and STUNC have LDO/STO's value and addressing rules. Their cache
  hints do not change that value specification.
* X is an unsigned byte; inclusive addresses A through A+X describe
  X+1 bytes, 1–256, with the machine's modular address convention.
  PRELD/PREGO announce possible future data/instruction accesses. PREST
  promises that the specified bytes will be overwritten before being read,
  permitting old contents to be discarded. It is not a data-write algorithm.
* Ordinary SYNCD makes prior stores visible in physical memory. Ordinary
  SYNCID establishes instruction visibility after code writes; the documented
  implementation may invalidate or update instruction-cache state. In the
  operating system's negative address domain the specified eviction rules
  differ, so an ordinary-user proof is not extended to that domain.
* SYNC 0 drains earlier work; 1 orders stores, 2 orders loads, and 3 orders
  both. The additional OS operations 4–7 do not contradict this book's
  ordinary-user list 0–3. They are outside the stated ordinary-user domain.
* CSWAP reads one old octabyte m. If m=rP, it writes old X and returns X=1;
  otherwise memory is unchanged, rP←m, X←0. Equality and inequality are
  exhaustive and disjoint. The destination and source register alias cases
  use the old operands. Indivisibility is an explicit architectural premise,
  not inferred from these sequential assignments.
* LDVTS is privileged. For its translation-cache key, the result encodes
  presence in the instruction/data caches as 0, 1, 2 or 3. A zero permission
  field removes matching entries; otherwise the documented permission
  update applies. This records the referenced contract, not the correctness
  of a physical translation-cache implementation.

There is no remaining proof obligation for this page's definitions. It does
not print a cache implementation or assert a universal hardware-realization
theorem. The simple simulator expressly has no caches, so its hint no-ops
are not used as evidence for physical coherence. A hypothetical cache design
would be a new task, not a reason to keep these matched definitions partial.
V0068 and file 25 are therefore closed at the printed scope.

## File 26 / page 18

V0069's register-layout argument covers all eight event names and bit values,
their eight enable bits, all four rounding modes, the 46 reserved zero bits,
the nine handler entry addresses, and leftmost-priority selection. This is
the architectural rule in `mmix-doc`, lines 1979–2027. It is not a claim
that every arithmetic operation sets all its flags correctly; those leaves
remain in `fp-verification-items.json`. In particular, enabled underflow
and handler-modified results are not covered by disabled-trip packing proofs.

V0070 was temporarily reopened when its former evidence did not explicitly
map the entire paragraph. The clause-by-clause disposition is now complete:
The actual direct trip transition in `mmix-sim`, lines 2594–2608, sets
rW to the established successor, rX's high half to #80000000 and low half
to the instruction, saves $255 into rB, moves rJ into $255, and selects
16k for the highest-priority enabled event (0 for TRIP). Thus the fixed
register transfers and the direct TRIP case have a complete local argument.
The existing C0003 proof gives the exact immediate-Y exception for NEG.

The register-input sentence is a universal claim and is **false**, as
already proved by C0003's legal NEG witness. That counterexample is a
complete disproof of the printed universal statement; it need not classify
every other way that the sentence could fail. The architecture's general
interrupt discussion (`mmix-doc` 2090–2170) allows internal instructions,
partially completed operations and implementation-defined captured operands
outside the ordinary binary case. A replacement universal classification
has not been proved, and no such replacement is claimed here. The verdict
on the actual printed sentence, together with the separately proved fixed
transfers, does close V0070 as argument_recorded with finding C0003. That
status records coverage of a refuted claim, not correctness of its wording.

The TRAP paragraph matches the architectural renaming to
rBB/rWW/rXX/rYY/rZZ and destination rT. This paragraph does not publish an
OS handler or claim its complete correctness. Extra mask/nesting contracts
are documented externally and do not create an unprinted implementation
obligation on this page. File 26 is argument-complete, with its existing
book finding preserved.

## File 27 / page 19

V0071's printed contracts are completely reconciled. Opcode 00 with XYZ=0
is exactly tetrabyte 00000000.
The primary contract makes that TRAP terminate a user process. A nonzero
bit of rK&rQ is exactly an enabled pending request; the documented dynamic
trap destination is rTT, whereas explicit TRAP uses rT. For RESUME 0,
negative rX selects rW; ropcode 0 executes its stored instruction at rW−4,
excluding RESUME itself. These branches match the already accepted analysis.
The full primary RESUME definition, `mmix-doc` 2342–2444, explicitly states
these two branches, the prohibition of inserting RESUME, and the existence
of further ropcodes described there. That is exactly what this page asserts;
it does not print their implementation. The general implementation and a
complete correction of C0015 remain the actual obligations of V0175 and
exercise 1.4.3′–14. They were not repeated and are not closed by this
architectural-definition comparison. V0071 itself is argument_recorded.

V0072 is a complete ordinary-user invariant proof. All 32 codes are readable
with GET. PUT's zero Y field and code range are instruction-format conditions.
For rG, 32≤newG≤255 and newG≥L preserve the register partition; for rL,
newL=min(oldL,unsigned operand) cannot enlarge it; for rA, value≤#3ffff
is precisely the active 18-bit domain. Codes 8–18 are unavailable to an
ordinary user. `mmix-doc` 2681–2714 distinguishes permanently read-only
9–11 from OS-writable 8 and 12–18; the book's user restriction is therefore
not being generalized to privileged software. C0014's already accepted
book-implementation counterexample is separate from this correct contract.

V0073 covers every opcode name and placement, now by the complete table
certificate below, in addition to the five printed ADD/ADDI/ORL/JMP/JMPB
examples. The descriptions of rC, rF and rI match primary definitions:
rC supplies a physical continuation page for stack overflow, rF records a
physical memory-fault location, and rI decreases per clock and requests an
interrupt on reaching zero (`mmix-doc` 2489ff, 2944ff, 3148ff). The book is
defining these roles, not presenting hardware detection/recovery algorithms.
All printed claims on file 27 are now covered at that scope.

## File 28 / page 20

All 256 opcode cells and their declared costs are covered below. The prose
continuing the register list has two further scopes. rU's selected-opcode
counter and rV's address-translation configuration match their normative
definitions. They do not claim correctness of an arbitrary OS implementation.

**New R0004, partial:** the phrase that rN “gives each MMIX machine a unique
number” has no unconditional injectivity proof. The primary definition
(`mmix-doc` 2571ff) uses version/modifier bytes and creation time in seconds,
and calls the identification essentially unique. A policy allocating
distinct modifier/time combinations would make the identification injective,
but that policy is not supplied by the text or the former argument. This is
a scope limitation, not a newly reported error; the exact intended uniqueness
domain or manufacturing premise is still needed.

**New R0002, argument recorded:** GETA stores the current instruction
address plus 4d modulo 2^64, where the forward form has d=YZ and the backward
form d=YZ−2^16. The full allowed displacement range and wrapping follow from
0≤YZ<2^16. GETA $0,@ selects forward d=0 and stores its own address.
The primary definition is `mmix-doc` 1005–1011. In the simulator the relative
address conversion (1731–1736) sets z to exactly that value and GETA/GETAB
(1939–1940) copy z to the destination. Source and destination register aliasing
cannot affect this constant relative address. A marginal destination uses
the already proved register-extension rule. Declared cost is 1υ.

The explicit rN uniqueness scope, R0004, prevents a whole-page green status.
No hypothetical physical-realization obligation is added to that gap.

## File 29 / page 21

V0074 now has a row-complete external comparison. The table lists each code
0–31 exactly once, with this order by numeric code (primary enum and
`special_name` array at `mmix-sim` 1312–1320):

| Code | Name | Saved | Ordinary PUT |
|---:|:---|:---:|:---:|
| 0 | rB | yes | yes |
| 1 | rD | yes | yes |
| 2 | rE | yes | yes |
| 3 | rH | yes | yes |
| 4 | rJ | yes | yes |
| 5 | rM | yes | yes |
| 6 | rR | yes | yes |
| 7 | rBB | no | yes |
| 8 | rC | no | no |
| 9 | rN | no | no |
| 10 | rO | no | no |
| 11 | rS | no | no |
| 12 | rI | no | no |
| 13 | rT | no | no |
| 14 | rTT | no | no |
| 15 | rK | no | no |
| 16 | rQ | no | no |
| 17 | rU | no | no |
| 18 | rV | no | no |
| 19 | rG | yes | yes |
| 20 | rL | yes | yes |
| 21 | rA | yes | yes |
| 22 | rF | no | yes |
| 23 | rP | yes | yes |
| 24 | rW | yes | yes |
| 25 | rX | yes | yes |
| 26 | rY | yes | yes |
| 27 | rZ | yes | yes |
| 28 | rWW | no | yes |
| 29 | rXX | no | yes |
| 30 | rYY | no | yes |
| 31 | rZZ | no | yes |

The 15 saved special registers are codes 0–6, 19–21 and 23–27. The accepted
SAVE proof supplies seven ordinary saved values plus five trip/prediction
values, packed G/A and the L marker, hence all fifteen and no extra saved
table entry. PUT is allowed at exactly the 21 codes outside 8–18, subject
to the value restrictions just proved. Register names/descriptions are the
normative roles, not assertions about fault-repair or manufacturing success.

**New R0003, argument recorded:** SWYM's flags are zero, its branch is
`case SWYM: break`, and its declared cost is 1υ. Thus all 2^24 XYZ fields
are ignored and no instruction-specific register or memory effect occurs.
Normal instruction fetching, PC advance and counters still occur, as for
any no-op. This is the precise meaning of the prose, not the false assertion
that the entire machine state stays identical. “The last” means the last
instruction discussed here; its numeric opcode is #fd and the table openly
places GET and TRIP after it. The lubrication/swimming sentences are jokes,
not a physical maintenance specification. See `mmix-doc` 3166–3185.

The timing introduction states that implementation choices affect running
time; no numerical hardware estimate is made on this page. All substantive
claims on this page have matching arguments.

## Files 30–31 / pages 22–23

V0075's declared cost model is completely covered by the certificate below.
Each contribution is a formal linear combination of μ and υ; addition gives
35μ+1000υ when the execution has those counts. B/PB costs are 1υ when the
prediction is right and 3υ otherwise. Integer MUL/DIV cost 10υ/60υ; the
floating instruction table gives the stated 4υ/40υ classes with listed
exceptions. LDSF and STSF specifically cost μ+υ, not 4υ.

V0076 remains partial and covers both pages, including the continuation:
the historical rise of μ/υ, cache performance examples, simultaneous issue,
precise fidelity and full configuration scope of the meta-simulator, and
the comparisons with commercial processors at the turn of the millennium.
Given a pipeline that issues independently and has 60-cycle divide latency,
60 independent cycles can hide the wait; that conditional fact does not
prove every physical pipeline has those properties. No old benchmark is
restarted. The original Kernighan/Van Wyk quotation is explicitly skipped.
The five commercial-machine bullets concern alignment, quotient/remainder
and product/shift/divide support, FINT/FREM speed, MOR/MXOR availability,
register count and stack flexibility. They have not been proved from a
complete specified collection of contemporary processor manuals. Claims of
meta-simulator fidelity also need its implementation and model assumptions.

## Files 32–33 / pages 24–25: all exercise subparts

V0077's summary reuses the 64-bit unit, three format and 256-code arguments;
RISC and programmer-friendly are descriptive labels. The Wordsworth source
quotation on file 32 is explicitly unverified bibliography. The description
of simple formats does not prove the correctness of all opcode implementations.

Every exercise is matched to its own proof in
`exercises-1.3.1-001-024.md`, rather than to V0077:

* 1: full binary/hexadecimal expansion of 2009. 2(a,b): parity of all twelve
  letters, separately for digit values and ASCII encodings.
* 3: the proposed two-bit nomenclature and its dimensional consistency;
  Purdy attribution and the byte-history citation in the answer remain
  bibliographic exclusions. 4: each SI power, name and symbol, with the
  2022 R/Q extension and the known 2023 erratum, which is not our finding.
* 5: both implications and uniqueness for every nonempty n-bit string.
  6: bitwise complement identity, carry and the unique signed-minimum
  negation overflow; n-bit modular negation remains valid there.
* 7: both proposed signed LDHT/STHT formulas, including floor for negatives.
  8: both mixed fixed-point inputs and the general sum of radix exponents.
* 9: quotient identity, zero divisor, alias cases X=Y/X=Z, and signed
  minimum divided by −1. 10: proof that this is the only division overflow.
* 11(a): all low-product bits by congruence. 11(b): all sign/zero/equal
  operand classes, under the question's explicit rD=0 assumption.
* 12: carry criterion plus each alias case and preserved scratch inputs.
  13: sign/overflow predicate and scratch liveness. 14: both subtraction
  sign cases and the equivalent addition predicate; no use of uncomputed X.
* 15: both signed corrections to the high half and the 128-bit range bound.
  16: necessary and sufficient sign-extension test using that corrected
  high half, not raw unsigned rH.
* 17–18: exact reciprocal constants, full stated dividend ranges, fractional
  error bounds and equivalence of high multiply then shift to one division.
  The input is read by MULU before scratch $0 is overwritten.
* 19: symbolic z=7 counterexample, complete maximum-residue criterion,
  restricted half-range and corrected reciprocal formula; the remaining
  finite census is closed below. The cited Granlund/Montgomery paper is
  not asserted verified. The formula using addition preserves its 65th bit;
  it is not silently replaced by one wrapping ADDU.
* 20: two 4ADDU steps produce 25y; intermediate 5y fits whenever 25y fits,
  with declared 2υ versus MUL's 10υ. 21: every shift count≥64 and all four
  operations, including sign extension and nonzero SL overflow.
* 22: whole stated failing families for subtraction-based comparison and
  both guaranteed-safe domains, plus correct CMP/BN replacement. 23: all
  three CMP results and BNP's ≤ predicate. 24: each indicator bit proves
  ANDN equals set difference; intersection/union follow from AND/OR.

Thus file 33 has complete mathematical coverage. File 32 retains the
specified quotation/history exclusions. Answer file 103 also contains
exercises 25–31, which are not closed merely by reading that page here.

## Answer 19: complete finite census

Let B=2^64, 2^e<z<2^(e+1), D=B*2^e, r=D mod z, a=ceil(D/z).
For the odd z≥3 counted here, 0<r<z. The error is
`δ=(z−r)y/(Dz)`, with `0≤δ<2/z` for 0≤y<B. Consequently, writing
y=qz+s with 0≤s<z, crossing an integer boundary requires s=z−1: if
s≤z−2 then s/z+δ<1. In the sole possible residue class z−1, crossing
occurs exactly when `(z−r)y≥D`. The largest permitted such dividend is
`y*=B−1−(B mod z)`; it is nonnegative for every census divisor and y*+z≥B.
The left side increases with y, so **the formula fails for some 64-bit
dividend iff `(z−r)y*≥D`**. This establishes sufficiency as well as necessity
for every dividend, rather than testing an unexplained chosen example.

`verify_reciprocal_divisor_census.py` applies that proved integer criterion
once to each of the 499 odd divisors 3,5,…,999. Its saved certificate
`results/reciprocal-divisor-census.json` contains every z, e, r, multiplier,
witness, inequality margin and both exact quotients. Divisor 1 is exact
and contributes no failure. There are exactly **189 failures**. The first
sixteen, 7,21,23,25,29,31,39,47,49,53,55,61,63,71,81,89, exactly match the
complete finite prefix printed in the answer. This was one sub-second
integer calculation at nice 15, not a search over 2^64 dividends.

## Every opcode cell and both ASCII endpapers

`verify_opcode_tables.py` expands each table independently: 256 unique
opcodes on file 28, 144 and 145, including both I and B variants and the
SAVE/UNSAVE pair. The primary simulator supplies an independently ordered
256-entry name/mems/oops table. All names, opcode numbers and μ/υ cost
coefficients agree. For each of the 32 B/PB opcodes, both taken and untaken
outcomes are separately reconciled: the dispatcher charges base 1υ plus
2υ exactly when actual direction differs from the B/PB prediction. This
is precisely υ+π or 3υ−π with π=2υ if taken, 0 otherwise. The saved
`results/opcode-table-reconciliation.json` includes all 768 expanded cells,
all 192 branch-outcome checks and source hashes; there are no differences.

The original images on files 144 and 145 show the same ASCII table: codes
#20–#7e are the 95 printing positions and #7f has the nonprinting DEL
placeholder. `verify_ascii_endpapers.py` compares every cell independently
with the already saved primary Unicode Consortium Latin-1 mapping.
`results/ascii-endpaper-reconciliation.json` records all 192 positions,
names and source hashes. Both tables agree. At #27 and #60 the typeface's
apostrophe and grave glyphs extract as curly quotes; this is not a claim
that U+2019/U+2018 have those ASCII byte codes. The original positions and
identities are unambiguous and were visually inspected.

V0183 can therefore change from partial to argument_recorded in its full
table scope. Full IEEE arithmetic remains V0054/V0055; an opcode table
asserts names, numbers and stipulated costs, not implementation correctness.
The two complete endpaper pages are reconciled now because they are exact
table duplicates, without moving the sequential cursor past file 34.

## Coverage after this block

Files 24–33 and 144–145 add twelve completely mapped pages. Newly complete
argument pages are 24–27,29,33,144,145; files 28,30–31 remain partial and
32 retains factual exclusions. V0070 was temporarily reopened and then
resolved clause by clause, including its already established disproof C0003;
V0068/V0071 are closed as the architectural definitions actually printed,
without demanding an unprinted hardware implementation. V0183 was closed
in its precise table scope, and R0002/R0003/R0004 expose unmapped prose.
No new book or program finding is claimed. The sequential next page is
file 34 / printed 26; the older FP obligations remain open concurrently.
