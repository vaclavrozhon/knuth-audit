# MMIX accompanying programs: publication review

Reviewed on 12 November 2026. All nine baseline-confirmed software cards are retained as program findings, without marking the correct book definitions as errors. Their proof notes and bounded reproduction results were read, and the relevant original CWEB source branches were checked directly. The affected code remains in both the frozen 17 October 2013 and corrected 20 June 2025 distributions. This is not a review of an unspecified physical printing of MMIXware.

## Prior publication checks

Checked the [current distribution and corrections](https://www-cs-faculty.stanford.edu/~knuth/mmixware.html), [historical MMIXware errata](https://www-cs-faculty.stanford.edu/~knuth/mmixware-errata.html), [maintainer bug index](https://mmix.cs.hm.edu/bugs/index.html), [2015 rounding report](https://mmix.cs.hm.edu/bugs/bug_rounding.html), and the already recorded warning patches and Fascicle 1 layers. The historical changes for epsilon comparisons, exponent scanning, EOF initialization, rounding-mode installation and undefined IS operands are different from these findings. The 2015 report concerns fplus alignment, not fepscomp, directed overflow, integerization or square-root NaN dispatch.

Fresh public searches used the specific routine/instruction names with bug/error and the pertinent behavior: fepscomp, froot negative NaN, FINT inexact, overflow ROUND_OFF, mmix_fwrite, Fgetws EOF, Ftell 32-bit, MMIXAL relative #8000000000000000, and scan_const 769. Primary source documentation was checked, including [floating arithmetic](https://mmix.cs.hm.edu/doc/instructions/farith.html), [conversions](https://mmix.cs.hm.edu/doc/instructions/flot.html) and the [ftoo interface](https://mmix.cs.hm.edu/tools/ftoo/index.html). Returned copies of program text and correct independent implementations were not treated as reports of a defect. No matching prior public report was found in the inspected material. Community implementations have not been exhaustively audited and absolute priority is not established.

## Individual decisions

- **MMIX-S0001:** The fepscomp branch for exponent difference d > 54 sets oo = zf and suppresses the needed upward correction. For y = 1, z = -2^-55, epsilon = 1/2 it reports similarity although the exact difference exceeds the allowed radius; the corresponding FCMPE result is 0 instead of +1.

- **MMIX-S0002:** Both floating packers return infinity on directed overflow even when rounding requires the finite limit. With trips disabled, STSF of 2^128 in ROUND_OFF must store #7f7fffff, but stores #7f800000. The interpretation explicitly uses the adopted IEEE 754-1985 overflow contract; the O and X flags themselves are set.

- **MMIX-S0003:** The negative-input guard in froot precedes NaN dispatch. Negative quiet NaN #fff8000000000001 loses its payload bit and spuriously raises invalid, contrary to MMIX’s explicit NaN rule. The correction must exempt NaNs while still rejecting negative nonzero numbers and negative infinity.

- **MMIX-S0004:** FINT rounds nonintegral finite inputs without setting X; FIX and FIXU additionally erase exceptions through a second funpack. For +1/2 in nearest mode the numeric result zero is right but rA remains zero instead of recording X. This relies on the adopted IEEE 754-1985 integerization/conversion contract, not a reversal of the one-way phrase only if.

- **MMIX-S0005:** Fwrite subtracts the requested block length before checking a short host write, then returns the negated remaining request. A one-byte request with host fwrite returning zero is consequently reported as success zero instead of -1. The general discrepancy is exactly the unwritten portion of that block; ignored fflush errors are outside this claim.

- **MMIX-S0006:** Fgetws on an already empty noninteractive stream with size >= 2 returns zero after the first EOF, whereas the book and the C analogy both require -1 before any character. The finding deliberately excludes the separate ambiguity of a nonempty final line without a newline.

- **MMIX-S0007:** MMIXAL shifts source and target separately using signed arithmetic before subtracting. A known target #8000000000000000 from location #7ffffffffffffffc is incorrectly rejected although its relative displacement is +1 instruction. The equivalent future reference succeeds; GETA witnesses that execution across the user/kernel boundary is not an assumption.

- **MMIX-S0008:** On a supported LP64 host, Ftell stores a successful long result only in the low 32-bit tetra and sets the high tetra to zero. A legal successful position 2^32 is returned as zero. The existing reproduction models this legal host state; it is not a claim that a real 4 GiB file was tested, and it does not apply to 32-bit long hosts.

- **MMIX-S0009:** scan_const fails to compensate the decimal exponent for significant integer digits discarded after its 769-digit buffer fills. The valid 775-character string 1 followed by 769 zeros and e-769 has exact value 1 but returns the nearest representation of 0.1. The independent review confirms the buffer/decimal-point invariant; the direct routine interface has no documented 769-digit limit.

