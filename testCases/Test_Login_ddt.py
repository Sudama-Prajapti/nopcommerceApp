import pytest

from pageObjects.Login_Page import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/logindata.xlsx"
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("*********** Test_002_DDT_Login ********")
        self.logger.info("*********** Verifying DDT Login Test ********")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows in Excel:", self.rows)

        lst_status = []   # collect Pass/Fail status

        # start from 2, because row 1 is usually header
        for r in range(2, self.rows + 1):
            self.username = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            # -------- Positive Test Case --------
            if act_title == exp_title:
                if self.exp.lower() == "pass":
                    self.logger.info(f"[POSITIVE] Passed  for user: {self.username}")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp.lower() == "fail":
                    self.logger.info(f"[NEGATIVE] Failed  for user: {self.username} "
                                     f"(Expected Fail, but Login Successful)")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            # -------- Negative Test Case --------
            else:  # login failed
                if self.exp.lower() == "pass":
                    self.logger.info(f"[POSITIVE] Failed for user: {self.username} "
                                     f"(Expected Pass, but Login Failed)")
                    lst_status.append("Fail")
                elif self.exp.lower() == "fail":
                    self.logger.info(f"[NEGATIVE] Passed for user: {self.username} "
                                     f"(Expected Fail, and Login Failed)")
                    lst_status.append("Pass")

        # -------- Final Result --------
        if "Fail" not in lst_status:
            self.logger.info("====> DDT Login Test PASSED <====")
            self.driver.close()
            assert True
        else:
            self.logger.info("====> DDT Login Test FAILED <====")
            self.driver.close()
            assert False

        self.logger.info("*********** Completed TC_LoginDDT_002 ***********")
