import time
from Pages.login_page import LoginPage
from config import PHONENUMBER, PASSWORD, COUNTRY, INVALID_PHONE_NUMBER  # Import the credentials
from conftest import setup_appium_driver


def test_user_login(setup_appium_driver):
    print("Test case 1 started- User is logging in")
    driver = setup_appium_driver  # The driver instance provided by the fixture
    # Create Page Object instance
    Login_Page = LoginPage(driver)
    # Perform login actions

    # This is Test case number 1
    Login_Page.choose_country_code()
    Login_Page.enter_country(COUNTRY)
    Login_Page.select_country()
    Login_Page.enter_phone_number(PHONENUMBER)
    Login_Page.enter_password(PASSWORD)
    Login_Page.click_login_button()
    time.sleep(10)
    # Add assertions here
    assert True  # Replace with your assertions
