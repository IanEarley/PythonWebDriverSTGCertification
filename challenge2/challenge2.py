import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Challenge2 (unittest.TestCase) :
    def setUp(self) :
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self) :
        self.driver.close()

    def test_challenge2 (self) :
        driver = self.driver
        driver.get("https://copart.com/")
        elem = driver.find_element_by_id("input-search")
        elem.send_keys("exotics")
        elem.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "serverSideDataTable")))
        assert driver.page_source.find("PORSCHE"), "Porsche not present in list"


if __name__ == '__main__' :
    unittest.main()