from selenium.webdriver.common.by import By



class DuckDuckGoResultPage:

    RESULT_LINKS = (By.CSS_SELECTOR, "a.result__a")
    SEARCH_INPUT = (By.ID, "search_from_input")

    def __init__(self, browser):
        self.browser = browser

    def result_link_titles(self):

        return []

    def search_input_value(self):
        
        return ""

    def title(self):

        return ""