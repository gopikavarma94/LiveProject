from selenium.webdriver.common.by import By

from pages.Basepage import BasePage
from pages.Homepage import Homepage
from utility.PageUtility import PageUtility
from utility.WaitUtility import WaitUtility


class Loginpage(BasePage):
    Username=(By.XPATH, "//input[@placeholder='Username']")
    Password=(By.XPATH, "//input[@placeholder='Password']")
    Signin=(By.XPATH, "//button[@type='submit']")
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.waitutility=WaitUtility()
        self.pageutility=PageUtility()

    def enterusername(self,usernamevalue):
        username = self.find(self.Username)
        #username.send_keys(usernamevalue)
        self.pageutility.send_data_to_element(username,usernamevalue)
        return self
    def enterpassword(self,passwordvalue):
        password = self.find(self.Password)
        #password.send_keys(passwordvalue)
        self.pageutility.send_data_to_element(password,passwordvalue)
        return self
    def signin(self):
        button = self.find(self.Signin)
        self.waitutility.wait_until_clickable(self.driver,button)
        #button.click()
        self.pageutility.click_on_element(button)
        return Homepage(self.driver)



