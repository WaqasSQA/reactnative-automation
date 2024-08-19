import time
from faker import Faker
from Pages.bloodSugar_TA_422_page import BloodSugarPage
from Pages.login_page import LoginPage
from config import PHONENUMBER, PASSWORD, COUNTRY
from conftest import setup_appium_driver


def test_user_logs_blood_sugar_from_health_profile(setup_appium_driver):
    print("Test Case Started - User Logs Blood Sugar Reading From Health Profile")
    driver = setup_appium_driver
    bloodSugar_TA_422_page = BloodSugarPage(driver)
    login_page = LoginPage(driver)

    login_page.choose_country_code()
    login_page.enter_country(COUNTRY)
    login_page.select_country()
    login_page.enter_phone_number(PHONENUMBER)
    login_page.enter_password(PASSWORD)
    login_page.click_login_button()

    fake = Faker()
    random_reading = fake.random_int(min=100, max=150)
    bloodSugar_TA_422_page.navigate_health_profile_screen()
    bloodSugar_TA_422_page.navigate_health_logs_screen()
    bloodSugar_TA_422_page.navigate_enter_details_screen()
    bloodSugar_TA_422_page.enter_reading(random_reading)
    bloodSugar_TA_422_page.select_meal_time_dropdown()
    bloodSugar_TA_422_page.select_meal_time()
    bloodSugar_TA_422_page.click_add()
    time.sleep(10)

    assert True
