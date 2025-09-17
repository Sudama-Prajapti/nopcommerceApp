import pytest
from selenium import webdriver
from pageObjects.Login_Page import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger  import LogGen


class Test_001_Login:
    # baseURL = "https://admin-demo.nopcommerce.com/"
    baseURL = ReadConfig.getApplicationURL()
    # username = "admin@yourstore.com"
    username = ReadConfig.getUsername()
    # password = "admin"
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    @pytest.mark.regression

    def test_homePageTitle(self, setup):
        self.logger.info("******************Test_001_Login*********************")
        self.logger.info("******************veryfiyin home page Title*********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "nopCommerce demo store. Login": #Example +Login123
            assert True
            self.driver.quit()
            self.logger.info("****************** home page Title test pass *********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png") #screenshots Folder .\\ insite the project folder
            self.driver.quit()
            self.logger.info("****************** home page Title filed*********************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("******************veryfiyin the login test*********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.quit()
            self.logger.info("****************** Login test is passed*********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png") #screenshots Folder .\\ insite the project folder Test Failears
            self.driver.quit()
            self.logger.error("****************** Login test is Failed*********************")
            assert False


