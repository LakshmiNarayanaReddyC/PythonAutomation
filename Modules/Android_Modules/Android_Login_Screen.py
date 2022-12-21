from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import WebDriverException, NoSuchAttributeException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
import time
from Base_Capabilities.Fetch_Desired_Capabilities import Fetch_Desired_Capabilities
from Locators.LoginScreen_Locators import *


class LoginScreen:

    def __init__(self, driver):
        self.driver = driver
        self.text = Fetch_Desired_Capabilities()

    # --------------------- LOGIN FIELDS VERIFICATION CODE SECTION ---------------------

    # Verify ConnectedControls App text
    def verify_LoginScreenHeader(self):

        try:
            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((AppiumBy.ID, AppName_id)))
            installapp = self.driver.find_element(AppiumBy.ID, AppName_id)
            installertext = installapp.get_attribute("text")
            assert installertext == "ConnectedControls"
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def verify_username_placeholder(self):
        try:
            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((AppiumBy.ID, UserName_id)))
            username = self.driver.find_element(AppiumBy.ID, UserName_id)
            username.clear()
            usertext = username.get_attribute("text")
            assert usertext == "Enter Email ID"
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def verify_password_placeholder(self):
        try:
            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((AppiumBy.ID, Password_id)))
            password = self.driver.find_element(AppiumBy.ID, Password_id)
            password.clear()
            pwdtext = password.get_attribute("text")
            assert pwdtext == "Enter Password"
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def enter_username(self, enterusername):
        try:
            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((AppiumBy.ID, UserName_id)))
            username_textbox = self.driver.find_element(AppiumBy.ID, UserName_id)
            username_textbox.click()
            username_textbox.clear()
            username_textbox.send_keys(enterusername)
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def enter_password(self, enterpassword):
        try:

            self.driver.hide_keyboard()
            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((AppiumBy.ID, Password_id)))
            password_textbox = self.driver.find_element(AppiumBy.ID, Password_id)
            password_textbox.click()
            password_textbox.clear()
            password_textbox.send_keys(enterpassword)
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def verify_Loginbuttonlabel(self):
        try:
            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((AppiumBy.ID, Login_id)))
            loginbtn = self.driver.find_element(AppiumBy.ID, Login_id)
            loginbtntext = loginbtn.get_attribute("text")
            assert loginbtntext == "Login"
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def click_Login_Button(self):
        try:
            self.driver.hide_keyboard()
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((AppiumBy.ID, Login_id)))
            login_btn = self.driver.find_element(AppiumBy.ID, Login_id)
            login_btn.click()
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    # --------------------- ERROR MESSAGE VERIFICATION CODE SECTION ---------------------
    def get_username_error_message(self):
        try:

            WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located((AppiumBy.ID, android_email_input_error)))
            usererr_msg = self.driver.find_element(AppiumBy.ID, android_email_input_error).get_attribute("text")
            return usererr_msg
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def clear_password(self):
        try:
            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((AppiumBy.ID, Password_id)))
            password = self.driver.find_element(AppiumBy.ID, Password_id)
            password.click()
            password.clear()
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def get_password_error_message(self):
        try:

            WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located((AppiumBy.ID, android_password_input_error)))
            passworderr_msg = self.driver.find_element(AppiumBy.ID, android_password_input_error).get_attribute("text")
            return passworderr_msg
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def click_MenuIcon(self):

        try:
            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((AppiumBy.ID, hamburg_id)))
            menu_icon = self.driver.find_element(AppiumBy.ID, hamburg_id)
            menu_icon.click()
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def click_logout(self):
        try:
            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((AppiumBy.ID, logout_id)))
            logout = self.driver.find_element(AppiumBy.ID, logout_id)
            logout.click()
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def click_Ok_Button(self):
        try:
            self.driver.hide_keyboard()
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((AppiumBy.ID, ok_btn)))
            okay_btn = self.driver.find_element(AppiumBy.ID, ok_btn)
            okay_btn.click()
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE
