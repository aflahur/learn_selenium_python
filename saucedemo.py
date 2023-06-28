
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

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
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('Products', response_data)

    def test_a_fail_login(self):
        driver = self.driver
        driver.get(self.url)
        driver.find_element(By.ID,"user-name").send_keys("xxx")
        driver.find_element(By.ID,"password").send_keys("xxx")
        driver.find_element(By.ID, "login-button").click()
        response_data = driver.find_element(By.CSS_SELECTOR,"[data-test='error']").text #by css selector means test using value that determined by SQA and SE
        self.assertIn('Epic sadface: Username and password do not match any user in this service', response_data)
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()