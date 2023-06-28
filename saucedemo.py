import unittest
from selenium import webdriver
from POM.data import inputan
import baseLogin

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = inputan.url
    def test_a_success_login(self):
        # steps
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        baseLogin.test_login(self,driver)

    def test_a_fail_login(self):
        driver = self.driver
        driver.get(self.url)
        baseLogin.test_fail_login(self,driver,inputan.invalid_username,inputan.invalid_password)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()