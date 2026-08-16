"""Solution to Exercise 13, step 4 : the tests.

    python -m unittest test_calculator13.py -v
"""

import unittest

from calculator13 import add, divide, multiply, subtract


class TestCalculator(unittest.TestCase):
    """Every method starting with test is collected and run."""

    def setUp(self) -> None:
        # Values shared by the tests, rebuilt fresh before each one.
        self.a = 12
        self.b = 4

    def test_add(self) -> None:
        self.assertEqual(add(self.a, self.b), 16)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(self.a, self.b), 8)

    def test_multiply(self) -> None:
        self.assertEqual(multiply(self.a, self.b), 48)

    def test_divide(self) -> None:
        self.assertEqual(divide(self.a, self.b), 3)

    def test_divide_by_zero_raises(self) -> None:
        with self.assertRaises(ValueError):
            divide(self.a, 0)


if __name__ == "__main__":
    unittest.main()
