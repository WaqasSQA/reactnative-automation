from Pages.drinking_details_TA_415_page import DrinkingDetails
from Pages.sleep_details_TA_417_page import SleepDetails
from Pages.login_page import LoginPage
from config import PHONENUMBER, PASSWORD, COUNTRY
from conftest import setup_appium_driver


def test_user_add_drinking_details(setup_appium_driver):
    print("Test Case Started - TA-415 - User Should Be Able To Add Drinking Details")
    driver = setup_appium_driver
    sleep_details = SleepDetails(driver)
    drinking_details_TA_415 = DrinkingDetails(driver)
    login_page = LoginPage(driver)

    # Login to application
    login_page.choose_country_code()
    login_page.enter_country(COUNTRY)
    login_page.select_country()
    login_page.enter_phone_number(PHONENUMBER)
    login_page.enter_password(PASSWORD)
    login_page.click_login_button()

    sleep_details.click_health_profile()
    sleep_details.click_health_questionnaire()
    drinking_details_TA_415.click_drinking()
    drinking_details_TA_415.select_no()
    drinking_details_TA_415.click_save()
    drinking_details_TA_415.click_drinking()
    drinking_details_TA_415.select_yes()
    #drinking_details_TA_415.select_beer()
    #drinking_details_TA_415.select_wine()
    #drinking_details_TA_415.select_spirit()
    drinking_details_TA_415.click_save()


