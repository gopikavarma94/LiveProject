from selenium.webdriver.common.by import By

from pages.Basepage import BasePage
from pages.Newspage import News
from utility.PageUtility import PageUtility
from utility.WaitUtility import WaitUtility


class Admin(BasePage):
    ResetAdmin=(By.XPATH,"//a[@class='btn btn-rounded btn-warning']")
    SearchNew=(By.XPATH,"//a[@class='btn btn-rounded btn-primary']")
    AdminSearch=(By.XPATH,"//button[@name='Search']")
    Usersearch=(By.XPATH,"//input[@class='form-control']")
    UserType=(By.XPATH,"//select[@class='form-control']")
    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)
        self.waitutility = WaitUtility()
        self.pageutility = PageUtility()

    def reset(self):
        #resetadmin=self.driver.find_element(By.XPATH,"//a[@class='btn btn-rounded btn-warning']")
        resetadmin=self.find(self.ResetAdmin)
        self.waitutility.wait_until_clickable(self.driver,resetadmin)
        resetadmin.click()
        self.pageutility.click_on_element(resetadmin)
        return self




    def admin_search(self):
        #adminsearch=self.driver.find_element(By.XPATH,"//button[@name='Search']")
        adminsearch=self.find(self.AdminSearch)
        self.pageutility.click_on_element(adminsearch)
        return self

    def usersearch(self,username):

        user_search=self.find(self.Usersearch)
        self.pageutility.send_data_to_element(user_search,username)
        return self

    def selectusertype(self):
        usertype=self.find(self.UserType)
        self.pageutility.select_data_with_value(usertype)
        return self
