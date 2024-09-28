import pytest
from PageObjectModel.search import DuckDuckSearchPage
from PageObjectModel.results import ResultDuckDuckpage
from playwright.sync_api import Page


@pytest.fixture
def result_page(page: Page):
    return ResultDuckDuckpage(page)

@pytest.fixture
def search_page(page: Page):
    return DuckDuckSearchPage(page)