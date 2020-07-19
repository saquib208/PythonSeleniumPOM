import time
import logging
import sys
import os
import unittest
import HtmlTestRunner
from selenium import webdriver
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))



class TestSearch(unittest.TestCase):

    path="D:\Coding\PageObjectSelenium\TestData\LoginData.xlsx"

    logging.basicConfig(filename="D:\Coding\PageObjectSelenium\Log\Login.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    level=logging.INFO
                    )
    logger=logging.getLogger()

    @classmethod
    def setUpClass(cls):
        print("Setup classs....!!!")




    @classmethod
    def setUp(self):
        print("Setup Method....!!")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        #logging.getLogger().info("Browser Maximized")
        self.logger.info("Browser Maximized")



    def test_google_search(self):
        driver=self.driver
        self.driver.get("https://google.com/")

        print("Title of the page->",self.driver.title)
        #Google

    def test_bin_search(self):
        driver=self.driver
        self.driver.get("https://bing.com/")

        print("Title of the page->",self.driver.title)
        #Bing



    def test_facebook_search(self):
        driver=self.driver
        self.driver.get("https://www.facebook.com/")

        print("Title of the page->",self.driver.title)
        #Facebook – log in or sign up

    @classmethod
    def tearDown(self):

        print("teardown method....!!")
        self.driver.close()

        self.logger.info("Browser Closed")
        self.driver.quit()
        print("Test Completed")

    @classmethod
    def tearDownClass(cls):
        print("Teardown classs....!!!")


if __name__ == '__name__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\Coding\PageObjectSelenium\Report'))
