from data.test_users import VALID_USER, INVALID_USER, LOCKED_USER
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_login_success(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login(VALID_USER["username"], VALID_USER["password"])

    assert inventory_page.is_inventory_displayed()
    assert inventory_page.get_inventory_title() == "Products"


def test_login_invalid_credentials(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(INVALID_USER["username"], INVALID_USER["password"])

    error_message = login_page.get_error_message()
    assert "Username and password do not match" in error_message


def test_login_locked_user(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(LOCKED_USER["username"], LOCKED_USER["password"])

    error_message = login_page.get_error_message()
    assert "Sorry, this user has been locked out." in error_message