import unittest
from selenium import webdriver
from POM.cartPage import cartPage
from POM.data import inputan
import baseLogin

class TestAddtoCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url=inputan.url

    def test_add_to_cart(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        baseLogin.test_login(self,driver)

        driver.find_element(*cartPage.addBackpack).click()
        cart = driver.find_element(*cartPage.cartBadge).text
        self.assertEqual(cart,"1")
        driver.find_element(*cartPage.cartBadge).click()
        url=driver.current_url
        self.assertIn('/cart.html',url)
        driver.find_element(*cartPage.inventoryItem)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()