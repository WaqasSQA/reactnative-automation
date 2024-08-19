from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class listDevices(BasePage):
    def click_devices_btn(self):
        devices_btn = self.wait_for_element(By.XPATH, "//android.widget.TextView[@text='Devices']")
        devices_btn.click()

    def click_add_new_device(self):
        add_new_device = self.wait_for_element(By.XPATH, "//android.widget.TextView[@text='Add New Device']")
        add_new_device.click()

    def devices_select(self):
        element_xpath = self.wait_for_element(By.XPATH, "(//android.widget.TextView)[9]")
        element_xpath.click()

    def wait_for_element(self, locator_strategy, locator):
        # Define a maximum wait time (e.g., 10 seconds)
        wait = WebDriverWait(self.driver, 20)

        # Use expected_conditions to wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

        return element
