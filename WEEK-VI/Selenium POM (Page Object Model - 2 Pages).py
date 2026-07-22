import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        return self

    def login(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        return DashboardPage(self.driver)


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def flash_message(self):
        return self.driver.find_element(By.ID, "flash").text

    def is_logged_in(self):
        return "secure" in self.driver.current_url


class LoginFlowTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1280,900")
        self.driver = webdriver.Chrome(options=options)

    def tearDown(self):
        self.driver.quit()

    def test_successful_login(self):
        dashboard = LoginPage(self.driver).open().login("tomsmith", "SuperSecretPassword!")
        self.assertTrue(dashboard.is_logged_in())
        self.assertIn("You logged into a secure area", dashboard.flash_message)


if __name__ == "__main__":
    unittest.main()
