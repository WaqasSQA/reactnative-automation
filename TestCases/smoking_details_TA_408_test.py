from faker import Faker

from Pages.smoking_details_TA_408_page import SmokingDetails
from Pages.login_page import LoginPage
from config import PHONENUMBER, PASSWORD, COUNTRY
from conftest import setup_appium_driver


def test_user_add_smoking_details(setup_appium_driver):
    print("Test Case Started - TA-408 - User Should Be Able To Add Smoking Details")
    driver = setup_appium_driver
    smoking_details = SmokingDetails(driver)
    login_page = LoginPage(driver)

    fake = Faker()
    random_cig1 = fake.random_int(min=5, max=19)
    random_cig2 = fake.random_int(min=5, max=19)

    # Login to application
    login_page.choose_country_code()
    login_page.enter_country(COUNTRY)
    login_page.select_country()
    login_page.enter_phone_number(PHONENUMBER)
    login_page.enter_password(PASSWORD)
    login_page.click_login_button()

    smoking_details.click_health_profile()
    smoking_details.click_health_questionnaire()
    smoking_details.click_smoking_tab()
    smoking_details.click_no()
    smoking_details.click_save()
    smoking_details.click_smoking_tab()
    smoking_details.click_yes()
    smoking_details.cig_no(random_cig1)
    smoking_details.year_start_dropdown()
    smoking_details.start_year()
    smoking_details.click_save()
    smoking_details.click_smoking_tab()
    smoking_details.click_used_to()
    smoking_details.cig_no(random_cig2)
    smoking_details.year_start_dropdown()
    smoking_details.start_year()
    smoking_details.year_end_dropdown()
    smoking_details.end_year()
    smoking_details.click_save()
