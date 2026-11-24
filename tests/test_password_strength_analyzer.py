import unittest
from unittest.mock import patch
from io import StringIO

from modules.password_strength_analyzer import analyze_password


class TestPasswordStrengthAnalyzer(unittest.TestCase):

    def test_weak_password_score(self):
        result = analyze_password("123456")

        self.assertIsNone(result)

    def test_stronger_password_analysis(self):
        result = analyze_password("correct-horse-battery-staple-92!")

        self.assertIsNone(result)

    def test_password_is_masked(self):
        with patch("sys.stdout", new_callable=StringIO) as output:
            analyze_password("Password123!")

        self.assertIn("Password: ************", output.getvalue())

    def test_strength_analysis_heading(self):
        with patch("sys.stdout", new_callable=StringIO) as output:
            analyze_password("Password123!")

        self.assertIn(
            "PASSWORD STRENGTH ANALYSIS",
            output.getvalue()
        )

    def test_security_feedback_heading(self):
        with patch("sys.stdout", new_callable=StringIO) as output:
            analyze_password("Password123!")

        self.assertIn(
            "SECURITY FEEDBACK",
            output.getvalue()
        )


if __name__ == "__main__":
    unittest.main()
