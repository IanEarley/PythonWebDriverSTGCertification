import unittest
from selenium import webdriver
from common_func.search_for import search_for
from common_func.navigate_to import navigate_to
from model_present import model_present

class Challenge6 (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge6(self):
        driver = self.driver
        navigate_to(driver, "https://www.copart.com/")
        search_for(driver, "Nissan")
        model_present(driver, "skyliner")


if __name__ == "__main__":
    unittest.main()