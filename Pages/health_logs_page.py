from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class HealthLogsPage(BasePage):

    def navigate_to_weight_screen(self):
        weight_screen = self.wait_for_element(By.XPATH, '//*[contains(@text,"Weight")]')
        weight_screen.click()

    def navigate_to_blood_pressure_screen(self):
        blood_pressure_screen = self.wait_for_element(By.XPATH, '//*[contains(@text,"Blood Pressure")]')
        blood_pressure_screen.click()

    def navigate_to_blood_sugar_screen(self):
        blood_sugar_screen = self.wait_for_element(By.XPATH, '//*[contains(@text,"Blood Sugar")]')
        blood_sugar_screen.click()

    def click_fast_action_button(self):
        weight_fast_action_button = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android'
                                                                    '.widget.LinearLayout/android.widget.FrameLayout'
                                                                    '/android.widget.LinearLayout/android.widget'
                                                                    '.FrameLayout/android.widget.FrameLayout/android'
                                                                    '.view.ViewGroup/android.view.ViewGroup/android'
                                                                    '.view.ViewGroup/android.view.ViewGroup['
                                                                    '2]/android.view.ViewGroup/android.view.ViewGroup'
                                                                    '/android.view.ViewGroup/android.view.ViewGroup'
                                                                    '/android.view.ViewGroup/android.view.ViewGroup'
                                                                    '/android.view.ViewGroup['
                                                                    '2]/android.view.ViewGroup/android.view.ViewGroup'
                                                                    '/android.view.ViewGroup/android.view.ViewGroup')
        weight_fast_action_button.click()

    def click_meal_dropdown(self):
        dropDown_locator = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                           '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                           '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                           '.FrameLayout/android.view.ViewGroup/android.view'
                                                           '.ViewGroup/android.view.ViewGroup/android.view.ViewGroup['
                                                           '2]/android.view.ViewGroup/android.view.ViewGroup/android'
                                                           '.view.ViewGroup/android.view.ViewGroup/android.view'
                                                           '.ViewGroup/android.view.ViewGroup/android.widget'
                                                           '.ScrollView/android.view.ViewGroup/android.view'
                                                           '.ViewGroup['
                                                           '2]/android.view.ViewGroup/android.view.ViewGroup/android'
                                                           '.view.ViewGroup/android.widget.Button/android.widget'
                                                           '.TextView')
        dropDown_locator.click()

    def select_meal_time(self):
        meal_time = self.wait_for_element(By.XPATH, '//*[contains(@text,"After Breakfast")]')
        meal_time.click()

    def enter_blood_sugar_value(self, sugar_data):
        sugar_value = self.wait_for_element(By.XPATH, '//*[contains(@text,"0.0")]')
        sugar_value.clear()
        sugar_value.send_keys(sugar_data)

    def enter_weigth_value(self, weight_data):
        weight_value = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                       '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                       '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                       '.FrameLayout/android.view.ViewGroup/android.view.ViewGroup'
                                                       '/android.view.ViewGroup/android.view.ViewGroup['
                                                       '2]/android.view.ViewGroup/android.view.ViewGroup/android.view'
                                                       '.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
                                                       '/android.view.ViewGroup/android.widget.ScrollView/android'
                                                       '.view.ViewGroup/android.view.ViewGroup/android.widget.EditText')
        weight_value.clear()
        weight_value.send_keys(weight_data)

    def enter_high_bp_value(self, high_data):
        high_value = self.wait_for_element(By.XPATH, '//*[contains(@text,"High (SYS)")]')
        high_value.clear()
        high_value.send_keys(high_data)

    def enter_low_bp_value(self, low_data):
        low_value = self.wait_for_element(By.XPATH, '//*[contains(@text,"Low (DIA)")]')
        low_value.clear()
        low_value.send_keys(low_data)

    def click_add_button(self):
        add_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"Add")]')
        add_button.click()

    def open_logs(self):
      logs_dropdown = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.TextView[2]')
      logs_dropdown.click()

    def get_log_value(self):
      log_value = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup')
      log_value.click()

    def save_edit(self):
      save_edit_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"Save Edit")]')
      save_edit_button.click()

    def delete_log(self):
      delete_log_button = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.TextView')
      delete_log_button.click()

    def click_yes(self):
      confirm_deletion_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"Yes")]')
      confirm_deletion_button.click()

    def wait_for_element(self, locator_strategy, locator):
        # Define a maximum wait time (e.g., 10 seconds)
        wait = WebDriverWait(self.driver, 10)

        # Use expected_conditions to wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

        return element
