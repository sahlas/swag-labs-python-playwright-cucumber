"""Step definitions for login feature."""
from behave import given, when, then, step
from playwright.sync_api import sync_playwright, Page, expect

from pages.catalog.pageobjects.checkout_complete_page import CheckoutCompletePage
from pages.catalog.pageobjects.checkout_overview_page import CheckoutOverviewPage
from pages.catalog.pageobjects.checkout_information_page import CheckoutInformationPage
from pages.catalog.pageobjects.login_page import LoginPage
from pages.catalog.pageobjects.product_list_page import ProductListPage
from pages.catalog.pageobjects.shopping_cart import ShoppingCartPage
from features.steps.User import User
"""
Logs in Sally using credentials based on the user type specified in environment variables.
The method retrieves the user type from the environment, determines the corresponding
username and password, and logs in Sally by navigating to the login page and submitting the credentials.
"""

import os

dotenv = os.environ  # Mock dotenv with environment variables

@given("Sally has logged in with her account")
def sally_has_logged_in_with_her_account(context):
    user_type = dotenv.get("USER_TYPE", "standard_user")

    username = None
    password = None

    if user_type == "standard_user":
        print("Logging in as standard user")
        username = dotenv.get("STANDARD_USERNAME", "standard_user")
        password = dotenv.get("STANDARD_PASSWORD", "secret_sauce")
    else:
        raise ValueError(f"Unknown user type: {user_type}")

    context.login_page = LoginPage(context.page)
    context.product_list_page = ProductListPage(context.page)
    context.shopping_cart_page = ShoppingCartPage(context.page)
    context.checkout_information_page = CheckoutInformationPage(context.page)
    context.checkout_overview_page = CheckoutOverviewPage(context.page)
    context.checkout_complete_page = CheckoutCompletePage(context.page)

    context.login_page.open_home_page()
    current_user = User(username, password)
    context.login_page.login_user(current_user)


@when("I am redirected to the products page")
def when_redirected_to_products_page(context):
    """Verify user is redirected to the products page."""
    expect(context.page).to_have_url("https://www.saucedemo.com/inventory.html")


@then('I should see the products page title "{title}"')
def then_see_products_title(context, title):
    """Verify the products page title is displayed."""
    title_element = context.product_list_page.get_title()
    expect(title_element).to_have_text(title)


@then('I should see an error message "{error_message}"')
def then_see_error_message(context, error_message):
    """Verify the error message is displayed."""
    error_element = context.page.locator('[data-test="error"]')
    expect(error_element).to_have_text(error_message)

@given('I navigate to the user details page')
def navigate_to_user_details_page(context):
    context.login_page = LoginPage(context.page)
    context.login_page.open_home_page()


@when('I enter "{username}" and "{password}" and submit the form')
def enter_username(context, username, password):
    current_user = User(username, password)
    context.login_page.login_user(current_user)

@then('I should see a "{message}"')
def validate_error_message(context, message):
    print(message)
    # Wait for the error message to appear
    actual_message = context.login_page.login_error_message()
    assert message in actual_message


@when('Sally sorts by "{sort_criteria}"')
def sort_by_test(context, sort_criteria):
    """
    :type context: behave.runner.Context
    :type sort_criteria: str
    """
    context.product_list_page.sort_by(sort_criteria)
    assert context.product_list_page.get_sort_option(sort_criteria) is True


@then('the first product displayed should be "{first_product}"')
def step_impl(context, first_product):
    """
    :type context: behave.runner.Context
    :type first_product: str
    """
    assert context.product_list_page.get_first_product_name(first_product) is True, \
        f"First product name does not match expected: {first_product}"
    print(f"First product name matches expected: {first_product}")

@step("Sally adds the following products to the cart")
def the_user_adds_the_following_products_to_the_cart(context):
    """Add the following products to the cart."""
    assert context.product_list_page.check_page_url(), "Should be on the inventory page"
    assert context.product_list_page.check_title(), "Product list title should contain 'Products'"
    products = context.table
    for product in products:
        product_name = product.get("product")
        context.product_list_page.add_product_to_cart(product_name)

@when("Sally is ready to check out her products")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.shopping_cart_page.open_shopping_cart_page()
    assert context.shopping_cart_page.check_page_url(), "Should be on the shopping cart page"
    assert context.shopping_cart_page.check_page_title(), "Shopping cart title should be correct"
    cart_count = context.shopping_cart_page.get_cart_count()
    assert cart_count > 0, "Cart should not be empty"
    print(f"Cart contains {cart_count} items")


@then("the shopping cart page should indicate all products picked for checkout")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    data_match = context.shopping_cart_page.verify_cart_contents(context.table)
    # assert data_match, "All product details should be represented in the cart"
    assert data_match, (
        f"All product details should be represented in the cart. Differences: "
        f"{context.shopping_cart_page.get_cart_difference(context.table) or 'No differences found'}"
    )


@when("Sally begins the checkout process")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: When Sally begins the checkout process')
    context.product_list_page.click_checkout_button()
    assert context.checkout_information_page.check_page_url(), "Checkout overview page URL should be correct"
    assert context.checkout_information_page.check_title(), "Checkout page title should be 'Checkout: Your Information'"


@then("Sally fills in her personal information")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: Then Sally fills in her personal information')
    context.checkout_information_page.fill_in_personal_information(context.table)
    assert  context.checkout_information_page.check_title(), "Checkout information page title should be 'Checkout: Your Information'"

@step("Sally continues to the overview page for review")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: And Sally continues to the overview page for review')
    context.checkout_information_page.button_click("continue")
    actual_subtotal = context.checkout_overview_page.get_subtotal_price()

    expected_subtotal = sum(
        context.shopping_cart_page.convert_to_price_format(product["total"])
        for product in context.table
    )

    expected_subtotal = round(expected_subtotal, 2)
    assert actual_subtotal == expected_subtotal, (
        f"Subtotal should be correct. Expected: {expected_subtotal}, Actual: {actual_subtotal}"
    )
    print(f"Subtotal is correct: {actual_subtotal}")


@when("Sally clicks on the finish button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: When Sally clicks on the finish button')
    context.checkout_overview_page.finish_button_click()


@then("she should see the confirmation message")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: Then she should see the confirmation message')
    assert context.checkout_complete_page.check_page_url(), "Checkout complete page URL should be correct"
    assert context.checkout_complete_page.check_page_title(), "Checkout complete page title should be 'Checkout: Complete!'"
    assert context.checkout_complete_page.get_order_confirmation_message(), "Order confirmation message should"

#
# @when("Sally removes the product from her car")
# def product_removal_test(context):
#         initial_cart_count: int = context.shopping_cart_page.get_cart_count()
#         print(f"Initial cart count: {initial_cart_count}")
#
#         context.shopping_cart_page.remove_product_from_cart(product)
#
#         final_cart_count = context.shopping_cart_page.get_cart_count()
#         print(f"Final cart count: {final_cart_count}")
#
#         assert final_cart_count < initial_cart_count, (
#             "Cart count should be less than initial count after removing a product"
#         )
#

@when("Sally removes the product from her cart")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: When Sally removes the product from her cart')
    initial_cart_count = context.shopping_cart_page.get_cart_count()
    print(f"Initial cart count: {initial_cart_count}")

    # Assuming 'product' is defined in the context or passed as a parameter
    product = context.table[0]["product"]
    context.shopping_cart_page.remove_product_from_cart(product)

    final_cart_count = context.shopping_cart_page.get_cart_count()
    print(f"Final cart count: {final_cart_count}")

    assert final_cart_count < initial_cart_count, (
        "Cart count should be less than initial count after removing a product"
    )