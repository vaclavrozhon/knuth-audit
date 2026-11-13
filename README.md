# Knuth audit notebook

A portable local notebook for an audit of TAOCP volumes 1, 2, 3, 4A, 4B,
the MMIX fascicle, and Fascicle 7. This repository is **private**.

All **806 previously confirmed cards** were rechecked before this export:
**797 retained, 4 previously public, 1 returned to candidate status, and
4 dismissed**. See [the review outcome](REVIEW.md) and
[all review decisions](data/review-decisions.json).

The UI contains 931 visible records: 797 confirmed, 117 candidates, and
17 dismissed. Earlier candidates and dismissed records were outside the
confirmed-card recheck. Previously public findings and known errata are
excluded from active finding cards.

## Research questions

The separate [TAOCP research catalogue](research/README.md) contains **236
entries across all seven supplied publications**, including research exercises,
questions in the main text and answers, and later-resolved questions. It records
original and amended ratings, precise book locations, and a literature review
as of **November 12, 2026**. Browse by volume or use the [CSV](research/catalog.csv).

The assessments distinguish resolved questions, recent reported resolutions,
partial results, dated statements of openness, and cases where a resolution
was not located. The last category does **not** establish that a problem is open.

## Open the UI

Python 3.10 or newer is sufficient. The compiled frontend is included.

```bash
git clone https://github.com/vaclavrozhon/knuth-audit.git
cd knuth-audit
python3 review-ui/server.py --port 4318
```

Open **http://localhost:4318**. Cloning requires access to the private
repository. The server listens only on the local computer. It does not start
audit computations or send reports.

Cards have English summaries, the latest publication-review decision,
detailed arguments, and available verification artifacts. Original argument
notes retain their language, including Czech. Historical status headings in
those notes are superseded by the current review shown on the card.

New personal notes are saved locally in `review-ui/data/annotations.sqlite3`,
which is ignored by Git. **No previous personal notes or annotation history
are included.** Use **Export notes** in the UI to save your new notes.

## Books and excerpts

The repository contains no books, full-page image collection, full-book OCR,
private correspondence, credentials, or earlier Git history. Three small
typesetting excerpts and three original witness diagrams are documented in
[the image inventory](data/IMAGE_SOURCES.md).

The arguments and page references work without books. To enable local book
links, put your own copies in `books/` using the filenames in
[the edition inventory](data/editions.json). The UI detects them automatically.
That directory is ignored by Git. Use the audited edition: page numbers and
wording can differ between printings. Physical copies were not checked.

## What the review establishes

“No matching prior report found” means no match in the sources recorded for
that card. It is not a guarantee of absolute priority or an assertion that
the author has confirmed it. The counts are counts of cards; related
occurrences are not necessarily independent discoveries.

The page maps preserve the review of 4,308 supplied file pages under its
documented scope and exceptions. Green means reviewed under that scope;
it does not mean a new proof of every theorem or a guarantee of no remaining
errors. Red strips identify supported findings independently of coverage.

## Arguments and verification scripts

- `findings/`: current English card summaries and links to detailed arguments.
- `workstreams/` and `audit-2026-10-31/`: selected original arguments,
  checker sources, companion programs, and saved results.
- `integration/2026-11-12-novelty-review/notes/`: the final correctness and
  prior-publication review, including changed assessments.
- `data/`: review decisions, source fingerprints, edition information,
  image provenance, and the package file manifest.

The UI needs no Python packages. Individual mathematical checkers may require
the libraries they import, such as SymPy, NumPy, SciPy, python-sat, Z3,
NetworkX, Matplotlib or Pillow; native checks may require a C/C++ compiler,
CWEB, or a named solver. Some historical extraction or source-comparison
scripts also require omitted books or external papers. Those inputs are not
silently substituted. Read the corresponding argument and script before
running it; some checks write results or perform substantial computations.
The saved results remain readable without rerunning them.

## Verify this package

```bash
python3 scripts/verify_package.py
python3 -m unittest discover -s review-ui/tests -p 'test_*.py'
```

The tests use a temporary annotation database. They check the reviewed-card
inventory, included evidence, book omission, local file access, and note
persistence; they do not repeat the historical mathematical computations.
The completed export checks are recorded in [VALIDATION.md](VALIDATION.md).

To rebuild the frontend, use Node 22 or newer:

```bash
cd review-ui
npm ci --ignore-scripts
npm run build
```

Browser checks are available with `npx playwright install chromium` followed
by `npx playwright test` in `review-ui/`. They start a temporary local server
on port 4319 and use disposable notes.

This export has a fixed catalog in `review-ui/catalog.json`; it does not need
the original private checkout or its ledger-generation pipeline.

Third-party material retains its attribution; see [THIRD_PARTY.md](THIRD_PARTY.md).
