from selenium import webdriver
import unittest
import time
from PageObject.LoginPage import LoginPage
from PageObject.HomePage import HomePage
import sys
import os
import HtmlTestRunner
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

#D:\Coding\PageObjectSelenium>python -m unittest TestCases\Login.py

class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_valid_login(self):
        driver=self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        login=LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        hp=HomePage(driver)
        hp.click_welcome()
        title=driver.title
        print("Title-->",title)
        self.assertEqual(title,"OrangeHRM","Web page title not matching")
        hp.click_logout()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__name__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\Coding\PageObjectSelenium\Report'))
