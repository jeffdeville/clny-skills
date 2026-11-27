import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "scripts/review_gate.py"


class PushGate(unittest.TestCase):
    def test_typo_sensitive_change_and_new_head(self):
        with tempfile.TemporaryDirectory() as folder:
            repo = pathlib.Path(folder)

            def git(*args):
                return subprocess.check_output(["git", *args], cwd=repo, text=True).strip()

            def commit():
                git("add", ".")
                git("commit", "-qm", "fixture")
                return git("rev-parse", "HEAD")

            def permits(head, remote="0" * 40, env=None):
                result = subprocess.run([sys.executable, SCRIPT, "pre-push"], cwd=repo,
                                        input=f"HEAD {head} refs/heads/work {remote}\n",
                                        capture_output=True, text=True, env=env)
                return result.returncode == 0

            git("init", "-q")
            git("config", "user.name", "Fixture")
            git("config", "user.email", "fixture@example.invalid")
            doc = repo / "overview.md"
            doc.write_text("Exampel")
            git("config", "clny.reviewBase", commit())
            git("config", "--file", "global.cfg", "clny.trivialDocument", "overview.md")
            global_config = repo / ".git" / "fixture-global"
            (repo / "global.cfg").rename(global_config)
            doc.write_text("Example")
            doc_head = commit()
            self.assertFalse(permits(doc_head, env=dict(os.environ, GIT_CONFIG_GLOBAL=str(global_config))))
            git("config", "clny.trivialDocument", "overview.md")
            self.assertTrue(permits(doc_head))
            git("update-index", "--add", "--cacheinfo", f"160000,{doc_head},vendor")
            git("commit", "-qm", "gitlink")
            git("config", "diff.ignoreSubmodules", "all")
            self.assertFalse(permits(git("rev-parse", "HEAD")))
            self.assertFalse(permits(doc_head, remote=git("rev-parse", "HEAD")))
            git("rm", "--cached", "-q", "vendor")
            (repo / "grant.ex").write_text("v1")
            head = commit()
            self.assertFalse(permits(head))
            subprocess.run([sys.executable, SCRIPT, "record", head, "Compared grant handling with contract"],
                           cwd=repo, check=True)
            self.assertTrue(permits(head))
            (repo / "grant.ex").write_text("v2")
            newer = commit()
            # Git may copy notes on rebase/amend. A copied receipt is stale.
            git("notes", "--ref", "clny-review", "copy", head, newer)
            self.assertFalse(permits(newer))


if __name__ == "__main__":
    unittest.main()
