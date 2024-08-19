from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
import random


class ExerciseDetails(BasePage):
    random_days_dict = {
        '1': {'by': By.XPATH, 'value': '(//android.view.View)[3]'},
        '2': {'by': By.XPATH, 'value': '(//android.view.View)[4]'},
        '3': {'by': By.XPATH, 'value': '(//android.view.View)[5]'},
        '4': {'by': By.XPATH, 'value': '(//android.view.View)[6]'},
    }
    random_days_key = random.choice(list(random_days_dict.keys()))
    random_day = random_days_dict[random_days_key]

    random_time_dict = {
        'less than 20 min': {'by': By.XPATH, 'value': '(//android.view.View)[3]'},
        '20-40 mins': {'by': By.XPATH, 'value': '(//android.view.View)[4]'},
        '40-60 mins': {'by': By.XPATH, 'value': '(//android.view.View)[5]'},
        '1-2 hours': {'by': By.XPATH, 'value': '(//android.view.View)[6]'},
    }
    random_time_key = random.choice(list(random_time_dict.keys()))
    random_time = random_time_dict[random_time_key]

    def click_health_profile(self):
        health_profile = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Health Profile"]')
        health_profile.click()

    def click_health_questionnaire(self):
        health_questionnaire = self.wait_for_element(By.XPATH, '//android.view.ViewGroup[@bounds="[66,279][118,324]"]')
        health_questionnaire.click()

    def click_exercise_tab(self):
        exercise_tab = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Exercise"]')
        exercise_tab.click()

    def click_no(self):
        tap_no = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="No"]')
        tap_no.click()

    def click_yes(self):
        tap_yes = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Yes"]')
        tap_yes.click()

    def days_dropdown(self):
        open_days_dropdown = self.wait_for_element(By.XPATH, '(//android.widget.Button)[1]')
        open_days_dropdown.click()

    def day_selection(self):
        select_days = self.wait_for_element(self.random_day['by'], self.random_day['value'])
        select_days.click()

    def time_dropdown(self):
        open_time_dropdown = self.wait_for_element(By.XPATH, '(//android.widget.Button)[2]')
        open_time_dropdown.click()

    def time_selection(self):
        select_time = self.wait_for_element(self.random_time['by'], self.random_time['value'])
        select_time.click()

    def click_save(self):
        save = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Save"]')
        save.click()

    def wait_for_element(self, locator_strategy, locator):
        # Define a maximum wait time (e.g., 10 seconds)
        wait = WebDriverWait(self.driver, 20)

        # Use expected_conditions to wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

        return element
