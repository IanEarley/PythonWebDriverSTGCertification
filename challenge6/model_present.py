from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def model_present(driver, model):
    print("Looking in search results for " + model + " model...")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".search-resultstable")))
    model_list = driver.find_elements(By.XPATH, "//*[@data-uname = 'lotsearchLotmodel']")
    try:
        for models in model_list:
            if model == models.text:
                print("Found " + model + " in model list")
                break
        raise ValueError
    except TimeoutError:
        print("Test timed out before completion.")
    except ValueError:
        print(model + " was not found in model list.")