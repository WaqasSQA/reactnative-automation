import time
from Pages.account_page import AccountPage
from Pages.login_page import LoginPage
from Pages.personalInfo_page import PersonalInfoPage
from faker import Faker
from config import PHONENUMBER, PASSWORD, WRONGNAME, COUNTRY  # Import the credentials
from conftest import setup_appium_driver


def test_user_can_change_personal_information(setup_appium_driver):
    print("Test case 3 started- User changes personal information")
    fake = Faker() # Initialize faker instance
    driver = setup_appium_driver  # The driver instance provided by the fixture
    fake_first_name = fake.first_name()
    fake_last_name =  fake.last_name()
    # Create Page Object instance
    Account_Page = AccountPage(driver)
    Login_Page = LoginPage(driver)
    Personal_Info = PersonalInfoPage(driver)
    # First login to the application
    Login_Page.choose_country_code()
    Login_Page.enter_country(COUNTRY)
    Login_Page.select_country()
    Login_Page.enter_phone_number(PHONENUMBER)
    Login_Page.enter_password(PASSWORD)
    Login_Page.click_login_button()

    #This is TestCase number 3, user logins, visits account screen and updates first and last name
    Account_Page.navigate_account_screen()
    Account_Page.click_personal_information()

    Personal_Info.change_first_name(fake_first_name)
    Personal_Info.change_last_name(fake_last_name)

    Account_Page.save_gender()


def test_user_cant_save_invlaid_personal_information(setup_appium_driver):
    print("Test case 4 started- User is not allowed to save wrong personal information")
    driver = setup_appium_driver  # The driver instance provided by the fixture
    # Create Page Object instance
    Account_Page = AccountPage(driver)
    Personal_Info = PersonalInfoPage(driver)
    time.sleep(10)

    # This is TestCase number 4, user logins, visits account screen, and uses wrong personal info which is not
    # allowed to be saved
    Account_Page.click_personal_information()

    fake = Faker() # Initialize faker instance
    fake_first_name = fake.first_name()
    Personal_Info.change_first_name(fake_first_name+WRONGNAME)
    Personal_Info.assert_user_cant_save_wront_personal_information()