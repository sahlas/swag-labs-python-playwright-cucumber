from playwright.sync_api import Page
import os
from behave import step
from tests.fixtures.screenshot_manager import ScreenshotManager

class CheckoutOverviewPage:
    """
    Represents the Checkout Overview Page in the application.
    """

    def __init__(self, page: Page):
        self.page = page
        self.CHECKOUT_OVERVIEW_PAGE_TITLE = os.getenv("CHECKOUT_OVERVIEW_PAGE_TITLE", "Checkout: Overview")
        self.CHECKOUT_OVERVIEW_PAGE_URL = os.getenv("CHECKOUT_OVERVIEW_PAGE_URL",
                                               "https://www.saucedemo.com/checkout-step-two.html")

    def check_title(self) -> bool:
        """
        Check the title of the checkout overview page.
        """
        title = self.page.get_by_test_id("title").text_content()
        return title == self.CHECKOUT_OVERVIEW_PAGE_TITLE

    def get_title(self) -> str:
        """
        Get the title of the checkout overview page.
        """
        return self.page.get_by_test_id("title").text_content()

    def get_total_price(self) -> str:
        """
        Get the total price of the items in the cart.
        """
        return self.page.get_by_test_id("total-label").text_content()


    def check_product_names(self, expected_product_names: list) -> bool:
        """
        Check if the product names in the cart match the expected product names.
        """
        product_names = self.page.get_by_test_id("inventory-item-name").all_text_contents()
        return set(expected_product_names).issubset(set(product_names))

    def finish_button_click(self):
        """
        Click the Finish button to complete the checkout process.
        """
        self.page.get_by_test_id("finish").click()

    def verify_cart_contents(self, products_in_cart: list) -> bool:
        """
        Verify if the product names in the cart match the expected product names.
        """
        return self.check_product_names(products_in_cart)

    def get_subtotal_price(self) -> float:
        """
        Get the subtotal price of the items in the cart.
        """
        price_text = self.page.get_by_test_id("subtotal-label").text_content()
        price_float: float = float(price_text.replace("$", "").strip().replace("Item total: ", ""))
        # Convert to float and round to 2 decimal places
        price_float = round(price_float, 2)
        return price_float

    def cancel_button_click(self):
        """
        Click the Cancel button to return to the previous page.
        """
        self.page.get_by_test_id("cancel").click()

    def check_page_url(self) -> bool:
        """
        Check if the current URL matches the expected checkout overview page URL.
        """
        current_url = self.page.url
        return current_url == self.CHECKOUT_OVERVIEW_PAGE_URL