from data.test_users import VALID_USER
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_inventory_page_loaded_after_login(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login(VALID_USER["username"], VALID_USER["password"])

    assert inventory_page.is_inventory_displayed()
    assert inventory_page.get_inventory_title() == "Products"


def test_add_product_to_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login(VALID_USER["username"], VALID_USER["password"])

    inventory_page.add_backpack_to_cart()

    assert inventory_page.is_remove_button_displayed()
    assert inventory_page.get_cart_badge_count() == "1"


def test_logout_success(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login(VALID_USER["username"], VALID_USER["password"])
    inventory_page.logout()

    assert login_page.is_login_page_displayed()