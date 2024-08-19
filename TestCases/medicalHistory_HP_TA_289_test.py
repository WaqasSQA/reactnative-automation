import time

from Pages.account_page import AccountPage
from Pages.login_page import LoginPage
from Pages.medicalHistory_HP_TA_289_page import MedicalHistory_HP
from config import PHONENUMBER, PASSWORD, COUNTRY # Import the credentials
from conftest import setup_appium_driver


def test_medical_history_health_profile(setup_appium_driver):
    print("Test Case Started - The user should be able to enter values and save in the 'Medical History' in the 'Health"
          "Profile' tab")
    driver = setup_appium_driver
    Login_Page = LoginPage(driver)
    Medical_History_HP = MedicalHistory_HP(driver)

    # Login into the App
    Login_Page.choose_country_code()
    Login_Page.enter_country(COUNTRY)
    Login_Page.select_country()
    Login_Page.enter_phone_number(PHONENUMBER)
    Login_Page.enter_password(PASSWORD)
    Login_Page.click_login_button()

    # TestCase
    Medical_History_HP.navigate_account_screen()
    Medical_History_HP.click_health_profile()
    Medical_History_HP.click_medical_history()
    Medical_History_HP.click_ethnicity_dropdown()
    Medical_History_HP.select_dropdown_option()
    Medical_History_HP.add_cholesterol_details("Aspirin")
    Medical_History_HP.add_blood_pressure_details()
    Medical_History_HP.add_diabetes_details("Insulin")
    Medical_History_HP.add_asthma_details()
    Medical_History_HP.add_cancer_details()
    Medical_History_HP.add_other_details("IBS", "Mebeverine")
    Medical_History_HP.click_save_n_continue_btn()


