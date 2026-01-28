from selenium.webdriver.common.by import By

from pages.Adminpage import Admin
from pages.Basepage import BasePage
from pages.Loginpage import Loginpage
from pages.Newspage import News
from utility.PageUtility import PageUtility
from utility.WaitUtility import WaitUtility


class Homepage(BasePage):
    Admin=(By.XPATH,"//a[@data-toggle='dropdown']")
    Signout=(By.XPATH,"//i[@class='ace-icon fa fa-power-off']")
    Adminusers=(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']")
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.waitutility = WaitUtility()
        self.pageutility = PageUtility()
    def clickadmin(self):
        admin = self.find(self.Admin)
        self.waitutility.wait_until_clickable(self.driver,admin)
        #admin.click()
        self.pageutility.click_on_element(admin)
        return self
    def clicksignout(self):
        signout = self.find(self.Signout)
        #signout.click()
        self.pageutility.click_on_element(signout)
        return Loginpage(self.driver)

    def adminuser(self):
        # adminusersbutton = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']")
        adminusersbutton = self.driver.find(self.Adminusers)
        adminusersbutton.click()
        return Admin(self.driver)

    def newsclick(self):
        news = self.find(self.Addnews)
        self.waitutility.wait_until_clickable(self.driver,news)
        news.click()
        self.pageutility.click_on_element(news)
        return News(self.driver)

