import time
from Pages.account_page import AccountPage
from Pages.login_page import LoginPage
from Pages.healthProfile_page import HealthProfilePage
from config import PHONENUMBER, PASSWORD, COUNTRY, ENGLISH_LANGUAGE, VIETNAMESE_LANGUAGE, THAI_LANGUAGE, CHINESE_LANGUAGE, USER_EMAIL  # Import the credentials
from conftest import setup_appium_driver
from faker import Faker




def test_user_can_change_language_settings(setup_appium_driver):
    print("Test that user can change language settings")
    driver = setup_appium_driver  # The driver instance provided by the fixture
    Account_Page = AccountPage(driver)
    Login_Page = LoginPage(driver)
    # First login to the application
    Login_Page.choose_country_code()
    Login_Page.enter_country(COUNTRY)
    Login_Page.select_country()
    Login_Page.enter_phone_number(PHONENUMBER)
    Login_Page.enter_password(PASSWORD)
    Login_Page.click_login_button()

    Account_Page.navigate_account_screen()
    Account_Page.select_language_menu(ENGLISH_LANGUAGE)
    Account_Page.choose_thai()
    Account_Page.select_language_menu(THAI_LANGUAGE)
    Account_Page.choose_chinese()
    Account_Page.select_language_menu(CHINESE_LANGUAGE)
    Account_Page.choose_vietnamese()
    Account_Page.select_language_menu(VIETNAMESE_LANGUAGE)
    Account_Page.choose_english()


def test_user_changes_gender_from_account_screen(setup_appium_driver):
    print("Test that user visits account screen and changes Gender")
    driver = setup_appium_driver  # The driver instance provided by the fixture
    # Create Page Object instance
    Account_Page = AccountPage(driver)
    Account_Page.click_personal_information()
    Account_Page.change_gender()
    Account_Page.save_gender()
    time.sleep(10)
    # Add assertions here
    assert True  # Replace with your assertions


def test_user_inputs_stress_data_from_stress_screen(setup_appium_driver):
    print("Test that user can input stress information")
    driver = setup_appium_driver  # The driver instance provided by the fixture
    Health_Profile_Page = HealthProfilePage(driver)
    Health_Profile_Page.navigate_to_health_profile_page()
    Health_Profile_Page.navigate_to_stress_screen()
    time.sleep(8)
    Health_Profile_Page.select_first_stress_option()
    Health_Profile_Page.select_second_stress_option()
    Health_Profile_Page.select_third_stress_option()
    Health_Profile_Page.click_save_stress_data()


def test_user_views_policies(setup_appium_driver):
    print("Test that user can view policies of account")
    driver = setup_appium_driver  # The driver instance provided by the fixture
    Account_Page = AccountPage(driver)
    Account_Page.navigate_back_to_accounts()
    time.sleep(10)
    Account_Page.scroll_down()
    Account_Page.click_policies()
    Account_Page.view_privacy_policy()
    time.sleep(5)
    Account_Page.view_terms()
    time.sleep(5)

def test_user_can_change_email(setup_appium_driver):
    fake = Faker()
    fake_email = fake.email()
    print("Test that user can change email")
    driver = setup_appium_driver  # The driver instance provided by the fixture
    Account_Page = AccountPage(driver)
    Account_Page.navigate_back_to_accounts()
    Account_Page.navigate_to_settings_page()
    Account_Page.navigate_to_email_page()
    Account_Page.primary_email(fake_email)
    Account_Page.confirm_email(fake_email)
    Account_Page.click_save_button()

    Account_Page.navigate_to_email_page()
    Account_Page.primary_email(USER_EMAIL)
    Account_Page.confirm_email(USER_EMAIL)
    Account_Page.click_save_button()
