#Write a pytest script for login functionality using Selenium
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.Loginpage import Loginpage
from utility.ExcelUtility import ExcelUtility
class Test_login:
    @pytest.mark.run(order=1)
    def test_validlogin(self,crossbrowser):
        self.driver=crossbrowser
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.maximize_window()
        utility= ExcelUtility("C:\\Users\\Admin\\Desktop\\ProjectTestData.xlsx")
        usernamevalue=utility.get_string_data(2,1,"LoginPage")
        passwordvalue=utility.get_string_data(2,2,"LoginPage")
        logindetails=Loginpage(self.driver)
        logindetails.enterusername(usernamevalue)
        logindetails.enterpassword(passwordvalue)
        logindetails.signin()
        current=self.driver.current_url
        assert current=="https://groceryapp.uniqassosiates.com/admin"

    @pytest.mark.run(order=2)
    def test_invalidusername(self,browserinstance):
        self.driver = browserinstance
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.maximize_window()
        utility = ExcelUtility("C:\\Users\\Admin\\Desktop\\ProjectTestData.xlsx")
        usernamevalue = utility.get_string_data(4, 1, "LoginPage")
        passwordvalue = utility.get_string_data(4, 2, "LoginPage")
        logindetails = Loginpage(self.driver)
        logindetails.enterusername(usernamevalue)
        logindetails.enterpassword(passwordvalue)
        logindetails.signin()
        current = self.driver.current_url
        assert current =="https://groceryapp.uniqassosiates.com/admin/login"

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("rowdata",[3,4,5,6])
    def test_invalidpassword(self,browserinstance,rowdata):
        self.driver = browserinstance
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.maximize_window()
        utility = ExcelUtility("C:\\Users\\Admin\\Desktop\\ProjectTestData.xlsx")
        usernamevalue = utility.get_string_data(rowdata, 1, "LoginPage")
        passwordvalue = utility.get_string_data(rowdata, 2, "LoginPage")
        logindetails = Loginpage(self.driver)
        logindetails.enterusername(usernamevalue)
        logindetails.enterpassword(passwordvalue)
        logindetails.signin()
        current = self.driver.current_url
        assert current == "https://groceryapp.uniqassosiates.com/admin/login"


