from Pages.login_page import LoginPage
from Pages.medicalHistory_HP_TA_289_page import MedicalHistory_HP
from Pages.vaccination_Health_Profile_TA_290_page import vaccination_HealthProfile
from config import PHONENUMBER, PASSWORD, COUNTRY
from conftest import setup_appium_driver


def test_vaccination_from_health_profile(setup_appium_driver):
    print("Test Case Started -  The user should be able to select If vaccinated or not, and select the vaccine in "
          "'Vaccination' tab")

    driver = setup_appium_driver
    Login_Page = LoginPage(driver)
    Medical_History = MedicalHistory_HP(driver)
    Vaccination_page = vaccination_HealthProfile(driver)

    # Login to Application
    Login_Page.choose_country_code()
    Login_Page.enter_country(COUNTRY)
    Login_Page.select_country()
    Login_Page.enter_phone_number(PHONENUMBER)
    Login_Page.enter_password(PASSWORD)
    Login_Page.click_login_button()

    # Testcase
    Medical_History.navigate_account_screen()
    Medical_History.click_health_profile()
    Vaccination_page.click_vaccination()
    Vaccination_page.click_on_yes()
    Vaccination_page.add_vaccine("Pfizer")
    Vaccination_page.save_btn()

    Vaccination_page.click_vaccination()
    Vaccination_page.click_no()
    Vaccination_page.save_btn()

    Vaccination_page.click_vaccination()
    Vaccination_page.click_yes_but_not_sure()
    Vaccination_page.save_btn()







