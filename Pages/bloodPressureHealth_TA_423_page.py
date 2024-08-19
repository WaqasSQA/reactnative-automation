from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class blood_HealthProfile(BasePage):

    def navigate_to_health_profile_page(self):
        health_profile_button = self.wait_for_element(By.XPATH, "//*[contains(@text,'Health Profile')]")
        health_profile_button.click()

    def navigate_to_health_logs(self):
        health_logs_button = self.wait_for_element(By.XPATH, "//android.view.ViewGroup[@bounds='[43,370][677,462]']")
        health_logs_button.click()

    def navigate_to_blood_pressure(self):
        blood_pressure_button = self.wait_for_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.TextView")
        blood_pressure_button.click()

    def navigate_to_heart_button(self):
        heart_button = self.wait_for_element(By.XPATH, "//android.view.ViewGroup[@bounds='[563,1381][615,1433]']")
        heart_button.click()

    def high_blood_field(self, highData):
        high_field = self.wait_for_element(By.XPATH, "//android.widget.EditText[@text='High (SYS)']")
        high_field.send_keys(highData)

    def low_blood_field(self, lowData):
        low_field = self.wait_for_element(By.XPATH, "//android.widget.EditText[@text='Low (DIA)']")
        low_field.send_keys(lowData)

    def click_add_button(self):
        add_button = self.wait_for_element(By.XPATH,  "//android.widget.TextView[@text='Add']")
        add_button.click()

    def wait_for_element(self, locator_strategy, locator):
        # Define a maximum wait time (e.g., 10 seconds)
        wait = WebDriverWait(self.driver, 10)

        # Use expected_conditions to wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

        return element
