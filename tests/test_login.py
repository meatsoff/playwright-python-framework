from data.test_users import VALID_USER
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_login_success(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login(VALID_USER["username"], VALID_USER["password"])

    assert inventory_page.is_inventory_displayed()
    assert inventory_page.get_title() == "Products"