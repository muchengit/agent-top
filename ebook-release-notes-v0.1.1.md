# Agent-Top Ebook Release Notes

## v0.1.1

### Summary

This release improves ebook packaging review quality and brings the book closer to a publishable state without changing the underlying repository learning content.

### Highlights

- Added a Python-only ebook builder with EPUB, HTML, print HTML, and PDF fallback support.
- Expanded ebook coverage to include repository docs, labs, examples, templates, and governance documents.
- Grouped the ebook table of contents into repository-friendly sections.
- Polished bilingual terminology in the Chinese documentation index.
- Added chapter title improvements so generated book titles use Markdown headings where possible.
- Added a review summary and search indexing for the review record.
- Strengthened the release workflow with PDF renderer installation for CI.

### Notes

- Local PDF generation falls back to a notice PDF when `wkhtmltopdf` or `weasyprint` is unavailable.
- CI is configured to install PDF renderers for real PDF output on release builds.

### Validation

- Repository checks passed.
- Ruff linting passed.
- Ebook build tests passed.
- Full ebook build completed successfully.
