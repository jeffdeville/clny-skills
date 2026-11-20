"""Check local guidance reachability from the contributor's root document."""

import argparse
from collections import defaultdict
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import subprocess
import sys
from urllib.parse import unquote, urlsplit


MARKDOWN = {".md", ".markdown", ".mdown"}


class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.anchors = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.anchors.add(attrs["id"])
        if tag == "a":
            if attrs.get("name"):
                self.anchors.add(attrs["name"])
            if attrs.get("href"):
                self.links.append(attrs["href"])

    def visit(self, node):
        if isinstance(node, list):
            for child in node:
                self.visit(child)
        elif isinstance(node, dict):
            kind = node.get("t")
            content = node.get("c")
            if kind == "Link":
                self.links.append(content[2][0])
            elif kind == "Header":
                self.anchors.add(content[1][0])
            elif kind in {"RawInline", "RawBlock"} and content[0] == "html":
                self.feed(content[1])
            self.visit(content)


def read_document(path):
    result = subprocess.run(
        ["pandoc", "--from=gfm", "--to=json", str(path)],
        capture_output=True, text=True, check=False,
    )
    if result.returncode:
        raise ValueError(result.stderr.strip() or "Pandoc failed to parse document")
    doc = Document()
    doc.visit(json.loads(result.stdout)["blocks"])
    doc.close()
    return doc


def local_path(repo, path):
    # Preserve the URL a reader followed when resolving the next relative link.
    lexical = Path(os.path.normpath(path))
    if not lexical.is_relative_to(repo) or not lexical.resolve().is_relative_to(repo):
        raise ValueError(f"path outside repository: {path}")
    return lexical


def check(repo, root, expected):
    pending = [root]
    reached = {root}
    documents = {}
    fragments = defaultdict(set)
    errors = set()
    while pending:
        source = pending.pop()
        try:
            doc = read_document(source)
        except (ValueError, OSError) as exc:
            errors.add(f"{source.relative_to(repo)}: {exc}")
            continue
        documents[source] = doc
        for href in doc.links:
            try:
                url = urlsplit(href)
                if url.scheme or url.netloc:
                    continue
                path = unquote(url.path)
                base = repo if path.startswith("/") else source.parent
                target = local_path(repo, base / path.lstrip("/")) if path else source
                if target.is_dir():
                    continue
                if not target.is_file():
                    raise ValueError("missing target")
                if target.suffix.lower() in MARKDOWN:
                    if target not in reached:
                        pending.append(target)
                    if url.fragment:
                        fragments[target, unquote(url.fragment)].add(source)
                reached.add(target)
            except (OSError, ValueError, RuntimeError) as exc:
                errors.add(f"{source.relative_to(repo)} -> {href}: {exc}")

    for (target, anchor), sources in fragments.items():
        if target in documents and anchor not in documents[target].anchors:
            for source in sources:
                errors.add(f"{source.relative_to(repo)} -> {target.relative_to(repo)}#{anchor}: missing anchor")
    for path in expected - reached:
        issue = "unreachable" if path.is_file() else "missing expected file"
        errors.add(f"{issue}: {path.relative_to(repo)}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd(), help="repository directory (default: cwd)")
    parser.add_argument("root", type=Path, help="root Markdown document, relative to repository")
    parser.add_argument("expected", nargs="+", type=Path, help="expected repository-relative guidance files")
    args = parser.parse_args()
    repo = args.repo.resolve()
    try:
        root = local_path(repo, repo / args.root)
        if not root.is_file() or root.suffix.lower() not in MARKDOWN:
            parser.error("root must be an existing Markdown document")
        expected = {local_path(repo, repo / path) for path in args.expected}
        errors = check(repo, root, expected)
    except (OSError, ValueError, RuntimeError) as exc:
        parser.error(str(exc))
    if errors:
        for error in sorted(errors):
            print(error, file=sys.stderr)
        return 1
    print(f"Reachable from {root.relative_to(repo)}: all {len(expected)} expected guidance files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
