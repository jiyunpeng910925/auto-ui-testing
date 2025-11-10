from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def get_item_name_in_cart(self):
        return self.get_element_text(self.INVENTORY_ITEM_NAME)