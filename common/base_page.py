import time, os
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from common.log_utils import LogUtils
from common.config_utils import local_config
from selenium.webdriver.support import expected_conditions as EC
from common import HTMLTestReportCN

current_dir = os.path.dirname(__file__)


class BasePage:

    def __init__(self, driver):
        self.logger = LogUtils.get_log()
        self.driver = webdriver.Chrome()
        # self.driver = driver

    # 浏览器操作封装  -->  二次封装
    def open_url(self, url):
        self.driver.get(url)
        self.logger.info('打开url地址：%s' % url)

    def set_browser_max(self):
        self.driver.maximize_window()
        self.logger.info('浏览器最大化')

    def set_browser_min(self):
        self.driver.minimize_window()
        self.logger.info('浏览器最小化')

    def refresh(self):
        self.driver.refresh()
        self.logger.info('浏览器刷新')

    def get_title(self, title):
        value = self.driver.title.text
        self.logger.info('获取元素名称:%s' % value)

    def close_tab(self):
        self.driver.close()
        self.logger.info('table页关闭')

    def exit_driver(self):
        self.driver.quit()
        self.logger.info('退出浏览器')

    '''self.username_input_box = {'element_name': '用户名输入框','locator_type': 'XPATH',
    'locator_value': '//input[@name="account"]','timeout': 3}'''

    def find_element(self, element_info):
        try:
            locator_element_name = element_info['element_name']
            locator_type_name = element_info['locator_type']
            locator_value_info = element_info['locator_value']
            locator_timeout = element_info['timeout']

            if locator_type_name == 'id':
                locator_type = By.ID
            elif locator_type_name == 'CLASS_NAME':
                locator_type = By.CLASS_NAME
            elif locator_type_name == 'XPATH':
                locator_type = By.XPATH

            elment = WebDriverWait(self.driver, int(locator_timeout)) \
                .until(lambda x: x.find_element(locator_type, locator_value_info))
            self.logger.info('%s：  元素识别成功' % locator_element_name)
            # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'kw')))
        except Exception as e:
            self.logger.error('[%s]元素不能识别，原因是%s' % (element_info['element_name'], e.__str__()))
            self.screenshot_as_file()
        return elment

    # frame跳转封装
    def switch_to_frame(self, **element_dict):
        if 'id' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['id'])
        elif 'name' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['name'])
        elif 'element' in element_dict.keys():
            element = self.driver.find_element(element_dict['element'])
            self.driver.switch_to.frame(element)

    # selenium执行js
    def delete_element_attribute(self, element_info, attribute_name):
        element = self.find_element(element_info)
        # self.driver.execute_script('arguments[0].removeAttribute("%s");' % attribute_name, element)
        self.excute_script('arguments[0].removeAttribute("%s");' % attribute_name, element)

    def update_element_attribute(self, element_info, attribute_name, attribute_value):
        element = self.find_element(element_info)
        # self.driver.execute_script('arguments[0].setAttribute("%s","%s");' % (attribute_name, attribute_value), element)
        self.excute_script('arguments[0].setAttribute("%s","%s");' % (attribute_name, attribute_value), element)

    # 综合js执行
    def excute_script(self, js_str, element_info=None):
        if element_info:
            self.driver.execute_script(js_str)
        else:
            self.driver.execute_script(js_str, None)

    # 点击
    def click(self, element_info):
        self.find_element(element_info).click()
        self.logger.info('%s：  点击操作成功' % element_info['element_name'])

    # 输入内容
    def input(self, element_info, content):
        self.find_element(element_info).send_keys(content)
        self.logger.info('%s：  输入内容【%s】' % (element_info['element_name'], content))

    # 获取属性值
    def get_attribute(self, element_info):
        value = self.find_element(element_info).get_attribute('title')
        self.logger.info('%s：  属性值为【%s】' % (element_info['element_name'], value))

    # 获取文本信息
    def get_text(self, element_info):
        text = self.find_element(element_info).text
        self.logger.info('%s：  对象的文本信息为【%s】' % (element_info['element_name'], text))

    # 跳转到frame
    def switch_to_frame(self, frame):
        self.driver.switch_to.frame(frame)
        time.sleep(2)

    # 跳转到默认内容
    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
        time.sleep(2)

    # 跳转到弹框
    def switch_to_alert(self, action='accept', time_out=local_config.time_out):
        WebDriverWait(self.driver, time_out).until(EC.alert_is_persent())
        alter = self.driver.switch_to.alert()
        alter_text = alter.text
        if action == 'accept':
            alter.accept()
        elif action == 'dismiss':
            alter.dismiss()
        return alter_text

    # 普通等待
    def wait(self, seconds=local_config.time_out):
        time.sleep(seconds)
        self.logger.info('等待时间' + str(seconds) + '秒(s)')

    # 隐式等待
    def implicitly_wait(self, seconds=local_config.time_out):
        self.driver.implicitly_wait(seconds)
        self.logger.info('隐式等待时间为%s' % (seconds))

    # 鼠标操作封装
    def move_to_element_by_mouse(self, element_info):
        element = self.find_element(element_info)
        ActionChains(self.driver).move_to_element(element).perform()

    def long_press_elemnt(self, element_info, seconds):
        element = self.find_element(element_info)
        ActionChains(self.driver).click_and_hold(element).pause(seconds).release().perform()

    # 截图处理
    def screenshot_as_file(self, *screenshot_path):
        if len(screenshot_path) == 0:
            screenshot_filepath = local_config.screenshot_path
        else:
            screenshot_filepath = screenshot_path[0]
        now = time.strftime('%Y_%m_%d_%H_%M_%S')
        screenshot_filepath = os.path.join(current_dir, screenshot_filepath, 'UITest_%s.png' % now)
        self.driver.get_screenshot_as_file(screenshot_filepath)

    def screenshot_as_file_in_report_page(self):
        report_path = os.path.join(os.path.dirname(__file__), '..', local_config.report_path)
        report_dir = HTMLTestReportCN.ReportDirectory(report_path)
        report_dir.get_screenshot(self.driver)

    # 获取windows句柄
    def get_window_handle(self):
        return self.driver.current_window_handle

    # 跳转到句柄
    def switch_to_window_by_handle(self, window_handle):
        self.driver.switch_to.window(window_handle)
