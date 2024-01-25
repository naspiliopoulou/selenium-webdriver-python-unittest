import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        """
        Setup method: Initializes WebDriver and navigates to the Python website.
        """
        print("setup")
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")

    def test_search_python(self):
        """
        Test case: Searches for 'pycon' on the Python website and verifies search results.
        """
        # Creating an instance of MainPage and interacting with elements
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
         # Creating an instance of SearchResultPage and checking for search results
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self):
        """
        Teardown method: Closes the WebDriver.
        """
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
