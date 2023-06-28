from POM.data import inputan
from POM.loginPage import loginPage

def test_login(self,driver):
    driver.find_element(*loginPage.dataTestUsername).send_keys(inputan.valid_username) # isi email
    driver.find_element(*loginPage.idPassword).send_keys(inputan.valid_password) # isi password
    driver.find_element(*loginPage.idLoginButton).click()
    # validasi
    response_data = driver.find_element(*loginPage.classNameTitle).text
    self.assertIn('Products', response_data)

def test_fail_login(self,driver,username,password):
    driver.find_element(*loginPage.dataTestUsername).send_keys(username) # isi email
    driver.find_element(*loginPage.idPassword).send_keys(password) # isi password
    driver.find_element(*loginPage.idLoginButton).click()
    #validasi
    response_data = driver.find_element(*loginPage.dataTestError).text #by css selector means test using value that determined by SQA and SE
    self.assertIn(loginPage.errorMessage, response_data)
