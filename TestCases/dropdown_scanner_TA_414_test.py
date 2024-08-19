import time
from Pages.login_page import LoginPage
from Pages.dropdown_scanner_TA_414_page import dropdownScanner
from config import PHONENUMBER, PASSWORD, COUNTRY, IC_VERIFICATION_BARCODE
from conftest import setup_appium_driver


def test_input_barcode_scanner_dropdown(setup_appium_driver):
    print("Test Started | The user should be able to input barcode from scanner drop down")
    driver = setup_appium_driver
    Login_Page = LoginPage(driver)
    scannerDropdown = dropdownScanner(driver)

    Login_Page.choose_country_code()
    Login_Page.enter_country(COUNTRY)
    Login_Page.select_country()
    Login_Page.enter_phone_number(PHONENUMBER)
    Login_Page.enter_password(PASSWORD)
    Login_Page.click_login_button()

    scannerDropdown.scanner_dropdown()
    scannerDropdown.input_barcode_btn()
    scannerDropdown.barcode_input_field(IC_VERIFICATION_BARCODE)
    scannerDropdown.enter_code_btn()
    scannerDropdown.view_result_btn()
    time.sleep(5)

