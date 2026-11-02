"""AI-assisted synthetic demonstration; not human soft-skill evidence."""
import unittest
from total import total


class TotalTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(total([]), 0)

    def test_positive(self):
        self.assertEqual(total([1, 2, 3]), 6)

    def test_mixed(self):
        self.assertEqual(total([-2, 0, 5]), 3)


if __name__ == "__main__":
    unittest.main()
