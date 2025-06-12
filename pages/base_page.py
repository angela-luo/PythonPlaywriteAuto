"""
File: pages/base_page.py
Creator: Angel
Created: 2025-06-05
Description: Base page class for common functionality
"""

from datetime import datetime
from playwright.sync_api import Page
from utils.logger import setup_logger
from config.config import Config


class BasePage:
    """The base class for all page objects, providing common methods and properties"""

    def __init__(self, page: Page):
        """Initialize the base page"""
        self.page = page
        self.logger = setup_logger(self.__class__.__name__)

    def navigate(self, url: str):
        """Navigate to the specified URL"""
        self.logger.info(f"Navigate to: {url}")
        self.page.goto(url)

    def click(self, selector: str):
        """Click on an element"""
        self.logger.info(f"Click element: {selector}")
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        """Enter text in an input field"""
        self.logger.info(f"Clear {selector}")
        self.page.fill(selector, '')

        self.logger.info(f"In {selector} input: {text}")
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        """Get the text content of an element"""
        text = self.page.inner_text(selector)
        self.logger.info(f"Get element text: {text}")
        return text

    def get_title(self):
        title = self.page.title()
        self.logger.info(f"Get element text: {title}")
        return title

    def is_visible(self, selector: str) -> bool:
        """ Check if an element is visible"""
        visible = self.page.is_visible(selector)
        self.logger.info(f"Element {selector} visibility: {visible}")
        return visible

    def take_screenshot(self, name: str):
        """Take a screenshot of the page"""
        self.logger.info(f"Capture screenshot: {name}")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.page.screenshot(path=f"{Config.SCREENSHOT_DIR}/{name}_{timestamp}.png", full_page=True)

    def wait_for_selector(self, selector: str, timeout: int = None):
        """Wait for an element to appear"""
        timeout = timeout or Config.TIMEOUT
        self.logger.info(f"Wait for element: {selector} (timeout: {timeout}ms)")
        self.page.wait_for_selector(selector, timeout=timeout)