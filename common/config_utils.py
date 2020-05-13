# @Time : 2020/4/29 20:24 

# @Author : Aliun.Liu

# @File : config_utils.py 

# @Software: PyCharm

import os
import configparser


class ConfigUtils(object):
    def __init__(self, conf_path='../conf/local_config.ini'):
        self.current_path = os.path.dirname(__file__)
        self.conf_path = os.path.join(self.current_path, conf_path)
        self.conf = configparser.ConfigParser()
        self.conf_data = self.conf.read(self.conf_path, encoding='utf-8')

    @property
    def url(self):
        return self.conf.get("default", "url")

    @property
    def driver_path(self):
        return self.conf.get("default", "driver_path")

    @property
    def driver_name(self):
        return self.conf.get("default", "dirver_name")

    @property
    def time_out(self):
        return self.conf.get("default", "time_out")

    @property
    def element_info_path(self):
        return self.conf.get('default', 'element_info_path')

    @property
    def screenshot_path(self):
        return self.conf.get("default", "screen_shot_path")

    @property
    def default_username(self):
        return self.conf.get('default', 'user_name')

    @property
    def default_password(self):
        return self.conf.get('default', 'password')

    @property
    def log_path(self):
        return self.conf.get('default', 'log_path')

    @property
    def log_level(self):
        return self.conf.get('default', 'log_level')

    @property
    def testdata_path(self):
        return self.conf.get('default', 'testdata_path')

    @property
    def report_path(self):
        return self.conf.get('default', 'report_path')

    @property
    def case_path(self):
        return self.conf.get('default', 'case_path')

    @property
    def smtp_server(self):
        return self.conf.get('email', 'smtp_server')

    @property
    def smtp_sender(self):
        return self.conf.get('email', 'smtp_sender')

    @property
    def smtp_senderpassword(self):
        return self.conf.get('email', 'smtp_senderpassword')

    @property
    def smtp_receiver(self):
        return self.conf.get('email', 'smtp_receiver')

    @property
    def smtp_cc(self):
        return self.conf.get('email', 'smtp_cc')


local_config = ConfigUtils()

if __name__ == '__main__':
    config = ConfigUtils()
    zantao_url = config.url
    chrome_path = config.driver_path
    print(zantao_url, chrome_path)
