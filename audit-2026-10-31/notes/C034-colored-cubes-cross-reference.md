# C034: Gardner's extension is question (d), not question (c)

**Confirmed, low severity.** TAOCP Volume 4B, first edition, second
printing (November 2022), answer 7.2.2.1–146, printed p. 456, file p. 476.
The September 11, 2019 Pre-Fascicle 5C, p. 160, has the same reference.
The candidate identifier is retained.

The historical paragraph says that Gardner extended the colored-cube
problem to question **(c)** in Scientific American, September 1978,
p. 26. The two parts of exercise 146, printed on p. 143, ask different
questions:

- Part (c) asks for the number of essentially different six-cube rows.
- Part (d) asks whether all thirty cubes can be divided into five such
  rows simultaneously.

The cited Gardner page first describes a six-cube row with the required
face colors, then asks whether the thirty cubes can be partitioned into
five sets that each form such a row. That is precisely **(d)**. It does
not ask for the number of equivalence classes of individual rows.
The correction is therefore `question (c)` to `question (d)`.

The original book, author draft, exercise statement, and Gardner page
were visually compared. Gardner's 1992 reprint, pp. 96–97, also describes
the five-row question. The separately published correction of the
journal volume from **235** to **239** is already known; it does not
correct this part letter and is not counted again.

## Why the earlier candidate can be resolved

The earlier note withheld confirmation pending a fuller historical
review, including the 1961 article. Those broader questions are not
needed to identify the part asked on the explicitly cited 1978 page.
This finding is confined to the internal cross-reference. It makes no
new claim about priority in 1961 or the exact number of symmetric
arrangements in Perjés's later construction.

The original 1981 report by Z. Perjés, *Tori of Colored Cubes*, has now
also been retrieved from the Hungarian Academy of Sciences archive.
Its section 5, printed p. 5, explicitly defines a complete set as a
partition of the thirty cubes into five six-cube arrangements and gives
constructions. It cites Gardner's September 1978 article. This supports
the surrounding historical context; its full classification was not
independently checked or used to alter the book's numerical findings.

## Evidence and novelty check

- [Book p. 456](../images/vol4b-p456-cubes146.png),
  [question p. 143](../images/vol4b-p143-cubes146.png), and
  [author draft p. 160](../images/fasc5c-p160-cubes146.png).
- [Gardner's original p. 26](../images/cubes146-sciam1978-09-pdf28.png),
  from the [September 1978 issue](https://www.wkbpic.com/wkbx/SA/1978/1978-09-01.pdf),
  file p. 28. The continuation on p. 30 was also read.
- [Perjés's report](https://real-eod.mtak.hu/7391/1/KFKIreports_81-057.pdf),
  [retrieval record](../../integration/2026-11-17-focused-4b/sources/perjes1981-retrieval.json),
  and [p. 5 image](../../integration/2026-11-17-focused-4b/sources/perjes1981-p5.png).
- [Focused source check](../results/focused-cubes146-reference.json).

The refreshed official short and complete errata were checked, including
the March 13, 2026 correction on this exact line. No correction of the
part letter was located. Focused public searches found no matching
report; absolute priority is not established. No physical copy or every
later printing was inspected, and no report was sent. The mathematical
solutions and counts are unaffected.
