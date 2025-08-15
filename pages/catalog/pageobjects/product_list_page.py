import os

import playwright.sync_api
from playwright.sync_api import Page
from tests.fixtures.screenshot_manager import ScreenshotManager

PRODUCT_LIST_PAGE_URL = os.getenv("PRODUCT_LIST_PAGE_URL", "https://www.saucedemo.com/inventory.html")

class ProductListPage:
    def __init__(self, page: Page):
        self.page = page

    def get_title(self) -> playwright.sync_api.Locator:
        """Get the title of the product list page."""
        title_element = self.page.get_by_test_id("title")
        if not title_element.is_visible():
            ScreenshotManager.take_screenshot(self.page, "title-not-visible")
            return None
        return title_element

    def get_first_product_name(self, product_name: str) -> bool:
        """Verify if the first product name matches the given name."""
        # first_product_name = self.page.locator('[data-test="inventory-item"]').first.locator('[data-test="inventory-item-name"]').text_content()
        first_product_name = self.page.get_by_test_id("inventory-item").first.get_by_test_id("inventory-item-name").text_content()
        is_equal = first_product_name == product_name
        if is_equal:
            ScreenshotManager.take_screenshot(self.page, f"first-product-name-{product_name}")
        else:
            ScreenshotManager.take_screenshot(self.page, f"first-product-name-not-equal-{first_product_name}")
        return is_equal

    def sort_by(self, sort_criteria: str):
        """Sort products by the given criteria."""
        self.page.get_by_test_id("product-sort-container").select_option(sort_criteria)
        ScreenshotManager.take_screenshot(self.page, f"sorted-by-{sort_criteria}")

    def get_sort_option(self, sort_criteria: str) -> bool:
        """Verify if the given sort option is selected."""
        selected_option = self.page.get_by_test_id("active-option").text_content()
        is_selected = selected_option == sort_criteria
        if is_selected:
            ScreenshotManager.take_screenshot(self.page, f"sort-option-{selected_option}")
        else:
            ScreenshotManager.take_screenshot(self.page, f"sort-option-not-selected-{selected_option}")
        return is_selected

    def open_product_list_page(self):
        """Navigate to the product list page."""
        self.page.goto(PRODUCT_LIST_PAGE_URL)
        ScreenshotManager.take_screenshot(self.page, "product-list-page")

    def add_product_to_cart(self, product_name: str):
        """Add a product to the shopping cart by its name."""
        product = self.page.get_by_test_id("inventory-item")
        product_id_name = product_name.lower().replace(" ", "-")
        add_to_cart_button = product.locator(f'[data-test="add-to-cart-{product_id_name}"]')
        add_to_cart_button.click()
        ScreenshotManager.take_screenshot(self.page, f"product-added-to-cart-{product_name}")

    def remove_product_from_cart(self, product_name: str):
        """Remove a product from the shopping cart by its name."""
        product = self.page.get_by_test_id("inventory-item")
        remove_from_cart_button = product.locator(f'[data-test="remove-{product_name.lower().replace(" ", "-")}"]')
        remove_from_cart_button.click()
        ScreenshotManager.take_screenshot(self.page, f"product-removed-from-cart-{product_name}")

    def get_cart_count(self) -> int:
        """Retrieve the number of items in the shopping cart."""
        if not self.page.get_by_test_id("shopping-cart-badge").is_visible():
            ScreenshotManager.take_screenshot(self.page, "shopping-cart-icon-not-visible")
            return 0
        return int(self.page.get_by_test_id("shopping-cart-badge").text_content())

    def click_checkout_button(self):
        """Click the checkout button."""
        self.page.get_by_test_id("checkout").click()

    def check_page_url(self) -> bool:
        """Check if the current page URL matches the expected URL."""
        current_url = self.page.url
        is_correct_url = current_url == PRODUCT_LIST_PAGE_URL
        if not is_correct_url:
            ScreenshotManager.take_screenshot(self.page, "current-url-not-correct")
        return is_correct_url

    def get_product_button_state(self, product_name: str) -> bool:
        """Check if the product button is enabled or marked for removal."""
        product_button = self.page.locator(f'[data-test="remove-{product_name.lower().replace(" ", "-")}"]')
        is_enabled = product_button.is_enabled()
        ScreenshotManager.take_screenshot(self.page, "product-button-enabled" if is_enabled else "product-button-disabled")
        return is_enabled

    def click_on_product_name(self, product_name: str):
        """Click on the product name to navigate to the product details page."""
        product = self.page.get_by_test_id("inventory-item")
        product_name_locator = product.get_by_test_id("inventory-item-name").filter(has_text=product_name)
        ScreenshotManager.take_screenshot(self.page, f"product-name-clicked-{product_name}")
        product_name_locator.click()

    def check_title(self) -> bool:
        """Check if the page title matches the expected title."""
        title_element = self.page.locator('[data-test="title"]')
        title = title_element.text_content()
        is_title_correct = title == "Products"
        if not is_title_correct:
            ScreenshotManager.take_screenshot(self.page, "page-title-not-correct")
        return is_title_correct