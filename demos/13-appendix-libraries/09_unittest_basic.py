"""A test case is a class of methods whose names start with test.

Run it either way :

    uv run python 09_unittest_basic.py
    uv run python -m unittest 09_unittest_basic.py
"""

import unittest


def add(a, b):
    return a + b


class TestAdd(unittest.TestCase):
    def test_two_positives(self):
        self.assertEqual(add(2, 3), 5)

    def test_with_zero(self):
        self.assertEqual(add(0, 7), 7)

    def test_negative(self):
        self.assertEqual(add(-2, -3), -5)


if __name__ == "__main__":
    unittest.main()
