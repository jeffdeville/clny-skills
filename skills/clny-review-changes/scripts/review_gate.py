"""Local, opt-in Git review receipts. Run in the consuming repository."""
import argparse
import os
from pathlib import PurePosixPath
import subprocess
import sys


NOTES = "refs/notes/clny-review"


def git(*args, check=True):
    return subprocess.run(["git", *args], capture_output=True, check=check)


def record(head, summary):
    commit = git("rev-parse", "--verify", f"{head}^{{commit}}").stdout.decode().strip()
    if head != commit or not summary.strip():
        raise ValueError("Supply the full reviewed commit ID and a review summary.")
    git("notes", "--ref", NOTES, "add", "-f", "-m", f"PASS {head}\n\n{summary}", head)


def documentation_only(head):
    base = git("config", "--local", "--get", "clny.reviewBase", check=False)
    allowed = git("config", "--local", "--null", "--get-all", "clny.trivialDocument", check=False)
    if base.returncode or allowed.returncode:
        return False
    policy = {os.fsdecode(path) for path in allowed.stdout.split(b"\0") if path}
    ancestor = git("merge-base", os.fsdecode(base.stdout).strip(), head).stdout.strip()
    # Require ordinary content modifications. A rename, symlink or executable
    # mode change must take the reviewed route even for an allowed filename.
    raw = git("diff", "--raw", "--ignore-submodules=none", "--no-renames", "-z", ancestor, head, "--").stdout
    fields = raw.split(b"\0")[:-1]
    if not fields or len(fields) % 2:
        return False
    for meta, path in zip(fields[::2], fields[1::2]):
        old, new, _, _, status = meta.split()
        name = os.fsdecode(path)
        parts = PurePosixPath(name).parts
        if (old != b":100644" or new != b"100644" or status != b"M"
                or name not in policy or not name.endswith(".md")
                or any(part.startswith(".") for part in parts)
                or parts[-1].upper() in {"AGENTS.MD", "CLAUDE.MD", "SECURITY.MD", "SKILL.MD"}):
            return False
    return True


def verify(head, remote_head):
    note = git("notes", "--ref", NOTES, "show", head, check=False)
    if note.returncode == 0 and note.stdout.splitlines()[:1] == [f"PASS {head}".encode()]:
        return
    fast_forward = (set(remote_head) == {"0"} or
                    git("merge-base", "--is-ancestor", remote_head, head, check=False).returncode == 0)
    if not fast_forward or not documentation_only(head):
        raise ValueError(f"Review required for {head}. Record the independent review of this commit.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_subparsers(dest="action", required=True)
    add = actions.add_parser("record")
    add.add_argument("commit")
    add.add_argument("summary")
    actions.add_parser("pre-push")
    args = parser.parse_args()
    if args.action == "record":
        record(args.commit, args.summary)
    else:
        for line in sys.stdin:
            _, head, destination, remote_head = line.split()
            if destination.startswith("refs/heads/") and set(head) != {"0"}:
                verify(head, remote_head)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, subprocess.CalledProcessError) as error:
        sys.exit(str(error))
