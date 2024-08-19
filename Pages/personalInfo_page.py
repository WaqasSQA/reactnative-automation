from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class PersonalInfoPage(BasePage):
    def change_first_name(self, changeFname):
        first_name = (
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
            '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup['
            '2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android'
            '.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view'
            '.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view'
            '.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText')
        first_name_locator = self.wait_for_element(By.XPATH, first_name)
        first_name_locator.clear()
        first_name_locator.send_keys(changeFname)

    def change_last_name(self, changeLname):
        last_name = (
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
            '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup['
            '2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android'
            '.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view'
            '.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view'
            '.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText')
        last_name_locator = self.wait_for_element(By.XPATH, last_name)
        last_name_locator.clear()
        last_name_locator.send_keys(changeLname)

    def assert_user_cant_save_wront_personal_information(self):
        button_element = self.wait_for_element(By.XPATH, "//*[contains(@text,'Save & Continue')]")
        assert button_element.is_enabled()

    def wait_for_element(self, locator_strategy, locator):
        # Define a maximum wait time (e.g., 10 seconds)
        wait = WebDriverWait(self.driver, 10)

        # Use expected_conditions to wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

        return element