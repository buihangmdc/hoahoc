#!/usr/bin/env python3
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

SUPPORTED = {".pdf", ".docx", ".pptx", ".txt", ".md", ".csv", ".xlsx", ".png", ".jpg", ".jpeg", ".webp"}
HOUSEKEEPING = {"readme.md", "huong-dan.md", "hướng-dẫn.md", "manifest.json"}

def infer_grade(path: Path):
    text = str(path).lower().replace("_", "-")
    match = re.search(r"(?:lop|lớp)[-\s]*(6|7|8|9|10|11|12)\b", text)
    return int(match.group(1)) if match else None

def sha256(path: Path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()

def main():
    parser = argparse.ArgumentParser(description="Tạo manifest truy vết tài liệu giáo dục.")
    parser.add_argument("source", nargs="?", default="tai-lieu-dau-vao")
    parser.add_argument("--output", default="tai-lieu-dau-vao/manifest.json")
    args = parser.parse_args()
    source = Path(args.source).resolve()
    output = Path(args.output).resolve()
    generated_dir = output.parent if output.parent != source else None
    files = []
    for path in sorted(source.rglob("*")):
        if (
            not path.is_file()
            or path.resolve() == output
            or (generated_dir is not None and path.resolve().is_relative_to(generated_dir))
            or path.suffix.lower() not in SUPPORTED
            or path.name.lower() in HOUSEKEEPING
        ):
            continue
        stat = path.stat()
        files.append({
            "relative_path": path.relative_to(source).as_posix(),
            "extension": path.suffix.lower(),
            "size_bytes": stat.st_size,
            "grade_inferred": infer_grade(path),
            "sha256": sha256(path),
        })
    first_by_hash = {}
    duplicate_groups = {}
    for item in files:
        digest = item["sha256"]
        if digest in first_by_hash:
            item["duplicate_of"] = first_by_hash[digest]
            duplicate_groups.setdefault(digest, [first_by_hash[digest]]).append(item["relative_path"])
        else:
            first_by_hash[digest] = item["relative_path"]
            item["duplicate_of"] = None
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_root": str(source),
        "file_count": len(files),
        "unique_file_count": len(first_by_hash),
        "duplicate_groups": [
            {"sha256": digest, "files": paths}
            for digest, paths in sorted(duplicate_groups.items())
        ],
        "files": files,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Đã lập manifest {len(files)} tệp: {output}")
    unresolved = [item["relative_path"] for item in files if item["grade_inferred"] is None]
    if unresolved:
        print(
            f"CẢNH BÁO: {len(unresolved)} tệp KHÔNG suy luận được lớp từ tên/đường dẫn "
            "(cần 'lop-N' hoặc 'lớp N'). Phải xác nhận lớp thủ công trước khi lưu vào "
            "kho-tai-lieu/vat-ly/lop-<n>/ — không được để lại ngoài cấu trúc lop-<n>/:"
        )
        for relative_path in unresolved:
            print(f"  - {relative_path}")

if __name__ == "__main__":
    main()
