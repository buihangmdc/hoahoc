import unittest
from datetime import date

from scripts.validate_tool_capabilities import validate


class ToolCapabilitiesTests(unittest.TestCase):
    def test_empty_disabled_config_is_valid(self):
        self.assertEqual([], validate({"schema_version": "1.0", "tools": []}))

    def test_enabled_video_requires_verified_capabilities(self):
        data = {"schema_version": "1.0", "tools": [{"id": "v", "kind": "video", "enabled": True}]}
        self.assertGreater(len(validate(data)), 0)

    def test_expired_tool_fails(self):
        data = {
            "schema_version": "1.0",
            "tools": [{
                "id": "v", "kind": "video", "enabled": True,
                "provider": "P", "model": "M",
                "verified_at": "2026-01-01", "expires_at": "2026-02-01",
                "official_source_url": "https://example.com/docs",
                "capabilities": {"max_clip_seconds": 8, "modes": ["image-to-video"]}
            }]
        }
        self.assertTrue(any("hết hạn" in error for error in validate(data, today=date(2026, 7, 14))))


if __name__ == "__main__":
    unittest.main()
