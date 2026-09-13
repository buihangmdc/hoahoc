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

from datetime import date
from pathlib import Path
from urllib.parse import urlparse


KINDS = {"image", "video", "tts", "post"}


def validate(data: object, today: date | None = None) -> list[str]:
    today = today or date.today()
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["Root phải là object."]
    if data.get("schema_version") != "1.0":
        errors.append("schema_version phải là 1.0.")
    tools = data.get("tools")
    if not isinstance(tools, list):
        return errors + ["tools phải là array."]
    seen: set[str] = set()
    for index, tool in enumerate(tools):
        prefix = f"tools[{index}]"
        if not isinstance(tool, dict):
            errors.append(f"{prefix} phải là object.")
            continue
        tool_id = tool.get("id")
        if not isinstance(tool_id, str) or not tool_id.strip():
            errors.append(f"{prefix}.id bị thiếu.")
        elif tool_id in seen:
            errors.append(f"{prefix}.id bị trùng: {tool_id}.")
        else:
            seen.add(tool_id)
        if tool.get("kind") not in KINDS:
            errors.append(f"{prefix}.kind không hợp lệ.")
        if not isinstance(tool.get("enabled"), bool):
            errors.append(f"{prefix}.enabled phải là boolean.")
            continue
        if not tool["enabled"]:
            continue
        for field in ("provider", "model", "verified_at", "expires_at", "official_source_url"):
            if not isinstance(tool.get(field), str) or not tool[field].strip():
                errors.append(f"{prefix}.{field} bắt buộc khi enabled=true.")
        source = tool.get("official_source_url")
        if isinstance(source, str) and source:
            parsed = urlparse(source)
            if parsed.scheme != "https" or not parsed.netloc:
                errors.append(f"{prefix}.official_source_url phải là HTTPS URL.")
        try:
            expires = date.fromisoformat(str(tool.get("expires_at")))
            if expires < today:
                errors.append(f"{prefix} đã hết hạn xác minh từ {expires.isoformat()}.")
        except ValueError:
            if tool.get("expires_at"):
                errors.append(f"{prefix}.expires_at phải theo YYYY-MM-DD.")
        capabilities = tool.get("capabilities")
        if not isinstance(capabilities, dict):
            errors.append(f"{prefix}.capabilities bắt buộc khi enabled=true.")
        elif tool.get("kind") == "video":
            cap = capabilities.get("max_clip_seconds")
            if not isinstance(cap, (int, float)) or cap <= 0:
                errors.append(f"{prefix}.capabilities.max_clip_seconds phải là số dương.")
            if not isinstance(capabilities.get("modes"), list) or not capabilities["modes"]:
                errors.append(f"{prefix}.capabilities.modes không được rỗng.")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Kiểm tra capability manifest của công cụ media")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}")
        return 1
    errors = validate(data)
    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    enabled = sum(bool(tool.get("enabled")) for tool in data.get("tools", []) if isinstance(tool, dict))
    print(f"PASS: capability manifest hợp lệ; enabled_tools={enabled}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
