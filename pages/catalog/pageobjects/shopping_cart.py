import os
from playwright.sync_api import Page, Locator
from tests.fixtures.screenshot_manager import ScreenshotManager
from behave import step

SHOPPING_CART_PAGE_URL = os.getenv("SHOPPING_CART_PAGE_URL", "https://www.saucedemo.com/cart.html")
SHOPPING_CART_PAGE_TITLE = os.getenv("SHOPPING_CART_TITLE", "Your Cart")

class ShoppingCartPage:
    """Page object for the shopping cart page."""
    def __init__(self, page: Page):
        self.page = page

    def convert_to_price_format(self, text: str) -> float:
        """Remove the dollar sign from a string."""
        return float(text.replace("$", "").strip().replace("Item total: ", "").strip())

    def open_shopping_cart_page(self):
        """Open the shopping cart page."""
        self.page.goto(SHOPPING_CART_PAGE_URL)

    def get_title(self) -> str:
        """Get the title of the shopping cart page."""
        title = self.page.locator('[data-test="title"]').text_content()
        ScreenshotManager.take_screenshot(self.page, "shopping-cart-title")
        return title

    def check_page_url(self) -> bool:
        """Check if the current page URL matches the shopping cart page URL."""
        is_url_correct = self.page.url == SHOPPING_CART_PAGE_URL
        if not is_url_correct:
            ScreenshotManager.take_screenshot(self.page, "shopping-cart-page-url-incorrect")
        return is_url_correct

    def check_page_title(self) -> bool:
        """Check if the shopping cart page title matches the expected title."""
        title = self.get_title()
        is_title_correct = title == SHOPPING_CART_PAGE_TITLE
        if not is_title_correct:
            ScreenshotManager.take_screenshot(self.page, "shopping-cart-page-title")
        return is_title_correct

    def get_cart_count(self) -> int:
        """Retrieve the number of items in the shopping cart."""
        if not self.page.locator('[data-test="shopping-cart-badge"]').is_visible():
            ScreenshotManager.take_screenshot(self.page, "shopping-cart-icon-not-visible")
            return 0
        return int(self.page.locator('[data-test="shopping-cart-badge"]').text_content())

    def verify_cart_contents(self, product_table):
        """Verify that the shopping cart contents match the expected products."""
        if not product_table:
            raise ValueError("Product table is empty or null")

        cart_list = self.page.get_by_test_id("cart-list")
        sub_items = cart_list.nth(0).get_by_test_id("inventory-item").all()

        # Check if cart is empty
        if sub_items.count == 0:
            print("Cart is empty.")
            return False

        for product in product_table:
            product_name = product["product"]
            quantity = product["quantity"]
            total = product["total"]

            # item = sub_items.filter(has_text=product_name)
            item = next((i for i in sub_items if product_name in i.text_content()), None)
            if not item or item.locator('[data-test="item-quantity"]').text_content() != quantity or \
               item.locator('[data-test="inventory-item-price"]').text_content() != total:
                return False
        return True

    def get_cart_difference(self, expected_table):
        """
        Compares the cart contents with the expected table and returns a string
        describing the differences, or None if there are no differences.
        """
        differences = []
        # Assuming self.get_cart_contents() returns a list of dicts with product info
        actual_cart = self.get_cart_contents()
        expected_cart = [row.as_dict() for row in expected_table]

        # Compare lengths
        if len(actual_cart) != len(expected_cart):
            differences.append(
                f"Expected {len(expected_cart)} items, found {len(actual_cart)} items."
            )

        # convert actual_cart to a list of dicts for easier comparison
        actual_cart = [{
            "name": item.locator('[data-test="inventory-item-name"]').text_content(),
            "quantity": item.locator('[data-test="item-quantity"]').text_content(),
            "total": item.locator('[data-test="inventory-item-price"]').text_content()
        } for item in actual_cart]

        # Compare each product
        for expected, actual in zip(expected_cart, actual_cart):
            for key, expected_value in expected.items():
                actual_value = actual.get(key, "")
                if expected_value != actual_value:
                    differences.append(
                        f"Mismatch for '{key}': expected '{expected_value}', found '{actual_value}'"
                    )

        # Snapshot the differences if any
        if differences:
            ScreenshotManager.take_screenshot(self.page, "cart-differences")
        return "\n".join(differences) if differences else None

    def remove_product_from_cart(self, product_name: str):
        """Remove a product from the shopping cart by its name."""
        remove_button = self.page.locator(f'[data-test="remove-{product_name.lower().replace(" ", "-")}"]')
        remove_button.click()
        ScreenshotManager.take_screenshot(self.page, f"product-removed-from-cart-{product_name}")

    def continue_shopping(self):
        """Navigate back to the product list page."""
        self.page.locator('[data-test="continue-shopping"]').click()
        ScreenshotManager.take_screenshot(self.page, "continue-shopping-button-clicked")

    def back_to_products(self):
        """Navigate back to the product list page."""
        self.page.locator('[data-test="back-to-products"]').click()
        ScreenshotManager.take_screenshot(self.page, "back-to-products-button-clicked")

    def get_cart_contents(self):
        """Retrieve the number of items currently in the shopping cart."""
        cart_list = self.page.get_by_test_id("cart-list")
        sub_items: list[Locator] = cart_list.nth(0).get_by_test_id("inventory-item").all()
        return sub_items