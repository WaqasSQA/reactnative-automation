from faker import Faker
from Pages.body_measurements_TA_286_page import BodyMeasurements
from Pages.login_page import LoginPage
from config import PHONENUMBER, PASSWORD, COUNTRY
from conftest import setup_appium_driver


def test_user_enter_body_measurements(setup_appium_driver):
    print(
        "Test Case Started - TA-286 - The user should be able to enter values and save in Body Measurement in Health "
        "Profile tab")
    driver = setup_appium_driver
    body_measurements_TA_286 = BodyMeasurements(driver)
    login_page = LoginPage(driver)

    login_page.choose_country_code()
    login_page.enter_country(COUNTRY)
    login_page.select_country()
    login_page.enter_phone_number(PHONENUMBER)
    login_page.enter_password(PASSWORD)
    login_page.click_login_button()

    fake = Faker()
    random_height_cm = fake.random_int(min=150, max=200)
    random_weight_kg = fake.random_int(min=50, max=100)
    random_weight_lbs = fake.random_int(min=150, max=210)

    body_measurements_TA_286.navigate_account_tab()
    body_measurements_TA_286.click_health_profile()
    body_measurements_TA_286.click_body_measurement()
    body_measurements_TA_286.click_height_drop_down()
    body_measurements_TA_286.select_cm()
    body_measurements_TA_286.enter_height(random_height_cm)
    body_measurements_TA_286.enter_weight(random_weight_kg)
    body_measurements_TA_286.select_save_continue()
    body_measurements_TA_286.click_body_measurement()
    body_measurements_TA_286.click_height_drop_down()
    body_measurements_TA_286.select_ft()
    body_measurements_TA_286.enter_height_ft()
    body_measurements_TA_286.enter_weight_lbs(random_weight_lbs)
    body_measurements_TA_286.select_save_continue()




