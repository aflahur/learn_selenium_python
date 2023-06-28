from selenium.webdriver.common.by import By

class loginPage():
    username = "[data-test='username']"
    passw = "password"
    loginTitle = "title"
    loginButton = "login-button"
    errorMessage = 'Epic sadface: Username and password do not match any user in this service'
    dataTestUsername = (By.CSS_SELECTOR,"[data-test='username']")
    idPassword = (By.ID,"password")
    idLoginButton = (By.ID, "login-button")
    classNameTitle = (By.CLASS_NAME,"title")
    dataTestError = (By.CSS_SELECTOR,"[data-test='error']")