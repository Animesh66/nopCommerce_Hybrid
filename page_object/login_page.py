from selenium import webdriver

class LoginNopCommerce:
    # identify all the locators in the page class
    username_textbox_id = "Email"
    password_textbox_id = "Password"
    logout_link_xpath = "//a[contains(text(),'Logout')]"

    def __init__(self, driver):  # constructor initiated
        self.driver = driver

    # initiate all action method
    def set_username(self,username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def set_password(self,password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.password_textbox_id).submit()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()
