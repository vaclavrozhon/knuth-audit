# MMIX book: publication review

Reviewed on 12 November 2026 against the third digital release (May 2023), SHA-256 `16f86d86839647a0c99be829a537a7516577704393ad8f95492ab42119905666`. All 22 baseline-confirmed book cards are retained within the scopes below. Their original proof notes, native witnesses and original page images were checked; previously successful computations were not rerun without a new reason.

## Source and novelty checks

The refreshed current and historical [Fascicle 1 errata](https://www-cs-faculty.stanford.edu/~knuth/all1f1.ps.gz), [current errata](https://www-cs-faculty.stanford.edu/~knuth/err1f1.ps.gz) and [TeX source](https://www-cs-faculty.stanford.edu/~knuth/err1f1.textxt) were screened at the cited pages. Their content is unchanged in the November 12 source refresh. Existing checks of related Volume 1 errata were also retained. None contains a matching correction. Known corrections on pages 97, 104, 111, 114, 116 and 118 were distinguished from the surviving claims.

The current [Stanford MMIXware page](https://www-cs-faculty.stanford.edu/~knuth/mmixware.html), [public bug index](https://mmix.cs.hm.edu/bugs/index.html), and relevant historical reports were checked. In particular, the [rI report](https://mmix.cs.hm.edu/bugs/bug_ri.html) concerns clock-cycle decrement and filtering, not the Delay reset invariant; the [IS report](https://mmix.cs.hm.edu/bugs/bug_is.html) concerns an undefined operand diagnostic, not repeated equal definitions. The SAVE/UNSAVE reports concern other failures. The independent [checksmix documentation](https://github.com/jac18281828/checksmix/blob/main/MMIX.md) contains instruction descriptions but no matching explicit report identified in the searched passages.

Targeted public searches combined MMIX with GetArgs, SAVE BNZ, golden ratio first 64 bits, ZSNZ no-op, StackRoom, NextChar NUL, MemFind, saddlepoint timing, Delay rI, GREG 255 and ropcode RESUME. Relevant instruction definitions were distinguished from reports of the specific book defects. No matching prior public report was found in the checked material. This is a bounded search result, not an assertion of absolute priority.

## Per-card decisions

- **MMIX-C0001:** The hexadecimal constant is the nearest rounded 64-bit value of phi inverse, not its first 64 fractional bits: the prefix ends in c15 and the printed constant in c16. The constant and its intended multiplication remain valid.

- **MMIX-C0002:** The preface contains the literal typo arent’t.

- **MMIX-C0003:** The blanket statement rY = $Y on a trip fails for NEG, whose Y operand is immediate. NEG $3,1,$2 with $2 the minimum signed octabyte trips with rY = 1, independently of $1.

- **MMIX-C0004:** The NextChar routine uses zero as an end-of-buffer sentinel, although the stated input convention accepts NUL as whitespace. An embedded NUL discards the unread suffix of the fetched line. Either track its length or exclude NUL explicitly.

- **MMIX-C0005:** Exercise 9 contains has been been enabled.

- **MMIX-C0006:** The jump-trace addresses advance by four bytes per instruction. The printed y1,y1+1 sequence uses the wrong address unit.

- **MMIX-C0007:** In the printed SAVE simulation the branch after incrementing s has the wrong polarity. With rG = 254, BNZ exits after the first global register; BZ is required at this test. This is a book-program error.

- **MMIX-C0008:** GetArgs masks the internal translated address x when computing bytes left in the chunk. It must mask the original virtual address z. At virtual offset #ff0 the printed code permits 4056 bytes instead of 16 and can write into allocation padding.

- **MMIX-C0009:** The MemFind timing paragraph interchanges the miss and allocation indicators. With U denoting a key miss and A a new allocation, their coefficients are (3mu+6v)U and (2mu+11v)A. The reported averages also violate A <= U if read with the printed labels; their empirical values were not recomputed.

- **MMIX-C0010:** The recursion simulation capacity argument compares a count of 4120-byte chunks with a byte capacity. The claimed 100^6065 guarantee does not follow. A corrected recurrence bound fits through depth 4640, but this is not a demonstrated maximum depth or a complete replacement theorem.

- **MMIX-C0011:** The claimed no-op opcode classification omits ZSNZ, CSZI and PUTI: ZSNZ $255,$255,$255, CSZI $255,$255,0 and PUTI rL,255 preserve state. The finding establishes these omissions, not a new exhaustive classification.

- **MMIX-C0012:** The GetReg cost uses a local-register indicator where the additional path also occurs for marginal registers. With rL = 2, rG = 32, k = 3 the marginal path costs 12v rather than 6v.

- **MMIX-C0013:** The cited PUSHJ path pushes three stack entries after promoting the marginal register. Its StackRoom count is 3+3+3+2 = 11, not 10. This establishes the stated path discrepancy, not a separately proved global worst case.

- **MMIX-C0014:** PutL shifts its operand left by three before comparing it. A value 2^61 wraps to zero and incorrectly changes rL = 1 to zero, whereas the instruction must leave rL unchanged. The primary C simulator compares the full value before shifting.

- **MMIX-C0015:** The BOD resuming,Install_Y branch reinstalls an ordinary Y operand during ropcode 1, which must use the saved rY/rZ operands. The recorded ADDU example produces 102 instead of 3. A complete repair also handles immediate-Y operations; changing this branch alone is insufficient.

- **MMIX-C0016:** Program P has 10037 and 2803 memory accesses in the two phases, not 10036 and 2804. The total 12840 and the printed operation counts are unchanged.

- **MMIX-C0017:** MMIXAL accepts a repeated global definition when both its value and type agree with the previous definition. Thus the book statement that every repeated global label is diagnosed is too strong. Both the 2013 and 2025 implementations allow X IS 1 twice.

- **MMIX-C0018:** Both saddlepoint timing answers omit costs. The first misses two units for the final unsuccessful predicted branch (constant 13, not 11). The second counts only phase-one memory accesses and omits phase-two costs of linear expected size on square arrays. The programs and the already applied 2012 branch correction remain valid.

- **MMIX-C0020:** Delay can loop forever under legal prompt resets of rI. With ref_time = 0 and every observed counter value in (0,2^63), its signed comparison always continues. The finite native trace illustrates the invariant; the infinite-loop claim follows from the repeating legal state schedule, not from a timeout. The known delay-to-delta correction is already applied.

- **MMIX-C0021:** The initial rG formula counts declarations instead of distinct allocated registers. Nonzero GREG declarations with equal values coalesce: two GREG 1 declarations both allocate register 254, giving rG = 254 rather than 253.

- **MMIX-C0022:** The answer explicitly extends local/global register equivalence to programs containing SAVE. SAVE sets rL to zero, so swapping a local register with a global register changes a subsequent read from 5 to 0 in the recorded witness. The original question excludes SAVE, but the separate extension in the answer does not.

- **MMIX-C0023:** The simulated RESUME rejects an original opcode RESUME even for ropcode 2, where that opcode is ignored. The recorded legal set-register example is rejected. MMIX-PIPE has the correct ordering; MMIX-SIM shares the book defect. This remains one finding, not a duplicate software card.

