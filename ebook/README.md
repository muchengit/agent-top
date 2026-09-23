# Ebook Build

This directory contains the offline ebook build system for Agent-Top.

## Build

```bash
python3 ebook/build_ebook.py
```

Outputs:

- `dist/ebooks/agent-top-practical-guide-en.epub`
- `dist/ebooks/agent-top-practical-guide-en.pdf`
- `dist/ebooks/agent-top-practical-guide-en.html`
- `dist/ebooks/agent-top-practical-guide-en.print.html`
- `dist/ebooks/agent-top-practical-guide-zh.epub`
- `dist/ebooks/agent-top-practical-guide-zh.pdf`
- `dist/ebooks/agent-top-practical-guide-zh.html`
- `dist/ebooks/agent-top-practical-guide-zh.print.html`
- `dist/ebooks/build-report.json`

The builder uses only the Python standard library by default, so no extra dependencies are required for EPUB, HTML, and fallback PDF generation.

## PDF mode

If `wkhtmltopdf` or `weasyprint` is installed, the builder uses it to render the print HTML into a full-layout PDF. Otherwise it emits a small valid fallback PDF and keeps the print HTML for manual browser print-to-PDF.

Recommended full-layout engines:

```bash
sudo apt-get install wkhtmltopdf
# or
python -m pip install weasyprint
```

## Structure

- `build_ebook.py`: generates bilingual ebook sources and EPUB/HTML/PDF outputs.
- `assets/`: generated cover art for EPUB packages.
- `dist/ebooks/`: generated build output; ignored by Git.

## Content Policy

The ebook is built from the repository Markdown sources. Each language edition includes:

- repository governance documents at the top level
- the full `docs/<lang>` documentation set for that language
- `labs/`, `examples/`, and `templates/` Markdown files
- the localized intro and appendix for that language

The generated books are grouped into a clearer hierarchy:

- `Introduction`
- `docs/en`
- `docs/zh`
- `labs`
- `examples`
- `templates`
- `Repository Docs`
- `Appendix`

It preserves code blocks, tables, checklists, and local source-path references where useful for practice workflows.
