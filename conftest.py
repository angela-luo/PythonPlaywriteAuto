"""
File: conftest.py
Creator:  Angel
Created Date: 2025-06-05
Description: Configuration and fixtures for pytest
"""

import pytest
import allure
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright
from config.config import Config
from datetime import datetime


@pytest.fixture(scope="session")
def browser():
    """Create browser instance"""
    with sync_playwright() as p:
        browser = p[Config.BROWSER].launch(headless=Config.HEADLESS)
        yield browser
        browser.close()


@pytest.fixture
def context(browser: Browser):
    """Create browser context"""
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(context: BrowserContext):
    """Create page instance"""
    page = context.new_page()
    page.set_default_timeout(Config.TIMEOUT)
    yield page
    page.close()


def pytest_addoption(parser):
    """Add command line options"""
    parser.addoption(
        "--module", action="store", default=None, help="Filter tests by module"
    )
    parser.addoption("--level", action="append", default=[], help="Filter tests by level")  # 新增 level 选项


# Add a marker filtering hook
def pytest_configure(config):
    # Handle command - line level filtering
    levels = config.getoption("--level")
    if levels:
        config.option.markexpr = (config.option.markexpr or "") + f" and ({' or '.join(levels)})"


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Test report hook for handling failure screenshots"""
    outcome = yield
    report = outcome.get_result()

    # Only handle failures during test execution phase
    if report.when == "call" and report.failed:
        # Get page object
        page = item.funcargs.get("page")
        if page:
            # Get test ID
            test_id = getattr(item, "callspec", None)
            if test_id is not None:
                test_id = getattr(test_id, "id", item.nodeid)
            else:
                test_id = item.nodeid
            safe_test_id = "".join(c if c.isalnum() else "_" for c in test_id)

            # Capture screenshot
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"{Config.SCREENSHOT_DIR}/failure_{safe_test_id}_{timestamp}.png"
            page.screenshot(path=screenshot_path, full_page=True)

            # Attach screenshot to Allure report
            allure.attach.file(
                screenshot_path,
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )
