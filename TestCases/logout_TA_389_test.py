import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from Pages.login_page import LoginPage
from Pages.logout_TA_389_page import logout
from Pages.medicalHistory_HP_TA_289_page import MedicalHistory_HP
from config import PHONENUMBER, PASSWORD, COUNTRY
from conftest import setup_appium_driver


def test_logout(setup_appium_driver):
    print("Test Started : Verify that user can logout of the application")
    driver = setup_appium_driver
    login_page = LoginPage(driver)
    logout_actions = logout(driver)
    medical_history_action = MedicalHistory_HP(driver)

    # Login to application
    login_page.choose_country_code()
    login_page.enter_country(COUNTRY)
    login_page.select_country()
    login_page.enter_phone_number(PHONENUMBER)
    login_page.enter_password(PASSWORD)
    login_page.click_login_button()

    medical_history_action.navigate_account_screen()

    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(644, 2609)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(644, 1084)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    medical_history_action.navigate_account_screen()

    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(644, 2609)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(644, 1084)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    logout_actions.logout()
    logout_actions.logout_yes()
    time.sleep(10)


