import unittest
from selenium import webdriver

class TestConcepts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_except_concept(self):
        title = "Hibachi"
        driver = self.driver
        driver.get("https://www.google.com")
        try:
            assert title in driver.title is True
        except AssertionError:
            raise Exception(f'Title needs to be {title}, but it was {driver.title}')
        finally:
            print("test complete.")


if __name__ == "__main__":
    unittest.main()