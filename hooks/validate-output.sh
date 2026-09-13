#!/usr/bin/env bash
set -euo pipefail

target="${1:-dau-ra}"
mode="${2:-lint}"
python scripts/validate_package.py "$target" --mode "$mode"
