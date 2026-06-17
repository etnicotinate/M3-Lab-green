"""Post-process citation authors with lab-member markers.

The citation generator writes ``_data/citations.yaml`` from external sources.
This script keeps the generated file mostly untouched while adding display
markers that depend on the current lab roster:

- ``#`` marks authors found in ``_members``.
- Existing ``*`` and ``†`` markers are preserved but not inferred.

It intentionally uses only Python's standard library so it can run in both the
citation-update workflow and the site-build workflow without extra packages.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path


MARKER_ORDER = ("*", "†", "#")
MARKER_RE = re.compile(r"([*†#]+)$")
AUTHOR_LINE_RE = re.compile(r"^(\s*-\s+)(.+?)(\r?\n?)$")


def normalize_name(name: str) -> str:
    """Normalize author/member names for matching."""
    cleaned = re.sub(r"</?[^>]+>", "", name)
    cleaned = cleaned.replace("**", "").replace("__", "")
    cleaned = MARKER_RE.sub("", cleaned.strip())
    cleaned = unicodedata.normalize("NFKC", cleaned)
    cleaned = re.sub(r"[\u2010-\u2015]", "-", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned.casefold()


def unquote_scalar(value: str) -> str:
    """Decode the simple YAML scalar forms used by author names."""
    value = value.strip()
    if len(value) >= 2 and value[0] == "'" and value[-1] == "'":
        return value[1:-1].replace("''", "'")
    if len(value) >= 2 and value[0] == '"' and value[-1] == '"':
        inner = value[1:-1]
        return bytes(inner, "utf-8").decode("unicode_escape")
    return value


def quote_scalar(value: str) -> str:
    """Quote author strings that contain Markdown or YAML-sensitive symbols."""
    escaped = value.replace("'", "''")
    return f"'{escaped}'"


def read_front_matter(path: Path) -> dict[str, object]:
    """Read the simple front matter fields needed from a member file."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    data: dict[str, object] = {}
    key_for_list: str | None = None

    for line in lines[1:]:
        stripped = line.strip()
        if stripped == "---":
            break
        if not stripped or stripped.startswith("#"):
            continue

        if key_for_list and line.startswith("  - "):
            items = data.setdefault(key_for_list, [])
            if isinstance(items, list):
                items.append(unquote_scalar(line.split("  - ", 1)[1]))
            continue

        key_for_list = None
        if ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if not value:
            data[key] = []
            key_for_list = key
        else:
            data[key] = unquote_scalar(value)

    return data


def collect_group_members(members_dir: Path) -> list[dict[str, object]]:
    """Collect member names and aliases from ``_members``."""
    members: list[dict[str, object]] = []

    for path in sorted(members_dir.glob("*.md")):
        data = read_front_matter(path)
        name = data.get("name")
        if not name:
            continue

        aliases = data.get("aliases") or []
        if isinstance(aliases, str):
            aliases = [aliases]

        alias_set = {str(alias) for alias in aliases if alias}
        file_name_alias = path.stem.replace("-", " ")
        alias_set.add(file_name_alias)
        for value in [str(name), file_name_alias]:
            parts = value.split()
            if len(parts) == 2:
                alias_set.add(" ".join(reversed(parts)))
        alias_set.discard(str(name))

        members.append(
            {
                "name": str(name),
                "aliases": sorted(alias_set),
                "role": str(data.get("role", "")),
                "file": path.name,
            }
        )

    return members


def build_name_lookup(members: list[dict[str, object]]) -> set[str]:
    """Build normalized lookup names from member names and aliases."""
    lookup: set[str] = set()
    for member in members:
        aliases = member.get("aliases", [])
        if not isinstance(aliases, list):
            aliases = []
        names = [str(member["name"]), *[str(alias) for alias in aliases]]
        lookup.update(normalize_name(name) for name in names if name)
    return lookup


def split_author_markers(author: str) -> tuple[str, list[str], bool]:
    """Split an author string into base name, trailing markers, and bold state."""
    text = author.strip()
    is_bold = text.startswith("**") and text.endswith("**") and len(text) >= 4
    inner = text[2:-2].strip() if is_bold else text

    match = MARKER_RE.search(inner)
    markers = list(match.group(1)) if match else []
    base = MARKER_RE.sub("", inner).strip()
    return base, markers, is_bold


def ordered_markers(markers: list[str]) -> str:
    """Return unique author markers in a stable display order."""
    present = set(markers)
    return "".join(marker for marker in MARKER_ORDER if marker in present)


def mark_author(author: str, group_lookup: set[str]) -> str:
    """Mark group-member authors with ``#`` while preserving existing markers."""
    base, markers, is_bold = split_author_markers(author)
    is_group_member = normalize_name(base) in group_lookup

    if not is_group_member:
        return author

    if "#" not in markers:
        markers.append("#")

    marked = f"{base}{ordered_markers(markers)}"
    return f"**{marked}**" if is_group_member or is_bold else marked


def process_citations(citations_path: Path, group_lookup: set[str]) -> bool:
    """Apply author markers to citation author-list lines."""
    lines = citations_path.read_text(encoding="utf-8").splitlines(keepends=True)
    output: list[str] = []
    changed = False
    in_authors = False

    for line in lines:
        if line.strip() == "authors:":
            in_authors = True
            output.append(line)
            continue

        if in_authors:
            match = AUTHOR_LINE_RE.match(line)
            if match:
                prefix, scalar, newline = match.groups()
                author = unquote_scalar(scalar)
                marked_author = mark_author(author, group_lookup)
                if marked_author != author:
                    line = f"{prefix}{quote_scalar(marked_author)}{newline}"
                    changed = True
                output.append(line)
                continue
            in_authors = False

        output.append(line)

    if changed:
        citations_path.write_text("".join(output), encoding="utf-8")

    return changed


def dump_list(values: list[str], indent: int = 2) -> list[str]:
    """Dump a short YAML string list."""
    prefix = " " * indent
    return [f"{prefix}- {quote_scalar(value)}\n" for value in values]


def write_group_members(path: Path, members: list[dict[str, object]]) -> bool:
    """Write the generated group-member list. Return True if changed."""
    lines = ["# DO NOT EDIT, GENERATED FROM _members\n\n"]
    for member in members:
        lines.append(f"- name: {quote_scalar(str(member['name']))}\n")
        aliases = member.get("aliases", [])
        if isinstance(aliases, list) and aliases:
            lines.append("  aliases:\n")
            lines.extend(dump_list([str(alias) for alias in aliases], indent=4))
        else:
            lines.append("  aliases: []\n")
        lines.append(f"  role: {quote_scalar(str(member.get('role', '')))}\n")
        lines.append(f"  file: {quote_scalar(str(member['file']))}\n")

    content = "".join(lines)
    old_content = path.read_text(encoding="utf-8") if path.exists() else ""

    if content == old_content:
        return False

    path.write_text(content, encoding="utf-8")
    return True


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true")
    return parser.parse_args()


def main() -> int:
    """Run citation author post-processing."""
    args = parse_args()
    repo = args.repo.resolve()

    members = collect_group_members(repo / "_members")
    group_lookup = build_name_lookup(members)

    changed_members = write_group_members(repo / "_data" / "group_members.yaml", members)
    changed_citations = process_citations(repo / "_data" / "citations.yaml", group_lookup)

    if args.check and (changed_members or changed_citations):
        print("Author marker outputs are not up to date.")
        return 1

    print(f"Loaded {len(members)} group members.")
    print(f"Updated group member list: {changed_members}.")
    print(f"Updated citation authors: {changed_citations}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
