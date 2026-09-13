import unittest

from scripts.validate_skills import run


class SkillStructureTests(unittest.TestCase):
    def test_all_project_skills(self):
        self.assertEqual([], run())


if __name__ == "__main__":
    unittest.main()
