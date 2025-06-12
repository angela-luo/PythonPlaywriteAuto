"""
Base page class for common functionality
pages/base_page_old.py
Author:  Angel
Created Date: 2025-06-05
"""

from playwright.sync_api import Page
from utils.logger import setup_logger
from config.config import Config


class BasePage:
    """The base class for all page objects, providing common methods and properties"""

    def __init__(self, page: Page):
        """
        初始化基础页面
        :param page: Playwright页面对象
        """
        self.page = page
        self.logger = setup_logger(self.__class__.__name__)

    def navigate(self, url: str):
        """
        Navigate to the specified URL
        :param url: Target URL
        """
        self.logger.info(f"Navigate to: {url}")
        self.page.goto(url)

    def click(self, selector: str):
        """
        点击元素
        :param selector: CSS选择器
        """
        self.logger.info(f"点击元素: {selector}")
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        """
        在输入框中输入文本
        :param selector: CSS选择器
        :param text: 要输入的文本
        """
        self.logger.info(f"clear {selector}")
        self.page.fill(selector,'')

        self.logger.info(f"In {selector} input: {text}")
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        """
        获取元素的文本内容
        :param selector: CSS选择器
        :return: 元素的文本内容
        """
        text = self.page.inner_text(selector)
        self.logger.info(f"获取元素文本: {text}")
        return text

    def get_title(self):
        title =self.page.title()
        self.logger.info(f"获取元素文本: {title}")
        return title


    def is_visible(self, selector: str) -> bool:
        """
        检查元素是否可见
        :param selector: CSS选择器
        :return: 是否可见
        """
        visible = self.page.is_visible(selector)
        self.logger.info(f"元素 {selector} 可见性: {visible}")
        return visible

    def take_screenshot(self, name: str):
        """
        截取页面截图
        :param name: 截图文件名
        """
        self.logger.info(f"截取截图: {name}")
        self.page.screenshot(path=f"{Config.SCREENSHOT_DIR}/{name}.png", full_page=True)

    def wait_for_selector(self, selector: str, timeout: int = None):
        """
        等待元素出现
        :param selector: CSS选择器
        :param timeout: 超时时间(毫秒)
        """
        timeout = timeout or Config.TIMEOUT
        self.logger.info(f"等待元素: {selector} (超时: {timeout}ms)")
        self.page.wait_for_selector(selector, timeout=timeout)