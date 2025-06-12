"""
File: pages/login_page.py
Creator:  Angel
Created: 2025-06-05
Description: Page Object Model for Login page
"""

from .base_page import BasePage
from config.config import Config

class LoginPage(BasePage):
    """Login Page Object Model"""

    # Locators
    SIGN_IN_LINK = "a:has-text('Sign In')"
    USERNAME_INPUT = "input[name='username']"
    PASSWORD_INPUT = "input[name='password']"
    LOGIN_BUTTON = "input[name='signon']"
    ERROR_MESSAGE = "#Content ul.messages li"
    WELCOME_MESSAGE = "#WelcomeContent"
    SIGN_OUT_LINK = "a:has-text('Sign Out')"

    def __init__(self, page):
        super().__init__(page)

    def navigate_to_login_page(self):
        """Navigate to login page"""
        self.navigate(f"{Config.BASE_URL}{Config.LOGIN_URL}")

    def login(self, username: str, password: str):
        """Perform login operation"""
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        """Get error message"""
        self.wait_for_selector(self.ERROR_MESSAGE)
        return self.get_text(self.ERROR_MESSAGE)

    def get_welcome_message(self) -> str:
        """Get welcome message"""
        self.wait_for_selector(self.WELCOME_MESSAGE)
        return self.get_text(self.WELCOME_MESSAGE)

    def logout(self):
        """Perform logout operation"""
        self.click(self.SIGN_OUT_LINK)
        self.wait_for_selector(self.SIGN_IN_LINK)

    def is_logged_in(self) -> bool:
        """Check if logged in"""
        return self.is_visible(self.SIGN_OUT_LINK)

    def is_login_successful(self):
        """Check if login was successful"""
        return self.page.is_visible(self.WELCOME_MESSAGE)