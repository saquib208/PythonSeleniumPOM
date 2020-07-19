import time
import logging
import pytest
import sys
import os
import unittest
import HtmlTestRunner
from selenium import webdriver

#sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
#D:\Coding\PageObjectSelenium\TestCases>pytest -v -s --html=..\Report\report.html test_PytestReport.py

class TestLaunchPage():

    logging.basicConfig(filename="D:\Coding\PageObjectSelenium\Log\Login.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    level=logging.INFO
                    )
    logger=logging.getLogger()
    @pytest.fixture()
    def setup(self):
        print("Setup Method....!!")
        self.driver = webdriver.Chrome()
        self.logger.info("Browser launched")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

        self.logger.info("Browser Maximize")
        # logging.getLogger().info("Browser Maximized")
        yield

        self.driver.close()

        self.logger.info("Browser Closed")
        self.driver.quit()
        print("Test Completed")

    def test_amazon_search(self, setup):
        self.driver.get("https://www.amazon.in/")
        title = self.driver.title
        print("Title of the page->", title)

        self.assertNotEqual(title, "Google")

    def test_flipkart_search(self, setup):
        self.driver.get("https://www.flipkart.com/")
        title = self.driver.title
        print("Title of the page->", title)
        self.assertFalse(title == "Google")
