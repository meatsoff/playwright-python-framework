from pages.base_page import BasePage


class CartPage(BasePage):
    CART_LIST = ".cart_list"
    CART_ITEM = ".cart_item"
    CHECKOUT_BUTTON = "#checkout"

    def is_cart_displayed(self):
        return self.is_visible(self.CART_LIST)

    def get_cart_item_count(self):
        return self.page.locator(self.CART_ITEM).count()

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)