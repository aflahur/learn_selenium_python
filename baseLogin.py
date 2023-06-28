
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_login(self,driver):
    driver.find_element(By.CSS_SELECTOR,"[data-test='username']").send_keys("standard_user") # isi email
    driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
    driver.find_element(By.ID, "login-button").click()
    # validasi
    response_data = driver.find_element(By.CLASS_NAME,"title").text
    self.assertIn('Products', response_data)

def test_fail_login(self,driver,username,password):
    driver.find_element(By.CSS_SELECTOR,"[data-test='username']").send_keys(username) # isi email
    driver.find_element(By.ID,"password").send_keys(password) # isi password
    driver.find_element(By.ID, "login-button").click()
    #validasi
    response_data = driver.find_element(By.CSS_SELECTOR,"[data-test='error']").text #by css selector means test using value that determined by SQA and SE
    self.assertIn('Epic sadface: Username and password do not match any user in this service', response_data)
