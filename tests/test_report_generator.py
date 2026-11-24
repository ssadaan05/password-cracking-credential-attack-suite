import csv
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from modules import report_generator


class TestReportGenerator(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_report_dir = Path(self.temp_dir.name)

        self.patcher = patch.object(
            report_generator, "REPORT_DIR", self.test_report_dir
        )
        self.patcher.start()

        self.data = report_generator.prepare_report_data()

        self.audit_results = {
            "password_audit": {
                "common_password": True,
                "strength": "Very Weak",
                "score": 0,
                "recommendations": [
                    "Use a longer and less predictable password.",
                    "Avoid commonly used passwords."
                ]
            },
            "hash_results": [
                {"hash_number": 1, "analysis": "Possible format: MD5"},
                {"hash_number": 2, "analysis": "Possible format: SHA-1"},
                {"hash_number": 3, "analysis": "Possible format: SHA-256"},
                {"hash_number": 4, "analysis": "Possible format: SHA-256"}
            ]
        }

    def tearDown(self):
        self.patcher.stop()
        self.temp_dir.cleanup()

    def test_prepare_report_data(self):
        self.assertEqual(
            self.data[0],
            ["Security Check", "Result", "Status"]
        )

    def test_prepare_report_data_uses_audit_results(self):
        data = report_generator.prepare_report_data(
            self.audit_results
        )

        self.assertIn("Found in common password list", data[1][1])
        self.assertEqual(data[2][1], "0/4 - Very Weak")
        self.assertEqual(data[3][1], "4 sample hashes analyzed")
        self.assertIn(
            "Avoid commonly used passwords.",
            data[4][1]
        )

    def test_generate_txt_report(self):
        file_path = report_generator.generate_txt_report(self.data)

        self.assertTrue(file_path.exists())
        self.assertIn(
            "PASSWORD SECURITY AUDIT REPORT",
            file_path.read_text()
        )

    def test_dynamic_txt_report(self):
        data = report_generator.prepare_report_data(
            self.audit_results
        )

        file_path = report_generator.generate_txt_report(data)
        content = file_path.read_text(encoding="utf-8")

        self.assertIn("Found in common password list", content)
        self.assertIn("0/4 - Very Weak", content)
        self.assertIn("4 sample hashes analyzed", content)
        self.assertIn("Avoid commonly used passwords.", content)
        self.assertNotIn("Sample password: password", content)

    def test_generate_csv_report(self):
        file_path = report_generator.generate_csv_report(self.data)

        self.assertTrue(file_path.exists())

        with open(file_path, newline="", encoding="utf-8") as file:
            rows = list(csv.reader(file))

        self.assertEqual(len(rows), 5)
        self.assertEqual(rows[0][0], "Security Check")

    def test_generate_pdf_report(self):
        file_path = report_generator.generate_pdf_report(self.data)

        self.assertTrue(file_path.exists())

        with open(file_path, "rb") as file:
            self.assertTrue(file.read(5).startswith(b"%PDF-"))

    def test_all_report_formats(self):
        txt = report_generator.generate_txt_report(self.data)
        csv_file = report_generator.generate_csv_report(self.data)
        pdf = report_generator.generate_pdf_report(self.data)

        self.assertTrue(txt.exists())
        self.assertTrue(csv_file.exists())
        self.assertTrue(pdf.exists())


if __name__ == "__main__":
    unittest.main()
