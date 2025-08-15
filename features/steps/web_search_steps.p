from behave import given, when, then
from playwright.sync_api import sync_playwright, Page, expect



@given(u'I navigate to google.com')
def step_impl(context):
    print(f'Given I navigate to google.com')
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context.page = browser.new_page()
    context.page.goto("https://www.google.com")

# You'll need to update all subsequent steps to use await as well.

# @when("I search for {search_term}")
# def step_impl(context, search_term):
#     print(f'When I search for "{search_term}"')
#     context.page.get_by_title("Search").fill(search_term)
#     context.page.get_by_label("Google Search").first.click()

@when('I search for "{term}"')
def step_impl(context, term):
    """
    :type term: str
    :type context: behave.runner.Context
    """
    print(f'When I search for {term}')
    context.page.get_by_title("Search").fill(term)
    context.page.get_by_label("Google Search").first.click()

@then("I should see {expected_text} in the search results")
def step_impl(context, expected_text):
    print(f'STEP Then I should see {expected_text} in the search results')
    expect(context.page.get_by_text(expected_text)).to_be_visible()

@then('I close the browser')
def step_impl(context):
    print('STEP Then I close the browser')
    context.page.close()
    context.page.context.browser.close()
    context.page.context.playwright.stop()


# @when("I search for {search_term}")
# def step_impl(context, search_term):
#     """
#     :type context: behave.runner.Context
#     :type search_term: str
#     """
#     raise NotImplementedError(u'STEP: When I search for <search_term>')
