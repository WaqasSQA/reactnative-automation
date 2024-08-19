from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class PatientSupportEcoSystem(BasePage):
  def open_PSP_program(self):
    psp_program = self.wait_for_element(By.XPATH, '//*[contains(@text,"Hypertension Support Center")]')
    psp_program.click()

  def click_continue_button(self):
    continue_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"Continue")]')
    continue_button.click()

  def click_next_button(self):
    next_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"Next")]')
    next_button.click()

  def click_finish_button(self):
    next_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"Finish")]')
    next_button.click()

  def click_withdraw_button(self):
    withdraw_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"Withdraw from Program")]')
    withdraw_button.click()

  def confirm_withdraw(self):
    confirm_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"Yes")]')
    confirm_button.click()

  def wait_for_element(self, locator_strategy, locator):
    # Define a maximum wait time (e.g., 10 seconds)
    wait = WebDriverWait(self.driver, 10)
    # Use expected_conditions to wait for the element to be visible
    element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))
    return element
