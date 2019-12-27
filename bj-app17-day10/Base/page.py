from Page.homePage import HomePage
from Page.personPage import PersonPage
from Page.loginPage import LoginPage
from Page.settingPage import SettingPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    def get_home_page(self):
        """返回首页对象"""
        return HomePage(self.driver)

    def get_person_page(self):
        """返回个人中心对象"""
        return PersonPage(self.driver)

    def get_login_page(self):
        """返回登录对象"""
        return LoginPage(self.driver)

    def get_setting_page(self):
        """返回设置对象"""
        return SettingPage(self.driver)
