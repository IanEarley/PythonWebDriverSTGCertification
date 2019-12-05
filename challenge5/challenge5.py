import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge5(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def navigate_to(self, driver, site):
        driver.get(site)

    def search(self, driver, keyword):
        elem = driver.find_element_by_id("input-search")
        elem.send_keys(keyword)
        elem.send_keys(Keys.RETURN)

    def find_matches(self, driver, car):
        drop = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "serverSideDataTable_length")))
        car_model = driver.find_elements_by_xpath("//*[@data-uname = 'lotsearchLotmodel']")
        unique_models = []
        for option in Select(drop).options:
            if option.text == "20":
                Select(drop).select_by_visible_text(option.text)
                break
            else:
                Select(drop).select_by_visible_text("20")
                break
        for i in range(19):
            if car_model[i].text not in unique_models:
                unique_models.insert(i, car_model[i].text)
        print(str(len(unique_models)) + " unique models of " + car + " found:")
        for unique in unique_models:
            print(unique)

    def test_challenge5(self):
        print("Testing number of unique models found on page:")
        driver = self.driver
        print("Getting page...")
        self.navigate_to(driver, "https://www.copart.com/")
        print("Searching for Porsche...")
        self.search(driver, "porsche")
        print("Finding unique models...")
        self.find_matches(driver, "Porsche")


if __name__ == '__main__':
    unittest.main()