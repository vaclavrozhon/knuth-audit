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
- The release includes exactly six documented PNGs: three original witness
  diagrams and three small typesetting excerpts. It contains no book files,
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
