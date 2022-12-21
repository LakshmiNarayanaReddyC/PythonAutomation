from appium.webdriver.appium_service import AppiumService
import subprocess


class AppiumServerManager:

    def __init__(self):
        self.appium = ""

    def startAppium(self):
        self.appium = subprocess.Popen('appium')
        return self.appium

    def stop_appium(self):
        self.appium.terminate()
