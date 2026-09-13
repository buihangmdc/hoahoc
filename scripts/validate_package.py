#!/usr/bin/env python3
"""Kiểm tra tĩnh gói giáo dục/video; không thay thế duyệt chuyên môn."""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable


TEXT_EXTENSIONS = {".md", ".txt", ".json", ".yaml", ".yml", ".srt", ".csv", ".tsv"}
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|PLACEHOLDER)\b", re.IGNORECASE)
FORBIDDEN_STYLE_RE = re.compile(
    r"(?:in\s+the\s+style\s+of|manabie\s+channel\s+style|kurzgesagt\s+style|3blue1brown\s+aesthetic)",
    re.IGNORECASE,
)
VIDEO_HINT_RE = re.compile(r"(?:video[-_ ]?prompts?|storyboard|clip[-_ ]?manifest|prompt-video)", re.IGNORECASE)
SOURCE_HINT_RE = re.compile(r"(?:nguon[-_ ]?su[-_ ]?dung|source[-_ ]?map|sources?)", re.IGNORECASE)
MANIFEST_HINT_RE = re.compile(r"clip[-_ ]?manifest", re.IGNORECASE)
FORMULA_ID_HINT_RE = re.compile(r"FORMULA-ID|FORMULA-LOCK", re.IGNORECASE)
FORMULA_LEDGER_NAME_RE = re.compile(r"formula[-_ ]?ledger", re.IGNORECASE)
LEGACY_CLIP_ID_RE = re.compile(r"\bSCENE[-\s]\d+[-\s][A-C]\b|\bSCENE-ID\b|\bSHOT-ID\b", re.IGNORECASE)
# Phát hiện dấu "+" sau Q trong công thức nhiệt động khi không bị phủ định
WRONG_THERMO_SIGN_RE = re.compile(r"ΔU\s*=\s*Q\s*\+\s*A(?!_)", re.UNICODE)


@dataclass(frozen=True)
class Issue:
    id: str
    severity: str
    file: str
    line: int | None
    message: str
    fix: str
    gate: str = "production"


class PackageValidator:
    def __init__(
        self,
        target: Path,
        mode: str = "lint",
        max_clip_seconds: float | None = None,
        tolerance_percent: float | None = None,
    ) -> None:
        self.target = target.resolve()
        self.mode = mode
        self.max_clip_seconds = max_clip_seconds
        self.tolerance_percent = tolerance_percent
        self.issues: list[Issue] = []
        self._counter = 0
        self.text_files: list[Path] = []
        self.json_values: dict[Path, Any] = {}

    def add(
        self,
        severity: str,
        code: str,
        path: Path,
        line: int | None,
        message: str,
        fix: str,
        gate: str = "production",
    ) -> None:
        self._counter += 1
        issue_id = f"{code}-{self._counter:03d}"
        self.issues.append(Issue(issue_id, severity, self._display(path), line, message, fix, gate))

    def _display(self, path: Path) -> str:
        try:
            return str(path.resolve().relative_to(self.target if self.target.is_dir() else self.target.parent))
        except ValueError:
            return str(path.resolve())

    def files(self) -> Iterable[Path]:
        if self.target.is_file():
            yield self.target
            return
        for path in sorted(self.target.rglob("*")):
            if path.is_file() and not any(part in {".git", "__pycache__"} for part in path.parts):
                yield path

    def scan_text(self, path: Path) -> None:
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            return
        self.text_files.append(path)
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            self.add(
                "MAJOR",
                "ENCODING",
                path,
                None,
                "Tệp văn bản không đọc được bằng UTF-8.",
                "Chuyển tệp sang UTF-8 và kiểm tra lại dấu tiếng Việt.",
            )
            return

        for line_no, line in enumerate(content.splitlines(), start=1):
            if PLACEHOLDER_RE.search(line):
                self.add(
                    "BLOCKER",
                    "PLACEHOLDER",
                    path,
                    line_no,
                    "Còn nội dung giữ chỗ trong gói bàn giao.",
                    "Điền nội dung thật hoặc đánh trạng thái INCOMPLETE ngoài thư mục phát hành.",
                )
            if FORBIDDEN_STYLE_RE.search(line):
                self.add(
                    "MAJOR",
                    "STYLE_IMITATION",
                    path,
                    line_no,
                    "Prompt yêu cầu bắt chước trực tiếp phong cách nhận diện của bên thứ ba.",
                    "Đổi sang thuộc tính chức năng trung tính và yêu cầu thiết kế nguyên bản.",
                )
            if LEGACY_CLIP_ID_RE.search(line) and not FORMULA_LEDGER_NAME_RE.search(path.name):
                self.add(
                    "MINOR",
                    "LEGACY_CLIP_ID",
                    path,
                    line_no,
                    "Dùng định danh CLIP kiểu cũ (SCENE-X-A/SCENE-ID/SHOT-ID) thay vì SC0X-A theo rules/CONG-THUC-SCENE-WORD.md.",
                    "Đổi sang định dạng SC0X-A/B/C cho CLIP-ID; SCENE chỉ dùng cho đơn vị sư phạm SC01, SC02...",
                )
            if WRONG_THERMO_SIGN_RE.search(line):
                # Bỏ qua nếu dòng này hoặc dòng liền kề có từ phủ định
                lines = content.splitlines()
                ctx_start = max(0, line_no - 2)
                ctx_end = min(len(lines), line_no + 1)
                context_block = " ".join(lines[ctx_start:ctx_end])
                if not re.search(r"KHÔNG|không|TUYỆT ĐỐI|tuyệt đối|wrong|incorrect|sai", context_block, re.IGNORECASE):
                    self.add(
                        "MAJOR",
                        "FORMULA_SIGN_ERROR",
                        path,
                        line_no,
                        "Công thức 'ΔU = Q + A' có thể sai quy ước dấu SGK KNTT (đúng: ΔU = Q − A, A = công hệ thực hiện).",
                        "Kiểm tra quy ước dấu: nếu dùng ΔU = Q + A thì A phải là công ngoại lực; nếu dùng ΔU = Q − A thì A là công hệ thực hiện. Giữ nhất quán xuyên suốt gói.",
                        gate="science",
                    )

        if path.suffix.lower() == ".json":
            try:
                self.json_values[path] = json.loads(content)
            except json.JSONDecodeError as exc:
                self.add(
                    "BLOCKER",
                    "JSON_INVALID",
                    path,
                    exc.lineno,
                    f"JSON không hợp lệ: {exc.msg}.",
                    "Sửa cú pháp JSON trước khi chạy pipeline.",
                )

    def is_video_package(self) -> bool:
        return VIDEO_HINT_RE.search(str(self.target)) is not None or any(
            VIDEO_HINT_RE.search(path.name) for path in self.text_files
        )

    def manifests(self) -> list[tuple[Path, dict[str, Any]]]:
        found: list[tuple[Path, dict[str, Any]]] = []
        for path, value in self.json_values.items():
            if isinstance(value, dict) and (MANIFEST_HINT_RE.search(path.name) or "clips" in value):
                found.append((path, value))
        return found

    def validate_manifest(self, path: Path, data: dict[str, Any]) -> None:
        clips = data.get("clips")
        if not isinstance(clips, list) or not clips:
            self.add("BLOCKER", "CLIPS_MISSING", path, None, "Manifest không có danh sách clip hợp lệ.", "Thêm mảng clips không rỗng.")
            return

        cap = self.max_clip_seconds if self.max_clip_seconds is not None else data.get("max_clip_seconds")
        target_duration = data.get("target_duration_seconds")
        tolerance = self.tolerance_percent if self.tolerance_percent is not None else data.get("tolerance_percent", 5)

        if not isinstance(cap, (int, float)) or cap <= 0:
            self.add("MAJOR", "CAP_MISSING", path, None, "Thiếu max_clip_seconds hợp lệ.", "Ghi giới hạn từ năng lực công cụ hoặc giả định có nhãn.")
            cap = None
        if not isinstance(target_duration, (int, float)) or target_duration <= 0:
            self.add("MAJOR", "TARGET_DURATION_MISSING", path, None, "Thiếu target_duration_seconds hợp lệ.", "Ghi thời lượng mục tiêu của gói.")
            target_duration = None
        if not isinstance(tolerance, (int, float)) or tolerance < 0:
            self.add("MAJOR", "TOLERANCE_INVALID", path, None, "tolerance_percent không hợp lệ.", "Dùng số không âm, mặc định 5.")
            tolerance = 5

        ids: set[str] = set()
        durations: list[float] = []
        previous_id: str | None = None
        required_text = ("id", "scene_id", "start_state", "action", "end_state", "video_prompt_ref")

        for index, clip in enumerate(clips, start=1):
            if not isinstance(clip, dict):
                self.add("BLOCKER", "CLIP_INVALID", path, None, f"Clip #{index} không phải object.", "Đổi clip thành object có đủ trường bắt buộc.")
                continue
            clip_id = clip.get("id")
            for field in required_text:
                value = clip.get(field)
                if not isinstance(value, str) or not value.strip():
                    self.add("MAJOR", "CLIP_FIELD_MISSING", path, None, f"Clip #{index} thiếu trường {field}.", f"Điền {field} rõ ràng cho từng clip.")
            if isinstance(clip_id, str) and clip_id.strip():
                if clip_id in ids:
                    self.add("BLOCKER", "CLIP_ID_DUPLICATE", path, None, f"Trùng clip id {clip_id}.", "Mỗi clip phải có ID duy nhất.")
                ids.add(clip_id)

            duration = clip.get("duration_seconds")
            if not isinstance(duration, (int, float)) or not math.isfinite(float(duration)) or duration <= 0:
                self.add("BLOCKER", "DURATION_INVALID", path, None, f"Clip {clip_id or index} có duration không hợp lệ.", "Dùng số giây dương.")
            else:
                durations.append(float(duration))
                if cap is not None and duration > cap + 1e-9:
                    self.add("BLOCKER", "CLIP_OVER_CAP", path, None, f"Clip {clip_id or index} dài {duration}s, vượt giới hạn {cap}s.", "Tách clip hoặc chọn cấu hình công cụ hỗ trợ thời lượng này.")

            if previous_id is not None:
                start_from = clip.get("start_from")
                reset_reason = clip.get("continuity_reset_reason")
                if not start_from and not reset_reason:
                    self.add("MINOR", "CONTINUITY_LINK_MISSING", path, None, f"Clip {clip_id or index} chưa khai báo start_from hoặc lý do reset.", "Liên kết end state của clip trước hoặc ghi lý do cắt cảnh.")
                elif start_from and start_from not in ids:
                    self.add("MAJOR", "CONTINUITY_LINK_INVALID", path, None, f"Clip {clip_id or index} tham chiếu start_from chưa tồn tại: {start_from}.", "Tham chiếu một clip trước đó hoặc dùng continuity_reset_reason.")
            previous_id = clip_id if isinstance(clip_id, str) and clip_id else previous_id

            if str(clip.get("status", "")).upper() == "READY":
                media_path = clip.get("media_path")
                if not isinstance(media_path, str) or not media_path.strip():
                    self.add("BLOCKER", "READY_WITHOUT_MEDIA", path, None, f"Clip {clip_id or index} ghi READY nhưng thiếu media_path.", "Thêm tệp media thật hoặc đổi trạng thái thành PLANNED/NOT_RENDERED.")
                else:
                    resolved = (path.parent / media_path).resolve()
                    if not resolved.exists():
                        self.add("BLOCKER", "MEDIA_NOT_FOUND", path, None, f"Clip {clip_id or index} ghi READY nhưng không tìm thấy {media_path}.", "Tạo tệp media hoặc sửa trạng thái/path.")

        if target_duration is not None and durations:
            actual = sum(durations)
            allowed = target_duration * float(tolerance) / 100
            if abs(actual - target_duration) > allowed + 1e-9:
                self.add("MAJOR", "TOTAL_DURATION_MISMATCH", path, None, f"Tổng clip {actual:g}s lệch mục tiêu {target_duration:g}s quá {tolerance:g}%.", "Điều chỉnh duration hoặc timeline mục tiêu.")

    def has_formula_content(self) -> bool:
        for path in self.text_files:
            if FORMULA_LEDGER_NAME_RE.search(path.name):
                continue
            try:
                if FORMULA_ID_HINT_RE.search(path.read_text(encoding="utf-8")):
                    return True
            except UnicodeDecodeError:
                continue
        return False

    def strict_checks(self) -> None:
        if self.has_formula_content() and not any(
            FORMULA_LEDGER_NAME_RE.search(path.name) for path in self.text_files
        ):
            self.add(
                "MAJOR",
                "FORMULA_LEDGER_MISSING",
                self.target,
                None,
                "Gói có FORMULA-ID/FORMULA-LOCK nhưng thiếu FORMULA-LEDGER.md.",
                "Tạo FORMULA-LEDGER.md theo skills/thiet-ke-bai-day-vat-ly/assets/mau-formula-ledger.md.",
                gate="science",
            )
        if not self.is_video_package():
            return
        manifests = self.manifests()
        if not manifests:
            self.add("MAJOR", "MANIFEST_MISSING", self.target, None, "Gói video chưa có CLIP-MANIFEST.json.", "Tạo manifest theo mau/clip-manifest.example.json.")
        if not any(SOURCE_HINT_RE.search(path.name) for path in self.text_files):
            self.add("MAJOR", "SOURCES_MISSING", self.target, None, "Gói video chưa có tệp nguồn sử dụng/source map.", "Thêm nguồn và vị trí đã dùng.", gate="science")

    def run(self) -> dict[str, Any]:
        if not self.target.exists():
            self.add("BLOCKER", "TARGET_NOT_FOUND", self.target, None, "Không tìm thấy đường dẫn cần kiểm tra.", "Kiểm tra lại đường dẫn.")
        else:
            for path in self.files():
                self.scan_text(path)
            for path, data in self.manifests():
                self.validate_manifest(path, data)
            if self.mode == "strict":
                self.strict_checks()

        counts = {level.lower(): sum(issue.severity == level for issue in self.issues) for level in ("BLOCKER", "MAJOR", "MINOR")}
        if counts["blocker"] or counts["major"]:
            status = "FAIL"
        elif counts["minor"]:
            status = "PASS_WITH_NOTES"
        else:
            status = "PASS"
        return {
            "status": status,
            "target": str(self.target),
            "mode": self.mode,
            "counts": counts,
            "machine_scope": "Kiểm tra tĩnh; phải duyệt khoa học và sư phạm độc lập.",
            "issues": [asdict(issue) for issue in self.issues],
        }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Kiểm tra tĩnh gói AI Agent Giáo viên")
    parser.add_argument("target", type=Path)
    parser.add_argument("--mode", choices=("lint", "strict"), default="lint")
    parser.add_argument("--max-clip-seconds", type=float)
    parser.add_argument("--tolerance-percent", type=float)
    parser.add_argument("--json-output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = PackageValidator(args.target, args.mode, args.max_clip_seconds, args.tolerance_percent).run()
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] in {"PASS", "PASS_WITH_NOTES"} else 1


if __name__ == "__main__":
    sys.exit(main())
