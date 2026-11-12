# F179 — the two noise events need not have the stated probability order

Volume4B, first edition, second printing2022, answer MPR140(e), printed396
(file416). The proof says Pr(*)≤Pr(**), where

    (*)   epsilon < Delta_k + delta_k,
    (**)  epsilon >= Delta_k + delta_k > max(delta_(k−1),...,delta_(k−m)).

Take n=100, epsilon=1/4, the sorted base sequence with50 zeros followed by
50 ones, and k=51. The prescribed m=floor(sqrt(epsilon*n)) is5, so
Delta_k=1. Since delta_k lies in[−1/4,1/4], event(*) always holds and
(**) never holds: the printed comparison is1≤0.

The claimed final asymptotic upper bound is not refuted. The argument
should separately bound the events, rather than compare their probabilities.
For k>m, Pr(*)=min(Delta_k/(2epsilon),1), and Pr(**)≤1/(m+1): integrate
the maximum of the m preceding independent uniform noises over the
truncated range. These are the terms the next displayed bound needs.
The beginning-of-sequence boundary is handled separately in the printed1/k
term. A full replacement proof is not required for the counterexample.

Original page: images/first100-p396.png; the statement on printed28
explicitly permits any base entries in[0,1]. The known20January2023
correction on this page only removes an extraneous parenthesis from(**);
it does not change the false probability comparison. Six errata layers,
three TeX sources and targeted public searches are recorded in
sources/first100-mpr140-145-novelty.json. No matching correction found;
absolute priority and later physical printings are not established.
