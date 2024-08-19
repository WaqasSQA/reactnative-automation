import time
from Pages.login_page import LoginPage
from Pages.home_page import HomePage
from config import PHONENUMBER, PASSWORD, COUNTRY, BARCODE  # Import the credentials
from conftest import setup_appium_driver


def test_user_views_abnormal_biomarker_from_homepage(setup_appium_driver):
  print("Test user can view abnormal biomarker from homepage")
  driver = setup_appium_driver  # The driver instance provided by the fixture
  # Create Page Object instance
  Login_Page = LoginPage(driver)
  Home_Page = HomePage(driver)

  Login_Page.choose_country_code()
  Login_Page.enter_country(COUNTRY)
  Login_Page.select_country()
  Login_Page.enter_phone_number(PHONENUMBER)
  Login_Page.enter_password(PASSWORD)
  Login_Page.click_login_button()

  Home_Page.open_potassium_biomarker()
  time.sleep(5)
  Home_Page.navigate_back()
  Home_Page.open_chloride_biomarker()
  time.sleep(5)