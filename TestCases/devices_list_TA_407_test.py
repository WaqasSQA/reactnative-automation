import time
from Pages.login_page import LoginPage
from Pages.medicalHistory_HP_TA_289_page import MedicalHistory_HP
from Pages.devices_list_TA_407_page import listDevices
from config import PHONENUMBER, PASSWORD, COUNTRY
from conftest import setup_appium_driver


def test_list_of_devices(setup_appium_driver):
    driver = setup_appium_driver
    login_page = LoginPage(driver)
    accounts_screen = MedicalHistory_HP(driver)
    devices_list = listDevices(driver)

    login_page.choose_country_code()
    login_page.enter_country(COUNTRY)
    login_page.select_country()
    login_page.enter_phone_number(PHONENUMBER)
    login_page.enter_password(PASSWORD)
    login_page.click_login_button()

    accounts_screen.navigate_account_screen()
    devices_list.click_devices_btn()
    devices_list.click_add_new_device()
    time.sleep(20)

