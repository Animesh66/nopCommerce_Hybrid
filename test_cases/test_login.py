# this testcase will perform the login functionality testing
# filename should always start with test as pytest have this naming convention
from selenium import webdriver
import time
import pytest
from page_object.login_page import LoginNopCommerce



class TestTC001Login:
    base_url = "https://admin-demo.nopcommerce.com"
    email = "admin@yourstore.com"
    password = "admin"

    def test_homepage_title(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
        else:
            assert False
        self.driver.close()

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
            assert True
        else:
            assert False
        self.driver.close()