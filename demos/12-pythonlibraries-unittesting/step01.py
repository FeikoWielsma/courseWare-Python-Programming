import unittest


class TestBasic(unittest.TestCase):
    "Basic tests"

    def test_basic(self):
        a = 1
        self.assert_equal(2, a)

    def test_basic_2(self):
        a = 1
        assert a == 1
