import json
import unittest
from pathlib import Path

from scripts.run_quality_evals import DOMAINS, validate_corpus


class QualityEvalCorpusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(Path("evals/golden-cases.json").read_text(encoding="utf-8"))

    def test_corpus_schema(self):
        self.assertEqual([], validate_corpus(self.data))

    def test_all_domains_are_covered(self):
        self.assertEqual(DOMAINS, {case["domain"] for case in self.data["cases"]})

    def test_has_at_least_twenty_cases(self):
        self.assertGreaterEqual(len(self.data["cases"]), 20)


if __name__ == "__main__":
    unittest.main()
