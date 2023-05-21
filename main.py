# THE STRUCTURE IS FOLLOWED FROM SELENIUM DOCUMENTATION

import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://www.amazon.com")

    def test_title_search(self):
        """Tests Amazon.com title"""
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()

    def test_search_results(self):
        searchpage = page.SearchResultsPage(self.driver)
        assert searchpage.is_results_found()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
