from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class vaccination_HealthProfile(BasePage):
    def click_vaccination(self):
        vaccination_button = self.wait_for_element(By.XPATH, "//*[contains(@text, 'Vaccination')]")
        vaccination_button.click()

    def click_on_yes(self):
        yes_button = self.wait_for_element(By.XPATH, "//android.view.ViewGroup[@bounds='[81,813][151,883]']")
        yes_button.click()

    def add_vaccine(self, Add_Vaccine):
        vaccine_field = self.wait_for_element(By.XPATH, "//android.widget.EditText[@bounds='[58,1252][1094,1392]']")
        vaccine_field.send_keys(Add_Vaccine)

    def save_btn(self):
        save_btn = self.wait_for_element(By.XPATH, "//android.widget.TextView[@text='Save']")
        save_btn.click()

    def click_no(self):
        no_btn = self.wait_for_element(By.XPATH, "//android.view.ViewGroup[@bounds='[81,631][151,701]']")
        no_btn.click()

    def click_yes_but_not_sure(self):
        yes_but_btn = self.wait_for_element(By.XPATH, "//android.view.ViewGroup[@bounds='[81,995][151,1065]']")
        yes_but_btn.click()

    def wait_for_element(self, locator_strategy, locator):
        # Define a maximum wait time (e.g., 10 seconds)
        wait = WebDriverWait(self.driver, 10)

        # Use expected_conditions to wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

        return element
