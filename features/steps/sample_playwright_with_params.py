from behave import given, when, then
from pages.catalog.pageobjects.login_page import LoginPage
from features.steps.User import User

# @given('I navigate to the user details page')
# def step_navigate_to_user_details_page(context):
#     context.login_page = LoginPage(context.page)
#     context.login_page.open_home_page()
#
#
# @when('I enter "{username}" and "{password}" and submit the form')
# def step_enter_username(context, username, password):
#     current_user = User(username, password)
#     context.login_page.login_user(current_user)
#
# @then('I should see a "{message}"')
# def step_see_message(context, message):
#     print(message)
#     # Wait for the error message to appear
#     actual_message = context.login_page.error_message()
#     print(f"Actual message: {actual_message}")
#     assert message == actual_message
