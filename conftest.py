import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="module")
def setup_appium_driver():
    # Initialize the Appium driver with desired capabilities
    appium_service = AppiumService()
    appium_service.start()
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Pixel_4_API_34',
        'app': 'C:/Users/dev/Desktop/patientapp-v3-react-native/app/bm_dev_nov.apk',
        'automationName': 'UiAutomator2',
        'fullReset': True,
        'autoGrantPermissions': True,
        # Set to True to avoid resetting app data
        # Add other desired capabilities as needed
    }

    # Initialize the driver
    driver = webdriver.Remote('http://127.0.0.1:4723', desired_caps)
    time.sleep(20)
    # Perform setup actions
    update_modal_xpath = '//*[contains(@text,"Close")]'
    close_button = driver.find_element(By.XPATH, update_modal_xpath)
    close_button.click()

    time.sleep(5)

    # Continue to the login screen
    login_button = '//*[contains(@text,"Login")]'
    login = driver.find_element(By.XPATH, login_button)
    login.click()

    yield driver  # Provide the driver object to the test
    driver.quit()  # Teardown: Quit the driver after the test
    appium_service.stop()
