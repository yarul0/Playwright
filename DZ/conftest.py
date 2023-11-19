from pytest import fixture
from playwright.sync_api import Playwright, sync_playwright
@fixture()
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright

@fixture()
def fixt1():
    return 39

@fixture()
def new_fixt(fixt1):
    return fixt1 + 30
