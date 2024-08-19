import time
import requests
from Pages.login_page import LoginPage
from Pages.scanner_api_page import ScannerAPIPage
from Pages.home_page import HomePage
from config import PHONENUMBER, PASSWORD, COUNTRY, BARCODE, WRONG_BARCODE, IC_VERIFICATION_BARCODE, WRONG_IC_NUMBER, UN_RELEASED_LAB_BARCODE
from config import API_ENDPOINT, API_PASSWORD  # Import the credentials
from conftest import setup_appium_driver


def test_user_can_see_error_when_IC_verification_limit_is_exceeded(setup_appium_driver):
  print("Test user can see error when IC verification limit is exceeded")
  driver = setup_appium_driver  # The driver instance provided by the fixture
  # Create Page Object instance
  Login_Page = LoginPage(driver)
  Scanner_Api_Page = ScannerAPIPage(driver)

  Login_Page.choose_country_code()
  Login_Page.enter_country(COUNTRY)
  Login_Page.select_country()
  Login_Page.enter_phone_number(PHONENUMBER)
  Login_Page.enter_password(PASSWORD)
  Login_Page.click_login_button()


  Scanner_Api_Page.open_scanner_api_from_home_page()
  Scanner_Api_Page.input_code()
  Scanner_Api_Page.fill_code(IC_VERIFICATION_BARCODE)
  Scanner_Api_Page.press_enter_code_button()
  Scanner_Api_Page.fill_IC_number(WRONG_IC_NUMBER)
  Scanner_Api_Page.click_verify_button()
  time.sleep(2)
  Scanner_Api_Page.click_verify_button_twice()
  time.sleep(2)
  Scanner_Api_Page.click_verify_button_thrice()
  time.sleep(2)
  Scanner_Api_Page.close_error_modal()
  requests.patch(API_ENDPOINT, json=API_PASSWORD)
  time.sleep(5)



def test_user_can_see_error_on_entering_wrong_barcode(setup_appium_driver):
  print("Test user can see error message when they input wrong Barcode")
  driver = setup_appium_driver  # The driver instance provided by the fixture
  # Create Page Object instance
  Scanner_Api_Page = ScannerAPIPage(driver)
  Scanner_Api_Page.open_scanner_api_from_home_page()
  Scanner_Api_Page.input_code()
  Scanner_Api_Page.fill_code(WRONG_BARCODE)
  Scanner_Api_Page.press_enter_code_button()
  Scanner_Api_Page.close_error_modal()
  time.sleep(5)


def test_user_views_lab_result_by_manually_entering_lab_code(setup_appium_driver):
  print("Test user can view lab results")
  driver = setup_appium_driver  # The driver instance provided by the fixture
  # Create Page Object instance
  Scanner_Api_Page = ScannerAPIPage(driver)

  Scanner_Api_Page.open_scanner_api_from_home_page()
  Scanner_Api_Page.input_code()
  Scanner_Api_Page.fill_code(BARCODE)
  Scanner_Api_Page.press_enter_code_button()
  Scanner_Api_Page.view_results()
  time.sleep(5)

def test_user_can_download_lab_results(setup_appium_driver):
  print("Test user can download lab reports")
  driver = setup_appium_driver  # The driver instance provided by the fixture
  # Create Page Object instance
  Scanner_Api_Page = ScannerAPIPage(driver)
  Home_Page  = HomePage(driver)
  Home_Page.navigate_back_to_lab_result_screen()
  time.sleep(5)
  Home_Page.click_lab_results()
  Scanner_Api_Page.view_results()
  Home_Page.see_report()
  time.sleep(8)
  Home_Page.download_report()

def test_user_can_download_secondary_lab_results(setup_appium_driver):
  print("Test user can download secondary lab reports")
  driver = setup_appium_driver  # The driver instance provided by the fixture
  # Create Page Object instance
  Scanner_Api_Page = ScannerAPIPage(driver)
  Home_Page = HomePage(driver)
  Home_Page.navigate_back_to_lab_result_screen()
  Home_Page.navigate_back_to_lab_result_screen()
  time.sleep(5)
  Home_Page.click_lab_results()
  Scanner_Api_Page.view_results()
  Home_Page.see_report()
  Scanner_Api_Page.select_report_menu()
  Scanner_Api_Page.choose_anatomical_lab_report()
  Home_Page.download_report()
  time.sleep(8)
  Home_Page.download_report()

def test_user_sees_error_for_unreleased_lab_results(setup_appium_driver):
  print("Test user sees error for unreleased lab results lab reports")
  driver = setup_appium_driver  # The driver instance provided by the fixture
  # Create Page Object instance
  Scanner_Api_Page = ScannerAPIPage(driver)
  Home_Page = HomePage(driver)
  Home_Page.navigate_back_to_lab_result_screen()
  Home_Page.navigate_back_to_lab_result_screen()
  Home_Page.navigate_back_to_lab_result_screen()

  Scanner_Api_Page.open_scanner_api_from_home_page()
  Scanner_Api_Page.input_code()
  Scanner_Api_Page.fill_code(UN_RELEASED_LAB_BARCODE)
  Scanner_Api_Page.press_enter_code_button()
  Scanner_Api_Page.close_error_modal()
  time.sleep(5)
