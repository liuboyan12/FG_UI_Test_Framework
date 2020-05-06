# encoding:utf-8
# @Time: 2020/5/5 16:48 
# @Author: Aliun.Liu
# @File: log_utils.py 
# @Software: PyCharm
# @desc:
import os
import time

import logging
from common.config_utils import local_config


class LogUtils:
    # def __init__(self, log_file_path=os.path.join(os.path.dirname(__file__), '../', local_config.log_path)):
    # self.log_file_path = log_file_path
    # self.logger = logging.getLogger(__name__)  # 创建一个日志对象 定义一个名词
    # self.logger.setLevel(level=logging.INFO)  # 设置全局日志基本  debug info worning error
    # console = logging.StreamHandler()  # 创建一个控制台输出日志的对象
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # console.se?tFormatter(formatter)
    # file_log = logging.FileHandler(self.log_file_path, 'a', encoding='utf-8')
    # file_log.setFormatter(formatter)
    # self.logger.addHandler(console)  # 日志对象配置在控制台输出
    # self.logger.addHandler(file_log)  # 日志对象配置在文件中输出
    def __init__(self, logger=None):
        self.log_path = os.path.join(os.path.dirname(__file__), '../', local_config.log_path)
        self.log_file_path = os.path.join(os.path.dirname(__file__), '../logs')
        self.log_name = os.path.join(self.log_path, 'UITest_%s.log' % time.strftime("%Y-%m-%dT%H:%M:%S"))
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(local_config.log_level)
        self.fh = logging.FileHandler(self.log_file_path, 'a', encoding='utf-8')
        self.fh.setLevel(local_config.log_level)
        self.ch = logging.StreamHandler()
        self.ch.setLevel(local_config.log_level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(formatter)
        self.ch.setFormatter(formatter)
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)
        self.fh.close()
        self.ch.close()

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def get_log(self):
        return self.logger


logger = LogUtils()

if __name__ == '__main__':
    log.info('newdream')
