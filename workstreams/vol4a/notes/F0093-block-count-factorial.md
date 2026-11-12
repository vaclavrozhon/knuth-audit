# The fixed-block generating function is missing k!

Volume 4A, first edition, first printing (2011), Answer 7.2.1.5–36, parenthetical explanation,
printed page 771, file page 788.

Let `S(z)=sum(z^s/s!, s an allowed block size)`. The answer correctly gives exp(S(z)) for all set partitions with allowed block sizes, but its explanation says that S(z)^k is the exponential generating function for partitions into exactly k blocks. That function must be **S(z)^k/k!**.

For a concrete example, allow only blocks of size 2 and take n=4,k=2. Then S(z)=z^2/2, so the printed S(z)^2 gives `4! * [z^4]S(z)^2=6`. There are only three pairings of a four-element set. Dividing by 2! gives the correct count.

The factor removes the k! orders of the same k disjoint blocks. Summing the corrected fixed-k expressions produces the exponential formula already stated in the answer.

Original typesetting inspected. Relevant errata and public-source screening:
`../sources/set-partition-counting-source-check.json`. No matching repair was found in the sources searched;
absolute novelty is not established.
