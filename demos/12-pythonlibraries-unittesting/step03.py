import unittest


class ReverseTests(unittest.TestCase):
    def test_normal(self):
        # do import here, makes test independent
        from listfunctions import reverse

        # can use python's normal asserts
        assert reverse([1, 2, 3]) == [3, 2, 1]

        # or more robust and informative unittest options
        self.assert_equal(reverse([1, 2, 3]), [3, 2, 1])
