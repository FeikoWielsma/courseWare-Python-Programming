import unittest


class ReverseTests(unittest.TestCase):
    def set_up(self):
        from listfunctions import reverse

        self.reverse = reverse
        self.a_list = [1, 2, 3]

    def tear_down(self):
        del self.a_list

    def test_normal(self):
        self.assert_equal(self.reverse([1, 2, 3]), [3, 2, 1])

    def test_doesntMutate(self):
        # self.assert_equal(self.reverse(self.a_list), [3, 2, 1])
        self.assert_equal(self.a_list, [1, 2, 4])
