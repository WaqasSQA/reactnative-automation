from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
import random


class SleepDetails(BasePage):
    random_options_dict = {
        'less than 4 hours': {'by': By.XPATH, 'value': '(//android.widget.TextView)[5]'},
        '4-7 hours': {'by': By.XPATH, 'value': '(//android.widget.TextView)[6]'},
        '7-10 hours': {'by': By.XPATH, 'value': '(//android.widget.TextView)[7]'},
        'more than 10 hours': {'by': By.XPATH, 'value': '(//android.widget.TextView)[8]'},
    }
    random_option_key = random.choice(list(random_options_dict.keys()))
    random_option = random_options_dict[random_option_key]

    def click_health_profile(self):
        health_profile = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Health Profile"]')
        health_profile.click()

    def click_health_questionnaire(self):
        health_questionnaire = self.wait_for_element(By.XPATH, '//android.view.ViewGroup[@bounds="[66,279][118,324]"]')
        health_questionnaire.click()

    def click_sleep_btn(self):
        sleep_btn = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Sleep"]')
        sleep_btn.click()

    def drop_down(self):
        click_drop_down = self.wait_for_element(By.XPATH, '(//android.widget.TextView)[3]')
        click_drop_down.click()

    def select_duration(self):
        duration = self.wait_for_element(self.random_option['by'], self.random_option['value'])
        duration.click()

    def click_save(self):
        save_continue = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Save"]')
        save_continue.click()

    def wait_for_element(self, locator_strategy, locator):
        # Define a maximum wait time (e.g., 10 seconds)
        wait = WebDriverWait(self.driver, 20)

        # Use expected_conditions to wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

        return element
