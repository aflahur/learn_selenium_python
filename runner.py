import unittest
from unittest.suite import TestSuite
import sdcart,saucedemo

if __name__ == "__main__":
     
     #inisiasi test suite
     loader = unittest.TestLoader()
     suite = unittest.TestSuite()

     #add test
     suite.addTests(loader.loadTestsFromModule(sdcart))
     suite.addTests(loader.loadTestsFromModule(saucedemo))

     #create runner
     runner = unittest.TextTestRunner()
     runner.run(suite)