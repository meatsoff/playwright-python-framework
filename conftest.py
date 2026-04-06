import os
import pytest
from playwright.sync_api import sync_playwright
from config.settings import Settings
from utils.logger import get_logger

logger = get_logger(__name__)


def _launch_browser(playwright):
    browser_name = Settings.BROWSER

    if browser_name == "firefox":
        browser = playwright.firefox.launch(headless=Settings.HEADLESS)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=Settings.HEADLESS)
    else:
        browser = playwright.chromium.launch(headless=Settings.HEADLESS)

    logger.info(f"Browser launched: {browser_name}, headless={Settings.HEADLESS}")
    return browser


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = _launch_browser(p)
        yield browser
        browser.close()
        logger.info("Browser closed")


@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context(
        viewport={
            "width": Settings.VIEWPORT_WIDTH,
            "height": Settings.VIEWPORT_HEIGHT
        }
    )
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page):
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)
        file_path = f"screenshots/{request.node.name}.png"
        page.screenshot(path=file_path, full_page=True)
        logger.error(f"Test failed. Screenshot saved: {file_path}")