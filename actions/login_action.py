# @Time : 2020/5/5 11:07 

# @Author : Aliun.Liu

# @File : login_action.py 

# @Software: PyCharm

# from element_infos.login.


from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage
from common.config_utils import local_config


class LoginAction:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        # self.main_page = MainPage(driver)

    def login_action(self, username, password):
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login()

    def login_success(self, username, password):
        self.login_action(username, password)
        return MainPage(self.login_page.dr)

    def login_fail(self, username, password):
        self.login_action(username, password)
        return self.login_page.get_login_fail_alert_content()

    def default_login(self):
        return self.login_success(local_config.default_username, local_config.default_password)

    def login_by_cookie(self):
        pass
