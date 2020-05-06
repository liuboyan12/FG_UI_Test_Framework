# @Time : 2020/5/5 15:08
# @Author : Aliun.Liu
# @File : selenium_base_case_sample.py
# @Software: PyCharm

import unittest
from common.base_page import BasePage
from common.browser import Browser
from common.config_utils import ConfigUtils


class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:  # 针对类级别的
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    def setUp(self) -> None:  # 针对方法级别的
        print('setUp')

    def tearDown(self) -> None:
        print('tearDown')

    def testcase01(self):
        print('testcase01')

    def testcase02(self):
        print('testcase02')


if __name__ == '__main__':
    unittest.main()
