# @Time : 2020/4/29 20:27 

# @Author : Aliun.Liu

# @File : browser.py 

# @Software: PyCharm

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from common.config_utils import local_config

current_path = os.path.abspath(os.path.dirname(__file__))
dri_path = os.path.join(current_path, local_config.driver_path)


class Browser(object):
    def __init__(self, driver_path=dri_path, driver_name=local_config.driver_name):
        self.driver_path = driver_path
        self.driver_name = driver_name

    def get_driver(self):
        if self.driver_name.lower() == 'chrome':
            return self.__get_chrome_driver()
        elif self.driver_name.lower() == 'firefox':
            return self.__get_firefox_driver()
        elif self.driver_name.lower() == 'edge':
            return self.__get_edge_driver()

    def __get_chrome_driver(self):
        chrome_options = Options()
        # 差options代码
        chrome_options.add_argument('')
        chrome_driver_path = os.path.join(self.driver_path, 'chromedriver')
        driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver_path)
        return driver

    def __get_firefox_driver(self):
        firefox_options = Options()
        firefox_driver_path = os.path.join(self.driver_path, 'geckodriver')
        driver = webdriver.Chrome(options=firefox_options, executable_path=firefox_driver_path)
        return driver

    def __get_edge_driver(self):
        firefox_options = Options()
        firefox_driver_path = os.path.join(self.driver_path, 'Microsoftdriver')
        driver = webdriver.Chrome(options=firefox_options, executable_path=firefox_driver_path)
        return driver

    def __get_remote_driver(self):  # selenium支持分布式 grid通过配置别人电脑的浏览器进行分布式调用
        pass
