"""Regression tests for layout diagnostics, using disposable fixtures only.

Git's tracked-file listing is mocked: these tests neither invoke Git nor touch
the real repository's papers/PDFs. They test the checker's documented literal
TeX-input and paper-link scope, not a general TeX or Markdown parser.
"""

from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import check_repo_layout as layout


class LayoutTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(prefix="rh-layout-test-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.tracked = [f"output/pdf/{name}.pdf" for name in layout.PAPERS]
        mocked = patch.object(layout.subprocess, "run", side_effect=self.git_listing)
        self.git_run = mocked.start()
        self.addCleanup(mocked.stop)
        self.populate()

    def write(self, relative: str, text: str = "fixture\n") -> None:
        target = self.root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

    def populate(self) -> None:
        for name in layout.PAPERS:
            self.write(f"papers/{name}.tex", "\\documentclass{article}\n")
            # The checker verifies existence, not PDF contents.
            self.write(f"output/pdf/{name}.pdf", "%PDF-fixture\n")
        for relative in ("README.md", "AUDIT_REPORT.md"):
            self.write(relative, "\n".join(
                f"[source](papers/{name}.tex) [PDF](output/pdf/{name}.pdf)"
                for name in layout.PAPERS
            ))
        self.write("papers/README.md", "\n".join(
            f"[source]({name}.tex) [PDF](../output/pdf/{name}.pdf#page=2)"
            for name in layout.PAPERS
        ))
        self.write("docs/history/README-progress-2026-10-07.md", "\n".join(
            f"[source](../../papers/{name}.tex) [PDF](../../output/pdf/{name}.pdf)"
            for name in layout.PAPERS
        ))
        self.write("paper-sections/section.tex", "Section fixture\n")
        self.write(
            f"papers/{layout.PAPERS[0]}.tex",
            "\\input{paper-sections/section}\n"
            "\\include{paper-sections/section.tex}\n",
        )

    def git_listing(self, command: list[str], **kwargs: object) -> subprocess.CompletedProcess:
        self.assertEqual(command, ["git", "ls-files", "-z", "--", "*.pdf"])
        self.assertEqual(kwargs, {"cwd": self.root, "check": True, "capture_output": True})
        listing = "\0".join(self.tracked) + "\0"
        return subprocess.CompletedProcess(command, 0, stdout=listing.encode("utf-8"))

    def check(self) -> list[str]:
        return layout.check_layout(self.root)

    def test_complete_layout_and_root_relative_inputs_pass(self) -> None:
        self.assertEqual(self.check(), [])
        self.git_run.assert_called_once()

    def test_root_tex_and_pdf_are_rejected(self) -> None:
        self.write("misplaced.tex")
        self.write("misplaced.pdf")
        errors = self.check()
        self.assertIn("Paper artifact still in repository root: misplaced.tex", errors)
        self.assertIn("Paper artifact still in repository root: misplaced.pdf", errors)

    def test_every_required_source_and_pdf_is_required(self) -> None:
        for name in layout.PAPERS:
            for relative in (f"papers/{name}.tex", f"output/pdf/{name}.pdf"):
                with self.subTest(relative=relative):
                    target = self.root / relative
                    saved = target.read_bytes()
                    target.unlink()
                    try:
                        self.assertIn(f"Missing paper artifact: {relative}", self.check())
                    finally:
                        target.write_bytes(saved)

    def test_both_literal_input_commands_are_checked(self) -> None:
        name = layout.PAPERS[0]
        self.write(
            f"papers/{name}.tex",
            "\\input{paper-sections/absent}\n"
            "\\include{paper-sections/also-absent.tex}\n",
        )
        errors = self.check()
        self.assertIn(f"Missing TeX input from {name}.tex: paper-sections/absent", errors)
        self.assertIn(f"Missing TeX input from {name}.tex: paper-sections/also-absent.tex", errors)

    def test_input_is_not_silently_resolved_from_papers_directory(self) -> None:
        (self.root / "paper-sections/section.tex").unlink()
        self.write("papers/paper-sections/section.tex")
        errors = self.check()
        self.assertEqual(sum("Missing TeX input" in item for item in errors), 2)

    def test_commented_inputs_are_ignored(self) -> None:
        self.write(
            f"papers/{layout.PAPERS[0]}.tex",
            "% \\input{absent}\n"
            "text % \\include{also-absent}\n"
            "\\input{paper-sections/section} % \\input{comment-only}\n",
        )
        self.assertEqual(self.check(), [])

    def test_all_layout_documents_are_required(self) -> None:
        for relative in (
            "README.md", "papers/README.md", "AUDIT_REPORT.md",
            "docs/history/README-progress-2026-10-07.md",
        ):
            with self.subTest(relative=relative):
                target = self.root / relative
                saved = target.read_bytes()
                target.unlink()
                try:
                    self.assertIn(f"Missing layout documentation: {relative}", self.check())
                finally:
                    target.write_bytes(saved)

    def test_broken_paper_links_in_each_document_are_reported(self) -> None:
        cases = (
            ("README.md", "papers/missing.tex"),
            ("papers/README.md", "../output/pdf/missing.pdf#page=2"),
            ("AUDIT_REPORT.md", "output/pdf/missing.pdf"),
            ("docs/history/README-progress-2026-10-07.md", "../../output/pdf/missing.pdf"),
        )
        for relative, target in cases:
            self.write(relative, f"[missing]({target})\n")
        errors = self.check()
        for relative, target in cases:
            self.assertIn(f"Broken paper link in {relative}: {target}", errors)

    def test_encoded_spaces_anchors_and_remote_links(self) -> None:
        self.write("output/pdf/spaced name.pdf", "%PDF-fixture\n")
        self.write(
            "papers/README.md",
            "[local](../output/pdf/spaced%20name.pdf#page=3)\n"
            "[remote](https://example.invalid/not-a-local-file.pdf)\n",
        )
        self.assertEqual(self.check(), [])

    def test_existing_versioned_pdf_outside_output_is_rejected(self) -> None:
        self.write("archive/misplaced.pdf", "%PDF-fixture\n")
        self.tracked.append("archive/misplaced.pdf")
        self.assertIn("Versioned PDF outside output/pdf or literature: archive/misplaced.pdf", self.check())

    def test_versioned_external_literature_is_allowed(self) -> None:
        self.write("literature/baseline/reference.pdf", "%PDF-fixture\n")
        self.tracked.append("literature/baseline/reference.pdf")
        self.assertEqual(self.check(), [])

    def test_deleted_tracked_paths_and_untracked_scratch_are_ignored(self) -> None:
        self.tracked.extend(["old-paper.pdf", "archive/deleted.pdf"])
        self.write("tmp/pdfs/scratch.pdf", "%PDF-fixture\n")
        self.assertEqual(self.check(), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
