import pytest
from playwright.sync_api import Browser, Page, sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser: Browser) -> Page:
    page = browser.new_page()
    page.set_default_timeout(30000)  # 设置默认超时时间
    yield page
    page.close()


# # 可选：添加失败截图功能
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#
#     if report.failed and "page" in item.funcargs:
#         page = item.funcargs["page"]
#         screenshot_path = f"reports/screenshots/{item.name}.png"
#         page.screenshot(path=screenshot_path, full_page=True)
#         report.extra = [pytest.extra.file(screenshot_path)]