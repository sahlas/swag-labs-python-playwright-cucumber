"""Environment setup for behave tests with Playwright."""

from playwright.sync_api import sync_playwright


def before_all(context):
    """Set up browser and context before all tests."""
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.browser_context = context.browser.new_context()
    context.playwright.selectors.set_test_id_attribute("data-test")


def before_scenario(context, scenario):
    """Set up page before each scenario."""
    context.page = context.browser_context.new_page()


def after_scenario(context, scenario):
    """Clean up page after each scenario."""
    if hasattr(context, "page"):
        context.page.close()


def after_all(context):
    """Clean up browser and playwright after all tests."""
    if hasattr(context, "browser_context"):
        context.browser_context.close()
    if hasattr(context, "browser"):
        context.browser.close()
    if hasattr(context, "playwright"):
        context.playwright.stop()
