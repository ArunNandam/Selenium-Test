#from element import BasePageElement
from locators import MainPageLocators
from selenium.webdriver.common.keys import Keys


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def is_title_matches(self):
        """Verifies that the hardcoded text "Amazon" appears in page title"""

        return "Amazon" in self.driver.title


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def __init__(self, driver):
        super().__init__(driver)

    def is_results_found(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.SUBMIT_BUTTON)
        element.send_keys("Iphone")
        element.send_keys(Keys.RETURN)
        
        return "Iphone" in self.driver.title