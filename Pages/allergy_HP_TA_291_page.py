from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
import random


class Allergy_health_profile(BasePage):
    random_options_dict = {
        'Medication': {'by': By.XPATH, 'value': "//android.widget.TextView[@text='Medication']"},
        'Food': {'by': By.XPATH, 'value': "//android.widget.TextView[@text='Food']"},
        'Animal': {'by': By.XPATH, 'value': "//android.widget.TextView[@text='Animal']"},
        'Environment': {'by': By.XPATH, 'value': "//android.widget.TextView[@text='Environment']"},
        'Other': {'by': By.XPATH, 'value': "//android.widget.TextView[@text='Other']"},
        # 'Not Sure': {'by': By.XPATH, 'value': "//android.widget.TextView[@text='Not Sure']"}

    }
    random_key = random.choice(list(random_options_dict.keys()))
    random_option = random_options_dict[random_key]

    def click_on_allergies(self):
        allergy_button = self.wait_for_element(By.XPATH, "//*[contains(@text, 'Allergies')]")
        allergy_button.click()

    def not_sure_radio_btn(self):
        not_sure = self.wait_for_element(By.XPATH, "//android.view.ViewGroup[@bounds='[86,1022][156,1092]']")
        not_sure.click()

    def save_btn(self):
        save_btn = self.wait_for_element(By.XPATH, "//android.widget.TextView[@text='Save']")
        save_btn.click()

    def no_btn(self):
        no_btn = self.wait_for_element(By.XPATH, "//*[contains(@text, 'No')]")
        no_btn.click()

    def yes_btn(self):
        yes_btn = self.wait_for_element(By.XPATH, "//android.view.ViewGroup[@bounds='[86,840][156,910]']")
        yes_btn.click()

    def allergy_type(self):
        random_allergy_type = self.wait_for_element(self.random_option['by'], self.random_option['value'])
        random_allergy_type.click()

    def allergy_type_yes(self):
        allergy_type_yes = self.wait_for_element(By.XPATH, "(//android.view.ViewGroup)[10]")
        allergy_type_yes.click()

    def medication_field(self, MEDICATION):
        medication_field = self.wait_for_element(By.XPATH, "//android.widget.EditText[@resource-id='text-input-flat']")
        medication_field.send_keys(MEDICATION)
        click_plus = self.wait_for_element(By.XPATH, "(//android.widget.TextView)[5]")
        click_plus.click()

    def wait_for_element(self, locator_strategy, locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))
        return element
