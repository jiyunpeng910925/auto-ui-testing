from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    ADD_TO_CART_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self):
        self.do_click(self.ADD_TO_CART_BACKPACK_BUTTON)

    def get_cart_badge_count(self):
        return self.get_element_text(self.SHOPPING_CART_BADGE)

    def go_to_cart(self):
        self.do_click(self.SHOPPING_CART_LINK)