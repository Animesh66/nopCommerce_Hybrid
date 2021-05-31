# this testcase will perform the login functionality testing
# filename should always start with test as pytest have this naming convention
from page_object.login_page import LoginNopCommerce
from test_cases.config_test import setup
from utilities.read_properties import ReadConfig
from utilities.cutom_logger import LogGeneration

class TestTC001Login:
    base_url = ReadConfig.get_application_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()
    logger = LogGeneration.log_generation()

    def test_homepage_title(self, setup):
        self.logger.info("************* TestTC001Login ************* ")  # this will be the heading of the logfile
        self.logger.info("************* Verify Home Page Title ************* ")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************* Home Page title test is passed ************* ")
        else:
            assert False
            self.driver.save_screenshot("./screenshots/test_homepage_title.png")  # this is the path and screenshot name
            self.driver.close()
            self.logger.error("************* Home Page title test is failed ************* ")

    def test_login(self, setup):
        self.logger.info("************* Verify Login Test ************* ")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.login = LoginNopCommerce(self.driver)
        self.login.set_email(self.email)
        self.login.set_password(self.password)
        self.login.click_login()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            self.logger.info("************* Login Test is passed ************* ")
            assert True
            self.driver.close()
        else:
            self.logger.error("************* Login Test is failer ************* ")
            assert False
            self.driver.save_screenshot("./screenshots/screenshotstest_login.png")  # this is the path and screenshot name
            self.driver.close()
