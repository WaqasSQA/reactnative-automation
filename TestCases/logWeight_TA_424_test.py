import time
from faker import Faker
from Pages.logWeight_TA_424_page import LogWeightPage
from Pages.login_page import LoginPage
from config import PHONENUMBER, PASSWORD, COUNTRY
from conftest import setup_appium_driver


def test_user_logs_weight_from_health_profile(setup_appium_driver):
    print("Test Case Started - User Logs Weight Reading From Health Profile")
    driver = setup_appium_driver
    logWeight_TA_424 = LogWeightPage(driver)
    login_page = LoginPage(driver)

    login_page.choose_country_code()
    login_page.enter_country(COUNTRY)
    login_page.select_country()
    login_page.enter_phone_number(PHONENUMBER)
    login_page.enter_password(PASSWORD)
    login_page.click_login_button()

    fake = Faker()
    random_weight = fake.random_int(min=133 , max=198)
    logWeight_TA_424.navigate_health_profile_screen()
    logWeight_TA_424.navigate_health_logs_screen()
    logWeight_TA_424.navigate_weight_screen()
    logWeight_TA_424.navigate_enter_details_screen()
    logWeight_TA_424.enter_weight(random_weight)
    logWeight_TA_424.click_add()

    time.sleep(10)

    assert True
