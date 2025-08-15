from playwright.sync_api import Page
from tests.fixtures.screenshot_manager import ScreenshotManager
import os
from behave import step


class CheckoutInformationPage:
    """
    Represents the Checkout Information Page in the application.
    """
    CHECKOUT_INFORMATION_PAGE_URL = os.getenv("CHECKOUT_INFORMATION_PAGE_URL", "https://www.saucedemo.com/checkout-step-one.html")
    CHECKOUT_INFORMATION_PAGE_TITLE = os.getenv("CHECKOUT_INFORMATION_PAGE_TITLE", "Checkout: Your Information")

    def __init__(self, page: Page):
        self.page = page

    @step("Check the title of the checkout information page")
    def check_title(self) -> bool:
        """
        Check the title of the checkout information page.
        """
        title = self.page.get_by_test_id("title").text_content()
        # return title == "Checkout: Your Information"
        is_title_correct = title == self.CHECKOUT_INFORMATION_PAGE_TITLE
        if is_title_correct:
            print(f"Current title is correct: {title}")
        else:
            ScreenshotManager.take_screenshot(self.page, "Current title is incorrect")
            print(f"Current title is incorrect: {title}")
        return is_title_correct

    @step("Get the title of the checkout information page")
    def get_title(self) -> str:
        """
        Get the title of the checkout information page.
        """
        return self.page.get_by_test_id("title").text_content()

    @step("Click the checkout button")
    def button_click(self, button_name: str):
        """
        Click a button identified by its test ID.
        """
        self.page.get_by_test_id(button_name).click()

    @step("Fill in personal information")
    def fill_in_personal_information(self, personal_info):
        """
        Fill in personal information on the checkout page.
        """
        first_name = ""
        last_name = ""
        postal_code = ""
        if not personal_info:
            raise ValueError("Personal data is either empty or null")

        for person in personal_info:
            first_name = person["first_name"]
            last_name = person["last_name"]
            postal_code = person["postal_code"]

        self.page.locator('[placeholder="First Name"]').fill(first_name)
        self.page.locator('[placeholder="Last Name"]').fill(last_name)
        self.page.locator('[placeholder="Zip/Postal Code"]').fill(postal_code)

    @step("Check the URL of the checkout information page")
    def check_page_url(self) -> bool:
        """
        Check if the current URL matches the expected checkout step one URL.
        """
        current_url = self.page.url
        is_url_correct = current_url == self.CHECKOUT_INFORMATION_PAGE_URL
        if is_url_correct:
            print(f"Current URL is correct: {current_url}")
        else:
            ScreenshotManager.take_screenshot(self.page, "Current URL is incorrect")
            print(f"Current URL is incorrect: {current_url}")
        return is_url_correct

    @step("Click the cancel button on the checkout information page")
    def cancel_button_click(self):
        """
        Click the cancel button on the checkout information page.
        """
        self.page.get_by_test_id("cancel").click()