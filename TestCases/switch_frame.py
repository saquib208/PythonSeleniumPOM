import selenium

from Utility.CaptureScreenShot import *
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

class SwitchfFrame(unittest.TestCase):

    path="D:\Coding\PageObjectSelenium\Screenshot\Screenshot.png"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_valid_login(self):
        driver=self.driver
        self.driver.get("https://docs.oracle.com/javase/7/docs/api/")
        #self.driver.save_screenshot(self.path)
        Secreenshot.save_screenshot(self)
        driver.switch_to.frame("packageFrame")
        driver.find_elements_by_link_text("AbstractBorder").click()
        driver.switch_to.default_content()
        driver.switch_to.frame("classFrame")
        driver.find_elements_by_link_text("java.applet").click()
        driver.switch_to.default_content()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__name__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\Coding\PageObjectSelenium\Report'))
