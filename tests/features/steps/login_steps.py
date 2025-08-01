import time

from behave import given, when, then

from pages.login_page import LoginPage
from utils.browser_setup import get_driver
from utils.healing_agent import analyze_and_heal_failure


@given("I launch the browser")
def step_open_login_page(context):
    context.driver = get_driver()
    context.login_page = LoginPage(context.driver)
    context.login_page.open()

@when("I enters username and password")
def step_enter_credentials(context):
    context.login_page.enter_username("standard_user")
    time.sleep(2)
    context.login_page.enter_password("secret_sauce")
    time.sleep(2)
    try:
        context.login_page.click_login()
    except Exception as e:
        context_data = {
            "feature": "Login Page Functionality",
            "scenario": "login into Swag Labs",
            "step": "click login button"
        }
        analyze_and_heal_failure(str(e), context_data)
        raise e


@then("I should see the inventory page")
def step_verify_login(context):
    assert context.login_page.is_logged_in(), "Login failed!"
    context.driver.quit()

