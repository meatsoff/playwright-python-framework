import os
import pytest
from playwright.sync_api import sync_playwright
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        logger.info("Browser launched")
        yield browser
        browser.close()
        logger.info("Browser closed")


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page):
    yield
    if request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)
        file_path = f"screenshots/{request.node.name}.png"
        page.screenshot(path=file_path, full_page=True)
        logger.error(f"Test failed. Screenshot saved: {file_path}")