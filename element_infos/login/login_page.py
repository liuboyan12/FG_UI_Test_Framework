from common.base_page import BasePage
from common import login
from common.config_value import config
from common import set_driver
from common.element_yaml_utills import ElementYamlData
# from common.element_data_utills import get_page_info
from common.browser import Browser

# elements = get_page_info('login_page')
elements = ElementYamlData('login_page').read_yaml()


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input_box = elements['username_input_box']
        self.password_input_box = elements['password_input_box']
        self.login_button = elements['login_button']

    def input_username(self, username):  # 方法 == 》 控件的操作
        self.input(self.username_input_box, username)

    def input_password(self, password):
        self.input(self.password_input_box, password)

    def click_login(self):
        self.click(self.login_button)

    def get_login_fail_alert_content(self):
        return self.switch_to_alert()


if __name__ == '__main__':
    # driver = set_driver.set_driver()
    driver = Browser().get_driver()
    # 测试用例一：登录成功
    login.test_login(config.zantao_url, config.user_name, config.password, driver)
    driver.close()
    # 测试用例二：登录失败
    driver = set_driver.set_driver()
    login.test_login(config.zantao_url, config.user_name, (config.password + '1'), driver)
    driver.close()
