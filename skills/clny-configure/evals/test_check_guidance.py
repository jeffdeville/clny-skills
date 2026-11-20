"""Exercise the checker through its CLI with an isolated synthetic repository."""

from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest


CHECKER = Path(__file__).resolve().parents[1] / "scripts" / "check_guidance.py"


class GuidanceCheck(unittest.TestCase):
    def setUp(self):
        temp = TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.repo = Path(temp.name) / "repo"
        self.docs = self.repo / "docs"
        self.docs.mkdir(parents=True)
        (self.repo / "ROOT.md").write_text("[Engineering][index]\n\n[index]: docs/index.md\n")
        (self.docs / "index.md").write_text(
            "| Read |\n|---|\n| [Recovery](Recovery%20guide.md#steps-1) |\n"
            "\n[Home](/ROOT.md)\n"
        )
        (self.docs / "Recovery guide.md").write_text("# Steps\n\n# Steps\n")
        (self.repo / "orphan.md").touch()

    def check(self, *expected):
        return subprocess.run(
            [sys.executable, str(CHECKER), "--repo", str(self.repo), "ROOT.md", *expected],
            text=True, capture_output=True,
        )

    def test_transitive_table_reference_cycle_and_extra_files(self):
        result = self.check("docs/Recovery guide.md")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_reports_disconnected_missing_and_broken_routes(self):
        (self.docs / "index.md").write_text(
            "`[Example](../orphan.md)`\n\n```md\n[Example](../orphan.md)\n```\n"
            "\n[Steps](Recovery%20guide.md#missing) [Next](next.md)\n"
        )
        result = self.check("orphan.md", "missing.md")
        self.assertNotEqual(result.returncode, 0)
        for issue in ["unreachable: orphan.md", "missing expected file: missing.md",
                      "docs/Recovery guide.md#missing: missing anchor", "next.md: missing target"]:
            self.assertIn(issue, result.stderr)

    def test_removed_incoming_link_leaves_unchanged_guide_unreachable(self):
        (self.repo / "ROOT.md").write_text("[Other](https://example.org/docs/index.md)")
        result = self.check("docs/Recovery guide.md")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unreachable: docs/Recovery guide.md", result.stderr)

    def test_explicit_html_navigation_and_anchor(self):
        (self.repo / "ROOT.md").write_text('<a href="docs/index.md#runbook">Guide</a>')
        (self.docs / "index.md").write_text('<a id="runbook"></a>\n')
        result = self.check("docs/index.md")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_symlink_uses_reader_path_and_cannot_cover_an_unlinked_alias(self):
        (self.docs / "index.md").write_text("[Policy](policy.md)")
        (self.repo / "entry.md").symlink_to(self.docs / "index.md")
        (self.repo / "ROOT.md").write_text("[Guide](entry.md)")
        (self.repo / "policy.md").touch()
        (self.repo / "alias.md").symlink_to(self.repo / "policy.md")
        result = self.check("policy.md", "alias.md")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stderr.strip(), "unreachable: alias.md")

    def test_symlink_outside_repository(self):
        private = self.repo.parent / "outside.md"
        private.touch()
        (self.repo / "external.md").symlink_to(private)
        (self.repo / "ROOT.md").write_text("[External](external.md)")
        result = self.check("ROOT.md")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("path outside repository", result.stderr)


if __name__ == "__main__":
    unittest.main()
