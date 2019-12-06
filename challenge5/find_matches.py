from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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