from pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_LIST = ".inventory_list"
    INVENTORY_TITLE = ".title"

    def is_inventory_displayed(self):
        return self.is_visible(self.INVENTORY_LIST)

    def get_title(self):
        return self.get_text(self.INVENTORY_TITLE)