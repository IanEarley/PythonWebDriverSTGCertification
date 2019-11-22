import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
        assert driver.page_source.find("PORSCHE"), "Porsche not present in list"

if __name__ == '__main__' :
    unittest.main()