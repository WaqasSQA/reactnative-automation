from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
from conftest import setup_appium_driver


class MedicalHistory_HP(BasePage):

    def navigate_account_screen(self):
        account_screen = self.wait_for_element(By.XPATH, "//*[contains(@text, 'Account')]")
        account_screen.click()

    def click_health_profile(self):
        health_profile_acc = self.wait_for_element(By.XPATH,
                                                   "//android.widget.TextView[@bounds='[221,1592][602,1665]']")
        health_profile_acc.click()

    def click_medical_history(self):
        medical_history_btn = self.wait_for_element(By.XPATH, "//android.widget.TextView[@text='Medical History']")
        medical_history_btn.click()

    def click_ethnicity_dropdown(self):
        ethnicity_dropdown = self.wait_for_element(By.XPATH, "//android.widget.EditText["
                                                             "@resource-id='text-input-flat']")
        ethnicity_dropdown.click()

    def select_dropdown_option(self):
        select_option_btn = self.wait_for_element(By.XPATH, "//android.widget.TextView[@text='Chinese']")
        select_option_btn.click()

    def add_cholesterol_details(self, Cholesterol_Medication):
        high_cholesterol_btn = self.wait_for_element(By.XPATH,
                                                     "//android.widget.TextView[@bounds='[235,1139][571,1219]']")
        high_cholesterol_btn.click()

        diagnosed_cholesterol_yes = self.wait_for_element(By.XPATH, "//android.view.ViewGroup[@bounds='[158,845][228,"
                                                                    "915]']")
        diagnosed_cholesterol_yes.click()

        taking_medication_yes = self.wait_for_element(By.XPATH, "//android.view.ViewGroup[@bounds='[158,1133]["
                                                                "228,1203]']")
        taking_medication_yes.click()

        add_medication = self.wait_for_element(By.XPATH, "//android.widget.EditText[@bounds='[155,1420][1256,1582]']")
        add_medication.send_keys(Cholesterol_Medication)

        add_medication_plusBtn = self.wait_for_element(By.XPATH, "//android.widget.TextView[@bounds='[1111,1442]["
                                                                 "1222,1561]']")
        add_medication_plusBtn.click()

        save_btn = self.wait_for_element(By.XPATH, "//android.widget.TextView[@text='Save']")
        save_btn.click()

    def add_blood_pressure_details(self):
        high_blood_pressure = self.wait_for_element(By.XPATH, "//android.widget.TextView[@bounds='[835,1139][1240,"
                                                              "1219]']")
        high_blood_pressure.click()

        diagnosed_high_pressure_no = self.wait_for_element(By.XPATH, "//android.view.ViewGroup[@bounds='[394,845]["
                                                                     "464,915]']")
        diagnosed_high_pressure_no.click()

        save_btn = self.wait_for_element(By.XPATH, "//android.widget.TextView[@text='Save']")
        save_btn.click()

    def add_diabetes_details(self, Diabetes_Medication):
        diabetes_btn = self.wait_for_element(By.XPATH, "//android.widget.TextView[@bounds='[315,1344][492,1424]']")
        diabetes_btn.click()

        diagnosed_diabetes_yes = self.wait_for_element(By.XPATH, "//android.view.ViewGroup[@bounds='[158,845][228,"
                                                                 "915]']")
        diagnosed_diabetes_yes.click()

        diabetes_dropdown = self.wait_for_element(By.XPATH,
                                                  "//android.widget.TextView[@bounds='[165,1140][1133,1206]']")
        diabetes_dropdown.click()
        select_diabetes_type = self.wait_for_element(By.XPATH, "//android.widget.TextView[@text='Type 2 only']")
        select_diabetes_type.click()

        take_medications_yes = self.wait_for_element(By.XPATH, "//android.view.ViewGroup[@bounds='[158,1430][228,"
                                                               "1500]']")
        take_medications_yes.click()

        add_medications_field = self.wait_for_element(By.XPATH, "//android.widget.EditText["
                                                                "@resource-id='text-input-flat']")
        add_medications_field.send_keys(Diabetes_Medication)

        save_btn = self.wait_for_element(By.XPATH, "//android.widget.TextView[@text='Save']")
        save_btn.click()

    def add_asthma_details(self):
        asthma_btn = self.wait_for_element(By.XPATH, "//android.widget.TextView[@bounds='[960,1344][1114,1424]']")
        asthma_btn.click()

        asthma_no = self.wait_for_element(By.XPATH, "//android.view.ViewGroup[@bounds='[412,863][447,898]']")
        asthma_no.click()

        save_btn = self.wait_for_element(By.XPATH, "//android.widget.TextView[@text='Save']")
        save_btn.click()

    def add_cancer_details(self):
        cancer_btn = self.wait_for_element(By.XPATH, "//android.widget.TextView[@text='Cancer']")
        cancer_btn.click()

        diagnosed_cancer_yes = self.wait_for_element(By.XPATH, "//android.view.ViewGroup[@bounds='[158,845][228,915]']")
        diagnosed_cancer_yes.click()

        cancer_type_dropdown = self.wait_for_element(By.XPATH, "//android.widget.TextView[@bounds='[165,1140][1133,"
                                                               "1206]']")
        cancer_type_dropdown.click()

        select_cancer_type = self.wait_for_element(By.XPATH, "//android.widget.TextView[@text='Cervical']")
        select_cancer_type.click()

        treatment_no = self.wait_for_element(By.XPATH, "//android.view.ViewGroup[@bounds='[412,1448][447,1483]']")
        treatment_no.click()

        save_btn = self.wait_for_element(By.XPATH, "//android.widget.TextView[@text='Save']")
        save_btn.click()

    def add_other_details(self, other_disease, Medicine):
        other_btn = self.wait_for_element(By.XPATH, "//android.widget.TextView[@text='Other']")
        other_btn.click()

        other_disease_field = self.wait_for_element(By.XPATH, "//android.widget.EditText[@bounds='[155,924][1256,"
                                                              "1086]']")
        other_disease_field.send_keys(other_disease)

        add_medication = self.wait_for_element(By.XPATH, "//android.widget.EditText[@bounds='[155,1436][1256,1598]']")
        add_medication.send_keys(Medicine)

        save_btn = self.wait_for_element(By.XPATH, "//android.widget.TextView[@text='Save']")
        save_btn.click()

    def click_save_n_continue_btn(self):
        save_btn = self.wait_for_element(By.XPATH, "//android.widget.TextView[@text='Save & Continue']")
        save_btn.click()

    def wait_for_element(self, locator_strategy, locator):
        # Define a maximum wait time (e.g., 10 seconds)
        wait = WebDriverWait(self.driver, 10)

        # Use expected_conditions to wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))

        return element
