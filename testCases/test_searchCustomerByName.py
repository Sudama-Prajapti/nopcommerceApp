
import time

import pytest

from pageObjects.Login_Page import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.SearchCustomerPage import SearchCustomer



class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()#logger

    @pytest.mark.regression
    def test_SearchCustomerByName(self,setup):
        self.logger.info("******** Test_SearchCustomerByName_005 ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* Login succesful *********")

        self.logger.info("******* Starting Search customer By Name ********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomers_Menu()
        self.addcust.clickonCustomersMenuItem()

        self.logger.info("********* Searching customer By Name Id ******")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Arthur")
        searchcust.setLastName("Holmes")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.SearchCustomerByName("Arthur Holmes")
        assert True ==status

        self.logger.info("********** TC_SearchCustomerBy_Name_005 Fineshed ********** ")
        self.driver.close()


