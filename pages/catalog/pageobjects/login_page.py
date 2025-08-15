# pages/catalog/pageobjects/login_page.py
from playwright.sync_api import Page, Locator, expect
from tests.fixtures.screenshot_manager import ScreenshotManager
import os

class LoginPage:
 URL = os.getenv("URL", "https://www.saucedemo.com/")

 def __init__(self, page: Page):
     self.page = page
     self.username_input: Locator = self.page.get_by_placeholder("Username")
     self.password_input: Locator = self.page.get_by_placeholder("Password")
     self.login_button: Locator = self.page.get_by_role("button", name="Login")
     self.error_message: Locator =  self.page.get_by_test_id("error")

 def login_user(self, user):
     """Login user with username and password."""
     if user.username == "NULL":  # You can define a placeholder for null
         user.username = ""  # Treat "NULL" as an empty string
     if user.password == "NULL":
         user.password = ""
     self.page.get_by_placeholder("Username").fill(user.username)
     self.page.get_by_placeholder("Password").fill(user.password)
     ScreenshotManager.take_screenshot(self.page, "login-page")  # Implement as needed
     self.page.get_by_role("button", name="Login").click()

 def title(self) -> str:
     """Get the title of the page."""
     ScreenshotManager.take_screenshot(self.page, "title is equal to Product")
     return self.page.get_by_test_id("title").text_content()

 def login_error_message(self) -> str:
     """Get error message."""
     print("Retrieving error message...")
     # self.page.get_by_test_id("error").wait_for()
     ScreenshotManager.take_screenshot(self.page, "error-message")
     # If there are no error messages then
     expect(self.page.get_by_test_id("error")).to_be_visible()
     error_message: str = self.page.get_by_test_id("error").text_content()
     print(f"Error message: {error_message}")
     return error_message

 def open_home_page(self):
     """Open the home page."""
     self.page.goto(self.URL)
     print(self.URL)
     ScreenshotManager.take_screenshot(self.page, "home-page")

 def check_page_url(self) -> bool:
     """Check if the current page URL is correct."""
     current_url = self.page.url
     is_correct_url = current_url == self.URL
     if is_correct_url:
         print(f"Current URL is correct: {current_url}")
     else:
         print(f"Current URL is not correct: {current_url}")
         ScreenshotManager.take_screenshot(self.page, "current-url-not-correct")
     return is_correct_url