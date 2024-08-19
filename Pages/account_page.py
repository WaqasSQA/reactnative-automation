from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy
# from appium.webdriver.common.uiautomator import UiScrollable



class AccountPage(BasePage):
    def execute_script(self):
        pass

    def navigate_account_screen(self):
        account_screen = self.wait_for_element(By.XPATH, '//*[contains(@text,"Account")]')
        account_screen.click()

    def get_window_size(self):
        # Get the window size from the WebDriver object.
        window_size = self.driver.get_window_size()

        return window_size

    def click_personal_information(self):
        personal_info = self.wait_for_element(By.XPATH, '//*[contains(@text,"Personal Information")]')
        personal_info.click()


    def navigate_back_to_accounts(self):
        navigate_back = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
        navigate_back.click()

    def scroll_down(self):
        window_size = self.driver.get_window_size()

        # Get the middle of the screen.
        middle_y = window_size["height"] // 2

        # Swipe from the middle of the screen to the top.
        self.driver.swipe(0, middle_y, 0, 0, 1000)


    def click_policies(self):
        # Click on the element with the text "Policies".
        policies_screen = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[19]/android.widget.TextView[1]')
        policies_screen.click()

    def view_privacy_policy(self):
        view_privacy_policy = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.TextView')
        view_privacy_policy.click()

    def view_terms(self):
        view_terms_and_conditions = self.wait_for_element(By.XPATH, '//*[contains(@text,"Terms & Conditions")]')
        view_terms_and_conditions.click()

    def change_gender(self):
        gender_option = self.wait_for_element(By.XPATH, '//*[contains(@text,"Female")]')
        gender_option.click()


    def save_gender(self):
        click_save = self.wait_for_element(By.XPATH, '//*[contains(@text,"Save & Continue")]')
        click_save.click()

    def select_language_menu(self, language_selection):
        chose_lan = '//*[contains(@text, "{}")]'.format(language_selection)
        click_menu = self.wait_for_element(By.XPATH, chose_lan)
        click_menu.click()

    def choose_thai(self):
        thai_lan = self.wait_for_element(By.XPATH, '//*[contains(@text,"Thai")]')
        thai_lan.click()

    def choose_vietnamese(self):
        vietnamese_lan = self.wait_for_element(By.XPATH, '//*[contains(@text,"Vietnamese")]')
        vietnamese_lan.click()

    def choose_chinese(self):
        chinese_lan = self.wait_for_element(By.XPATH, '//*[contains(@text,"Chinese")]')
        chinese_lan.click()

    def choose_english(self):
        english_lan = self.wait_for_element(By.XPATH, '//*[contains(@text,"English")]')
        english_lan.click()

    def navigate_to_settings_page(self):
        settings_page = self.wait_for_element(By.XPATH, '//*[contains(@text,"Settings")]')
        settings_page.click()

    def navigate_to_email_page(self):
        email_page = self.wait_for_element(By.XPATH, '//*[contains(@text,"Email")]')
        email_page.click()

    def primary_email(self, email):
        enter_primary_email = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.EditText')
        enter_primary_email.clear()
        enter_primary_email.send_keys(email)

    def confirm_email(self, confirm_mail):
        confirm_primary_email = self.wait_for_element(By.XPATH,
                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.EditText')
        confirm_primary_email.send_keys(confirm_mail)

    def click_save_button(self):
        save_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"Save")]')
        save_button.click()
    def wait_for_element(self, locator_strategy, locator):
        # Define a maximum wait time (e.g., 10 seconds)
        wait = WebDriverWait(self.driver, 10)

        # Use expected_conditions to wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

        return element