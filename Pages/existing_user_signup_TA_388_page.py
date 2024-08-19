from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class ExistingUserSignup(BasePage):
    def click_signup(self):
        signup = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text=" Sign up"]')
        signup.click()

    def firstname(self):
        first_name = self.wait_for_element(By.XPATH, '//android.widget.EditText[@text="Enter first name. e-g John"]')
        first_name.send_keys("Yousma")

    def lastname(self):
        last_name = self.wait_for_element(By.XPATH, '//android.widget.EditText[@text="Enter last name. e-g Doe"]')
        last_name.send_keys("Siddiqui")

    def gender(self):
        select_gender = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Female"]')
        select_gender.click()

    def countrycode(self):
        country_code = self.wait_for_element(By.XPATH, '//android.view.ViewGroup[@bounds="[57,1396][208,1450]"]')
        country_code.click()

    def search_countrycode(self):
        enter_countrycode = self.wait_for_element(By.XPATH, '//android.widget.EditText[@text="Enter country name"]')
        enter_countrycode.send_keys("United Kingdom")

    def select_country(self):
        country = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="United Kingdom (+44)"]')
        country.click()

    def enter_number(self):
        number = self.wait_for_element(By.XPATH, '//android.widget.EditText[@text="Phone Number"]')
        number.send_keys("7946268462")

    def citizenship_dropdown(self):
        citizenship = self.wait_for_element(By.XPATH, '//android.view.ViewGroup[@bounds="[57,644][663,698]"]')
        citizenship.click()

    def enter_citizenship(self):
        input_citizenship = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Singapore (+65)"]')
        input_citizenship.click()

    def enter_email(self):
        email = self.wait_for_element(By.XPATH, '//android.widget.EditText[@text="E.g. Sample@email.com"]')
        email.send_keys("yousma.siddiqui@biomarking.com")

    def enter_password(self):
        password = self.wait_for_element(By.XPATH, '//android.widget.EditText[@text="Enter a password"]')
        password.send_keys("Yousma@biomark1")

    def accept_terms(self):
        terms1 = self.wait_for_element(By.XPATH, '//android.view.ViewGroup[@bounds="[60,1099][107,1146]"]')
        terms1.click()
        terms2 = self.wait_for_element(By.XPATH, '//android.view.ViewGroup[@bounds="[60,1228][107,1275]"]')
        terms2.click()

    def click_continue(self):
        tap_continue = self.wait_for_element(By.XPATH, '//android.widget.TextView[@text="Continue"]')
        tap_continue.click()

    def wait_for_element(self, locator_strategy, locator):
        # Define a maximum wait time (e.g., 10 seconds)
        wait = WebDriverWait(self.driver, 20)

        # Use expected_conditions to wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

        return element
