from playwright.sync_api import Playwright, sync_playwright, expect


def test_assert():
    # print('before_' * 5)
    result = False
    # print('after_' * 5)
    assert result, '- state of test'

