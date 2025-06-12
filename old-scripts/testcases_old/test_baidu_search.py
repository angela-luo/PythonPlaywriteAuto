import time
import pytest
from playwright.sync_api import sync_playwright


def test_search_playwright_in_baidu():
    # 启动 Playwright 浏览器
    with sync_playwright() as p:
        # 启动 Chromium 浏览器
        browser = p.chromium.launch(headless=False)  # headless=False 让浏览器可见
        # 创建新的浏览器上下文和页面
        page = browser.new_page()

        # 打开百度首页
        page.goto("https://www.baidu.com")

        # 确保百度页面已经加载成功
        assert "百度" in page.title()

        # 在搜索框中输入 "playwright"
        search_box = page.locator("input#kw")  # 百度的搜索框的定位器
        search_box.fill("playwright")  # 输入搜索内容
        search_box.press("Enter")  # 按下 Enter 键进行搜索

        # 等待搜索结果加载
        # page.wait_for_selector(".result-op")  # 等待搜索结果页面加载完成

        # 获取搜索结果的标题并验证是否包含 "Playwright"
        first_result_title = page.locator(".result-op h3").text_content()
        print(first_result_title)
        assert "Playwright" in first_result_title

        # 休眠几秒钟查看搜索结果
        page.wait_for_timeout(2000)

        # 关闭浏览器
        browser.close()
