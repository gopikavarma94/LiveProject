import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.Adminpage import Admin
from pages.Loginpage import Loginpage
from utility.ExcelUtility import ExcelUtility


class Test_adminusers:
    @pytest.mark.timeout(3)
    def test_reset(self,browserinstance):
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
        admininfo=home.adminuser()
        #admininfo=Admin(self.driver)
        admininfo.reset()
        """adminuser=self.driver.find_element(By.XPATH,"//i[@class='fas fa-arrow-circle-right']")
        adminuser.click()
        reset=self.driver.find_element(By.XPATH,"//a[@class='btn btn-rounded btn-warning']")
        reset.click()"""


    def test_adminsearch(self, browserinstance):
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
        #admin=Admin(self.driver)
        admin=home.adminuser()
        admin.admin_search().usersearch("Chloe").selectusertype()




        """adminuser = self.driver.find_element(By.XPATH, "//i[@class='fas fa-arrow-circle-right']")
        adminuser.click()
        search=self.driver.find_element(By.XPATH,"//a[@class='btn btn-rounded btn-primary']")
        search.click()"""
        """username1=self.driver.find_element(By.XPATH,"//input[@class='form-control']")
        username1.send_keys("Chloe")
        usertype=self.driver.find_element(By.XPATH,"//select[@class='form-control']")
        select=Select(usertype)
        select.select_by_index(2)
        searchadmin=self.driver.find_element(By.XPATH,"//button[@name='Search']")
        searchadmin.click()"""
        user_search=self.driver.find_element(By.XPATH,"//table[@class='table table-bordered table-hover table-sm']/tbody/tr[1]/td[1]")
        user_info=user_search.text
        assert 'Chloe' in user_info



