import unittest

from modules.brute_force_simulator import (
    calculate_search_space,
    estimate_time,
    format_time,
)


class TestBruteForceSimulator(unittest.TestCase):

    def test_search_space_calculation(self):
        self.assertEqual(calculate_search_space(4, 10), 10000)

    def test_search_space_with_letters(self):
        self.assertEqual(calculate_search_space(2, 26), 676)

    def test_invalid_password_length(self):
        with self.assertRaises(ValueError):
            calculate_search_space(0, 10)

    def test_invalid_character_set_size(self):
        with self.assertRaises(ValueError):
            calculate_search_space(4, 0)

    def test_character_set_limit(self):
        with self.assertRaises(ValueError):
            calculate_search_space(4, 101)

    def test_estimated_time(self):
        self.assertEqual(estimate_time(10000, 1000), 10)

    def test_invalid_guess_rate(self):
        with self.assertRaises(ValueError):
            estimate_time(10000, 0)

    def test_format_time(self):
        self.assertEqual(format_time(30), "30.00 seconds")
        self.assertEqual(format_time(120), "2.00 minutes")
        self.assertEqual(format_time(7200), "2.00 hours")


if __name__ == "__main__":
    unittest.main()
