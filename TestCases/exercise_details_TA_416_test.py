from Pages.exercise_details_TA_416_page import ExerciseDetails
from Pages.login_page import LoginPage
from config import PHONENUMBER, PASSWORD, COUNTRY
from conftest import setup_appium_driver


def test_user_add_exercise_details(setup_appium_driver):
    print("Test Case Started - TA-416 - User Should Be Able To Add Exercise Details")
    driver = setup_appium_driver
    exercise_details = ExerciseDetails(driver)
    login_page = LoginPage(driver)

    # Login to application
    login_page.choose_country_code()
    login_page.enter_country(COUNTRY)
    login_page.select_country()
    login_page.enter_phone_number(PHONENUMBER)
    login_page.enter_password(PASSWORD)
    login_page.click_login_button()

    exercise_details.click_health_profile()
    exercise_details.click_health_questionnaire()
    exercise_details.click_exercise_tab()
    exercise_details.click_no()
    exercise_details.click_save()
    exercise_details.click_exercise_tab()
    exercise_details.click_yes()
    exercise_details.days_dropdown()
    exercise_details.day_selection()
    exercise_details.time_dropdown()
    exercise_details.time_selection()
    exercise_details.click_save()

