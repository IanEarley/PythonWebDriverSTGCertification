import unittest
from selenium import webdriver
from find_matches import find_matches
from common_func.navigate_to import navigate_to
from common_func.search_for import search_for


class Challenge5(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge5(self):
        print("Testing number of unique models found on page:")
        driver = self.driver
        print("Getting page...")
        navigate_to(driver, "https://www.copart.com/")
        print("Searching for Porsche...")
        search_for(driver, "porsche")
        print("Finding unique models...")
        find_matches(driver, "Porsche")


if __name__ == '__main__':
    unittest.main()