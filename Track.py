
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Track:
    def __init__(self, driver):
        self.driver = driver

        self.driver.get('https://www.ordertracker.com/couriers/aliexpress')
        time.sleep(5)

        self.search_input = self.driver.find_element(By.TAG_NAME, 'input')

    def track_package(self, code):
        try:
            self.search_input.send_keys(code)
            time.sleep(1)
            self.search_input.submit()

            time.sleep(10)
            status = self.driver.find_element(By.CLASS_NAME, 'status-content')

            return status

        except Exception as e:
            print(f'Failed to access the information: {e}')
            return None
