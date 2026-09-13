import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_package import PackageValidator


def valid_manifest() -> dict:
    return {
        "target_duration_seconds": 16,
        "max_clip_seconds": 8,
        "tolerance_percent": 5,
        "clips": [
            {
                "id": "SC01-A",
                "scene_id": "SC01",
                "duration_seconds": 8,
                "start_state": "Bàn thí nghiệm trống",
                "action": "Đặt nam châm cạnh cuộn dây",
                "end_state": "Nam châm ở sát cuộn dây",
                "video_prompt_ref": "10-VIDEO-PROMPTS.md#SC01-A",
                "status": "PLANNED",
            },
            {
                "id": "SC01-B",
                "scene_id": "SC01",
                "duration_seconds": 8,
                "start_from": "SC01-A",
                "start_state": "Nam châm ở sát cuộn dây",
                "action": "Di chuyển nam châm vào cuộn dây",
                "end_state": "Kim điện kế lệch sang phải theo góc nhìn đã khóa",
                "video_prompt_ref": "10-VIDEO-PROMPTS.md#SC01-B",
                "status": "PLANNED",
            },
        ],
    }


class PackageValidatorTests(unittest.TestCase):
    def make_package(self, manifest: dict | None = None) -> Path:
        root = Path(tempfile.mkdtemp()) / "prompt-video"
        root.mkdir(parents=True)
        (root / "02-NGUON-SU-DUNG.md").write_text("Nguồn giáo viên cung cấp, trang 2.\n", encoding="utf-8")
        (root / "10-VIDEO-PROMPTS.md").write_text("# Video prompts\n", encoding="utf-8")
        if manifest is not None:
            (root / "08-CLIP-MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
        return root

    def test_valid_strict_package_passes(self):
        root = self.make_package(valid_manifest())
        result = PackageValidator(root, mode="strict").run()
        self.assertEqual("PASS", result["status"])

    def test_placeholder_is_blocker(self):
        root = self.make_package(valid_manifest())
        (root / "script.md").write_text("Nội dung TBD\n", encoding="utf-8")
        result = PackageValidator(root).run()
        self.assertEqual("FAIL", result["status"])
        self.assertIn("PLACEHOLDER", {issue["id"].rsplit("-", 1)[0] for issue in result["issues"]})

    def test_clip_over_cap_is_blocker(self):
        manifest = valid_manifest()
        manifest["clips"][0]["duration_seconds"] = 9
        manifest["target_duration_seconds"] = 17
        result = PackageValidator(self.make_package(manifest), mode="strict").run()
        self.assertTrue(any(issue["id"].startswith("CLIP_OVER_CAP") for issue in result["issues"]))

    def test_total_duration_mismatch_is_major(self):
        manifest = valid_manifest()
        manifest["target_duration_seconds"] = 60
        result = PackageValidator(self.make_package(manifest), mode="strict").run()
        self.assertTrue(any(issue["id"].startswith("TOTAL_DURATION_MISMATCH") for issue in result["issues"]))

    def test_ready_requires_real_media(self):
        manifest = valid_manifest()
        manifest["clips"][0]["status"] = "READY"
        manifest["clips"][0]["media_path"] = "media/SC01-A.mp4"
        result = PackageValidator(self.make_package(manifest), mode="strict").run()
        self.assertTrue(any(issue["id"].startswith("MEDIA_NOT_FOUND") for issue in result["issues"]))

    def test_named_style_imitation_is_major(self):
        root = self.make_package(valid_manifest())
        (root / "10-VIDEO-PROMPTS.md").write_text("Create it in the style of a famous channel.\n", encoding="utf-8")
        result = PackageValidator(root).run()
        self.assertTrue(any(issue["id"].startswith("STYLE_IMITATION") for issue in result["issues"]))

    def test_strict_video_package_requires_manifest(self):
        result = PackageValidator(self.make_package(), mode="strict").run()
        self.assertTrue(any(issue["id"].startswith("MANIFEST_MISSING") for issue in result["issues"]))


if __name__ == "__main__":
    unittest.main()
