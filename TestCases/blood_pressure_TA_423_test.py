from faker import Faker

from Pages.login_page import LoginPage
from Pages.bloodPressureHealth_TA_423_page import blood_HealthProfile
from config import PHONENUMBER, PASSWORD, COUNTRY
from conftest import setup_appium_driver


def test_blood_pressure_health_profile_homepage(setup_appium_driver):
    print("Test user can log blood pressure details through Health Profile")
    driver = setup_appium_driver
    login_page = LoginPage(driver)
    blood_pressure_healthPro = blood_HealthProfile(driver)

    login_page.choose_country_code()
    login_page.enter_country(COUNTRY)
    login_page.select_country()
    login_page.enter_phone_number(PHONENUMBER)
    login_page.enter_password(PASSWORD)
    login_page.click_login_button()

    fake = Faker()
    random_blood_pressure1 = fake.random_int(min=150, max=180)
    random_blood_pressure2 = fake.random_int(min=80, max=120)
    blood_pressure_healthPro.navigate_to_health_profile_page()
    blood_pressure_healthPro.navigate_to_health_logs()
    blood_pressure_healthPro.navigate_to_blood_pressure()
    blood_pressure_healthPro.navigate_to_heart_button()
    blood_pressure_healthPro.high_blood_field(random_blood_pressure1)
    blood_pressure_healthPro.low_blood_field(random_blood_pressure2)
    blood_pressure_healthPro.click_add_button()
    print("Added Blood Pressure Details")
