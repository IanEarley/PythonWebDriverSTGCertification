import unittest
from selenium import webdriver
from fibonacci import fibR
from num2word import num2word


class Challenge4(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge4(self):
        print(num2word(fibR(12)))


if __name__ == "__main__":
    unittest.main()