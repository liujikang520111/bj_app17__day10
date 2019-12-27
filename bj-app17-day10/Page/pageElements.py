from selenium.webdriver.common.by import By


class PageElements:
    """管理所有页面元素"""

    """首页"""
    # 稍后更新
    home_after_btn_id = (By.ID, "com.bjcsxq.chat.carfriend:id/bt_no")
    # 我的
    home_my_btn_id = (By.ID, "com.bjcsxq.chat.carfriend:id/tv_home_mine")

    """个人中心"""
    # 登录/注册按钮
    person_login_sigin_btn_xpath = (By.XPATH, "//*[contains(@text,'登录/注册')]")
    # 用户名
    person_user_name_id = (By.ID, "com.bjcsxq.chat.carfriend:id/mine_username_tv")
    # 设置
    person_setting_btn_id = (By.ID, "com.bjcsxq.chat.carfriend:id/mine_set_rl")

    """登录页面"""
    # 手机号
    login_phone_id = (By.ID, "com.bjcsxq.chat.carfriend:id/login_phone_et")
    # 密码
    login_passwd_id = (By.ID, "com.bjcsxq.chat.carfriend:id/login_pwd_et")
    # 登录按钮
    login_btn_id = (By.ID, "com.bjcsxq.chat.carfriend:id/login_btn")
    # 返回按钮
    login_return_btn_id = (By.ID, "com.bjcsxq.chat.carfriend:id/title_back")
    # 登录成功确认按钮
    login_suc_acc_btn_id = (By.ID, "com.bjcsxq.chat.carfriend:id/btn_neg")

    """设置页面"""
    # 退出按钮
    setting_logout_btn_id = (By.ID, "com.bjcsxq.chat.carfriend:id/set_logout_tv")
    # 确认退出
    setting_logout_acc_btn_id = (By.ID, "com.bjcsxq.chat.carfriend:id/bt_ok")
    # 取消退出
    setting_logout_dis_btn_id = (By.ID, "com.bjcsxq.chat.carfriend:id/bt_no")
