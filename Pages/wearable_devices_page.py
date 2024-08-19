from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class WearableDevicesPage(BasePage):

    def navigate_to_devices_page(self):
        devices_screen = self.wait_for_element(By.XPATH, '//*[contains(@text,"Devices")]')
        devices_screen.click()
        
    def add_new_devices(self):

        add_device = self.wait_for_element(By.XPATH, '//*[contains(@text,"Add New Device")]')
        add_device.click()

    def select_freestyle_device(self):
        freestyle_device = self.wait_for_element(By.XPATH, '//*[contains(@text,"Freestyle Libre")]')
        freestyle_device.click()

    def enter_email(self, email):
        provide_email = self.wait_for_element(By.XPATH, '//*[contains(@text,"Email")]')
        provide_email.send_keys(email)

    def select_region(self):
        dropdown_locator = self.wait_for_element(By.XPATH, '//*[contains(@text,"Select Region")]')
        dropdown_locator.click()

    def choose_country(self):
        country = self.wait_for_element(By.XPATH, '//*[contains(@text,"Australia")]')
        country.click()

    def click_connect_button(self):
        connect_device = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.FrameLayout/android.view.ViewGroup/android.view.ViewGroup'
                                                         '/android.view.ViewGroup/android.view.ViewGroup['
                                                         '2]/android.view.ViewGroup/android.view.ViewGroup/android'
                                                         '.view.ViewGroup/android.view.ViewGroup/android.view'
                                                         '.ViewGroup/android.view.ViewGroup/android.view.ViewGroup['
                                                         '3]/android.view.ViewGroup[2]/android.widget.TextView')
        connect_device.click()

    def click_close_button(self):
        close_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"Close")]')
        close_button.click()

    def delete_wearable_device(self):
        click_delete_device = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                              '.LinearLayout/android.widget.FrameLayout/android'
                                                              '.widget.LinearLayout/android.widget.FrameLayout'
                                                              '/android.widget.FrameLayout/android.view.ViewGroup'
                                                              '/android.view.ViewGroup/android.view.ViewGroup/android'
                                                              '.view.ViewGroup['
                                                              '2]/android.view.ViewGroup/android.view.ViewGroup'
                                                              '/android.view.ViewGroup/android.view.ViewGroup/android'
                                                              '.view.ViewGroup/android.view.ViewGroup/android.view'
                                                              '.ViewGroup['
                                                              '3]/android.view.ViewGroup/android.widget.ImageView')
        click_delete_device.click()

    def unlink_device(self):
        unlink_device_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"Unlink device")]')
        unlink_device_button.click()

    def click_okay_button(self):
        click_yes = self.wait_for_element(By.XPATH, '//*[contains(@text,"Okay")]')
        click_yes.click()

    def wait_for_element(self, locator_strategy, locator):
        # Define a maximum wait time (e.g., 10 seconds)
        wait = WebDriverWait(self.driver, 10)

        # Use expected_conditions to wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

        return element