from locator import *
from element import BasePageElement


class SearchTextElement(BasePageElement):
    locator = "q"


class BasePage(object):
    def __init__(self, driver):
        """
        BasePage class: Initializes the driver.
        """
        self.driver = driver


class MainPage(BasePage):
    search_text_element = SearchTextElement()


    def is_title_matches(self):
        """
        Checks if the title of the main page contains 'Python'.
        """
        return "Python" in self.driver.title
    
    def click_go_button(self):
        """
        Clicks the search button on the main page.
        """
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

class SearchResultPage(BasePage):
    
    def is_results_found(self):
        """
        Checks if search results are found on the results page.
        """
        return "No results found." not in self.driver.page_source