from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class HealthLogs(BasePage):
    def navigate_health_profile_screen(self):
        health_profile = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Health Profile"]')
        health_profile.click()

    def navigate_health_logs_screen(self):
        health_logs = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Health Logs"]')
        health_logs.click()

    def click_blood_sugar(self):
        blood_sugar = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Blood Sugar"]')
        blood_sugar.click()

    def navigate_blood_sugar_details_screen(self):
        blood_sugar_details_screen = self.wait_for_element(By.XPATH,
                                                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.View')
        blood_sugar_details_screen.click()

    def enter_blood_sugar_reading(self, reading):
        input_blood_sugar_reading = self.wait_for_element(By.XPATH, '//android.widget.EditText[@text="0.0"]')
        input_blood_sugar_reading.send_keys(reading)

    def select_meal_time_dropdown(self):
        meal_time_dropdown = self.wait_for_element(By.XPATH, '//android.widget.EditText[@text="Select Meal time"]')
        meal_time_dropdown.click()

    def select_meal_time(self):
        meal_time = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Before Breakfast"]')
        meal_time.click()

    def click_add_blood_sugar_button(self):
        add_blood_sugar_button = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Add"]')
        add_blood_sugar_button.click()

    def click_blood_pressure(self):
        blood_pressure = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Blood Pressure"]')
        blood_pressure.click()

    def navigate_blood_pressure_details_screen(self):
        blood_pressure_details_screen = self.wait_for_element(By.XPATH,
                                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.View')
        blood_pressure_details_screen.click()

    def high_blood_field(self, highData):
        high_field = self.wait_for_element(By.XPATH, "//android.widget.EditText[@text='High (SYS)']")
        high_field.send_keys(highData)

    def low_blood_field(self, lowData):
        low_field = self.wait_for_element(By.XPATH, "//android.widget.EditText[@text='Low (DIA)']")
        low_field.send_keys(lowData)

    def click_add_blood_pressure_button(self):
        add_blood_pressure_button = self.wait_for_element(By.XPATH, "//android.widget.TextView[@text='Add']")
        add_blood_pressure_button.click()

    def click_HbA1c(self):
        tap_HbA1c = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="HbA1c"]')
        tap_HbA1c.click()

    def navigate_HbA1c_details_screen(self):
        HbA1c_details_screen = self.wait_for_element(By.XPATH,
                                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.View')
        HbA1c_details_screen.click()

    def enter_HbA1c_reading(self, HbA1c_reading):
        Input_HbA1c_reading = self.wait_for_element(By.XPATH, '//android.widget.EditText[@text="0.0"]')
        Input_HbA1c_reading.send_keys(HbA1c_reading)

    def click_add_HbA1c_button(self):
        add_HbA1c_button = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Add"]')
        add_HbA1c_button.click()

    def click_weight(self):
        tap_weight = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Weight"]')
        tap_weight.click()

    def navigate_enter_weight_details_screen(self):
        enter_weight_details_screen = self.wait_for_element(By.XPATH,
                                                            '/hierarchy/android.widget.FrameLayout/android.widget'
                                                            '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                            '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                            '.FrameLayout/android.view.ViewGroup/android.view'
                                                            '.ViewGroup/android.view.ViewGroup/android.view'
                                                            '.ViewGroup['
                                                            '2]/android.view.ViewGroup/android.view.ViewGroup/android'
                                                            '.view.ViewGroup/android.view.ViewGroup/android.view'
                                                            '.ViewGroup/android.view.ViewGroup/android.view'
                                                            '.ViewGroup['
                                                            '2]/android.view.ViewGroup/android.view.ViewGroup/android'
                                                            '.view.View')
        enter_weight_details_screen.click()

    def enter_weight(self, weight):
        input_weight = self.wait_for_element(By.XPATH, '//android.widget.EditText[@text="0.00"]')
        input_weight.send_keys(weight)

    def click_add_weight(self):
        add_log = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Add"]')
        add_log.click()

    def wait_for_element(self, locator_strategy, locator):
        # Define a maximum wait time (e.g., 10 seconds)
        wait = WebDriverWait(self.driver, 20)

        # Use expected_conditions to wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

        return element
