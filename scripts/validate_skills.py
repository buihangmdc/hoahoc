#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

from pathlib import Path


LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
NAME_RE = re.compile(r"^name:\s*([a-z0-9-]+)\s*$", re.MULTILINE)
DESCRIPTION_RE = re.compile(r"^description:\s*(.+)\s*$", re.MULTILINE)


def validate_skill(folder: Path) -> list[str]:
    errors: list[str] = []
    skill = folder / "SKILL.md"
    if not skill.exists():
        return [f"{folder.name}: thiếu SKILL.md"]
    text = skill.read_text(encoding="utf-8").replace("\r\n", "\n")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        errors.append(f"{folder.name}: frontmatter không hợp lệ")
        return errors
    frontmatter = text.split("---", 2)[1]
    name = NAME_RE.search(frontmatter)
    description = DESCRIPTION_RE.search(frontmatter)
    if not name or name.group(1) != folder.name:
        errors.append(f"{folder.name}: name phải trùng tên thư mục")
    if not description or len(description.group(1).strip()) < 20:
        errors.append(f"{folder.name}: description quá ngắn hoặc thiếu")
    if re.search(r"\b(?:TODO|TBD|PLACEHOLDER)\b", text, re.IGNORECASE):
        errors.append(f"{folder.name}: còn placeholder")
    for md in folder.rglob("*.md"):
        content = md.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(content):
            target = match.group(1).split("#", 1)[0]
            if not target or re.match(r"^(?:https?:|mailto:|/)", target):
                continue
            if not (md.parent / target).resolve().exists():
                errors.append(f"{folder.name}: link hỏng {md.relative_to(folder)} -> {target}")
    return errors


def run(root: Path = Path("skills")) -> list[str]:
    errors: list[str] = []
    if not root.is_dir():
        return [f"Không tìm thấy thư mục skills: {root}"]
    for folder in sorted(path for path in root.iterdir() if path.is_dir()):
        errors.extend(validate_skill(folder))
    return errors


def main() -> int:
    errors = run(Path(sys.argv[1]) if len(sys.argv) > 1 else Path("skills"))
    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: cấu trúc và liên kết skill hợp lệ")
    return 0


if __name__ == "__main__":
    sys.exit(main())
