from data.test_users import VALID_USER
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_cart_contains_added_item(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.open()
    login_page.login(VALID_USER["username"], VALID_USER["password"])

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    assert cart_page.is_cart_displayed()
    assert cart_page.get_cart_item_count() == 1