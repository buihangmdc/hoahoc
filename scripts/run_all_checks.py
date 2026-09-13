#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(label: str, *args: str) -> bool:
    print(f"\n=== {label} ===", flush=True)
    completed = subprocess.run(args, cwd=ROOT)
    return completed.returncode == 0


def strict_packages() -> list[Path]:
    return sorted({path.parent for path in (ROOT / "dau-ra").rglob("CLIP-MANIFEST.json")})


def main() -> int:
    python = sys.executable
    checks = [
        run("UNIT TESTS", python, "-m", "unittest", "discover", "-s", "tests", "-v"),
        run("SKILLS", python, "scripts/validate_skills.py"),
        run("TOOL CAPABILITIES", python, "scripts/validate_tool_capabilities.py", "config/tool-capabilities.json"),
        run("GOLDEN CORPUS", python, "scripts/run_quality_evals.py", "evals/golden-cases.json"),
        run("OUTPUT LINT", python, "scripts/validate_package.py", "dau-ra", "--mode", "lint"),
    ]
    for package in strict_packages():
        checks.append(run(f"STRICT {package.relative_to(ROOT)}", python, "scripts/validate_package.py", str(package), "--mode", "strict"))
    summary = {"passed": sum(checks), "total": len(checks), "strict_packages": len(strict_packages())}
    print("\n" + json.dumps(summary, ensure_ascii=False))
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
