import time
from Pages.login_page import LoginPage
from Pages.home_page import HomePage
from config import PHONENUMBER, PASSWORD, COUNTRY  # Import the credentials
from conftest import setup_appium_driver


def test_user_can_view_vitals_data_from_homepage(setup_appium_driver):
    print("Test user can see vitals detail from Homescreen")
    driver = setup_appium_driver  # The driver instance provided by the fixture
    # Create Page Object instance
    Login_Page = LoginPage(driver)
    Home_Page = HomePage(driver)

    # First login to the application
    Login_Page.choose_country_code()
    Login_Page.enter_country(COUNTRY)
    Login_Page.select_country()
    Login_Page.enter_phone_number(PHONENUMBER)
    Login_Page.enter_password(PASSWORD)
    Login_Page.click_login_button()

    Home_Page.click_steps_card()
    time.sleep(3)
    Home_Page.select_one_month_data()
    time.sleep(3)
    Home_Page.select_three_month_data()
    time.sleep(3)