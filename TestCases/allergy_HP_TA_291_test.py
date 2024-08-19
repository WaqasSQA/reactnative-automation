from Pages.login_page import LoginPage
from Pages.medicalHistory_HP_TA_289_page import MedicalHistory_HP
from Pages.allergy_HP_TA_291_page import Allergy_health_profile
from config import PHONENUMBER, PASSWORD, COUNTRY
from conftest import setup_appium_driver


def test_allergy_details_health_profile(setup_appium_driver):
    print("Test Case Started - The user should be able to add details of allergies in 'Allergies' tab")

    driver = setup_appium_driver
    Login_Page = LoginPage(driver)
    Medical_History = MedicalHistory_HP(driver)
    Allergy_details = Allergy_health_profile(driver)

    Login_Page.choose_country_code()
    Login_Page.enter_country(COUNTRY)
    Login_Page.select_country()
    Login_Page.enter_phone_number(PHONENUMBER)
    Login_Page.enter_password(PASSWORD)
    Login_Page.click_login_button()

    Medical_History.navigate_account_screen()
    Medical_History.click_health_profile()

    Allergy_details.click_on_allergies()
    Allergy_details.yes_btn()
    Allergy_details.allergy_type()
    Allergy_details.allergy_type_yes()
    Allergy_details.medication_field("Any Medicine")
    Allergy_details.save_btn()
    Allergy_details.save_btn()
