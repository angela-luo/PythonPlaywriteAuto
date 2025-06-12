"""
File: pages/register_page.py
Creator: Angel
Created: 2025-06-10
Last Updated: 2025-06-11 by Angel
Description: Page object for user registration
"""

from pages.base_page import BasePage
from config.config import Config
import uuid


class RegisterPage(BasePage):
    """Register Page Object Model"""

    # Locators
    USER_ID_INPUT = "input[name='username']"
    PASSWORD_INPUT = "input[name='password']"
    CONFIRM_PASSWORD_INPUT = "input[name='repeatedPassword']"
    FIRST_NAME_INPUT = "input[name='account.firstName']"
    LAST_NAME_INPUT = "input[name='account.lastName']"
    EMAIL_INPUT = "input[name='account.email']"
    PHONE_INPUT = "input[name='account.phone']"
    ADDRESS1_INPUT = "input[name='account.address1']"
    CITY_INPUT = "input[name='account.city']"
    STATE_INPUT = "input[name='account.state']"
    ZIP_INPUT = "input[name='account.zip']"
    COUNTRY_INPUT = "input[name='account.country']"
    LANGUAGE_PREF_DROPDOWN = "select[name='account.languagePreference']"
    FAV_CATEGORY_DROPDOWN = "select[name='account.favouriteCategoryId']"
    ENABLE_MYLIST_CHECKBOX = "input[name='account.listOption']"
    ENABLE_MYBANNER_CHECKBOX = "input[name='account.bannerOption']"
    REGISTER_BUTTON = "input[name='newAccount']"
    ERROR_MSG = ".error"
    FIELD_ERROR_MSG = "//td[contains(@class, 'error')]/following-sibling::td"

    def __init__(self, page):
        super().__init__(page)

    def navigate_to_register(self):
        """Navigate to registration page"""
        # self.navigate(self.url)
        self.navigate(f"{Config.BASE_URL}{Config.REGISTER_URL}")

    def generate_unique_username(self, prefix="Autotest_"):
        """Generate unique username with prefix"""
        unique_id = str(uuid.uuid4())[:8]
        return f"{prefix}{unique_id}"

    def register_user(self, user_data):
        """Register new user with provided data"""
        # Generate unique username if not provided
        username = user_data.get("username", self.generate_unique_username())
        self.logger.info(f"Registering user: {username}")

        # Fill registration form
        self.fill(self.USER_ID_INPUT, username)
        self.fill(self.PASSWORD_INPUT, user_data["password"])
        self.fill(self.CONFIRM_PASSWORD_INPUT, user_data["confirm_password"])
        self.fill(self.FIRST_NAME_INPUT, username)
        self.fill(self.LAST_NAME_INPUT, user_data["last_name"])
        self.fill(self.EMAIL_INPUT, user_data["email"])
        self.fill(self.PHONE_INPUT, user_data["phone"])
        self.fill(self.ADDRESS1_INPUT, user_data["address1"])
        self.fill(self.CITY_INPUT, user_data["city"])
        self.fill(self.STATE_INPUT, user_data["state"])
        self.fill(self.ZIP_INPUT, user_data["zip"])
        self.fill(self.COUNTRY_INPUT, user_data["country"])

        # Additional preferences (if provided)
        if "language" in user_data:
            self.page.select_option(self.LANGUAGE_PREF_DROPDOWN, value=user_data["language"])
        if "fav_category" in user_data:
            self.page.select_option(self.FAV_CATEGORY_DROPDOWN, value=user_data["fav_category"])
        if user_data.get("enable_mylist", False):
            self.click(self.ENABLE_MYLIST_CHECKBOX)
        if user_data.get("enable_mybanner", False):
            self.click(self.ENABLE_MYBANNER_CHECKBOX)

        # Submit registration
        self.click(self.REGISTER_BUTTON)
        return username

    def get_success_message(self):
        """Get success message after registration"""
        self.wait_for_selector(self.SUCCESS_MSG)
        return self.get_text(self.SUCCESS_MSG)

    def get_error_message(self):
        """Get error message if registration fails"""
        # Check for general error message
        if self.page.is_visible(self.ERROR_MSG):
            return self.get_text(self.ERROR_MSG)

        # Check for field-specific error messages
        error_elements = self.page.query_selector_all(self.FIELD_ERROR_MSG)
        if error_elements:
            errors = [element.text_content().strip() for element in error_elements]
            return " | ".join(errors)

        return "No error message found"