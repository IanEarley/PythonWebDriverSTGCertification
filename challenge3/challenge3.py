import unittest
from selenium import webdriver
from extract_data import extract_data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Challenge3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge3(self):
        driver = self.driver
        driver.get("https://copart.com")
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ar-right")))
        button.clickable = True if button.get_attribute('src').find('icon_right_active') != -1 else False
        while button.clickable:
            for car in extract_data(driver):
                print(car)
            button.click()
            button.clickable = True if button.get_attribute('src').find('icon_right_active') != -1 else False
        else:
            for car in extract_data(driver):
                print(car)


if __name__ == "__main__":
    unittest.main()