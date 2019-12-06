def extract_data(driver):
    pop_cars = driver.find_elements_by_css_selector(
        ".items > .d-flex > .d-flex > .items-description > div > .lot-desc > strong")
    pop_car_links = driver.find_elements_by_css_selector(
        ".items > .d-flex > .d-flex > .items-description > .view-vehicle-btn > a")
    return [car.text + " - " + pop_car_links[pop_cars.index(car)].get_attribute("href") for car in pop_cars]