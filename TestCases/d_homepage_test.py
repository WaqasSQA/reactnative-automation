from Pages.login_page import LoginPage
from Pages.home_page import HomePage
from Pages.health_logs_page import HealthLogsPage
from config import PSP_ACCOUNT, PASSWORD, COUNTRY  # Import the credentials
from conftest import setup_appium_driver
from faker import Faker


def test_user_can_navigate_to_verification_screen(setup_appium_driver):
    print("Test user can can go to verification screen from fast action button")
    driver = setup_appium_driver  # The driver instance provided by the fixture
    # Create Page Object instance
    Login_Page = LoginPage(driver)
    Home_Page = HomePage(driver)

    # First login to the application
    Login_Page.choose_country_code()
    Login_Page.enter_country(COUNTRY)
    Login_Page.select_country()
    Login_Page.enter_phone_number(PSP_ACCOUNT)
    Login_Page.enter_password(PASSWORD)
    Login_Page.click_login_button()

    Home_Page.click_action_button()
    Home_Page.navigate_to_verification_screen()
    Home_Page.click_continue()
    Home_Page.navigate_back_to_verification()
    Home_Page.return_to_home()




def test_user_logs_weight_data_from_fast_action_button(setup_appium_driver):
    print("Test user can log weight value from fast action button")
    driver = setup_appium_driver  # The driver instance provided by the fixture
    # Create Page Object instance
    Home_Page = HomePage(driver)
    Health_Logs_Page = HealthLogsPage(driver)

    Home_Page.click_action_button()
    Home_Page.click_log_data_button()

    fake = Faker()  # Initialize faker instance
    random_weight_value = fake.random_int(min=150, max=200)
    Health_Logs_Page.navigate_to_weight_screen()
    Health_Logs_Page.click_fast_action_button()
    Health_Logs_Page.enter_weigth_value(random_weight_value)
    Health_Logs_Page.click_add_button()

def test_user_can_edit_log_data(setup_appium_driver):
    print("Test user can edit log weight value from fast action button")
    driver = setup_appium_driver  # The driver instance provided by the fixture
    # Create Page Object instance
    Health_Logs_Page = HealthLogsPage(driver)

    fake = Faker()  # Initialize faker instance
    random_weight_value = fake.random_int(min=150, max=200)
    Health_Logs_Page.open_logs()
    Health_Logs_Page.get_log_value()
    Health_Logs_Page.enter_weigth_value(random_weight_value)
    Health_Logs_Page.save_edit()

def test_user_can_delete_log_data(setup_appium_driver):
    print("Test user can delete log weight value from fast action button")
    driver = setup_appium_driver  # The driver instance provided by the fixture
    # Create Page Object instance
    Health_Logs_Page = HealthLogsPage(driver)

    fake = Faker()  # Initialize faker instance
    Health_Logs_Page.get_log_value()
    Health_Logs_Page.delete_log()
    Health_Logs_Page.click_yes()


def test_user_logs_blood_pressure_data_from_fast_action_button(setup_appium_driver):
    print("Test user can log blood pressure value from fast action button")
    driver = setup_appium_driver  # The driver instance provided by the fixture
    Health_Logs_Page = HealthLogsPage(driver)
    fake = Faker()  # Initialize faker instance

    random_high_bp_value = fake.random_int(min=120, max=200)
    random_low_bp_value = fake.random_int(min=80, max=120)

    Health_Logs_Page.navigate_to_blood_pressure_screen()
    Health_Logs_Page.click_fast_action_button()
    Health_Logs_Page.enter_high_bp_value(random_high_bp_value)
    Health_Logs_Page.enter_low_bp_value(random_low_bp_value)
    Health_Logs_Page.click_add_button()


def test_user_logs_blood_sugar_data_from_fast_action_button(setup_appium_driver):
    print("Test user can log blood sugar value from fast action button")
    driver = setup_appium_driver  # The driver instance provided by the fixture
    Health_Logs_Page = HealthLogsPage(driver)
    fake = Faker()  # Initialize faker instance
    random_blood_sugar_value = fake.random_int(min=200, max=250)

    Health_Logs_Page.navigate_to_blood_sugar_screen()
    Health_Logs_Page.click_fast_action_button()
    Health_Logs_Page.click_meal_dropdown()
    Health_Logs_Page.select_meal_time()
    Health_Logs_Page.enter_blood_sugar_value(random_blood_sugar_value)
    Health_Logs_Page.click_add_button()