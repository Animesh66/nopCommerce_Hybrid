# this testcase will perform the login functionality testing
# filename should always start with test as pytest have this naming convention
from page_object.login_page import LoginNopCommerce
from selenium import webdriver
import pytest


class TestTC001Login:
    base_url = "https://admin-demo.nopcommerce.com"
    email = "admin@yourstore.com"
    password = "admin"

    def test_homepage_title(self):
        self.driver = webdriver.Chrome()
        # self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        if actual_title == "Your store. Login123":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("./screenshots/test_homepage_title.png")  # this is the path and screenshot name
            self.driver.close()
            assert False

    def test_login(self):
        # self.driver = setup
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.login = LoginNopCommerce(self.driver)
        self.login.set_email(self.email)
        self.login.set_password(self.password)
        self.login.click_login()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration123":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("./screenshots/screenshotstest_login.png")  # this is the path and screenshot name
            self.driver.close()
            assert False
