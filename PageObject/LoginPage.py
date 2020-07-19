from Locator.Locator import Locators

from Utility.CaptureScreenShot import Secreenshot
class LoginPage ():
    def __init__(self,driver):
        self.driver=driver
        self.username_texbox_id=Locators.username_texbox_id
        self.password_textbox_id=Locators.password_textbox_id
        self.login_button_id=Locators.login_button_id

    def enter_username(self,username):

        self.driver.find_element_by_id(self.username_texbox_id).clear()
        self.driver.find_element_by_id(self.username_texbox_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()
