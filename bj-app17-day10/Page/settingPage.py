from Base.base import Base
from Page.pageElements import PageElements


class SettingPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def logout(self, tag=1):
        """
        退出登录
        :param tag: 1:确认退出 2:取消退出
        :return:
        """
        # 点击退出按钮
        self.click_ele(PageElements.setting_logout_btn_id)
        # 判断
        if tag == 1:
            """确认退出"""
            self.click_ele(PageElements.setting_logout_acc_btn_id)
        if tag == 2:
            """取消退出"""
            self.click_ele(PageElements.setting_logout_dis_btn_id)
        # 向下滑动
        self.swipe_screen(tag=2)
