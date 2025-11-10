# 文件名: tests/test_e2e_add_to_cart.py

import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Pytest Fixture: 类似于JUnit的@Before和@After，用于测试的准备和清理工作
@pytest.fixture
def driver():
    # --- 这是全新的前置操作 (Setup) ---
    print("\n正在使用 webdriver-manager 自动配置 ChromeDriver...")
    # 下面这一行代码将自动完成：检测版本 -> 下载 -> 缓存 -> 配置路径 的所有工作
    service = ChromeService(executable_path=ChromeDriverManager().install())

    # 使用自动配置好的 service 来启动 Chrome
    driver_instance = webdriver.Chrome(service=service)
    print("ChromeDriver 配置成功，浏览器实例已创建！")

    driver_instance.maximize_window()
    driver_instance.get("https://www.saucedemo.com/")
    yield driver_instance

    # --- 后置操作 (Teardown) ---
    print("\n测试结束，关闭浏览器...")
    driver_instance.quit()

# 测试用例函数必须以 "test_" 开头
def test_add_item_to_cart_successfully(driver):
    """
    测试一个完整的端到端流程：
    1. 登录
    2. 添加一件商品到购物车
    3. 验证购物车
    """
    # 实例化所有需要的页面对象
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # --- 测试步骤和断言 ---

    # 1. 登录
    print("\n步骤1: 执行登录操作...")
    login_page.login("standard_user", "secret_sauce")

    # 2. 验证登录成功
    print("步骤2: 验证是否成功跳转到商品页...")
    # 使用Python内置的assert关键字进行断言
    assert inventory_page.is_url_contains("inventory.html"), "登录后URL不正确！"

    # 3. 添加商品到购物车
    print("步骤3: 添加背包到购物车...")
    inventory_page.add_backpack_to_cart()

    # 4. 验证购物车图标数量
    print("步骤4: 验证购物车图标数量为'1'...")
    badge_count = inventory_page.get_cart_badge_count()
    assert badge_count == "1", f"购物车图标数量错误，期望是'1'，实际是'{badge_count}'"

    # 5. 进入购物车页面
    print("步骤5: 进入购物车...")
    inventory_page.go_to_cart()

    # 6. 验证购物车中的商品名称
    print("步骤6: 验证购物车中的商品是否正确...")
    item_name = cart_page.get_item_name_in_cart()
    expected_item_name = "Sauce Labs Backpack"
    assert item_name == expected_item_name, f"购物车商品不匹配，期望'{expected_item_name}'，实际'{item_name}'"

    print("测试用例执行成功！")