from common import login
from common.config_value import config
from common import set_driver
from common.base_page import BasePage
from common.element_yaml_utills import ElementYamlData
# from common.element_data_utills import get_page_info
#
# elements = get_page_info('main_page')
elements = ElementYamlData('main_page').read_yaml()


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.company_show_box = elements['company_show_box']
        self.my_zone_menu = elements['my_zone_menu']
        self.product_menu = elements['product_menu']
        self.username_show_span = elements['username_show_span']
        self.logout_menu = elements['logout_menu']
        self.zentao_vaesion = elements['zentao_vaesion']
        self.forget_password_menu = elements['forget_password_menu']
        self.forget_password_original_password = elements['forget_password_original_password']
        self.forget_password_password1 = elements['forget_password_password1']
        self.forget_password_password2 = elements['forget_password_password2']
        self.forget_password_save_button = elements['forget_password_save_button']

    def get_company_name(self):
        value = self.get_attribute(self.company_show_box)
        return value

    def goto_myzone(self):
        self.click(self.my_zone_menu)

    def goto_product(self):
        self.click(self.product_menu)

    def get_user_name(self):
        text = self.get_text(self.username_show_span)
        return text

    def get_zentao_version(self):
        zantao_version = self.get_text(self.zentao_vaesion)
        return zantao_version

    def goto_forget_password(self):
        self.click(self.username_show_span)
        self.click(self.forget_password_menu)

    def change_password(self, original_password, password1, password2):
        self.switch_to_frame('iframe-triggerModal')
        self.input(self.forget_password_original_password, original_password)
        self.input(self.forget_password_password1, password1)
        self.input(self.forget_password_password2, password2)
        self.click(self.forget_password_save_button)
        self.switch_to_default_content()

    def logout(self):
        self.click(self.username_show_span)
        self.click(self.logout_menu)


if __name__ == '__main__':
    driver = set_driver.set_driver()
    login.test_login(config.zantao_url, config.user_name, config.password, driver)
    main_page = MainPage(driver)
    # 测试用例三：获取"我的公司"名称
    company_name = main_page.get_company_name()
    # 测试用例四：点击【我的地盘】
    main_page.goto_myzone()
    # 测试用例五：点击【项目】
    main_page.goto_product()
    # 测试用例六：获取用户名称文本信息
    username_text = main_page.get_user_name()
    # 测试用例七：获取禅道版本
    zantao_version = main_page.get_zentao_version()
    # 测试用例八：点击忘记密码
    main_page.goto_forget_password()
    # 测试用例九：修改密码
    main_page.change_password(config.password, config.password, config.password)
    # 测试用例十： 签退
    main_page.logout()
    driver.close()
