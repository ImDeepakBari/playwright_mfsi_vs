from playwright.sync_api import Page, expect

class DuckDuckSearchPage:

    URL = "https://www.duckduckgo.com"


    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.get_by_label('Search with DuckDuckGo')
        self.search_btn = page.locator("//button[@aria-label='Search']")


    def load_page(self):
        self.page.goto(self.URL)

    def search(self, phrase:str):
        self.search_input.fill(phrase)
        self.search_btn.click()