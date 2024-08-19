import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from Pages.search_bar_TA_392_page import searchBar
from Pages.login_page import LoginPage
from config import PHONENUMBER, PASSWORD, COUNTRY
from conftest import setup_appium_driver
from appium.webdriver.common.touch_action import TouchAction


def test_search_item(setup_appium_driver):
    driver = setup_appium_driver
    Login_Page = LoginPage(driver)
    search_bar_item = searchBar(driver)

    Login_Page.choose_country_code()
    Login_Page.enter_country(COUNTRY)
    Login_Page.select_country()
    Login_Page.enter_phone_number(PHONENUMBER)
    Login_Page.enter_password(PASSWORD)
    Login_Page.click_login_button()

    search_bar_item.search_bar("Lab Results")
    time.sleep(2)

    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(237, 632)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    time.sleep(4)
