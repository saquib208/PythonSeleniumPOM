
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
from selenium import webdriver
import unittest
import time
import sys
import os
import HtmlTestRunner
sys.path.append("D:\Coding\PageObjectSelenium")
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

#allure serve D:\Coding\PageObjectSelenium\Report
#D:\Coding\PageObjectSelenium\TestCases>pytest -v -s --alluredir="D:\Coding\PageObjectSelenium\Report" test_AllureReportGenerate.py

@allure.severity(allure.severity_level.NORMAL)

class TestAllure():

    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        yield
        self.driver.close()

    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self,setup):
        driver=self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        status=self.driver.find_element_by_xpath("//*[@id='divLogo']").is_displayed()
        if status==True:
            assert True
        else:
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_list_Employee(self):
        pytest.skip("Implement later")

    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self,setup):
        driver=self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        titile=self.driver.title
        if titile=="OrangeHRM1":
            assert True

        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="testLogin",
                          attachment_type=AttachmentType.PNG)
            assert False

