import os
from allure_commons._allure import attach
from allure_commons.types import AttachmentType

class ScreenshotManager:
    @staticmethod
    def take_screenshot(page, name):
        # Ensure the screenshots directory exists
        screenshots_dir = os.path.join("target", "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)
        file_path = os.path.join(screenshots_dir, f"{name}.png")
        # Take screenshot and save to file
        page.screenshot(path=file_path, full_page=True)
        # Attach screenshot to Allure report
        with open(file_path, "rb") as image_file:
            attach(image_file.read(), name, AttachmentType.PNG)