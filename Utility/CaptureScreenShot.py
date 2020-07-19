

class Secreenshot():
    #path="D:\Coding\PageObjectSelenium\Screenshot\Screenshot.png"
    path="D:\Coding\PageObjectSelenium\Screenshot"

    def __init__(self,driver):
        self.driver=driver

    def save_screenshot(self):
        self.driver.save_screenshot(self.path)
        print("Screenshoot captured")


    def get_screenshot_asfile(self,name):
        actual_path="{}\{}".format(self.path,name)
        self.driver.get_screenshot_as_file(actual_path)

