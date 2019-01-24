import unittest
from .common import driver
from .pages.main_page import *
from .pages.search_page import *


class TestsTwo(unittest.TestCase):

    def setUp(self):
        self.driver = driver.initialize()
        self.initPages()

    def test_opening_search_page(self):
        self.main.open("")
        self.main.search_item("apple")
        self.assertTrue(self.search.check_page_loaded())

    def test_finding_item_on_first_page(self):
        self.main.open("")
        self.main.search_item("apple")
        self.assertTrue(self.search.check_founded_items("apple"))

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
