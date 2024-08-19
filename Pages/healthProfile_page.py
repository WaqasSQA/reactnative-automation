from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class HealthProfilePage(BasePage):

    def navigate_to_health_profile_page(self):
        health_profile_button = self.wait_for_element(By.XPATH, "//*[contains(@text,'Health Profile')]")
        health_profile_button.click()

    def navigate_to_stress_screen(self):
        stress_button = self.wait_for_element(By.XPATH, "//*[contains(@text,'Stress')]")
        stress_button.click()

    def select_first_stress_option(self):
        stress_option_1 = self.wait_for_element(By.XPATH, "//*[contains(@text,'Almost Never')]")
        stress_option_1.click()

    def select_second_stress_option(self):
        stress_option_2 = self.wait_for_element(By.XPATH, "//*[contains(@text,'Sometimes')]")
        stress_option_2.click()

    def select_third_stress_option(self):
        stress_option_3 = self.wait_for_element(By.XPATH, "//*[contains(@text,'Never')]")
        stress_option_3.click()

    def click_save_stress_data(self):
        save_button = self.wait_for_element(By.XPATH, "//*[contains(@text,'Save')]")
        save_button.click()

    def wait_for_element(self, locator_strategy, locator):
        # Define a maximum wait time (e.g., 10 seconds)
        wait = WebDriverWait(self.driver, 10)

        # Use expected_conditions to wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

        return element
