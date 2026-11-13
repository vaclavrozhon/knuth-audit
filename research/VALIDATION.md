# Catalogue validation

Checked on November 12, 2026.

- The catalogue has 236 unique entries from all seven supplied publications:
  152 research exercises, two replacements, and 82 text or answer questions.
  Of the 152, 151 have an original rating of at least 46; one was promoted from
  M45 to M46 in official amendments.
- Every entry has a book location, a question, an assessment, and recorded
  searches. All resolved, reported-resolution, partial-result and explicitly
  open-in-source assessments have evidence links.
- The counts are 23 resolved, five reported resolutions, 54 partial results,
  nine open in a dated source, 137 with no verified resolution located, and
  eight open-ended projects. These categories are not proof of current openness.
- The screening record contains 606 rating checks and 403 passage decisions
  across three overlapping language passes. It includes no original page crops
  or book OCR.
- The CSV has exactly 236 data rows. The seven volume documents and the search
  index reproduce the reviewed JSON. The document check validated 1,268 local
  links before the final evidence-link cleanup.
- External-link checking caught incorrect extensions on official amendment
  links and the wrong historical 4A archive. They were corrected and the
  resulting official URLs returned HTTP 200. A dead optional paper link was
  removed. Publisher access denials and timeouts do not establish that a paper
  is unavailable to readers; this is not a guarantee that every external URL
  will remain accessible.

Reproduce the data and package checks with:

```bash
python3 scripts/build_research_catalog.py --check
python3 scripts/verify_package.py
```

This addition changes research documents and their generator. It does not
change the finding-card data or UI. The earlier UI checks are recorded in the
repository's [validation report](../VALIDATION.md). No old mathematical
computations were restarted, and no recent paper's full proof or computation
was independently certified as part of the catalogue validation.
