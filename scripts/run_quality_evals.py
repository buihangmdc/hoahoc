#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

from pathlib import Path


DOMAINS = {"science", "pedagogy", "safety", "language", "video", "source"}
STATUSES = {"PASS", "FAIL"}


def validate_corpus(data: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict) or data.get("schema_version") != "1.0":
        return ["Corpus phải là object với schema_version=1.0."]
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        return ["cases phải là array không rỗng."]
    ids: set[str] = set()
    for index, case in enumerate(cases):
        prefix = f"cases[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{prefix} phải là object.")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id:
            errors.append(f"{prefix}.id bị thiếu.")
        elif case_id in ids:
            errors.append(f"{prefix}.id bị trùng: {case_id}.")
        else:
            ids.add(case_id)
        if case.get("domain") not in DOMAINS:
            errors.append(f"{prefix}.domain không hợp lệ.")
        if case.get("expected_status") not in STATUSES:
            errors.append(f"{prefix}.expected_status không hợp lệ.")
        if not isinstance(case.get("input"), str) or not case["input"].strip():
            errors.append(f"{prefix}.input bị thiếu.")
        for field in ("must_include", "must_not_include"):
            value = case.get(field)
            if not isinstance(value, list) or not all(isinstance(item, str) and item for item in value):
                errors.append(f"{prefix}.{field} phải là array chuỗi không rỗng.")
    if len(cases) < 20:
        errors.append("Corpus phải có ít nhất 20 ca.")
    missing_domains = DOMAINS - {case.get("domain") for case in cases if isinstance(case, dict)}
    if missing_domains:
        errors.append("Thiếu domain: " + ", ".join(sorted(missing_domains)))
    return errors


def score_responses(data: dict, responses: Path) -> dict:
    rows = []
    for case in data["cases"]:
        path = responses / f"{case['id']}.txt"
        if not path.exists():
            rows.append({"id": case["id"], "status": "MISSING", "missing": case["must_include"], "forbidden": []})
            continue
        text = path.read_text(encoding="utf-8").casefold()
        missing = [term for term in case["must_include"] if term.casefold() not in text]
        forbidden = [term for term in case["must_not_include"] if term.casefold() in text]
        rows.append({"id": case["id"], "status": "PASS" if not missing and not forbidden else "FAIL", "missing": missing, "forbidden": forbidden})
    return {"passed": sum(row["status"] == "PASS" for row in rows), "total": len(rows), "cases": rows}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate or score the golden evaluation corpus")
    parser.add_argument("corpus", type=Path, nargs="?", default=Path("evals/golden-cases.json"))
    parser.add_argument("--responses", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.corpus.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}")
        return 1
    errors = validate_corpus(data)
    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    if not args.responses:
        print(f"PASS: golden corpus hợp lệ; cases={len(data['cases'])}; domains={len(DOMAINS)}")
        return 0
    result = score_responses(data, args.responses)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["passed"] == result["total"] else 1


if __name__ == "__main__":
    sys.exit(main())
