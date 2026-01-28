import pytest
from selenium.webdriver.common.by import By

from pages.Loginpage import Loginpage
from pages.Newspage import News
from utility.ExcelUtility import ExcelUtility


class Test_news:
    def test_returnhome(self,browserinstance):
        self.driver = browserinstance
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.maximize_window()
        utility = ExcelUtility("C:\\Users\\Admin\\Desktop\\ProjectTestData.xlsx")
        usernamevalue = utility.get_string_data(2, 1, "LoginPage")
        passwordvalue = utility.get_string_data(2, 2, "LoginPage")
        """username = self.driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        password = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        username.send_keys(usernamevalue)
        password.send_keys(passwordvalue)
        button.click()"""
        logindetails = Loginpage(self.driver)
        logindetails.enterusername(usernamevalue)
        logindetails.enterpassword(passwordvalue)
        logindetails.signin()
        newsinfo= News(self.driver)
        newsinfo.newsclick()
        newsinfo.homepage()
        """news=self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news' and @class='small-box-footer']")
        news.click()
        home=self.driver.find_element(By.XPATH,"//a[text()='Home']")
        home.click()"""

    @pytest.mark.parametrize("newsdata", ["Hello,Good Morning!","NewsToday!"])
    def test_addnews(self,browserinstance,newsdata):
        self.driver = browserinstance
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.maximize_window()
        utility = ExcelUtility("C:\\Users\\Admin\\Desktop\\ProjectTestData.xlsx")
        usernamevalue = utility.get_string_data(2, 1, "LoginPage")
        passwordvalue = utility.get_string_data(2, 2, "LoginPage")
        username = self.driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        password = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        username.send_keys(usernamevalue)
        password.send_keys(passwordvalue)
        button.click()
        news = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news' and @class='small-box-footer']")
        news.click()
        newinfo=self.driver.find_element(By.XPATH,"//a[@class='btn btn-rounded btn-danger']")
        newinfo.click()
        enter=self.driver.find_element(By.XPATH,"//textarea[@placeholder='Enter the news']")
        enter.send_keys(newsdata)
        save=self.driver.find_element(By.XPATH,"//button[@type='submit']")
        save.click()
        alert= self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']")
        alert_text=alert.text
        assert 'News Created Successfully' in alert_text

    #@pytest.mark.parametrize("AddingNews", ["Hello,Good Morning!", "NewsToday!"])
    def test_searchnews(self,browserinstance):
        self.driver = browserinstance
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.maximize_window()
        utility = ExcelUtility("C:\\Users\\Admin\\Desktop\\ProjectTestData.xlsx")
        usernamevalue = utility.get_string_data(2, 1, "LoginPage")
        passwordvalue = utility.get_string_data(2, 2, "LoginPage")
        username = self.driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        password = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        username.send_keys(usernamevalue)
        password.send_keys(passwordvalue)
        button.click()
        news = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news' and @class='small-box-footer']")
        news.click()
        searchnews=self.driver.find_element(By.XPATH,"//a[@class='btn btn-rounded btn-primary']")
        searchnews.click()
        enter = self.driver.find_element(By.XPATH, "//input[@class='form-control']")
        enter.send_keys("AddingNews")
        entersearch=self.driver.find_element(By.XPATH,"//button[@class='btn btn-danger btn-fix']")
        entersearch.click()
        table_info=self.driver.find_element(By.XPATH,"//table[@class='table table-bordered table-hover table-sm']/tbody/tr[1]/td[1]")
        table=table_info.text
        assert 'AddingNews' in table

