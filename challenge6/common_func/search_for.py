from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def search_for(driver, text):
    print("searching for " + text + "...")
    search = driver.find_element(By.ID, "input-search")
    search.send_keys(text)
    search.send_keys(Keys.RETURN)