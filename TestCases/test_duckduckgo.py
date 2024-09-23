from PageObjectModel.search import DuckDuckSearchPage
from PageObjectModel.results import ResultDuckDuckpage
from playwright.sync_api import Page, expect


def test_duckduckgo_search_page(page: Page):
    search_page = DuckDuckSearchPage(page)
    result_page = ResultDuckDuckpage(page)

    # Given the duckduckgo page is displayed
    search_page.load_page()
    
    # When the user searched for a phrase
    search_page.search('panda')

    # Then phrase in search result
    expect(page.locator('.js-search-input')).to_have_value('panda')

    # And phrase is in rersult links 
    titles = result_page.result_link_titles()
    matches= [title for title in titles if 'panda' in title.lower()]  
    assert len(titles) == 10, "Invalid no of tiltle in first page."

    # And the search result contains title the searched phrase
    expect(page).to_have_title('panda at DuckDuckGo')


