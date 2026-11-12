# Reused findings F006 and F008: complete review of MPR121

These are the original findings, not newly numbered reports. The exact
counterexamples in results/information.json and the archived unsent draft
have been read and retained. The 2026-11-07 review adds full arguments for
all parts of exercise121 and scans all six local errata layers plus three
TeX sources. No original calculation or enumeration was restarted.

## F006: entropy evaluates the mass function at the random value

On printed p24, exercise121(d), the book prints H_Y=E lg(1/Y).
For the deterministic variable Y=2 this is −1. Its actual entropy is 0,
since y(2)=1. The correct expression is E lg(1/y(Y)).

The original second-printing PDF, file44, and the author's September11,
2019 Pre-Fascicle5A, printed p24/file30, have the same expression.
The referenced original Vol3 Eq6.2.2–(18), p442/file453, defines entropy
as the sum of p_k lg(1/p_k); p443/file454 supplies the zero convention.
No applicable correction was found in the six errata layers or their
available TeX sources. The error location is only p24/file44.

## F008: the first divergence expression loses singular target mass

On printed p24 the definition equates E[rho(X) lg rho(X)] with
E lg rho(Y) and the sum of y(t)lg(y(t)/x(t)), while explicitly allowing
an infinite density ratio. Take x=(1,0) and y=(1/2,1/2).

Then X always selects the first atom and rho(X)=1/2. The first expression
is exactly −1/2. The other expressions are +infinity because Y has
positive mass at the second atom, where x=0. Also E rho(X)=1/2,
contradicting the normalization used in answer121(b), printed p390.

Define divergence by the sum, and use the first expectation only under
y absolutely continuous with respect to x. In the proof of (b), first
handle support mismatch by D=+infinity; then E rho(X)=1 and Jensen is
valid. The corrected nonnegativity and equality characterization have
complete proofs in notes/sequential-mpr-ex121.md.

Original PDF files44 and410 and author PS files30 and52 confirm the
definition and the answer. All six local official errata snapshots and
three TeX sources contain no applicable repair. The known May31,2021
change of divergence terminology is recorded separately as E135 and
does not repair this support issue.

The same support error recurs in the introductory identity of MPR124,
printed p25/file45 (author PS p25/file31). With the same x,y and f=1,
E f(Y)=1 but E[rho(X)f(X)]=1/2. This extends the original F008 scope
without creating another ID. The finite-sample bounds later in124 have
finite D through their n=c^4 2^D parametrization and therefore imply
absolute continuity; the problem onp25 is precisely the unrestricted
introductory change-of-measure claim. The known E002 correction to the
later expected-error bound does not amend that introductory identity.
All six layers and three TeX sources were checked again for124;
see notes/sequential-mpr-ex124.md and its errata manifest.

The audit also resolves the old partial scope concerning null
conditioning events and infinite entropies. Entropy differences are
used only where defined; nonnegative chain rules and mixture concavity
prove the general countable-distribution statements without infinity
minus infinity. Those domain explanations create no new finding.

Neither finding claims a physical printed-copy inspection, priority,
or a reward. Existing IDs and severity classifications are preserved.

