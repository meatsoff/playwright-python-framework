from config.settings import Settings


class BasePage:
    def __init__(self, page):
        self.page = page
        self.page.set_default_timeout(Settings.DEFAULT_TIMEOUT)

    def navigate(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, text):
        self.page.locator(locator).fill(text)

    def get_text(self, locator):
        return self.page.locator(locator).inner_text()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def wait_for_visible(self, locator):
        self.page.locator(locator).wait_for(state="visible")

    def get_title(self):
        return self.page.title()