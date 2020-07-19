import time
import logging
import sys
import os
import unittest
from Utility.XLUtils import *
from PageObject.LoginPage import LoginPage
import HtmlTestRunner
from selenium import webdriver
from PageObject.HomePage import HomePage
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))



class Login(unittest.TestCase):
    path="D:\Coding\PageObjectSelenium\TestData\LoginData.xlsx"

    logging.basicConfig(filename="D:\Coding\PageObjectSelenium\Log\Login.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    level=logging.INFO
                    )
    logger=logging.getLogger()

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        logging.getLogger().info("Browser Launched")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        #logging.getLogger().info("Browser Maximized")
        cls.logger.info("Browser Maximized")


    def test_data_driven_login(self):
        driver=self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        logging.getLogger().info("URL Launced")
        time.sleep(2)
        rows=get_row_count(self.path,'Sheet1')
        for r in range(2,rows+1):
            username=read_data(self.path,"Sheet1",r,1)
            password=read_data(self.path,"Sheet1",r,2)
            login = LoginPage(driver)
            login.enter_username(username)

            self.logger.info("Username entered")
            login.enter_password(password)

            self.logger.info("Password entered")
            login.click_login()


            flag=len(driver.find_elements_by_id("welcome"))
            #print("Flag value",flag)


            if flag>0:
                print("Test Case Pass",username,password)
                logging.getLogger().info("Valid Login")
                write_data(self.path,'Sheet1',r,3,"Test Pass")

                hp = HomePage(driver)
                hp.click_welcome()

                self.logger.info("Home Page Open")
                hp.click_logout()
                time.sleep(2)


            else:

                self.logger.error("Login Failed")
                print("Test Case Fail",username,password)
                write_data(self.path,'Sheet1',r,3,"Test Fail")



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

        cls.logger.info("Browser Closed")
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__name__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\Coding\PageObjectSelenium\Report'))
