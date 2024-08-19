from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class ScannerAPIPage(BasePage):

  def open_scanner_api_from_home_page(self):
    menu_button = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                  '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                  '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                  '.FrameLayout/android.view.ViewGroup/android.view.ViewGroup'
                                                  '/android.view.ViewGroup/android.view.ViewGroup['
                                                  '2]/android.view.ViewGroup/android.view.ViewGroup/android.view'
                                                  '.ViewGroup/android.view.ViewGroup/android.view.ViewGroup['
                                                  '1]/android.widget.FrameLayout/android.view.ViewGroup/android'
                                                  '.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup['
                                                  '1]/android.view.ViewGroup/android.view.ViewGroup['
                                                  '2]/android.view.ViewGroup['
                                                  '2]/android.view.ViewGroup/android.view.ViewGroup/android.view'
                                                  '.ViewGroup')
    menu_button.click()

  def input_code(self):
    barcode_option_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"Input Barcode")]')
    barcode_option_button.click()

  def fill_code(self, barcode):
    barcode_field = self.wait_for_element(By.XPATH, '//*[contains(@text,"ABC-1234-5678")]')
    barcode_field.send_keys(barcode)

  def press_enter_code_button(self):
    enter_code_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"Enter Code")]')
    enter_code_button.click()

  def view_results(self):
    view_results_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"View Results")]')
    view_results_button.click()

  def select_report_menu(self):
    select_menu_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"Main Lab")]')
    select_menu_button.click()

  def choose_anatomical_lab_report(self):
    select_anatomical_report_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"Anatomical Pathology")]')
    select_anatomical_report_button.click()


  def fill_IC_number(self, icNumber):
    ic_field = self.wait_for_element(By.XPATH, '//*[contains(@text,"Ex. S1234567X")]')
    ic_field.send_keys(icNumber)

  def click_verify_button(self):
    click_verify = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.Button')
    click_verify.click()

  def click_verify_button_twice(self):
    click_verify_twice = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.Button')
    click_verify_twice
  def click_verify_button_thrice(self):
    click_verify_thrice = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.Button')
    click_verify_thrice.click()

  def close_modal(self):
    close_error_modal = self.wait_for_element(By.XPATH, '//*[contains(@text,"OK")]')
    close_error_modal.click()

  def close_error_modal(self):
    close_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"Close")]')
    close_button.click() 
    
  def check_terms_box(self):
    checkbox = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                               '/android.widget.FrameLayout/android.widget.FrameLayout/android.view'
                                               '.ViewGroup/android.view.ViewGroup/android.view.ViewGroup['
                                               '1]/android.view.ViewGroup/android.view.ViewGroup/android.view'
                                               '.ViewGroup[2]/android.view.ViewGroup')
    checkbox.click()

  def agree_terms(self):
    view_results_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"Agree & Continue")]')
    view_results_button.click()

  def wait_for_element(self, locator_strategy, locator):
    # Define a maximum wait time (e.g., 10 seconds)
    wait = WebDriverWait(self.driver, 10)

    # Use expected_conditions to wait for the element to be visible
    element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

    return element
