import os
import tempfile
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class ExampleBrowserTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1280,900")
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_python_homepage(self):
        self.driver.get("https://www.python.org/")
        self.assertIn("Python", self.driver.title)
        search_box = self.driver.find_element(By.ID, "id-search-field")
        search_box.send_keys("selenium")
        self.assertEqual(search_box.get_attribute("value"), "selenium")

        screenshot_path = os.path.join(tempfile.gettempdir(), "python-homepage.png")
        self.driver.save_screenshot(screenshot_path)
        self.assertTrue(os.path.exists(screenshot_path))
        print(f"Screenshot saved to: {screenshot_path}")


if __name__ == "__main__":
    unittest.main()
