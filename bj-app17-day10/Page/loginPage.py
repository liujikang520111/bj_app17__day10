from Base.base import Base
from Page.pageElements import PageElements


class LoginPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def login(self, phone, passwd):
        """
        登录操作
        :param phone: 手机号
        :param passwd: 密码
        :return:
        """
        # 输入手机号
        self.send_ele(PageElements.login_phone_id, phone)
        # 输入密码
        self.send_ele(PageElements.login_passwd_id, passwd)
        # 点击登录
        self.click_ele(PageElements.login_btn_id)

    def click_login_acc_btn(self):
        """登录确认按钮"""
        self.click_ele(PageElements.login_suc_acc_btn_id)

    def click_return_btn(self):
        """登录返回按钮"""
        self.click_ele(PageElements.login_return_btn_id)
