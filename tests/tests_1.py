import unittest
from .common import driver
from .pages.main_page import *
from .pages.search_page import *


class TestsOne(unittest.TestCase):

    def setUp(self):
        self.driver = driver.initialize()
        self.initPages()

    def test_opening_main_page(self):
        self.main.open("")
        self.assertTrue(self.main.check_page_loaded())

    # will fail to show how work assertion
    def test_finding_item_in_first_row(self):
        self.main.open("")
        self.main.search_item("iphone x")
        search_result = self.search.check_founded_item()
        self.assertIn("iphone xx", search_result)

    # as a previous test but will be pass
    def test_finding_item_in_first_row_1(self):
        self.main.open("")
        self.main.search_item("iphone x")
        search_result = self.search.check_founded_item()
        self.assertIn("iPhone X", search_result)

    def tearDown(self):
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        driver.close_driver()

    def initPages(self):
        self.main = MainPage(self.driver)
        self.search = SearchPage(self.driver)


if __name__ == "__main__":
    unittest.main()
