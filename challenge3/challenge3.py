import unittest
from selenium import webdriver


class Challenge3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def extract_data(self, driver):
        pop_cars = driver.find_elements_by_css_selector(".items > .d-flex > .d-flex > .items-description > div > .lot-desc > strong")
        pop_car_links = driver.find_elements_by_css_selector(".items > .d-flex > .d-flex > .items-description > .view-vehicle-btn > a")
        return [car.text + " - " + pop_car_links[pop_cars.index(car)].get_attribute("href") for car in pop_cars]

    def test_challenge3(self):
        driver = self.driver
        driver.get("https://copart.com")
        button = driver.find_element_by_class_name("ar-right")
        button.clickable = True if button.get_attribute('src').find('icon_right_active') != -1 else False
        while button.clickable:
            for car in self.extract_data(driver):
                print(car)
            button.click()
            button.clickable = True if button.get_attribute('src').find('icon_right_active') != -1 else False
        else :
            for car in self.extract_data(driver):
                print(car)


if __name__ == "__main__":
    unittest.main()