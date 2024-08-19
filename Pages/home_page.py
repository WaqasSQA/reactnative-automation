from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class HomePage(BasePage):

    def click_action_button(self):
        action_button = self.wait_for_element(By.XPATH,
                                              '//android.widget.Button[@content-desc="collapsed"]/android.view.ViewGroup')
        action_button.click()

    def click_log_data_button(self):
        log_data_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"Log Health Data")]')
        log_data_button.click()

    def navigate_back_to_lab_result_screen(self):
     navigate_back = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup')
     navigate_back.click()

    def navigate_to_home_screen(self):
        navigate_to_home = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup')
        navigate_to_home.click()

    def click_lab_results(self):
        lab_result_screen = self.wait_for_element(By.XPATH, '//*[contains(@text,"Lab Results")]')
        lab_result_screen.click()

    def see_report(self):
        see_report_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"See Report")]')
        see_report_button.click()

    def download_report(self):
        download_report_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"Download Report Results")]')
        download_report_button.click()

    def open_potassium_biomarker(self):
        potassium_biomarker = self.wait_for_element(By.XPATH, '//*[contains(@text,"Potassium")]')
        potassium_biomarker.click()

    def navigate_back(self):
        navigation_button = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                            '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                            '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                            '.FrameLayout/android.view.ViewGroup/android.view'
                                                            '.ViewGroup/android.view.ViewGroup/android.view'
                                                            '.ViewGroup['
                                                            '2]/android.view.ViewGroup/android.view.ViewGroup/android'
                                                            '.view.ViewGroup/android.view.ViewGroup/android.view'
                                                            '.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
                                                            '/android.view.ViewGroup')
        navigation_button.click()

    def open_chloride_biomarker(self):
        chloride_biomarker = self.wait_for_element(By.XPATH, '//*[contains(@text,"Chloride")]')
        chloride_biomarker.click()

    def click_steps_card(self):
        steps_card = self.wait_for_element(By.XPATH, '//*[contains(@text,"Steps")]')
        steps_card.click()

    def select_one_month_data(self):
        one_month_data = self.wait_for_element(By.XPATH, '//*[contains(@text,"1 Month")]')
        one_month_data.click()

    def select_three_month_data(self):
        three_month_data = self.wait_for_element(By.XPATH, '//*[contains(@text,"3 Month")]')
        three_month_data.click()

    def navigate_to_verification_screen(self):
      navigation_screen = self.wait_for_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]')
      navigation_screen.click()

    def click_continue(self):
      continue_button = self.wait_for_element(By.XPATH, '//*[contains(@text,"Continue")]')
      continue_button.click()

    def navigate_back_to_verification(self):
      navigate_back = self.wait_for_element(By.XPATH, '//android.widget.ImageButton[@content-desc="back"]')
      navigate_back.click()

    def return_to_home(self):
      return_home = self.wait_for_element(By.XPATH, '//*[contains(@text,"Return to home")]')
      return_home.click()
    def wait_for_element(self, locator_strategy, locator):
        # Define a maximum wait time (e.g., 10 seconds)
        wait = WebDriverWait(self.driver, 10)

        # Use expected_conditions to wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

        return element