from selenium.webdriver.common.keys import Keys
from ..common.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.LOGO) else False

    def search_item(self, item):
        self.find_element(*self.locator.SEARCH_FIELD).send_keys(item)
        self.find_element(*self.locator.SEARCH_FIELD).send_keys(Keys.ENTER)


class MainPageLocators(object):
    LOGO = (By.ID, 'hplogo')
    SEARCH_FIELD = (By.CSS_SELECTOR, '[name=q]')
