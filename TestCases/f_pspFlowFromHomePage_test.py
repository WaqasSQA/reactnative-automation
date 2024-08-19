import time
import requests
from Pages.login_page import LoginPage
from Pages.scanner_api_page import ScannerAPIPage
from Pages.PSP_page import PatientSupportEcoSystem
from config import PSP_ACCOUNT, PASSWORD, PSP_SFI_CODE, API_PASSWORD, API_ENDPOINT, COUNTRY  # Import the credentials
from conftest import setup_appium_driver


def test_user_views_lab_result_by_manually_entering_lab_code(setup_appium_driver):
  print("Test user can enroll in PSP program")
  driver = setup_appium_driver  # The driver instance provided by the fixture
  # Create Page Object instance
  Login_Page = LoginPage(driver)
  Scanner_Api_Page = ScannerAPIPage(driver)
  # First login to the application
  Login_Page.choose_country_code()
  Login_Page.enter_country(COUNTRY)
  Login_Page.select_country()
  Login_Page.enter_phone_number(PSP_ACCOUNT)
  Login_Page.enter_password(PASSWORD)
  Login_Page.click_login_button()

  Scanner_Api_Page.open_scanner_api_from_home_page()
  Scanner_Api_Page.input_code()
  Scanner_Api_Page.fill_code(PSP_SFI_CODE)
  Scanner_Api_Page.press_enter_code_button()
  Scanner_Api_Page.check_terms_box()
  Scanner_Api_Page.agree_terms()


def test_user_can_withdraw_from_PSP_program(setup_appium_driver):
  print("Test user can withdraw from PSP program")
  driver = setup_appium_driver  # The driver instance provided by the fixture
  # Create Page Object instance
  Psp_Page = PatientSupportEcoSystem(driver)
  Psp_Page.open_PSP_program()
  Psp_Page.click_continue_button()
  Psp_Page.click_next_button()
  time.sleep(5)
  Psp_Page.click_next_button()
  time.sleep(5)
  Psp_Page.click_next_button()
  time.sleep(5)
  Psp_Page.click_finish_button()
  Psp_Page.click_withdraw_button()
  Psp_Page.confirm_withdraw()
  requests.patch(API_ENDPOINT, json=API_PASSWORD)