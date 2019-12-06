from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def search_for(driver, text, xpath):
    try:
        search = driver.find_element(By.XPATH, xpath)
    except exceptions.NoSuchElementException:
        raise Exception("No search bar found with xpath given.")
    print("searching for " + text + "...")
    search.click()
    search.send_keys(text)
    search.send_keys(Keys.RETURN)