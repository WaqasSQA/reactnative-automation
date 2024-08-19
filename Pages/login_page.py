from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class LoginPage(BasePage):

  def choose_country_code(self):
    choose_field = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                   '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                   '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                   '.FrameLayout/android.view.ViewGroup/android.view.ViewGroup'
                                                   '/android.view.ViewGroup/android.view.ViewGroup['
                                                   '2]/android.view.ViewGroup/android.view.ViewGroup/android.view'
                                                   '.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
                                                   '/android.view.ViewGroup/android.widget.ScrollView/android'
                                                   '.view.ViewGroup/android.view.ViewGroup['
                                                   '3]/android.view.ViewGroup[1]')
    choose_field.click()

  def enter_country(self, country_name):
    choose_country = self.wait_for_element(By.XPATH, '//*[contains(@text,"Enter country name")]')
    choose_country.send_keys(country_name)

  def select_country(self):
    selected_country = self.wait_for_element(By.XPATH, '//*[contains(@text,"Pakistan (+92)")]')
    selected_country.click()

  def enter_phone_number(self, phone_number):
    phone_input = self.wait_for_element(By.XPATH, '//*[contains(@text,"Phone Number")]')
    phone_input.send_keys(phone_number)

  def enter_password(self, password):
    password_input = self.wait_for_element(By.XPATH,
                                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                           '/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view'
                                           '.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup['
                                           '2]/android.view.ViewGroup/android.view.ViewGroup/android.view'
                                           '.ViewGroup/android.view.ViewGroup'
                                           '/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup'
                                           '/android.view.ViewGroup[4]/android.view.ViewGroup/android.widget.EditText')
    password_input.send_keys(password)

  def click_login_button(self):
    login_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"Login")]')
    login_button.click()

  def close_error_modal(self):
    ok_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"Ok")]')
    ok_button.click()

  def clear_phonenumber(self):
    clear_number = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                   '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                                   '.widget.FrameLayout/android.widget.FrameLayout/android.view'
                                                   '.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android'
                                                   '.view.ViewGroup['
                                                   '2]/android.view.ViewGroup/android.view.ViewGroup/android.view'
                                                   '.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android'
                                                   '.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup'
                                                   '/android.view.ViewGroup[3]/android.widget.EditText')
    clear_number.clear()

  def clear_password(self):
    clear_password = self.wait_for_element(By.XPATH,
                                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                           '.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                           '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android'
                                           '.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup['
                                           '2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
                                           '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
                                           '/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup['
                                           '4]/android.view.ViewGroup/android.widget.EditText')
    clear_password.clear()

  def wait_for_element(self, locator_strategy, locator):
    # Define a maximum wait time (e.g., 10 seconds)
    wait = WebDriverWait(self.driver, 10)

    # Use expected_conditions to wait for the element to be visible
    element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

    return element
