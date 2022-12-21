import time

from Base_Capabilities.Driver_Initialization import *
from Modules.Android_Modules.Android_Login_Screen import LoginScreen
from Test_Cases.Credentials import *


class TestLoginValidation:
    login = LoginScreen(driver)

    def setup_module(self, module):
        self.driver = driver

    # Verify the Email and Password Field placeholders
    def test_LoginVerification01(self):
        self.login.verify_LoginScreenHeader()
        self.login.verify_username_placeholder()
        self.login.verify_password_placeholder()

    # Verify the error message when user click on login button by providing invalid email and valid password
    def test_LoginVerification02(self):
        self.login.enter_username(invalidUser)
        self.login.click_Login_Button()
        assert self.login.get_username_error_message() == "Please valid email address"

    # Verify the error message when user click on login button by providing valid email and invalid password
    def test_LoginVerification03(self):
        self.login.enter_username(valid_username)
        self.login.clear_password()
        self.login.click_Login_Button()
        assert self.login.get_password_error_message() == "Please enter password"

    # Verify the Login components states
    def test_LoginVerification04(self):
        self.login.enter_username(valid_username)
        self.login.enter_password(valid_password)

    # Verify the  Login button label
    def test_LoginVerification05(self):
        self.login.verify_Loginbuttonlabel()
        self.login.click_Login_Button()

    # Verify the Logout button label
    def test_LogoutVerification06(self):
        time.sleep(15)
        self.login.click_MenuIcon()
        self.login.click_logout()
        self.login.click_Ok_Button()

    # Terminate the Application
    def test_LoginVerification07(self):
        driver.terminate_app("com.connectedcontrols.ccdev")
        driver.launch_app()
        self.login.verify_LoginScreenHeader()
