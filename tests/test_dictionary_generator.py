import unittest
import tempfile
from pathlib import Path

from modules.dictionary_generator import (
    validate_limit,
    generate_variations,
    build_candidates,
    save_wordlist
)


class TestDictionaryGenerator(unittest.TestCase):

    def test_generate_variations(self):
        result = generate_variations("sadaan")

        self.assertIn("sadaan", result)
        self.assertIn("SADAAN", result)
        self.assertIn("Sadaan", result)
        self.assertIn("sadaan1", result)
        self.assertIn("sadaan!", result)
        self.assertIn("54d44n", result)

    def test_duplicate_removal(self):
        profiles = [{"name": "Aarav"}]
        common = ["password", "password"]

        result = build_candidates(profiles, common, 100)

        self.assertEqual(len(result), len(set(result)))

    def test_maximum_entry_limit(self):
        profiles = [{"name": "Aarav"}]
        common = ["password", "admin", "welcome"]

        result = build_candidates(profiles, common, 2)

        self.assertLessEqual(len(result), 2)

    def test_invalid_limit(self):
        with self.assertRaises(ValueError):
            validate_limit(0)

    def test_save_wordlist(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "test.txt"

            count = save_wordlist(
                ["sample1", "sample2"],
                output
            )

            self.assertEqual(count, 2)
            self.assertTrue(output.exists())


if __name__ == "__main__":
    unittest.main()
