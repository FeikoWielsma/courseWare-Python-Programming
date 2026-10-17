from selenium import webdriver
import unittest


class GoogleTestCase(unittest.TestCase):
    def set_up(self):
        self.browser = webdriver.Chrome()
        self.add_cleanup(self.browser.quit)

    def test_page_title(self):
        self.browser.get("http://www.google.com")
        self.assert_in("Google", self.browser.title)


if __name__ == "__main__":
    unittest.main(verbosity=2)
