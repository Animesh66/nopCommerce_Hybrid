# this testcase will perform the login functionality testing
# filename should always start with test as pytest have this naming convention
import time
from page_object.login_page import LoginNopCommerce
from test_cases.config_test import setup
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGeneration
import utilities.excel_utiles as xl


# this is data driven test case where data is fed from excel sheet
class TestTC002DDTLogin:
    data_excel_path = "./test_data/Data_Driven_TC_Selenium.xlsx"
    base_url = ReadConfig.get_application_url()
    logger = LogGeneration.log_generation()

    def test_login(self, setup):
        self.logger.info("************* TestTC002DDTLogin ************* ")
        self.logger.info("************* Verify Login Test ************* ")
        self.driver = setup()
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.login = LoginNopCommerce(self.driver)
        self.row_count = xl.get_row_count(self.data_excel_path, "Sheet1")
        list_status = []  # empty list created
        for r_count in range(2, self.row_count + 1):
            self.email = xl.read_data(self.data_excel_path, "Sheet1", r_count, 1)
            self.password = xl.read_data(self.data_excel_path, "Sheet1", r_count, 2)
            self.expected_result = xl.read_data(self.data_excel_path, "Sheet1", r_count, 3)
            self.login.set_email(self.email)
            self.login.set_password(self.password)
            self.login.click_login()
            time.sleep(3)
            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"
            if actual_title == expected_title:
                if self.expected_result == "Pass":
                    self.logger.info("************* Valid login attempt ************* ")
                    self.login.click_logout()
                    list_status.append("Pass")
                    time.sleep(3)
                elif self.expected_result == "Fail":
                    self.logger.info("************* Valid login attempt ************* ")
                    self.login.click_logout()
                    list_status.append("Fail")
                    time.sleep(3)
            elif actual_title != expected_title:
                if self.expected_result == "Pass":
                    self.logger.info("************* Invalid login attempt ************* ")
                    self.login.click_logout()
                    list_status.append("fail")
                    time.sleep(3)
                elif self.expected_result == "Fail":
                    self.logger.info("************* Invalid login attempt ************* ")
                    self.login.click_logout()
                    list_status.append("Pass")
                    time.sleep(3)

            if "Fail" not in list_status:
                self.logger.info("DDT test case is passed")
                assert True
                self.driver.close()
            else:
                self.logger.info("DDT test case is failed")
                assert False
                self.driver.close()



