from faker import Faker
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from Pages.health_logs_TA_287_page import HealthLogs
from Pages.login_page import LoginPage
from config import PHONENUMBER, PASSWORD, COUNTRY
from conftest import setup_appium_driver


def test_user_enter_health_logs(setup_appium_driver):
    print("Test Case Started - TA-287 - User Should Be Able To Enter Their Health Logs")
    driver = setup_appium_driver
    health_logs_TA_287 = HealthLogs(driver)
    login_page = LoginPage(driver)

    # Login to application
    login_page.choose_country_code()
    login_page.enter_country(COUNTRY)
    login_page.select_country()
    login_page.enter_phone_number(PHONENUMBER)
    login_page.enter_password(PASSWORD)
    login_page.click_login_button()

    fake = Faker()
    random_blood_sugar = fake.random_int(min=100, max=150)
    random_blood_pressure1 = fake.random_int(min=150, max=180)
    random_blood_pressure2 = fake.random_int(min=80, max=120)
    random_weight = fake.random_int(min=133, max=198)
    random_HbA1c = fake.random_int(min=7, max=14)

    health_logs_TA_287.navigate_health_profile_screen()
    health_logs_TA_287.navigate_health_logs_screen()
    health_logs_TA_287.click_blood_sugar()
    health_logs_TA_287.navigate_blood_sugar_details_screen()
    health_logs_TA_287.enter_blood_sugar_reading(random_blood_sugar)
    health_logs_TA_287.select_meal_time_dropdown()
    health_logs_TA_287.select_meal_time()
    health_logs_TA_287.click_add_blood_sugar_button()

    health_logs_TA_287.click_blood_pressure()
    health_logs_TA_287.navigate_blood_pressure_details_screen()
    health_logs_TA_287.high_blood_field(random_blood_pressure1)
    health_logs_TA_287.low_blood_field(random_blood_pressure2)
    health_logs_TA_287.click_add_blood_pressure_button()

    # Swipe action in order to get weight locators
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(583, 180)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(165, 177)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(448, 180)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(82, 180)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    health_logs_TA_287.click_HbA1c()
    health_logs_TA_287.navigate_HbA1c_details_screen()
    health_logs_TA_287.enter_HbA1c_reading(random_HbA1c)
    health_logs_TA_287.click_add_HbA1c_button()
    health_logs_TA_287.click_weight()
    health_logs_TA_287.navigate_enter_weight_details_screen()
    health_logs_TA_287.enter_weight(random_weight)
    health_logs_TA_287.click_add_weight()
