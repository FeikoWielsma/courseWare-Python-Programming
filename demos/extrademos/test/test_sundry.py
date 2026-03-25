"""Do a minimal test of all the modules that aren't otherwise tested."""

from test import support
import sys
import unittest


class TestUntestedModules(unittest.TestCase):
    def test_at_least_import_untested_modules(self):
        with support.check_warnings(quiet=True):
            if sys.platform.startswith("win"):
                pass

            if sys.platform.startswith("win"):
                pass

            try:
                import tty  # not available on Windows
            except ImportError:
                if support.verbose:
                    print("skipping tty")


def test_main():
    support.run_unittest(TestUntestedModules)


if __name__ == "__main__":
    test_main()
