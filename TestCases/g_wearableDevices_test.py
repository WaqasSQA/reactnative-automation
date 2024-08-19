import time
from Pages.login_page import LoginPage
from Pages.account_page import AccountPage
from Pages.wearable_devices_page import WearableDevicesPage
from Pages.PSP_page import PatientSupportEcoSystem
from config import PHONENUMBER, PASSWORD, COUNTRY, FREESTYLE_EMAIL  # Import the credentials
from conftest import setup_appium_driver

def test_user_can_connect_wearable_devices(setup_appium_driver):
  print("Test user can connect to devices")
  driver = setup_appium_driver  # The driver instance provided by the fixture
  # Create Page Object instance
  Login_Page = LoginPage(driver)
  Wearable_devices = WearableDevicesPage(driver)
  Account_Page = AccountPage(driver)
  Psp_Page = PatientSupportEcoSystem(driver)

  # First login to the application
  Login_Page.choose_country_code()
  Login_Page.enter_country(COUNTRY)
  Login_Page.select_country()
  Login_Page.enter_phone_number(PHONENUMBER)
  Login_Page.enter_password(PASSWORD)
  Login_Page.click_login_button()

  Account_Page.navigate_account_screen()
  time.sleep(10)
  Wearable_devices.navigate_to_devices_page()
  Wearable_devices.add_new_devices()
  time.sleep(10)
  Wearable_devices.select_freestyle_device()
  Psp_Page.click_next_button()
  Wearable_devices.enter_email(FREESTYLE_EMAIL)
  Wearable_devices.select_region()
  Wearable_devices.choose_country()
  Wearable_devices.click_connect_button()
  time.sleep(10)
  Wearable_devices.click_close_button()
  Wearable_devices.delete_wearable_device()
  Wearable_devices.unlink_device()
  Wearable_devices.click_okay_button()

