"""
用户信息模块测试用例
创建日期: 2025-06-05
创建人: Angel
"""

import pytest
import allure
from playwright.sync_api import Page
from pages.login_page import LoginPage
from utils_old.user_info_page import UserInfoPage
from utils_old.testcases_old.user_info_data import USER_INFO_DATA
from utils.logger import setup_logger

# 设置日志记录器
logger = setup_logger(__name__)


@allure.feature("用户信息模块")
class TestUserInfo:
    """用户信息模块测试用例"""

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """
        测试前置操作：登录系统
        :param page: Playwright页面对象
        """
        self.login_page = LoginPage(page)
        self.user_info_page = UserInfoPage(page)

        # 登录系统
        with allure.step("登录系统"):
            self.login_page.navigate_to_login_page()
            self.login_page.login("testuser", "testpass")
            welcome_message = self.login_page.get_welcome_message()
            assert "Welcome testuser!" in welcome_message, "登录失败"
            logger.info("成功登录系统")
            allure.attach(page.screenshot(), name="登录成功", attachment_type=allure.attachment_type.PNG)

        yield

        # 测试后置操作：登出系统
        with allure.step("登出系统"):
            self.login_page.logout()
            assert self.login_page.is_visible(self.login_page.SIGN_IN_LINK), "登出后应显示登录链接"
            logger.info("成功登出")
            allure.attach(page.screenshot(), name="登出成功", attachment_type=allure.attachment_type.PNG)

    @allure.story("用户信息更新功能测试")
    @pytest.mark.user_info
    @pytest.mark.parametrize("test_data", USER_INFO_DATA, ids=[item["test_id"] for item in USER_INFO_DATA])
    def test_user_info_update(self, page: Page, test_data: dict):
        """
        用户信息更新功能测试
        :param page: Playwright页面对象
        :param test_data: 测试数据
        """
        # 设置Allure报告属性
        allure.dynamic.title(test_data["test_id"] + ": " + test_data["test_name"])
        allure.dynamic.description(f"测试级别: {test_data['level']}")
        allure.dynamic.severity(test_data["level"])
        allure.dynamic.tag("user_info")

        try:
            # 步骤1: 导航到用户信息页面
            with allure.step("导航到用户信息页面"):
                self.user_info_page.navigate_to_user_info_page()
                allure.attach(page.screenshot(), name="用户信息页面", attachment_type=allure.attachment_type.PNG)

            # 步骤2: 更新用户信息
            with allure.step("更新用户信息"):
                self.user_info_page.update_user_info(test_data["user_data"])

            # 验证步骤
            if test_data["is_positive"]:
                # 正向测试用例验证
                with allure.step("验证更新成功"):
                    success_message = self.user_info_page.get_success_message()
                    assert test_data["expected"] in success_message, \
                        f"预期成功消息包含 '{test_data['expected']}', 实际: '{success_message}'"
                    logger.info(f"用户信息更新成功: {success_message}")
                    allure.attach(page.screenshot(), name="更新成功", attachment_type=allure.attachment_type.PNG)
            else:
                # 逆向测试用例验证
                with allure.step("验证更新失败并显示错误消息"):
                    error_messages = self.user_info_page.get_error_messages()
                    for expected_error in test_data["expected"]:
                        assert any(expected_error in msg for msg in error_messages), \
                            f"预期错误 '{expected_error}' 未在 {error_messages} 中找到"
                    logger.info(f"用户信息更新失败，错误消息: {error_messages}")
                    allure.attach(page.screenshot(), name="更新失败", attachment_type=allure.attachment_type.PNG)

        except AssertionError as e:
            # 测试失败处理
            logger.error(f"测试失败: {str(e)}")
            self.user_info_page.take_screenshot(f"user_info_failure_{test_data['test_id']}")
            allure.attach.file(
                f"{Config.SCREENSHOT_DIR}/user_info_failure_{test_data['test_id']}.png",
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            allure.attach(
                page.content(),
                name="page_source",
                attachment_type=allure.attachment_type.HTML
            )
            raise
        except Exception as e:
            # 其他异常处理
            logger.error(f"测试执行错误: {str(e)}")
            self.user_info_page.take_screenshot(f"user_info_error_{test_data['test_id']}")
            allure.attach.file(
                f"{Config.SCREENSHOT_DIR}/user_info_error_{test_data['test_id']}.png",
                name="error_screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            raise