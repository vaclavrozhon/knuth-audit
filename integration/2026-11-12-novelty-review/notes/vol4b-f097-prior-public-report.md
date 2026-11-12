# F097: correct program defect, already publicly reported

On 12 November 2026 the author-hosted
[BACK-20Q source](https://www-cs-faculty.stanford.edu/~knuth/programs/back-20q.w)
still contains the unconditional rejection between its two tests for
question 18. Its SHA-256 is
`12084722cdf5b04b1c2301811181347d1795041c005d61a234e3976e7f9881f3`,
identical to the source used for the local finding. The second test is
unreachable. The existing explicit questionnaire and independent model
therefore remain a valid correctness witness.

However, the public repository `sjnam/gweb-examples` already explains
this exact defect and corrects it in its Go translation. The
[original source at commit d92b5f8](https://github.com/sjnam/gweb-examples/blob/d92b5f8329426b28b8bc14d8a486d74b6c5f0443/back-20q.w)
reproduces both erroneous C statements and explains that the first
unconditional rejection makes question 18 impossible to mark incorrect.
It replaces those statements with a combined truth-condition check.
The [commit record](https://github.com/sjnam/gweb-examples/commit/d92b5f8329426b28b8bc14d8a486d74b6c5f0443)
is dated **17 August 2026, 06:28:55 UTC**, before the local November audit.
The current [program README](https://github.com/sjnam/gweb-examples/blob/main/back-20q/README.md)
also identifies the question-18 defect and distinguishes it from another
question-15 defect. The latter is outside F097's scope.

Decision: retain the technical evidence but classify F097 as
`previously_publicly_discussed`. It must not appear among new findings
or as a red new-finding page marker. This establishes an earlier public
description, not the earliest discovery date or any author's private
reporting history. No message or report was sent.
