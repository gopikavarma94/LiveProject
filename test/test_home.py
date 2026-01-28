import pytest
from selenium.webdriver.common.by import By

from pages.Homepage import Homepage
from pages.Loginpage import Loginpage
from utility.ExcelUtility import ExcelUtility


class Test_home:
    @pytest.mark.regression
    def test_logout(self,browserinstance):
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
        logindetails.enterusername(usernamevalue).enterpassword(passwordvalue)
        #logindetails.enterpassword(passwordvalue)
        home=logindetails.signin()
        #home=Homepage(self.driver)
        home.clickadmin().clicksignout()
        #home.clicksignout()
        """admin=self.driver.find_element(By.XPATH,"//a[@data-toggle='dropdown']")
        signout=self.driver.find_element(By.XPATH,"//i[@class='ace-icon fa fa-power-off']")
        admin.click()
        signout.click()"""
