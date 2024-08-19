from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class logout(BasePage):

    def account(self):
        accounts_btn = self.wait_for_element(By.XPATH, "//android.widget.TextView[@text='Account']")
        accounts_btn.click()

    def logout(self):
        logout_btn = self.wait_for_element(By.XPATH, "(//android.widget.TextView)[23]")
        logout_btn.click()

    def logout_yes(self):
        logout_yes = self.wait_for_element(By.XPATH, "//android.widget.TextView[@text='Yes']")
        logout_yes.click()

    def wait_for_element(self, locator_strategy, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))
        return element
