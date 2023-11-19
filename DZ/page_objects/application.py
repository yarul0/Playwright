from playwright.sync_api import Playwright
class App:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto("https://dentalzing.com/")
    def login(self):
        self.page.get_by_label("Account icon link").click()
        self.page.get_by_label("Username or email address").fill("yaroslav.perederii+DZ@onpoint.to")
        self.page.get_by_label("Password").fill("0reh0vk@2")
        self.page.get_by_label("Remember me").check()
        self.page.get_by_role("button", name="Log in").click()
    def create_test(self):
        pass
    def open_tests(self):
        pass
    def check_test_created(self):
        pass
    def delete_test(self):
        pass
    def close(self):
        pass