import time

from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Base_Capabilities.Find_Elements import FindElements
from Locators.LoginScreen_Locators import *


class TestLoginScreenA(FindElements):
    # --------------------- LOGIN FIELDS VERIFICATION SECTION ---------------------

    def get_login_username(self):
        user_mail = self.find_element_by_id(username_tf).get_attribute("text")
        return user_mail

    def get_login_password(self):
        user_password = self.find_element_by_id(password_tf).get_attribute("text")
        return user_password

    def enter_username(self, username):
        username_textbox = self.find_element_by_id(username_tf)
        if username_textbox.is_displayed():
            username_textbox.click()
            username_textbox.clear()
            username_textbox.send_keys(username)

    def clear_username(self):
        username_textbox = self.find_element_by_id(username_tf)
        if username_textbox.is_displayed():
            username_textbox.click()
            username_textbox.clear()

    def enter_password(self, password):
        password_textbox = self.find_element_by_id(password_tf)
        if password_textbox.is_displayed():
            password_textbox.click()
            password_textbox.clear()
            password_textbox.send_keys(password)

    def clear_password(self):
        password_textbox = self.find_element_by_id(password_tf)
        if password_textbox.is_displayed():
            password_textbox.click()
            password_textbox.clear()

    def verify_Login_Button(self):
        time.sleep(10)
        login_button = self.find_element_by_id(login_bt)
        assert login_button

    def click_Login_Button(self):
        time.sleep(10)
        login_button = self.find_element_by_id(login_bt)
        if login_button.is_displayed():
            login_button.click()
