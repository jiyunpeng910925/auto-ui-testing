# 文件名: pages/base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    基础页面类，封装所有页面都可能用到的通用方法。
    """
    def __init__(self, driver):
        self.driver = driver
        # 设置一个10秒的显式等待，作为所有查找元素的默认等待时间
        self.wait = WebDriverWait(self.driver, 10)

    def do_click(self, locator):
        """
        封装的点击方法，会等待元素可见后再点击。
        locator: 一个元组，包含定位方式和值，例如 (By.ID, "username")
        """
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def do_send_keys(self, locator, text):
        """封装的输入文本方法。"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()  # 输入前最好先清空
        element.send_keys(text)

    def get_element_text(self, locator):
        """封装的获取元素文本的方法。"""
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_url_contains(self, partial_url):
        """判断当前URL是否包含指定的字符串。"""
        self.wait.until(EC.url_contains(partial_url))
        return True