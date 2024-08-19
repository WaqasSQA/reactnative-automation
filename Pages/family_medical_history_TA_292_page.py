from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
import random


class FamilyMedicalHistory(BasePage):
    random_options_dict = {
        'Heart Disease': {'by': By.XPATH, 'value': '(//android.widget.TextView)[3]'},
        'Stroke': {'by': By.XPATH, 'value': '(//android.widget.TextView)[4]'},
        'High Blood Pressure': {'by': By.XPATH, 'value': '(//android.widget.TextView)[5]'},
        'High Cholestrol': {'by': By.XPATH, 'value': '(//android.widget.TextView)[6]'},
        'Diabetes': {'by': By.XPATH, 'value': '(//android.widget.TextView)[7]'},
        'None': {'by': By.XPATH, 'value': '(//android.widget.TextView)[10]'}
    }
    random_option_key = random.choice(list(random_options_dict.keys()))
    random_option = random_options_dict[random_option_key]

    def click_health_profile(self):
        health_profile = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Health Profile"]')
        health_profile.click()

    def click_health_questionnaire(self):
        health_questionnaire = self.wait_for_element(By.XPATH, '//android.view.ViewGroup[@bounds="[66,279][118,324]"]')
        health_questionnaire.click()

    def click_family_medical_history(self):
        family_medical_history = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Family Medical '
                                                                 'History"]')
        family_medical_history.click()

    def select_disease(self):
        element = self.wait_for_element(self.random_option['by'], self.random_option['value'])
        element.click()

    def click_save(self):
        save_continue = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Save & Continue"]')
        save_continue.click()

    def wait_for_element(self, locator_strategy, locator):
        # Define a maximum wait time (e.g., 10 seconds)
        wait = WebDriverWait(self.driver, 20)

        # Use expected_conditions to wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

        return element
