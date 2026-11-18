# F023 — The tail distribution: series constant and object name

**Edition:** Volume 4B, first edition, second printing (November 2022).
The original finding concerns answer 7.2.2.1–191 on printed page 469
(file page 489). The November 17 follow-up adds a wording correction in
the question on printed page 148 (file page 168), under the same card.

## Existing finding: the missing constant

The question defines the probability generating function `G(z)`, whose
coefficient of `z^k` is the probability of tail length `k`, by

```text
G(z) = integral from 0 to infinity of exp(-x) (1+x)^z dx - 1.
```

In particular, `G(0) = 0`. The alternative series in the answer has the
value `e` at zero, and needs the constant term `-e`:

```text
G(z) = e Gamma(1+z) - e
       - sum over k >= 1 of (-1)^k e z / ((k+z) k!).
```

Here `Gamma` is the gamma function, with `Gamma(1) = 1`. The previous
[derivation and checks](../EXTREME_COVER_NOTES.md) establish this correction;
they were not rerun. The reported mean and variance are unchanged.

## Added wording correction

The question calls the object a random **set permutation**. It should say
**set partition**. The tail is defined on printed pages 101–102 as the last
block of a set partition, when its blocks are ordered by their least
elements. A set partition divides a set into disjoint nonempty blocks;
a permutation rearranges its elements.

This identification is also explicit in the cited Asakly–Blecher–Brennan–
Knopfmacher–Mansour–Wagner paper, Section 3.3 and Corollary 4. It gives
the limiting probabilities for the size of the last block of a random
set partition, with the same initial values as exercise 191. The exercise's
intended limiting interpretation and its numerical probabilities are not
additional findings.

The [book question](../images/gould189-192-original-168.png) and
[author draft question](../images/gould189-192-draft-90.png) both visibly
contain the incorrect word. The latter is the September 11, 2019
Pre-Fascicle 5C, printed page 84, file page 90.

No matching correction of this wording was found in the six short/complete
errata layers for Volume 4B and Fascicles 5 and 6, their three current TeX
sources, or focused public searches. Search results included a copy of the
draft repeating the wording, not a correction. Absolute priority and all
later printings remain unverified. See the
[follow-up source record](../results/focused-tail191-sources.json).

This small terminology correction extends F023; it does not increase the
number of finding cards. Nothing was computed, published, or sent.
