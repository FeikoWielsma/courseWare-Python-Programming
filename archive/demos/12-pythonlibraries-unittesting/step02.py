import unittest


class TestBasic2(unittest.TestCase):
    "Show setup and teardown"

    def set_up(self):
        self.a = 1

    def tear_down(self):
        del self.a

    def test_basic1(self):
        "Basic with setup"
        self.assert_not_equal(self.a, 2)

    def test_basic2(self):
        "Basic2 with setup"
        assert self.a != 2

    def test_fail(self):
        "This test should fail"
        assert self.a == 2
