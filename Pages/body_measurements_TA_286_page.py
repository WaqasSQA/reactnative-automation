from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class BodyMeasurements(BasePage):

    def navigate_account_tab(self):
        tap_account_tab = self.wait_for_element(By.XPATH, '//android.widget.ImageView[@bounds="[551,1415][601,1465]"]')
        tap_account_tab.click()

    def click_health_profile(self):
        tap_health_profile = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Health Profile"]')
        tap_health_profile.click()

    def click_body_measurement(self):
        tap_body_measurement = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Body Measurement"]')
        tap_body_measurement.click()

    def click_height_drop_down(self):
        tap_height_drop_down = self.wait_for_element(By.XPATH, '//android.widget.TextView[@bounds="[607,392][655,442]"]')
        tap_height_drop_down.click()

    def select_cm(self):
        tap_cm = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="cm"]')
        tap_cm.click()

    def enter_height(self, height_reading):
        input_height = self.wait_for_element(By.XPATH, '//android.widget.EditText[@bounds="[29,358][514,474]"]')
        input_height.clear()
        input_height.send_keys(height_reading)

    def enter_weight(self, weight_reading):
        input_weight = self.wait_for_element(By.XPATH, '//android.widget.EditText[@bounds="[29,713][526,829]"]')
        input_weight.clear()
        input_weight.send_keys(weight_reading)

    def select_ft(self):
        tap_ft = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="ft/in"]')
        tap_ft.click()

    def enter_height_ft(self):
        input_height_ft = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                          '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                          '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                          '.FrameLayout/android.view.ViewGroup/android.view.ViewGroup'
                                                          '/android.view.ViewGroup/android.view.ViewGroup['
                                                          '2]/android.view.ViewGroup/android.view.ViewGroup/android'
                                                          '.view.ViewGroup/android.view.ViewGroup/android.view'
                                                          '.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
                                                          '/android.view.ViewGroup/android.view.ViewGroup/android'
                                                          '.widget.ScrollView/android.view.ViewGroup/android.view'
                                                          '.ViewGroup[1]/android.widget.EditText')
        input_height_ft.clear()
        input_height_ft.send_keys("5'11")

    def enter_weight_lbs(self, reading):
        input_weight_lbs = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                           '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                           '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                           '.FrameLayout/android.view.ViewGroup/android.view'
                                                           '.ViewGroup/android.view.ViewGroup/android.view.ViewGroup['
                                                           '2]/android.view.ViewGroup/android.view.ViewGroup/android'
                                                           '.view.ViewGroup/android.view.ViewGroup/android.view'
                                                           '.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
                                                           '/android.view.ViewGroup/android.view.ViewGroup/android'
                                                           '.widget.ScrollView/android.view.ViewGroup/android.view'
                                                           '.ViewGroup[2]/android.widget.EditText')
        input_weight_lbs.clear()
        input_weight_lbs.send_keys(reading)

    def select_save_continue(self):
        tap_save_continue = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Save & Continue"]')
        tap_save_continue.click()

    def wait_for_element(self, locator_strategy, locator):
        # Define a maximum wait time (e.g., 10 seconds)
        wait = WebDriverWait(self.driver, 20)

        # Use expected_conditions to wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

        return element
