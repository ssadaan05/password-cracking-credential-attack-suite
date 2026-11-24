import unittest

from modules.hash_analyzer import (
    identify_hash,
    generate_hash
)


class TestHashAnalyzer(unittest.TestCase):

    def test_md5_identification(self):
        result = identify_hash(
            "5d41402abc4b2a76b9719d911017c592"
        )
        self.assertIn("MD5", result)

    def test_sha1_identification(self):
        result = identify_hash(
            "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"
        )
        self.assertIn("SHA-1", result)

    def test_sha256_identification(self):
        result = identify_hash(
            "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
        )
        self.assertIn("SHA-256", result)

    def test_invalid_hash(self):
        result = identify_hash("hello123")
        self.assertIn("Invalid", result)

    def test_sha256_generation(self):
        result = generate_hash("hello", "sha256")

        expected = (
            "2cf24dba5fb0a30e26e83b2ac5b9e29e1"
            "b161e5c1fa7425e73043362938b9824"
        )

        self.assertEqual(result, expected)

    def test_unsupported_algorithm(self):
        with self.assertRaises(ValueError):
            generate_hash("hello", "unsupported")


if __name__ == "__main__":
    unittest.main()
