from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://dentalzing.com/")
    page.get_by_label("Account icon link").click()
    page.get_by_label("Username or email address").fill("yaroslav.perederii+DZ@onpoint.to")
    page.get_by_label("Password").fill("0reh0vk@2")
    page.get_by_label("Remember me").check()
    page.get_by_role("button", name="Log in").click()
    # assert page.url == 'https://dentalzing.com/my-account/'
    assert page.locator(":nth-match(:text('yar'), 2)").text_content() == 'Yaroslav TE2'

    # page.goto("https://dentalzing.com/my-account/")
    # # page.get_by_text('My Courses').click()
    page.wait_for_timeout(3000)


    # ---------------------
    context.close()
    browser.close()

def test_login():
    with sync_playwright() as playwright:
        run(playwright)