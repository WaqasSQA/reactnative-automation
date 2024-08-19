from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class searchBar(BasePage):
    def search_bar(self, searchItem):
        search_bar = self.wait_for_element(By.XPATH, "//android.widget.EditText[@hint='Search Hive app']")
        search_bar.send_keys(searchItem)

    def wait_for_element(self, locator_strategy, locator):
        wait = WebDriverWait(self.driver, 20)

        # Use expected_conditions to wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

        return element
