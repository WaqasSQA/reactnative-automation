from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from Pages.existing_user_signup_TA_388_page import ExistingUserSignup
from conftest import setup_appium_driver


def test_user_should_not_signup_using_existing_creds(setup_appium_driver):
    print("Test Case Started - TA-388 - User Should Sees Error If They Sign Up With An Existing Number")
    driver = setup_appium_driver
    existingUser = ExistingUserSignup(driver)

    existingUser.click_signup()
    existingUser.firstname()
    existingUser.lastname()
    existingUser.gender()
    existingUser.countrycode()
    existingUser.search_countrycode()
    existingUser.select_country()
    existingUser.enter_number()
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(323, 1327)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(308, 583)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    existingUser.citizenship_dropdown()
    existingUser.enter_citizenship()
    existingUser.enter_email()
    existingUser.enter_password()
    existingUser.accept_terms()
    existingUser.click_continue()
