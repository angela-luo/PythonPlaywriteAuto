"""
用户信息页面对象模型
创建日期: 2025-06-05
创建人: Angel
"""

from pages.base_page import BasePage
from config.config import Config


class UserInfoPage(BasePage):
    """用户信息页面对象模型"""

    # 定位器
    MY_ACCOUNT_LINK = "a:has-text('My Account')"
    USER_ID_INPUT = "input[name='username']"
    NEW_PASSWORD_INPUT = "input[name='password']"
    REPEAT_PASSWORD_INPUT = "input[name='repeatedPassword']"
    FIRST_NAME_INPUT = "input[name='account.firstName']"
    LAST_NAME_INPUT = "input[name='account.lastName']"
    EMAIL_INPUT = "input[name='account.email']"
    PHONE_INPUT = "input[name='account.phone']"
    ADDRESS1_INPUT = "input[name='account.address1']"
    ADDRESS2_INPUT = "input[name='account.address2']"
    CITY_INPUT = "input[name='account.city']"
    STATE_INPUT = "input[name='account.state']"
    ZIP_INPUT = "input[name='account.zip']"
    COUNTRY_INPUT = "input[name='account.country']"
    LANGUAGE_SELECT = "select[name='account.languagePreference']"
    FAVORITE_CATEGORY_SELECT = "select[name='account.favouriteCategoryId']"
    ENABLE_MYLIST_CHECKBOX = "input[name='account.listOption']"
    ENABLE_BANNER_CHECKBOX = "input[name='account.bannerOption']"
    SAVE_ACCOUNT_BUTTON = "input[name='editAccount']"
    SUCCESS_MESSAGE = "#Content ul.messages li"
    ERROR_MESSAGES = "#Content ul.errors li"

    def __init__(self, page):
        super().__init__(page)

    def navigate_to_user_info_page(self):
        """导航到用户信息页面"""
        self.navigate(f"{Config.BASE_URL}{Config.USER_INFO_URL}")

    def update_user_info(self, user_data: dict):
        """
        更新用户信息
        :param user_data: 包含用户信息的字典
        """
        # 填写基本信息
        self.fill(self.USER_ID_INPUT, user_data["username"])
        if user_data.get("password"):
            self.fill(self.NEW_PASSWORD_INPUT, user_data["password"])
            self.fill(self.REPEAT_PASSWORD_INPUT, user_data["password"])
        self.fill(self.FIRST_NAME_INPUT, user_data["first_name"])
        self.fill(self.LAST_NAME_INPUT, user_data["last_name"])
        self.fill(self.EMAIL_INPUT, user_data["email"])
        self.fill(self.PHONE_INPUT, user_data["phone"])
        self.fill(self.ADDRESS1_INPUT, user_data["address1"])
        self.fill(self.ADDRESS2_INPUT, user_data.get("address2", ""))
        self.fill(self.CITY_INPUT, user_data["city"])
        self.fill(self.STATE_INPUT, user_data["state"])
        self.fill(self.ZIP_INPUT, user_data["zip"])
        self.fill(self.COUNTRY_INPUT, user_data["country"])

        # 选择偏好设置
        self.page.select_option(self.LANGUAGE_SELECT, user_data["language"])
        self.page.select_option(self.FAVORITE_CATEGORY_SELECT, user_data["favorite_category"])

        # 设置复选框
        if user_data.get("enable_mylist", False):
            self.page.check(self.ENABLE_MYLIST_CHECKBOX)
        else:
            self.page.uncheck(self.ENABLE_MYLIST_CHECKBOX)

        if user_data.get("enable_banner", False):
            self.page.check(self.ENABLE_BANNER_CHECKBOX)
        else:
            self.page.uncheck(self.ENABLE_BANNER_CHECKBOX)

        # 保存更改
        self.click(self.SAVE_ACCOUNT_BUTTON)

    def get_success_message(self) -> str:
        """获取成功消息"""
        self.wait_for_selector(self.SUCCESS_MESSAGE)
        return self.get_text(self.SUCCESS_MESSAGE)

    def get_error_messages(self) -> list:
        """获取所有错误消息"""
        if self.page.locator(self.ERROR_MESSAGES).count() > 0:
            return [self.get_text(f"{self.ERROR_MESSAGES}:nth-child({i + 1})")
                    for i in range(self.page.locator(self.ERROR_MESSAGES).count())]
        return []