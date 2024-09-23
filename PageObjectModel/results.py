from playwright.sync_api import Page, expect

class ResultDuckDuckpage:


    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator('.js-search-input')
        self.result_links = page.get_by_test_id('result-title-a')

    def result_link_titles(self):
        self.result_links.nth(5).wait_for() # adding explicit wait for element
        return self.result_links.all_text_contents()

