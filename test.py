import unittest
from selenium import webdriver

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://saucedemo.com/")

    def test_search_in_python_org(self):
        self.driver.get("https://saucedemo.com/")
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()