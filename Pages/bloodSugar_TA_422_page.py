from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class BloodSugarPage(BasePage):
    def navigate_health_profile_screen(self):
        health_profile = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Health Profile"]')
        health_profile.click()

    def navigate_health_logs_screen(self):
        health_logs = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Health Logs"]')
        health_logs.click()

    def navigate_enter_details_screen(self):
        enter_details_screen = self.wait_for_element(By.XPATH,
                                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.View')
        enter_details_screen.click()

    def enter_reading(self, reading):
        input_reading = self.wait_for_element(By.XPATH, '//android.widget.EditText[@text="0.0"]')
        input_reading.send_keys(reading)

    def select_meal_time_dropdown(self):
        meal_time_dropdown = self.wait_for_element(By.XPATH, '//android.widget.EditText[@text="Select Meal time"]')
        meal_time_dropdown.click()

    def select_meal_time(self):
        meal_time = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Before Breakfast"]')
        meal_time.click()

    def click_add(self):
        add_log = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Add"]')
        add_log.click()

    def wait_for_element(self, locator_strategy, locator):
        # Define a maximum wait time (e.g., 10 seconds)
        wait = WebDriverWait(self.driver, 20)

        # Use expected_conditions to wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

        return element
