"""setUp runs before every test, tearDown after every test."""

import unittest


class Basket:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def total(self):
        return len(self.items)


class TestBasket(unittest.TestCase):
    def setUp(self):
        # A fresh basket for every test, so no test can affect another.
        self.basket = Basket()

    def test_starts_empty(self):
        self.assertEqual(self.basket.total(), 0)

    def test_counts_items(self):
        self.basket.add("apple")
        self.basket.add("pear")
        self.assertEqual(self.basket.total(), 2)

    def test_raises_on_missing_method(self):
        with self.assertRaises(AttributeError):
            self.basket.remove("apple")


if __name__ == "__main__":
    unittest.main()
