from pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_LIST = ".inventory_list"
    INVENTORY_TITLE = ".title"
    ADD_TO_CART_BACKPACK = "#add-to-cart-sauce-labs-backpack"
    REMOVE_BACKPACK = "#remove-sauce-labs-backpack"
    CART_BADGE = ".shopping_cart_badge"
    CART_ICON = ".shopping_cart_link"
    BURGER_MENU = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"

    def is_inventory_displayed(self):
        return self.is_visible(self.INVENTORY_LIST)

    def get_inventory_title(self):
        self.wait_for_visible(self.INVENTORY_TITLE)
        return self.get_text(self.INVENTORY_TITLE)

    def add_backpack_to_cart(self):
        self.click(self.ADD_TO_CART_BACKPACK)

    def is_remove_button_displayed(self):
        return self.is_visible(self.REMOVE_BACKPACK)

    def get_cart_badge_count(self):
        if self.is_visible(self.CART_BADGE):
            return self.get_text(self.CART_BADGE)
        return "0"

    def open_cart(self):
        self.click(self.CART_ICON)

    def logout(self):
        self.click(self.BURGER_MENU)
        self.wait_for_visible(self.LOGOUT_LINK)
        self.click(self.LOGOUT_LINK)