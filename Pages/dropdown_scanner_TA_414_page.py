from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class dropdownScanner(BasePage):
    def scanner_dropdown(self):
        scannerDropBtn = self.wait_for_element(By.XPATH, "//android.view.ViewGroup[@bounds='[137,401][207,471]']")
        scannerDropBtn.click()

    def input_barcode_btn(self):
        input_barcode_btn = self.wait_for_element(By.XPATH, "//android.widget.TextView[@text='Input Barcode']")
        input_barcode_btn.click()

    def barcode_input_field(self, barcode):
        barcode_field = self.wait_for_element(By.XPATH, "//android.widget.EditText[@text='ABC-1234-5678']")
        barcode_field.send_keys(barcode)

    def enter_code_btn(self):
        enter_btn = self.wait_for_element(By.XPATH, "//android.widget.TextView[@text='Enter Code']")
        enter_btn.click()

    def view_result_btn(self):
        view_resultsBtn = self.wait_for_element(By.XPATH, "//android.widget.TextView[@text='View Results']")
        view_resultsBtn.click()

    def wait_for_element(self, locator_strategy, locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))
        return element
