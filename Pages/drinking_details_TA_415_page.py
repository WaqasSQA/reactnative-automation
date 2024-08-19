import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class DrinkingDetails(BasePage):
    def click_drinking(self):
        open_drinking = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Drinking"]')
        open_drinking.click()

    def select_no(self):
        click_no = self.wait_for_element(By.XPATH,'//android.widget.TextView[@text="No"]')
        click_no.click()

    def select_yes(self):
        click_yes = self.wait_for_element(By.XPATH,'//android.widget.TextView[@text="Yes"]')
        click_yes.click()

    def select_beer(self):
        count = random.randint(5, 15)
        beer = self.wait_for_element(By.XPATH,'//android.widget.TextView[@bounds="[592,631][625,672]"]')
        for _ in range(count):
            beer.click()

    def select_wine(self):
        count = random.randint(5, 15)
        wine = self.wait_for_element(By.XPATH,'//android.widget.TextView[@bounds="[592,762][625,803]"]')
        for _ in range(count):
            wine.click()

    def select_spirit(self):
        count = random.randint(5, 15)
        spirit = self.wait_for_element(By.XPATH,'//android.widget.TextView[@bounds="[592,893][625,934]"]')
        for _ in range(count):
            spirit.click()

    def click_save(self):
        save = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Save"]')
        save.click()

    def wait_for_element(self, locator_strategy, locator):
        # Define a maximum wait time (e.g., 10 seconds)
        wait = WebDriverWait(self.driver, 20)

        # Use expected_conditions to wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

        return element
