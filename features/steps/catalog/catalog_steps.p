from playwright.async_api import async_playwright, expect
from behave import given, when, then

# from features.environment import after_all

@given(u'Sally logs in')
async def step_sally_logs_in(context):
    # Navigate to the Swag Labs login page
    context.playwright = await async_playwright().start()  # Use async_playwright and await
    context.browser = await context.playwright.chromium.launch()
    context.page = await context.browser.new_page()
    await context.page.goto("https://www.saucedemo.com/")
    await context.page.fill("#user-name", "standard_user")
    await context.page.fill("#password", "secret_sauce")
    await context.page.click("#login-button")


@when('Sally views the details of the "Sauce Labs Backpack" by clicking on the product name')
def step_sally_views_backpack_details(context):
    # Click on the product name to view details
    context.page.click("text='Sauce Labs Backpack'")


@then("Sally should see the product details page")
def step_sally_sees_product_details(context):
    # Verify the product details page is displayed
    assert (
        context.page.url == "https://www.saucedemo.com/inventory-item.html?id=4"
    ), "Product details page URL does not match"
    assert context.page.locator(".inventory_details_name").is_visible(), "Product name is not visible"
    assert context.page.locator(".inventory_details_desc").is_visible(), "Product description is not visible"
    assert context.page.locator(".inventory_details_price").is_visible(), "Product price is not visible"


@then("the product details page should display the following information")
def step_the_product_details_page_should_display_information(context):
    for row in context.table:
        key = row['field']
        value = row['value']
        assert (
            context.page.locator(f".inventory_details_{key}").text_content() == value
        ), f"{key} does not match expected value"

@then('the product image for "Sauce Labs Backpack" should be displayed')
def step_the_product_image_for_product_should_be_displayed(context):
    assert context.page.locator(".inventory_details_img").is_visible(), "Product image is not visible"


# @then("the product details page should display the following information")
# def step_sally_sees_product_details_info(context):
#     # Verify the product details page displays the expected information
#     expected_details = {
#         "name": "Sauce Labs Backpack",
#         "description": "This is a description of the Sauce Labs Backpack.",
#         "price": "$29.99",
#         "image": "https://example.com/sauce-labs-backpack.jpg"
#     }
#     for key, value in expected_details.items():
#         assert context.page.locator(f".product-{key}").text_content() == value, f"{key} does not match expected value."


# @then('the product image for "Sauce Labs Backpack" should be displayed')
# def step_product_image_displayed(context):
#     # Verify the product image is displayed
#     assert context.page.locator(".product-image").is_visible(), "Product image is not visible"


@then("Sally goes back to the inventory page")
def step_goes_back_to_inventory(context):
    # Navigate back to the inventory page
    context.page.locator(".back-to-inventory").click()


# @when("Sally adds the following products to the cart")
# def step_impl(context):
#     raise StepNotImplementedError("When Sally adds the following products to the cart")
#
#
# @when("Sally views her cart")
# def step_impl(context):
#     raise StepNotImplementedError("When Sally views her cart")
#
#
# @when("Sally begins the checkout process")
# def step_impl(context):
#     raise StepNotImplementedError("When Sally begins the checkout process")
#
#
# @then("Sally continues to the overview page for review only to cancel the order")
# def step_impl(context):
#     raise StepNotImplementedError("Then Sally continues to the overview page for review only to cancel the order")
#
#
# @when("Sally fills in her personal information")
# def step_impl(context):
#     raise StepNotImplementedError("When Sally fills in her personal information")
#
#
# @then("Sally continues to the information page for review only to cancel the order")
# def step_impl(context):
#     raise StepNotImplementedError("Then Sally continues to the information page for review only to cancel the order")
#
#
# @given("Sally adds the following products to the cart")
# def step_impl(context):
#     raise StepNotImplementedError("Given Sally adds the following products to the cart")
#
#
# @then("the shopping cart page should indicate all products picked for checkout")
# def step_impl(context):
#     raise StepNotImplementedError("Then the shopping cart page should indicate all products picked for checkout")
#
#
# @then("Sally fills in her personal information")
# def step_impl(context):
#     raise StepNotImplementedError("Then Sally fills in her personal information")
#
#
# @then("Sally continues to the overview page for review")
# def step_impl(context):
#     raise StepNotImplementedError("Then Sally continues to the overview page for review")
#
#
# @when("Sally clicks on the finish button")
# def step_impl(context):
#     raise StepNotImplementedError("When Sally clicks on the finish button")
#
#
# @then("she should see the confirmation message")
# def step_impl(context):
#     raise StepNotImplementedError("Then she should see the confirmation message")
#
#
# @when('Sally removes the "Sauce Labs Backpack" from her cart')
# def step_impl(context):
#     raise StepNotImplementedError('When Sally removes the "Sauce Labs Backpack" from her cart')
#
#
# @when('Sally adds a "Sauce Labs Backpack" to her cart')
# def step_impl(context):
#     raise StepNotImplementedError('When Sally adds a "Sauce Labs Backpack" to her cart')
#
#
# @then('the "Sauce Labs Backpack" status indicates it has been added to the cart')
# def step_impl(context):
#     raise StepNotImplementedError('Then the "Sauce Labs Backpack" status indicates it has been added to the cart')
#
#
# @then("Sally views her cart")
# def step_impl(context):
#     raise StepNotImplementedError("Then Sally views her cart")
#
#
# @when("Sally continues shopping after adding products to her cart")
# def step_impl(context):
#     raise StepNotImplementedError("When Sally continues shopping after adding products to her cart")
#
#
# @then("she should be able to view the inventory page and add more products")
# def step_impl(context):
#     raise StepNotImplementedError("Then she should be able to view the inventory page and add more products")
#
#
# @when('Sally removes the "Test.allTheThings() T-Shirt (Red)" from her cart on inventory page')
# def step_impl(context):
#     raise StepNotImplementedError(
#         'When Sally removes the "Test.allTheThings() T-Shirt (Red)" from her cart on inventory page'
#     )
#
#
# @then("check that only the expected products are in her cart")
# def step_impl(context):
#     raise StepNotImplementedError("Then check that only the expected products are in her cart")
#
#
# @when("Sally removes all products from her cart")
# def step_impl(context):
#     raise StepNotImplementedError("When Sally removes all products from her cart")
#
#
# @then("Sally views her cart and checks that all the products have been removed")
# def step_impl(context):
#     raise StepNotImplementedError("Then Sally views her cart and checks that all the products have been removed")
#
#
# @when('Sally sorts by "Price (low to high)"')
# def step_impl(context):
#     raise StepNotImplementedError('When Sally sorts by "Price (low to high)"')
#
#
# @then('the first product displayed should be "Sauce Labs Onesie"')
# def step_impl(context):
#     raise StepNotImplementedError('Then the first product displayed should be "Sauce Labs Onesie"')
#
#
# @when('Sally sorts by "Price (high to low)"')
# def step_impl(context):
#     raise StepNotImplementedError('When Sally sorts by "Price (high to low)"')
#
#
# @then('the first product displayed should be "Sauce Labs Fleece Jacket"')
# def step_impl(context):
#     raise StepNotImplementedError('Then the first product displayed should be "Sauce Labs Fleece Jacket"')
#
#
# @when('Sally sorts by "Name (A to Z)"')
# def step_impl(context):
#     raise StepNotImplementedError('When Sally sorts by "Name (A to Z)"')
#
#
# @then('the first product displayed should be "Sauce Labs Backpack"')
# def step_impl(context):
#     raise StepNotImplementedError('Then the first product displayed should be "Sauce Labs Backpack"')
#
#
# @when('Sally sorts by "Name (Z to A)"')
# def step_impl(context):
#     raise StepNotImplementedError('When Sally sorts by "Name (Z to A)"')
#
#
# @then('the first product displayed should be "Test.allTheThings() T-Shirt (Red)"')
# def step_impl(context):
#     raise StepNotImplementedError('Then the first product displayed should be "Test.allTheThings() T-Shirt (Red)"')
#
#
# @given("Sally is on the login page")
# def step_impl(context):
#     raise StepNotImplementedError("Given Sally is on the login page")
#
#
# @when('Sally enters her "standard_user" and "not_so_secret_sauce that are invalid"')
# def step_impl(context):
#     raise StepNotImplementedError('When Sally enters her "standard_user" and "not_so_secret_sauce that are invalid"')
#
#
# @then('the error message should be "Username and password do not match any user in this service"')
# def step_impl(context):
#     raise StepNotImplementedError(
#         'Then the error message should be "Username and password do not match any user in this service"'
#     )
#
#
# @when('Sally enters her "" and " that are invalid"')
# def step_impl(context):
#     raise StepNotImplementedError('When Sally enters her "" and " that are invalid"')
#
#
# @then('the error message should be "Username is required"')
# def step_impl(context):
#     raise StepNotImplementedError('Then the error message should be "Username is required"')
#
#
# @when('Sally enters her "standard_user" and " that are invalid"')
# def step_impl(context):
#     raise StepNotImplementedError('When Sally enters her "standard_user" and " that are invalid"')
#
#
# @when('Sally enters her "" and "secret_sauce that are invalid"')
# def step_impl(context):
#     raise StepNotImplementedError('When Sally enters her "" and "secret_sauce that are invalid"')
#
#
# @given("Sally opens a browser link to the inventory page")
# def step_impl(context):
#     raise StepNotImplementedError("Given Sally opens a browser link to the inventory page")
#
#
# @when("Sally is redirected to the login page")
# def step_impl(context):
#     raise StepNotImplementedError("When Sally is redirected to the login page")
#
#
# @then("the error message should be \"You can only access '/inventory.html' when you are logged in.\"")
# def step_impl(context):
#     raise StepNotImplementedError(
#         "Then the error message should be \"You can only access '/inventory.html' when you are logged in.\""
#     )
