import pytest
from selenium.webdriver.common.by import By

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
        """username=self.driver.find_element(By.XPATH,"//input[@placeholder='Username']")
        password=self.driver.find_element(By.XPATH,"//input[@placeholder='Password']")
        button=self.driver.find_element(By.XPATH,"//button[@type='submit']")
        username.send_keys(usernamevalue)
        password.send_keys(passwordvalue)
        button.click()"""
        logindetails=Loginpage(self.driver)
        logindetails.enterusername(usernamevalue).enterpassword(passwordvalue)
        #logindetails.enterpassword(passwordvalue)
        homepage=logindetails.signin()
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
        """username = self.driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        password = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        username.send_keys(usernamevalue)
        password.send_keys(passwordvalue)
        button.click()"""
        logindetails = Loginpage(self.driver)
        logindetails.enterusername(usernamevalue).enterpassword(passwordvalue).signin()
        #logindetails.enterpassword(passwordvalue)
        #logindetails.signin()
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
        """username = self.driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        password = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        username.send_keys(usernamevalue)
        password.send_keys(passwordvalue)
        button.click()"""
        logindetails = Loginpage(self.driver)
        logindetails.enterusername(usernamevalue).enterpassword(passwordvalue).signin()
        #logindetails.enterpassword(passwordvalue)
        #logindetails.signin()
        current = self.driver.current_url
        assert current == "https://groceryapp.uniqassosiates.com/admin/login"

    @pytest.mark.run(order=4)
    def test_invalidusernamepassword(self,browserinstance):
        self.driver = browserinstance
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.maximize_window()
        utility = ExcelUtility("C:\\Users\\Admin\\Desktop\\ProjectTestData.xlsx")
        usernamevalue = utility.get_string_data(5, 1, "LoginPage")
        passwordvalue = utility.get_string_data(5, 2, "LoginPage")
        """username = self.driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        password = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        username.send_keys(usernamevalue)
        password.send_keys(passwordvalue)
        button.click()"""
        logindetails = Loginpage(self.driver)
        logindetails.enterusername(usernamevalue).enterpassword(passwordvalue).signin()
        #logindetails.enterpassword(passwordvalue)
        #logindetails.signin()
        current = self.driver.current_url
        assert current == "https://groceryapp.uniqassosiates.com/admin/login"








