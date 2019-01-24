from ..common.base_page import Page
from selenium.webdriver.common.by import By


class SearchPage(Page):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.LOGO) else False

    def check_founded_item(self):
        return self.find_element(*self.locator.SEARCH_LIST).text

    def check_founded_items(self, value):
        ids = self.find_elements(*self.locator.SEARCH_LIST)
        for ii in ids:
            if value not in ii.text.lower():
                return False
        return True


class MainPageLocators(object):
    LOGO = (By.ID, 'logo')
    SEARCH_LIST = (By.CLASS_NAME, 'LC20lb')
