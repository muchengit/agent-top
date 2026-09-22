#!/usr/bin/env python3
"""Build bilingual Agent-Top ebooks from Markdown sources."""

from __future__ import annotations

import html
import json
import re
import shutil
import subprocess
import zipfile
import zlib
from dataclasses import dataclass
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist" / "ebooks"
EBOOK = ROOT / "ebook"
FRONTMATTER = re.compile(r"^---\n.*?\n---\n", re.DOTALL)
HEADING = re.compile(r"^(#{1,6})(\s+)(.+?)\s*$")
CODE = re.compile(r"^```(.*)$")
LIST = re.compile(r"^(\s*)([-+]|\d+\.)\s+(.*)$")
BLOCKQUOTE = re.compile(r"^>\s?(.*)$")
BULLET_CHARS = {"ul": "•", "ol": "1."}
CODE_FENCE_STACK: list[tuple[str, str]] = []
LIST_STACK: list[tuple[str, int, str]] = []
TABLE_SEP = re.compile(r"^\s*\|?\s*:?-{3,}:?(\s*\|\s*:?-{3,}:?)+\s*\|?\s*$")


@dataclass(frozen=True)
class Section:
    title: str
    source: Path


@dataclass(frozen=True)
class Book:
    lang: str
    title: str
    subtitle: str
    description: str
    slug: str
    cover: str
    sections: tuple[Section, ...]



ROOT_DOCUMENTS: tuple[str, ...] = (
    "README.md",
    "README.zh-CN.md",
    "CONTRIBUTING.md",
    "CONTRIBUTING.zh-CN.md",
    "CODE_OF_CONDUCT.md",
    "CODE_OF_CONDUCT.zh-CN.md",
    "GOVERNANCE.md",
    "GOVERNANCE.zh-CN.md",
    "ROADMAP_STATUS.md",
    "ROADMAP_STATUS.zh-CN.md",
    "SECURITY.md",
    "SECURITY.zh-CN.md",
    "STYLE.md",
    "STYLE.zh-CN.md",
    "agent-top-roadmap.md",
    "agent-top-roadmap.zh-CN.md",
    "ebook-packaging-research.md",
)

def _section_title(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    stem = path.stem
    return stem if path.parent == ROOT else rel


def _sorted_md_files(root: Path) -> tuple[Path, ...]:
    return tuple(
        sorted((p for p in root.rglob("*.md") if p.is_file()), key=lambda p: p.relative_to(ROOT).as_posix())
    )


def _docs_sections(lang: str) -> tuple[Section, ...]:
    docs_root = ROOT / "docs" / lang
    if not docs_root.exists():
        return ()
    return tuple(Section(_section_title(path), path) for path in _sorted_md_files(docs_root))


def _shared_sections() -> tuple[Section, ...]:
    sections: list[Section] = []
    for name in ROOT_DOCUMENTS:
        path = ROOT / name
        if path.exists():
            sections.append(Section(name, path))
    for root_name in ("labs", "examples", "templates"):
        root_dir = ROOT / root_name
        if root_dir.exists():
            for path in _sorted_md_files(root_dir):
                sections.append(Section(_section_title(path), path))
    return tuple(sections)


def _book_sections(lang: str, intro: Path, appendix: Path) -> tuple[Section, ...]:
    sections: list[Section] = []
    sections.append(Section("How to Use This Book", intro))
    sections.extend(_docs_sections(lang))
    sections.extend(_shared_sections())
    sections.append(Section("Appendix", appendix))
    return tuple(sections)

EN_BOOK = Book(
    lang="en",
    title="Agent-Top: Practical Guide to Building LLM Agents",
    subtitle="From First LLM Calls to Production-Grade Multi-Agent Systems",
    description="A practice-first guide for building, evaluating, and operating LLM agents using Agent-Top.",
    slug="agent-top-practical-guide-en",
    cover="#0f766e",
    sections=_book_sections("en", ROOT / "ebook/en/how-to-use.md", ROOT / "ebook/en/appendix.md"),
)
ZH_BOOK = Book(
    lang="zh",
    title="Agent-Top：LLM Agent 开发实践指南",
    subtitle="从第一次 LLM 调用到生产级多 Agent 系统",
    description="面向工程师的 Agent-Top 实践指南，覆盖 L0-L5 学习路径、Lab、评测、生产化和开源贡献。",
    slug="agent-top-practical-guide-zh",
    cover="#2563eb",
    sections=_book_sections("zh", ROOT / "ebook/zh/how-to-use.md", ROOT / "ebook/zh/appendix.md"),
)



def escape(text: str) -> str:
    return html.escape(text, quote=True)


def reset_render_state() -> None:
    CODE_FENCE_STACK.clear()
    LIST_STACK.clear()


def slugify(text: str, prefix: str) -> str:
    text = re.sub(r"<[^>]+>", "", text).strip().lower()
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"[^0-9a-z\u4e00-\u9fff_-]", "", text)
    return f"{prefix}-{text}"[:90] or f"{prefix}-section"


def inline_html(text: str) -> str:
    out = escape(text)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", out)
    out = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', out)
    return out


def render_table(lines: list[str], start: int) -> tuple[str, int]:
    rows: list[list[str]] = []
    i = start
    while i < len(lines) and "|" in lines[i]:
        row = [cell.strip() for cell in lines[i].strip().strip("|").split("|")]
        if not (i == start + 1 and TABLE_SEP.match(lines[i])):
            rows.append(row)
        i += 1
    if len(rows) < 1:
        return "", start
    head, *body = rows
    parts = ["<table><thead><tr>"]
    parts += [f"<th>{inline_html(cell)}</th>" for cell in head]
    parts.append("</tr></thead><tbody>")
    for row in body:
        parts.append("<tr>" + "".join(f"<td>{inline_html(cell)}</td>" for cell in row) + "</tr>")
    parts.append("</tbody></table>")
    return "".join(parts), i


def read_markdown(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    return FRONTMATTER.sub("", text, count=1).lstrip()


def render_markdown_down(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    paragraphs: list[str] = []

    def flush_paragraph() -> None:
        if paragraphs:
            out.append("<p>" + "<br>".join(inline_html(line) for line in paragraphs) + "</p>")
            paragraphs.clear()

    def close_lists() -> None:
        while LIST_STACK:
            out.append(f"</{LIST_STACK.pop()[0]}>")

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        code_match = CODE.match(stripped)
        if code_match:
            flush_paragraph()
            close_lists()
            lang = code_match.group(1).strip() or "text"
            code_lines: list[str] = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            cls = f' class="language-{escape(lang)}"' if lang else ""
            out.append(f'<pre{cls}><code>{escape(chr(10).join(code_lines))}</code></pre>')
            i += 1
            continue

        if not stripped:
            flush_paragraph()
            close_lists()
            i += 1
            continue

        heading = HEADING.match(stripped)
        if heading:
            flush_paragraph()
            close_lists()
            level = min(len(heading.group(1)) + 1, 6)
            out.append(f"<h{level}>{inline_html(heading.group(3))}</h{level}>")
            i += 1
            continue

        if stripped.startswith("|") or (i + 1 < len(lines) and TABLE_SEP.match(lines[i + 1].strip()) and "|" in stripped):
            flush_paragraph()
            close_lists()
            table_html, i = render_table(lines, i)
            out.append(table_html)
            continue

        if stripped.startswith("---") or stripped.startswith("***") or stripped.startswith("___"):
            flush_paragraph()
            close_lists()
            out.append("<hr>")
            i += 1
            continue

        list_match = LIST.match(line)
        if list_match:
            flush_paragraph()
            indent = len(list_match.group(1).expandtabs(2))
            marker = list_match.group(2)
            typ = "ol" if marker.isdigit() else "ul"
            current_indent = indent + 1
            content = inline_html(list_match.group(3))
            while LIST_STACK and LIST_STACK[-1][1] > current_indent:
                out.append(f"</{LIST_STACK.pop()[0]}>")
            if not LIST_STACK or LIST_STACK[-1][1] < current_indent or LIST_STACK[-1][0] != typ:
                if LIST_STACK and LIST_STACK[-1][1] >= current_indent:
                    out.append(f"</{LIST_STACK.pop()[0]}>")
                LIST_STACK.append((typ, current_indent, typ))
                out.append(f"<{typ}>")
            if typ == "ol":
                out.append(f"<li>{content}</li>")
            else:
                out.append(f"<li>{content}</li>")
            i += 1
            continue

        close_lists()
        if BLOCKQUOTE.match(stripped):
            quote_lines: list[str] = [BLOCKQUOTE.match(stripped).group(1)]
            i += 1
            while i < len(lines) and BLOCKQUOTE.match(lines[i].strip()):
                quote_lines.append(BLOCKQUOTE.match(lines[i].strip()).group(1))
                i += 1
            out.append("<blockquote>" + "<br>".join(inline_html(line) for line in quote_lines) + "</blockquote>")
            continue

        paragraphs.append(stripped)
        i += 1

    flush_paragraph()
    close_lists()
    return "\n".join(out)


def render_markdown(text: str) -> str:
    reset_render_state()
    return render_markdown_down(text)


CSS = """
:root { --ink:#17202a; --muted:#5b6770; --accent:#0f766e; --line:#e5e7eb; --code:#f6f8fa; }
* { box-sizing: border-box; }
body { font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; color: var(--ink); line-height: 1.65; margin: 0; padding: 0; background: #fff; }
h1, h2, h3, h4 { line-height: 1.25; margin-top: 1.8em; }
h2 { border-bottom: 1px solid var(--line); padding-bottom: 0.35em; margin-top: 3.2em; font-size: 1.55em; }
h3 { margin-top: 2.4em; }
a { color: var(--accent); }
p { margin: 0.9em 0; }
ul, ol { padding-left: 1.4em; }
li { margin: 0.35em 0; }
code { background: var(--code); padding: 0.15em 0.35em; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 0.92em; }
pre { background: var(--code); border: 1px solid var(--line); border-radius: 8px; padding: 1em; overflow: auto; white-space: pre-wrap; }
pre code { background: transparent; padding: 0; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; }
th, td { border: 1px solid var(--line); padding: 0.55em 0.7em; text-align: left; vertical-align: top; }
thead { background: #f6f8fa; }
blockquote { border-left: 4px solid var(--accent); background: #f0fdfa; padding: 0.7em 1em; margin: 1em 0; color: #14524d; }
.cover { padding: 4.5em 0 3em; border-bottom: 1px solid var(--line); margin-bottom: 3em; }
.cover .kicker { text-transform: uppercase; letter-spacing: 0.12em; color: var(--muted); font-weight: 700; font-size: 0.85em; }
.cover h1 { margin: 0.35em 0; font-size: 2.4em; }
.cover .subtitle { font-size: 1.15em; color: var(--muted); max-width: 34em; }
.meta { color: var(--muted); font-size: 0.95em; margin-top: 1.2em; }
.toc { border: 1px solid var(--line); border-radius: 10px; padding: 1em 1.2em; background: #fafafa; max-height: 70vh; overflow: auto; }
.book { max-width: 860px; margin: 0 auto; padding: 3em 1.4em 5em; }
@page { size: A4; margin: 18mm 16mm; }
@media print {
  body { background: #fff; }
  .book { max-width: none; padding: 0; }
  .cover { padding-top: 8vh; page-break-after: always; }
  h2 { page-break-after: avoid; }
  pre, blockquote, table { page-break-inside: avoid; }
}
"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_source(book: Book) -> tuple[str, list[dict[str, str]]]:
    generated_at = date.today().isoformat()
    toc: list[dict[str, str]] = []
    pieces: list[str] = [
        "# How to Use This Book" if book.lang == "en" else "# 如何使用这本书",
        "This book is generated from the Agent-Top repository Markdown sources.",
        "The intended path is practical: read a chapter, run or inspect the related Lab, then use the checklists before moving on.",
        "",
        f"Generated: {generated_at}",
        "License: MIT",
        "",
    ]
    pieces.append("<div class=\"toc\">")
    for index, section in enumerate(book.sections, 1):
        slug = f"chapter-{index:02d}"
        title = section.title
        toc.append({"id": slug, "title": title})
        pieces.extend([f'<h2 id="{slug}">{html.escape(title)}</h2>', f"Source: `{section.source.relative_to(ROOT)}`", ""])
        markdown = read_markdown(section.source)
        if markdown.lstrip().startswith("# "):
            lines = markdown.splitlines()
            markdown = "\n".join(lines[1:]).lstrip()
        pieces.append(render_markdown(markdown))
        pieces.append("")
    pieces.append("</div>")
    return "\n".join(pieces), toc


def toc_html(toc: list[dict[str, str]]) -> str:
    rows = [f'<li><a href="#{escape(item["id"])}">{inline_html(item["title"])}</a></li>' for item in toc]
    return "<ol>\n" + "\n".join(rows) + "\n</ol>"


def standalone_html(book: Book, body: str, toc: list[dict[str, str]]) -> str:
    meta = {
        "en": ("en-US", "English"),
        "zh": ("zh-CN", "Chinese"),
    }[book.lang]
    generated_at = date.today().isoformat()
    return f"""<!doctype html>
<html lang="{meta[0]}">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{escape(book.title)}</title>
<style>{CSS}</style>
</head>
<body>
<article class="book">
<header class="cover">
  <div class="kicker">Agent-Top Ebook</div>
  <h1>{inline_html(book.title)}</h1>
  <p class="subtitle">{inline_html(book.subtitle)}</p>
  <p class="meta">Agent-Top Contributors · {generated_at} · MIT License</p>
</header>
<section aria-label="Table of Contents">
  <h2>Contents</h2>
  {toc_html(toc)}
</section>
{body}
</article>
</body>
</html>
"""


def print_html(book: Book, body: str, toc: list[dict[str, str]]) -> str:
    lang = "zh-CN" if book.lang == "zh" else "en-US"
    generated_at = date.today().isoformat()
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8" />
<title>{escape(book.title)}</title>
<meta name="description" content="{escape(book.description)}" />
<style>{CSS}</style>
</head>
<body>
<article class="book">
<header class="cover">
  <div class="kicker">Agent-Top Ebook</div>
  <h1>{inline_html(book.title)}</h1>
  <p class="subtitle">{inline_html(book.subtitle)}</p>
  <p class="meta">Agent-Top Contributors · {generated_at} · MIT License</p>
</header>
<section aria-label="Table of Contents">
  <h2>Contents</h2>
  {toc_html(toc)}
</section>
{body}
</article>
</body>
</html>
"""


def pdf_escape(text: str) -> str:
    return text.encode("latin-1", "replace").decode("latin-1").replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def minimal_pdf(text_lines: list[str], output: Path) -> Path:
    stream_lines = ["BT", "/F1 18 Tf", "56 760 Td", "(Agent-Top Ebook) Tj"]
    y = 724
    for line in text_lines:
        safe = pdf_escape(line)
        stream_lines.extend(["ET", "BT", "/F1 11 Tf", f"56 {y} Td", f"({safe}) Tj"])
        y -= 18
    stream_lines.append("ET")
    stream = "\n".join(stream_lines).encode("latin-1", "replace")
    objects = [
        b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n",
        b"2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n",
        b"3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>\nendobj\n",
        b"4 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n",
        f"5 0 obj\n<< /Length {len(stream)} >>\nstream\n".encode("latin-1") + stream + b"\nendstream\nendobj\n",
    ]
    output.parent.mkdir(parents=True, exist_ok=True)
    positions = []
    header = b"%PDF-1.4\n"
    cursor = len(header)
    for obj in objects:
        positions.append(cursor)
        cursor += len(obj)
    xref_offset = cursor
    xref = b"xref\n0 6\n0000000000 65535 f \n" + b"".join(
        f"{pos:010d} 00000 n \n".encode("ascii") for pos in positions
    )
    trailer = f"trailer\n<< /Size 6 /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n".encode("ascii")
    output.write_bytes(header + b"".join(objects) + xref + trailer)
    return output


def build_pdf(book: Book, html_body: str, toc: list[dict[str, str]], html_path: Path) -> tuple[Path, str]:
    print_path = DIST / f"{book.slug}.print.html"
    write(print_path, print_html(book, html_body, toc))
    output = DIST / f"{book.slug}.pdf"
    if (engine := shutil.which("wkhtmltopdf")):
        subprocess.run(
            [engine, "--quiet", "--encoding", "utf-8", str(print_path.resolve()), str(output.resolve())],
            check=True,
        )
        return output, "wkhtmltopdf"
    if (engine := shutil.which("weasyprint")):
        subprocess.run([engine, str(print_path.resolve()), str(output.resolve())], check=True)
        return output, "weasyprint"
    notice = [
        "This file is a fallback PDF notice, not a full-book render.",
        "Install wkhtmltopdf or weasyprint to generate the full PDF layout.",
        f"Print-ready HTML: {print_path.relative_to(ROOT)}",
        f"Generated: {date.today().isoformat()}",
    ]
    return minimal_pdf(notice, output), "minimal-notice"


def png_chunk(typ: bytes, data: bytes) -> bytes:
    return (
        len(data).to_bytes(4, "big")
        + typ
        + data
        + zlib.crc32(typ + data).to_bytes(4, "big")
    )


def solid_color_png(width: int, height: int, hex_color: str, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    rgb = tuple(int(hex_color.strip("#")[i:i+2], 16) for i in (0, 2, 4))
    row = bytes([0, *rgb] * width)
    image = zlib.compress(row * height)
    signature = b"\x89PNG\r\n\x1a\n"
    ihdr = width.to_bytes(4, "big") + height.to_bytes(4, "big") + b"\x08\x02\x00\x00\x00"
    output.write_bytes(signature + png_chunk(b"IHDR", ihdr) + png_chunk(b"IDAT", image) + png_chunk(b"IEND", b""))


def make_cover_png(book: Book, output: Path) -> None:
    solid_color_png(1600, 2400, book.cover, output)


def build_epub(book: Book, html_body: str, toc: list[dict[str, str]], cover_path: Path) -> Path:
    out = DIST / f"{book.slug}.epub"
    title_page = f"""<!doctype html><html xmlns="http://www.w3.org/1999/xhtml" xml:lang="{book.lang}"><head><meta charset="utf-8" /></head><body><section class="titlepage"><h1>{inline_html(book.title)}</h1><p>{inline_html(book.subtitle)}</p><p>Agent-Top Contributors</p><p>MIT License</p></section></body></html>"""
    toc_xhtml = f"""<!doctype html><html xmlns="http://www.w3.org/1999/xhtml" xml:lang="{book.lang}"><head><meta charset="utf-8" /></head><body><nav><h1>Contents</h1>{toc_html(toc)}</nav></body></html>"""
    opf = f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="pub-id">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="pub-id">urn:agent-top:{book.slug}</dc:identifier>
    <dc:title>{escape(book.title)}</dc:title>
    <dc:subtitle>{escape(book.subtitle)}</dc:subtitle>
    <dc:language>{book.lang}</dc:language>
    <dc:description>{escape(book.description)}</dc:description>
    <dc:rights>MIT License</dc:rights>
    <dc:creator>Agent-Top Contributors</dc:creator>
    <meta property="dcterms:modified">{date.today().isoformat()}T00:00:00Z</meta>
    <meta name="cover" content="cover-image"/>
  </metadata>
  <manifest>
    <item id="stylesheet" href="style.css" media-type="text/css"/>
    <item id="cover-image" href="cover.png" media-type="image/png" properties="cover-image"/>
    <item id="titlepage" href="titlepage.xhtml" media-type="application/xhtml+xml"/>
    <item id="toc" href="toc.xhtml" media-type="application/xhtml+xml" properties="nav"/>
    <item id="body" href="body.xhtml" media-type="application/xhtml+xml"/>
  </manifest>
  <spine>
    <itemref idref="titlepage"/>
    <itemref idref="toc"/>
    <itemref idref="body"/>
  </spine>
  <guide><reference type="cover" href="titlepage.xhtml"/><reference type="toc" href="toc.xhtml"/></guide>
</package>"""
    nav = f"""<?xml version="1.0" encoding="UTF-8"?>
<nav xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
  <head><meta charset="utf-8" /></head>
  <body><ol>{''.join(f'<li><a href="body.xhtml#{escape(item["id"])}">{inline_html(item["title"])}</a></li>' for item in toc)}</ol>
</body>
</nav>"""
    container = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>"""
    mimetype = "application/epub+zip"
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.writestr("mimetype", mimetype)
        zip_file.writestr("META-INF/container.xml", container)
        zip_file.writestr("OEBPS/content.opf", opf)
        zip_file.writestr("OEBPS/nav.xhtml", nav)
        zip_file.writestr("OEBPS/titlepage.xhtml", title_page)
        zip_file.writestr("OEBPS/toc.xhtml", toc_xhtml)
        zip_file.writestr("OEBPS/body.xhtml", html_body)
        zip_file.writestr("OEBPS/style.css", CSS)
        zip_file.write(cover_path, arcname="OEBPS/cover.png")
    return out


def build_book(book: Book) -> dict[str, object]:
    cover = EBOOK / "assets" / f"cover-{book.lang}.png"
    make_cover_png(book, cover)
    source_md, toc = build_source(book)
    body = render_markdown(source_md)
    html_body = f'<article class="book">\n<section aria-label="Table of Contents"><h2>Contents</h2>{toc_html(toc)}</section>\n{body}\n</article>'
    standalone = standalone_html(book, body, toc)
    epub = build_epub(book, html_body, toc, cover)
    html_path = DIST / f"{book.slug}.html"
    write(html_path, standalone)
    pdf_path, pdf_engine = build_pdf(book, html_body, toc, html_path)
    return {
        "lang": book.lang,
        "epub": str(epub.relative_to(ROOT)),
        "pdf": str(pdf_path.relative_to(ROOT)),
        "pdf_engine": pdf_engine,
        "html": str(html_path.relative_to(ROOT)),
        "sections": len(book.sections),
        "epub_bytes": epub.stat().st_size,
        "pdf_bytes": pdf_path.stat().st_size,
        "html_bytes": html_path.stat().st_size,
    }


def main() -> int:
    DIST.mkdir(parents=True, exist_ok=True)
    report = {"generated_at": date.today().isoformat(), "outputs": []}
    for book in (EN_BOOK, ZH_BOOK):
        report["outputs"].append(build_book(book))
    write(DIST / "build-report.json", json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
