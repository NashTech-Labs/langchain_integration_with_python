

from selenium.webdriver.common.by import By
from utils.locator_loader import load_locators

class LoginPage:
    def __init__(self, driver):
        self.locators = load_locators("/home/nashtech/Documents/Python_BDD_Framework/tests/resources/locator_registry.json")
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def get_title(self):
        return self.driver.title

    def enter_username(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, "login-buttonss").click()

    def is_logged_in(self):
        return "inventory" in self.driver.current_url
