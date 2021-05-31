# this testcase will perform the login functionality testing
# filename should always start with test as pytest have this naming convention
from page_object.login_page import LoginNopCommerce
from test_cases.config_test import setup
from utilities.read_properties import ReadConfig

class TestTC001Login:
    base_url = ReadConfig.get_application_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_homepage_title(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("./screenshots/test_homepage_title.png")  # this is the path and screenshot name
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.login = LoginNopCommerce(self.driver)
        self.login.set_email(self.email)
        self.login.set_password(self.password)
        self.login.click_login()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("./screenshots/screenshotstest_login.png")  # this is the path and screenshot name
            self.driver.close()
            assert False
