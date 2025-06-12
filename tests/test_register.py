"""
File: tests/test_register.py
Creator: Angel
Created: 2025-06-10
Description: Test cases for user registration
"""

import pytest
import allure
from utils.data_loader import load_test_data
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from utils.logger import setup_logger

logger = setup_logger("TestRegister")
# Load test data
register_test_data = load_test_data('register_data.yaml')["test_cases"]


@allure.feature("User Registration module")
class TestRegister:
    @allure.story("Test Register")
    @pytest.mark.register
    # @pytest.mark.p0
    @pytest.mark.smoke
    # @pytest.mark.parametrize("test_data", register_test_data)
    @pytest.mark.parametrize(
        "test_data",
        [pytest.param(item, marks=getattr(pytest.mark, item["test_level"]))
         for item in register_test_data],
        ids=[item["test_id"] for item in register_test_data]
    )
    def test_register(self, page, test_data: dict):
        """Test user registration with various data"""
        with allure.step(f"Executing test: {test_data['test_id']} - {test_data['test_title']}"):
            allure.dynamic.title(test_data["test_id"] + ": " + test_data["test_title"])
            allure.dynamic.title(test_data["test_title"])
            allure.dynamic.severity(test_data["test_level"])
            logger.info(f"Starting test: {test_data['test_id']} - {test_data['test_title']}")

            # Arrange
            register_page = RegisterPage(page)
            login_page = LoginPage(page)

            # Act
            register_page.navigate_to_register()
            username = register_page.register_user(test_data)

            # Assert
            if test_data["test_id"] == "TC_REG_001":
                # # Verify success message
                # success_msg = register_page.get_success_message()
                # assert test_data["expected"] in success_msg
                # logger.info(f"Registration success message: {success_msg}")

                # Verify user can log in with new credentials
                login_page.navigate_to_login_page()
                login_page.login(username, test_data["password"])
                welcome_msg = login_page.get_welcome_message()
                assert f"Welcome {username}!" in welcome_msg
                logger.info(f"Login successful with new user: {username}")
            else:
                # Verify error message for negative cases
                error_msg = register_page.get_error_message()
                assert test_data["expected"] in error_msg
                logger.warning(f"Registration error message: {error_msg}")