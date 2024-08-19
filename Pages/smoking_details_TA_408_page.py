from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
import random


class SmokingDetails(BasePage):
    random_start_dict = {
        '2010': {'by': By.XPATH, 'value': '//android.widget.TextView[@text="1975"]'},
        '2011': {'by': By.XPATH, 'value': '//android.widget.TextView[@text="1976"]'},
        '2012': {'by': By.XPATH, 'value': '//android.widget.TextView[@text="1977"]'},
        '2013': {'by': By.XPATH, 'value': '//android.widget.TextView[@text="1978"]'},
    }
    random_start_key = random.choice(list(random_start_dict.keys()))
    random_start = random_start_dict[random_start_key]

    random_end_dict = {
        '2020': {'by': By.XPATH, 'value': '//android.widget.TextView[@text="1976"]'},
        '2021': {'by': By.XPATH, 'value': '//android.widget.TextView[@text="1977"]'},
        '2022': {'by': By.XPATH, 'value': '//android.widget.TextView[@text="1978"]'},
        '2023': {'by': By.XPATH, 'value': '//android.widget.TextView[@text="1979"]'},
    }
    random_end_key = random.choice(list(random_end_dict.keys()))
    random_end = random_end_dict[random_end_key]

    random_int = random.randint(5, 15)

    def click_health_profile(self):
        health_profile = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Health Profile"]')
        health_profile.click()

    def click_health_questionnaire(self):
        health_questionnaire = self.wait_for_element(By.XPATH, '//android.view.ViewGroup[@bounds="[66,279][118,324]"]')
        health_questionnaire.click()

    def click_smoking_tab(self):
        smoking_tab = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Smoking"]')
        smoking_tab.click()

    def click_no(self):
        tap_no = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="No"]')
        tap_no.click()

    def click_yes(self):
        tap_yes = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Yes"]')
        tap_yes.click()

    def click_used_to(self):
        tap_used_to = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="I used to"]')
        tap_used_to.click()

    def cig_no(self, no_cig):
        no_of_cig = self.wait_for_element(By.XPATH, '(//android.widget.EditText)[1]')
        no_of_cig.send_keys(no_cig)

    def year_start_dropdown(self):
        start_dropdown = self.wait_for_element(By.XPATH, '(//android.widget.TextView)[8]')
        start_dropdown.click()

    def start_year(self):
        year_start = self.wait_for_element(self.random_start['by'], self.random_start['value'])
        year_start.click()

    def year_end_dropdown(self):
        end_dropdown = self.wait_for_element(By.XPATH, '(//android.widget.TextView)[10]')
        end_dropdown.click()

    def end_year(self):
        year_end = self.wait_for_element(self.random_end['by'], self.random_end['value'])
        year_end.click()

    def click_save(self):
        tap_save = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Save"]')
        tap_save.click()

    def wait_for_element(self, locator_strategy, locator):
        # Define a maximum wait time (e.g., 10 seconds)
        wait = WebDriverWait(self.driver, 20)

        # Use expected_conditions to wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

        return element
