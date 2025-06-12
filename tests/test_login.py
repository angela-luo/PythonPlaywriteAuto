"""
File: tests/test_login.py
Creator: Angel
Created: 2025-06-05
Description: Test cases for login functionality
"""

import pytest
import allure
from playwright.sync_api import Page
from pages.login_page import LoginPage
from utils.logger import setup_logger
from utils.data_loader import load_test_data

# Set up the logger
logger = setup_logger(__name__)

# Load test data
login_test_data = load_test_data('login_data.yaml')


@allure.feature("Login module")
class TestLogin:
    """Test cases for the login module"""

    @allure.story("Test login")
    @pytest.mark.login
    @pytest.mark.parametrize(
        "test_data",
        [pytest.param(item, marks=getattr(pytest.mark, item["test_level"]))
         for item in login_test_data],
        ids=[item["test_id"] for item in login_test_data]
    )
    def test_login(self, page: Page, test_data: dict):
        """Test login"""

        # Set Allure report attributes
        allure.dynamic.title(test_data["test_id"] + ": " + test_data["test_title"])
        allure.dynamic.description(f"Test priority: {test_data['test_level']}")
        allure.dynamic.severity(test_data["test_level"])
        allure.dynamic.tag("login")

        # init login page object
        login_page = LoginPage(page)

        try:
            # Step 1: Navigate to login page
            with allure.step("Navigate to login page"):
                login_page.navigate_to_login_page()
                allure.attach(page.screenshot(), name="Login page", attachment_type=allure.attachment_type.PNG)

            # Step 2:  Perform the login operation
            with allure.step(f"Login with name '{test_data['username']}' and password '{test_data['password']}'"):
                login_page.login(test_data["username"], test_data["password"])

            # Verification steps
            if test_data["is_positive"].lower() == "true":
                # Verify positive test cases
                with allure.step("Verify successful login"):
                    welcome_message = login_page.get_welcome_message()
                    assert test_data["expected"] in welcome_message, \
                        f"The expected welcome message contains '{test_data['expected']}', actual: '{welcome_message}'"
                    logger.info(f"Login successful, welcome message: {welcome_message}")
                    allure.attach(page.screenshot(), name="Login successfully", attachment_type=allure.attachment_type.PNG)

                # Step 3: Log out
                with allure.step("Log out of the system"):
                    login_page.logout()
                    assert login_page.is_visible(login_page.SIGN_IN_LINK), "After logging out, the login link should be displayed."
                    logger.info("Successfully logged out")
                    allure.attach(page.screenshot(), name="Logout successfully", attachment_type=allure.attachment_type.PNG)
            else:
                # Verification of reverse test cases
                with allure.step("Verify that the login fails and display an error message"):
                    error_message = login_page.get_error_message()
                    assert test_data["expected"] in error_message, \
                        f"The expected error message contains '{test_data['expected']}', actual: '{error_message}'"
                    logger.info(f"Login failed, error message: {error_message}")
                    allure.attach(page.screenshot(), name="Login failed", attachment_type=allure.attachment_type.PNG)

        except AssertionError as e:
            # Test failure handling
            logger.error(f"The test failed: {str(e)}")
            raise
        except Exception as e:
            # Other exception handling
            logger.error(f"Test execution error: {str(e)}")
            raise