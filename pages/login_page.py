from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def login(self, username, password):
        self.do_send_keys(self.USERNAME_INPUT, username)
        self.do_send_keys(self.PASSWORD_INPUT, password)
        self.do_click(self.LOGIN_BUTTON)