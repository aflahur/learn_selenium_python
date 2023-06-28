
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import baseLogin

class TestLogin(unittest.TestCase):
    def setUp(self):
        # self.browser = webdriver.Chrome(ChromeDriverManager().install())
        # webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver = webdriver.Chrome()
        # self.driver.get("https://saucedemo.com/")
        self.url="https://www.saucedemo.com/"
    def test_a_success_login(self):
        # steps
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        baseLogin.test_login(self,driver)

    def test_a_fail_login(self):
        driver = self.driver
        driver.get(self.url)
        baseLogin.test_fail_login(self,driver,"xxx","xxx")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()