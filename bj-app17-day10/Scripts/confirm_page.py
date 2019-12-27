# from selenium.webdriver.common.by import By
#
# from Base.getDriver import get_android_driver
# from Base.page import Page
#
# """调用各个页面确定方法正确性"""
#
# # 实例化统一入口类
# page = Page(get_android_driver("com.bjcsxq.chat.carfriend", ".module_main.activity.MainActivity"))
# # 首页-点击稍后更新
# page.get_home_page().click_after_btn()
# # 首页-点击我
# page.get_home_page().click_my_btn()
# # 个人中心-点击登录注册
# page.get_person_page().click_login_sigin_btn()
# # 登录页面-登录操作--登录失败
# page.get_login_page().login("13488834010", "159357")
# page.get_setting_page().get_toast("错误")
# # 登录页面-登录确认
# page.get_login_page().click_login_acc_btn()
# # 个人中心 -获取用户名
# print("用户名:{}".format(page.get_person_page().get_username()))
# # 个人中心-点击设置
# page.get_person_page().click_setting_btn()
# # 设置页面-退出操作
# page.get_setting_page().logout()

from Base.page import Page
from Base.getDriver import get_android_driver
from Base.getData import GetData

import pytest, os, sys

sys.path.append(os.getcwd())


def login_value():
    # 存储数据
    lis = []
    # 读数据
    data = GetData().get_yml_data("login.yml")
    print(data)
    # 组装数据
    for i in data.values():
        lis.append(tuple(i.values()))
    print(lis)
    return lis


# login_value()
class TestLogin:
    def setup_class(self):
        """初始化driver和统一入口类"""
        # 声明driver
        self.driver = get_android_driver("com.bjcsxq.chat.carfriend", ".module_main.activity.MainActivity")
        # 实例化统一入口
        self.page_obj = Page(self.driver)

    def teardown_class(self):
        """退出driver"""
        self.driver.quit()

    @pytest.fixture(autouse=True, scope="class")
    def goto_person(self):
        """进入未登录个人中心 -class"""
        # 点击稍后更新
        self.page_obj.get_home_page().click_after_btn()
        # 点击我的
        self.page_obj.get_home_page().click_my_btn()

    @pytest.fixture(autouse=True)
    def goto_login(self):
        """进入登录页面 function"""
        # 点击登录/注册
        self.page_obj.get_person_page().click_login_sigin_btn()

    @pytest.mark.parametrize("phone, passwd,mess,expData", [("18773201771", "123456", None, "用户"),
                                                            ("18773201773", "123456", "未注册", "账号还未注册，请您先进行注册户")])
    def test_login(self, phone, passwd, mess, expData):
        """测试方法"""
        # 登录操作
        self.page_obj.get_login_page().login(phone, passwd)
        # 判断用例走向
        if mess:
            """失败用例"""
            # 获取toast消息
            toast_message = self.page_obj.get_login_page().get_toast(mess)
            try:
                # 断言toast
                assert expData in toast_message
            except AssertionError:  # 断言失败异常
                # 截图
                self.page_obj.get_setting_page().screen_png("预期断言失败截图")
                # 抛出异常
                raise
            finally:
                self.page_obj.get_login_page().click_return_btn()
        else:
            """成功用例"""
            # 登录确认
            self.page_obj.get_login_page().click_login_acc_btn()
            # 取用户名
            username = self.page_obj.get_person_page().get_username()
            try:
                # 断言用户名
                assert expData in expData
            except AssertionError:
                # 截图
                self.page_obj.get_setting_page().screen_png("预期断言成功截图")
                # 抛出异常
                raise
            finally:
                # 点击设置
                self.page_obj.get_person_page().click_setting_btn()
                # 退出登录
                self.page_obj.get_setting_page().logout()


if __name__ == '__main__':
    pytest.main(["confirm_page.py"])
