import json
from selenium.webdriver.common.by import By

BY_MAPPING = {
    "ID": By.ID,
    "NAME": By.NAME,
    "XPATH": By.XPATH,
    "CSS": By.CSS_SELECTOR
}

def load_locators(json_path):
    with open(json_path, "r") as file:
        data = json.load(file)
        return {key: (BY_MAPPING[value[0]], value[1]) for key, value in data.items()}
