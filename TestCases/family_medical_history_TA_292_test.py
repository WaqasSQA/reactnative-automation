from Pages.family_medical_history_TA_292_page import FamilyMedicalHistory
from Pages.login_page import LoginPage
from config import PHONENUMBER, PASSWORD, COUNTRY
from conftest import setup_appium_driver


def test_user_enter_family_medical_history(setup_appium_driver):
    print("Test Case Started - TA-292 - User Should Be Able To Enter Their Family Medical History")
    driver = setup_appium_driver
    family_medical_history_TA_292 = FamilyMedicalHistory(driver)
    login_page = LoginPage(driver)

    # Login to application
    login_page.choose_country_code()
    login_page.enter_country(COUNTRY)
    login_page.select_country()
    login_page.enter_phone_number(PHONENUMBER)
    login_page.enter_password(PASSWORD)
    login_page.click_login_button()

    family_medical_history_TA_292.click_health_profile()
    family_medical_history_TA_292.click_health_questionnaire()
    family_medical_history_TA_292.click_family_medical_history()
    family_medical_history_TA_292.select_disease()
    family_medical_history_TA_292.click_save()
