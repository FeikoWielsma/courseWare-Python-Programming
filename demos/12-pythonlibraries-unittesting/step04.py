import unittest


# Here's our "unit".
def IsOdd(n):
    return n % 2 == 1


# Here's our "unit tests".
class IsOddTests(unittest.TestCase):
    def test_one(self):
        self.assert_true(IsOdd(2))

    def test_two(self):
        self.assert_false(IsOdd(1))


def main():
    unittest.main()


if __name__ == "__main__":
    main()
