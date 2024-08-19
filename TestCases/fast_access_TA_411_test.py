import time
from Pages.login_page import LoginPage
from Pages.fastAction_logHealthData_TA_412_page import FastAction
from Pages.fast_access_TA_411_page import fastAction
from Pages.dropdown_scanner_TA_414_page import dropdownScanner
from config import PHONENUMBER, PASSWORD, COUNTRY, IC_VERIFICATION_BARCODE
from conftest import setup_appium_driver


def test_fast_action_access_code(setup_appium_driver):
    driver = setup_appium_driver
    login_page = LoginPage(driver)
    fast_action = FastAction(driver)
    fast_action_2 = fastAction(driver)
    dropdown_scanner = dropdownScanner(driver)

    login_page.choose_country_code()
    login_page.enter_country(COUNTRY)
    login_page.select_country()
    login_page.enter_phone_number(PHONENUMBER)
    login_page.enter_password(PASSWORD)
    login_page.click_login_button()

    fast_action.click_fastActionBtn()
    fast_action_2.input_access_code_btn()
    dropdown_scanner.barcode_input_field(IC_VERIFICATION_BARCODE)
    dropdown_scanner.enter_code_btn()
    dropdown_scanner.view_result_btn()

    time.sleep(5)
