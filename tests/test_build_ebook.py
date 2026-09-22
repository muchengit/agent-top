from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class BuildEbookTest(unittest.TestCase):
    def test_build_creates_report(self) -> None:
        subprocess.run(
            [sys.executable, "ebook/build_ebook.py"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        report_path = ROOT / "dist" / "ebooks" / "build-report.json"
        self.assertTrue(report_path.exists())
        report = json.loads(report_path.read_text(encoding="utf-8"))
        self.assertEqual(len(report["outputs"]), 2)
        languages = {item["lang"] for item in report["outputs"]}
        self.assertEqual(languages, {"en", "zh"})
        for item in report["outputs"]:
            self.assertTrue(item["epub"].endswith(".epub"))
            self.assertTrue(item["pdf"].endswith(".pdf"))
            self.assertTrue(item["html"].endswith(".html"))
            self.assertGreater(item["epub_bytes"], 0)
            self.assertGreater(item["pdf_bytes"], 0)
            self.assertGreater(item["html_bytes"], 0)

    def test_build_stdout_is_json(self) -> None:
        result = subprocess.run(
            [sys.executable, "ebook/build_ebook.py"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertTrue(result.stdout.strip())
        parsed = json.loads(result.stdout)
        self.assertIn("generated_at", parsed)
        self.assertIn("outputs", parsed)


if __name__ == "__main__":
    unittest.main()
