# Export validation — 12 November 2026

The 806-card correctness and prior-publication recheck is recorded separately
in [REVIEW.md](REVIEW.md). The checks below validate the portable package;
they do not repeat the saved mathematical computations.

- All 806 decisions are present: 797 retained, 4 previously public,
  1 candidate and 4 dismissed. Every current confirmed card has a retained
  review. The four public matches are absent from active cards and page markers.
- All 931 visible cards have current English summaries and included evidence.
  Every linked review record and page-coverage record is present. The seven
  page maps contain 4,308 file pages.
- The original private export included six PNGs. For the public release,
  the three book-figure excerpts were removed from all published commits;
  only the three original witness diagrams remain. It contains no book files,
  full-page image collection, original annotation database, correspondence,
  credentials or original Git history. File selection, private-data patterns
  and the actual Git inventory were checked before upload.
- All included Python files were parsed without running their mathematical
  computations. Seven Python HTTP integration tests passed, covering catalog
  access, note persistence and revision conflicts, input validation, local
  origin checks, evidence boundaries, image byte ranges and optional local books.
- The frontend built successfully with Vite 7.3.8. Three Chromium tests passed:
  catalog/search/review records/excerpts/coverage, note persistence/export,
  and a 390-pixel mobile view with document navigation.
- `scripts/verify_package.py` checks inventory, included evidence, prohibited
  material and the SHA-256 file manifest. It never opens personal annotations.

The package has a fixed catalog. Some original checker scripts depend on
omitted books, external papers or separately installed libraries/solvers;
the README explains this limitation. Successful package tests do not establish
the mathematical correctness or historical priority of every finding.

The dependency audit after updating Vite reported no high or critical issues.
Four low-severity entries remain associated with KaTeX and the Markdown math
dependency chain; see [the upstream advisory](https://github.com/advisories/GHSA-238p-pmpm-9mq7).
The lockfile preserves the tested versions. Starting the included Python
server does not require Node or a Vite development server.

## Public-release checks - 13 November 2026

- Removed the three book-figure excerpts from every published commit, the
  catalog evidence lists, and the served-file allowlist. The three remaining
  raster images were visually checked as original witness diagrams.
- Scanned all 5,988 reachable historical blobs before the release commit:
  no credential-pattern matches, PDF/DjVu/PostScript book signatures, or
  SQLite database signatures were found. Exactly three original PNG objects
  remained. Personal annotations stay ignored and local.
- Updated image provenance, public-facing status explanations, and package
  validation. All seven HTTP integration tests passed. The temporary-book
  test now resolves its temporary directory to handle macOS path aliases.
- Refreshed and verified the file hash manifest. The five selected examples
  are linked from the README; the editable working PDF is not distributed.

## Volume 4B update — November 17, 2026

- Added the 15 new cards and five promoted candidates from the final focused
  audit. The catalog has 946 records: 817 confirmed, 112 candidates and 17
  dismissed. The original 806 review decisions remain unchanged; 20 additional
  retained decisions are recorded separately.
- Published 274 selected corrections in `volume-4b-findings.txt`, with an
  index linking the numbered items to their evidence. All 272 existing
  descriptions and their layout were preserved, apart from renumbering;
  F270 and F271 were inserted in topic order. The rectangle-packing ASCII
  diagram was preserved. Draft review markers were removed afterward.
- Checked the changed files for correspondence, local paths and prohibited
  content. The package still includes only the three original witness images.
- The frontend built with the existing Vite 7.3.8 lockfile. All seven HTTP
  integration tests passed. All three browser scenarios passed: the catalog
  scenario was updated and rerun after its old expectation of removed book
  excerpts failed; the note-persistence and mobile scenarios passed unchanged.
- Parsed changed Python files and refreshed the package file manifest. These
  checks validate the export and its UI; they do not independently prove the
  mathematical findings.
