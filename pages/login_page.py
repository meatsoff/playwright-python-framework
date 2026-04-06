from config.settings import Settings
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"
    LOGIN_LOGO = ".login_logo"

    def open(self):
        self.navigate(Settings.BASE_URL)

    def is_login_page_displayed(self):
        return self.is_visible(self.LOGIN_LOGO)

    def login(self, username, password):
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        self.wait_for_visible(self.ERROR_MESSAGE)
        return self.get_text(self.ERROR_MESSAGE)