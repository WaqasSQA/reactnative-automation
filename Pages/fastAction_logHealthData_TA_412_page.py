from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class FastAction(BasePage):
    def click_fastActionBtn(self):
        tap_fastActionBtn = self.wait_for_element(By.XPATH,
                                                  '//android.widget.Button[@content-desc="collapsed"]/android.view'
                                                  '.ViewGroup')
        tap_fastActionBtn.click()

    def click_logHealthData(self):
        tap_logHealthData = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Log Health Data"]')
        tap_logHealthData.click()

    def wait_for_element(self, locator_strategy, locator):
        # Define a maximum wait time (e.g., 10 seconds)
        wait = WebDriverWait(self.driver, 20)

        # Use expected_conditions to wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

        return element
