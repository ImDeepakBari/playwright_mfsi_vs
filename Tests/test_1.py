from playwright.sync_api import Page, expect, Playwright


def test_check_basic_playwright(page: Page):
    # Given the duckduckgo page is displayed
    page.goto("https://www.duckduckgo.com")
    # When the user searched for a phrase
    page.get_by_label('Search with DuckDuckGo').fill("panda")
    page.get_by_label('Search', exact=True).click()

    # button = page.get_by_role('button').and_(page.get_by_label('Search', exact=True))
    # button.click()
    # page.locator("//button[@aria-label='Search']").click()

    # Then phrase in search result
    expect(page.locator('.js-search-input')).to_have_value('panda')

    # And phrase is in rersult links 
    titles = page.get_by_test_id('result-title-a').all_text_contents()
    print("tiles===", titles)
    matches= [title for title in titles if 'panda' in title.lower()]
    print(len(titles))
    assert len(titles) == 10, "Invalid no of tiltle in first page."
    # And the search result contains title the searched phrase
    expect(page).to_have_title('panda at DuckDuckGo')