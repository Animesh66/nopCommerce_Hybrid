# this testcase will perform the login functionality testing
from selenium import webdriver
import time
import pytest
from page_object.login_page import LoginNopCommerce

class TestTC001Login:
  base_url = "https://admin-demo.nopcommerce.com"
  email = "admin@yourstore.com"
  password = "admin"



