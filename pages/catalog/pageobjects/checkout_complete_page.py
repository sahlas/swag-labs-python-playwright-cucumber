from playwright.sync_api import Page
from tests.fixtures.screenshot_manager import ScreenshotManager
import os
from behave import step

class CheckoutCompletePage:
    """Page object for the checkout complete page."""
    CHECKOUT_COMPLETE_CONFIRMATION_MESSAGE = os.getenv("CHECKOUT_COMPLETE_CONFIRMATION_MESSAGE", "Thank you for your order!")
    CHECKOUT_COMPLETE_PAGE_URL = os.getenv("CHECKOUT_COMPLETE_PAGE_URL", "https://www.saucedemo.com/checkout-complete.html")
    CHECKOUT_COMPLETE_PAGE_TITLE = os.getenv("CHECKOUT_COMPLETE_PAGE_TITLE", "Checkout: Complete!")

    def __init__(self, page: Page):
        self.page = page

    @step("Get Order Confirmation Message")
    def get_order_confirmation_message(self) -> bool:
        """
        Get order confirmation message from the checkout complete page.
        """
        order_confirmation_message = self.page.get_by_test_id("complete-header").text_content()
        is_message_correct = order_confirmation_message == self.CHECKOUT_COMPLETE_CONFIRMATION_MESSAGE
        if is_message_correct:
            print(f"Order confirmation message is correct: {order_confirmation_message}")
        else:
            print(f"Order confirmation message is incorrect: {order_confirmation_message}")
            ScreenshotManager.take_screenshot(self.page, f"order-confirmation-message-{order_confirmation_message}")
        return is_message_correct

    @step("Check the title of the checkout complete page")
    def check_page_title(self) -> bool:
        """
        Check the title of the checkout complete page.
        """
        title = self.page.get_by_test_id("title").text_content()
        is_title_correct = title == self.CHECKOUT_COMPLETE_PAGE_TITLE
        if is_title_correct:
            print(f"Checkout complete page title is correct: {title}")
        else:
            print(f"Checkout complete page title is incorrect: {title}")
            ScreenshotManager.take_screenshot(self.page, f"checkout-complete-title-{title}")
        return is_title_correct

    def check_page_url(self) -> bool:
        """
        Check the URL of the checkout complete page.
        """
        current_url = self.page.url
        is_url_correct = current_url == self.CHECKOUT_COMPLETE_PAGE_URL
        if is_url_correct:
            print(f"Checkout complete page URL is correct: {current_url}")
        else:
            print(f"Checkout complete page URL is incorrect: {current_url}")
            ScreenshotManager.take_screenshot(self.page, f"checkout-complete-url-{current_url}")
        return is_url_correct