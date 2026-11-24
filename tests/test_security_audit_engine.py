import unittest
from modules.security_audit_engine import (
    check_common_password,
    audit_password,
    audit_sample_hashes,
)


class TestSecurityAuditEngine(unittest.TestCase):

    def test_common_password_detection(self):
        self.assertTrue(check_common_password("password"))

    def test_uncommon_password_detection(self):
        self.assertFalse(
            check_common_password("unique-example-phrase-928!")
        )

    def test_password_audit_returns_results(self):
        result = audit_password("password")

        self.assertIsInstance(result, dict)
        self.assertTrue(result["common_password"])
        self.assertEqual(result["score"], 0)
        self.assertEqual(result["strength"], "Very Weak")
        self.assertIn(
            "Avoid commonly used passwords.",
            result["recommendations"]
        )

    def test_sample_hash_audit_returns_results(self):
        result = audit_sample_hashes()

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0]["hash_number"], 1)
        self.assertIn("MD5", result[0]["analysis"])

    def test_common_password_case_insensitive(self):
        self.assertTrue(check_common_password("PASSWORD"))


if __name__ == "__main__":
    unittest.main()
