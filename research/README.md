# Research questions in TAOCP

**236 entries from seven supplied publications** of Donald Knuth’s *The Art of Computer Programming* (TAOCP), with a literature review as of **2026-11-12**. This is a separate research catalogue; entries are not error-finding cards.

It includes all 152 exercises identified with original or amended ratings of 46–50, 2 replacement questions, and 82 additional questions or research notes from the main text and answers. Questions later resolved are retained. Closely related subquestions can share an entry, so the count is not a count of independent conjectures.

**The catalogue is not a list of 236 problems known to be open today.** In particular, “Resolution not located” means the present search did not verify a solution. It must not be cited as evidence of openness. Recent reported resolutions are distinguished from established results.

[Spreadsheet CSV](catalog.csv) · [Structured JSON](catalog.json) · [Search record](SEARCHES.md) · [Terms and notation](GLOSSARY.md)

## Browse by publication

| Publication | Supplied edition | Entries |
| --- | --- | ---: |
| [1: Fundamental Algorithms](vol1.md) | 3rd edition · 1st printing · 1997 | 9 |
| [2: Seminumerical Algorithms](vol2.md) | 3rd edition · 1st printing · 1997 | 51 |
| [3: Sorting and Searching](vol3.md) | 2nd edition · 1st printing · 1998 | 44 |
| [4A: Combinatorial Algorithms, Part 1](vol4a.md) | 1st edition · 1st printing · 2011 | 67 |
| [4B: Combinatorial Algorithms, Part 2](vol4b.md) | 1st edition · 2nd printing · 2022 | 38 |
| [MMIX: Volume 1, Fascicle 1: MMIX](vol1-fasc1.md) | Published fascicle · Digital release 3 · 2023 | 2 |
| [F7: Volume 4, Fascicle 7: Constraint Satisfaction](vol4-fasc7.md) | Published fascicle · Digital release 1 · 2025 | 25 |

## Reading the assessments

| Assessment | Entries | Meaning |
| --- | ---: | --- |
| Resolved | 23 | A source resolves the specified target; false conjectures count as resolved. This is not an independent proof audit. |
| Reported resolution | 5 | A recent preprint or computational record reports a resolution; its proof or computation has not been independently certified here. |
| Partial results | 54 | The cited work settles a subquestion or improves bounds; the exact remaining target or its current status is stated in the note. |
| Open in a cited source | 9 | A dated primary source explicitly describes the target as unresolved. The search found no verified later resolution; this is not a timeless guarantee. |
| Resolution not located | 137 | The bounded search did not identify a verified resolution. Current status remains unverified; this does not assert that the problem is open. |
| Open-ended project | 8 | A design, implementation or exploratory task without a single binary solved/open criterion. |

## Scope and method

The scope is TAOCP volumes 1, 2, 3, 4A and 4B, the MMIX fascicle, and Fascicle 7, in the editions above. Other books by Knuth and unavailable future volumes are outside this inventory.

Knuth’s number is an exercise difficulty/research rating. The modern guide treats ratings 46 and above as research problems; [50] alone is too narrow. M marks a mathematical exercise and HM marks one involving higher mathematics. A lower amended rating is preserved alongside the original; it does not erase the historical research question. An ungraded note inherits no invented rating.

The scan screened exercise-like OCR records, checked 606 potentially high or ambiguous ratings against original page crops (including a second pass through ratings 40–45), and reviewed 403 language hits across three overlapping passes. Each included question was read with its surrounding text or answer. The screening decisions are in [rating-review.json](rating-review.json) and [coverage-review.json](coverage-review.json); private images and book OCR are omitted.

The literature pass contains 89 search batches and 310 recorded query strings. It uses book locators, named conjectures, authors, and terminology; result pages were followed to relevant primary sources. Current and historical official amendments were compared; their fingerprints are in the [official-source manifest](../data/official-source-manifest.json). The search log records the questions asked, not a claim that every result or every paper was read in full.

The intended coverage is comprehensive for these supplied editions, but prose questions require judgment and omissions remain possible. General encouragement to do research, unknown input values, attribution questions, and historical conjectures already settled in the same discussion are normally excluded. Explicit research exercises and specifically highlighted historical targets are retained even if later solved.

These are concise original paraphrases for navigation. Mathematical notation is local to each entry; named algorithms, graph families and exact computational models are defined at its book location. The [glossary](GLOSSARY.md) explains recurring terms. In particular, a theorem for a different machine model, asymptotic objective, graph family or probability convention is not silently treated as a solution.

## Useful starting points

- [Dynamic optimality of splay trees](vol3.md#v3-t-splay): an unnumbered research question on page 478.
- [Research exercises and questions in Volume 4A](vol4a.md).
- [Questions from Constraint Satisfaction, Fascicle 7](vol4-fasc7.md).

For unresolved work, start with entries marked “Open in a cited source” and read the remaining target in “Partial results.” The 137 entries marked “Resolution not located” need further literature verification before being advertised as open.

## Data and reproducibility

`catalog.json` is the reviewed source. Each entry records its location, original and amended ratings, a short question, an assessment, primary-source links, and search batch IDs. `catalog.csv` contains one row per entry, with source links and amendments in separate columns. `search-log.json` contains only query metadata; no third-party search excerpts or copies of papers are included.

Regenerate the readable files after editing the JSON:

```bash
python3 scripts/build_research_catalog.py
python3 scripts/build_research_catalog.py --check
```

The check validates IDs, assessments, evidence references, source URL structure and consistency of the generated documents. It does not prove the mathematical claims or certify literature completeness. The repository remains private.
