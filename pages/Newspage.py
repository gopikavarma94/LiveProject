from selenium.webdriver.common.by import By

from pages.Basepage import BasePage
from pages.Homepage import Homepage
from utility.PageUtility import PageUtility
from utility.WaitUtility import WaitUtility


class News(BasePage):
    ReturnHome=(By.XPATH,"//a[text()='Home']")
    Addnews=(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news' and @class='small-box-footer']")

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.waitutility = WaitUtility()
        self.pageutility = PageUtility()



    def newssearch(self):
        #searchnew=self.driver.find_element(By.XPATH,"//a[@class='btn btn-rounded btn-primary']")
        searchnew=self.find(self.SearchNew)
        self.pageutility.click_on_element(searchnew)
        return self

    def homepage(self):
        home = self.find(self.ReturnHome)
        home.click()
        return Homepage(self.driver)